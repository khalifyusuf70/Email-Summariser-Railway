#!/usr/bin/env python3
"""
Worker script for Railway Cron Job
This script fetches and summarizes emails from the last 24 hours
"""

import os
import sys
import time
from datetime import datetime
import logging

# Add the current directory to path so we can import from app
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the email processing function from app
from app import fetch_and_summarize_emails, init_db, get_db_path

def setup_logging():
    """Setup logging for the worker"""
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    
    # Log to stdout (Railway captures this)
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[logging.StreamHandler(sys.stdout)]
    )

def main():
    """Main worker function"""
    setup_logging()
    logger = logging.getLogger(__name__)
    
    logger.info("=" * 50)
    logger.info("🚀 Starting email summary worker")
    logger.info(f"🕐 Time: {datetime.now().isoformat()}")
    logger.info(f"📁 Database path: {get_db_path()}")
    
    try:
        # Initialize database (ensures tables exist)
        logger.info("📁 Initializing database...")
        init_db()
        
        # Run the email fetch and summarize function
        logger.info("📧 Fetching and summarizing emails...")
        success = fetch_and_summarize_emails()
        
        if success:
            logger.info("✅ Worker completed successfully")
        else:
            logger.error("❌ Worker failed")
            sys.exit(1)
            
    except Exception as e:
        logger.error(f"❌ Worker error: {e}")
        sys.exit(1)
    
    logger.info("=" * 50)

if __name__ == "__main__":
    main()
