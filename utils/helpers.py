# This module contains helper functions for logging and masking sensitive data in the intelligent email automation system.

import logging
from datetime import datetime

def setup_logging():
    """Setup logging for auditability """
    logging.basicConfig(
        filename='logs/app.log',
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return logging.getLogger(__name__)

def mask_sensitive_data(text: str) -> str:
    """Mask account/card numbers for security"""
    import re
    text = re.sub(r'\b\d{9,10}\b', 'XXXXXX', text)   # mask account numbers
    text = re.sub(r'\b\d{4}X{4}\d{4}\b', 'XXXX-XXXX-XXXX', text)  # mask cards
    return text
