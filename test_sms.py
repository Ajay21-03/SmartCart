import os
import logging
from utils.sms_service import send_order_status_sms

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def test_sms_notification():
    """Test sending an SMS notification using Twilio"""
    # Get the user's phone number from the environment
    # Or replace with your phone number for testing
    phone_number = input("Enter your phone number to test SMS (include country code, e.g., +1234567890): ")
    
    # Test sending an SMS for a sample order
    order_id = 12345  # Test order ID
    status = "confirmed"  # Test status
    
    logger.info(f"Sending test SMS to {phone_number} for order #{order_id} with status '{status}'")
    
    result = send_order_status_sms(phone_number, status, order_id)
    
    if result:
        logger.info("✅ SMS sent successfully!")
    else:
        logger.error("❌ Failed to send SMS. Check your Twilio credentials and phone number format.")

if __name__ == "__main__":
    test_sms_notification()