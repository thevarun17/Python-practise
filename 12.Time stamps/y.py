import datetime

# Get the current date and time
now = datetime.datetime.now()

# Display the current date and time
print("Current date and time:")
print(now)

# Format the timestamp in different ways
formatted_timestamp1 = now.strftime("%Y-%m-%d | %H:%M:%S")  # Format: YYYY-MM-DD HH:MM:SS
formatted_timestamp2 = now.strftime("%A, %B %d, %Y")     # Format: Day, Month DD, YYYY

print("\nFormatted timestamps:")
print("1. ", formatted_timestamp1)
print("2. ", formatted_timestamp2)

# Example of using timestamps in logging
import logging

# Configure logging to include timestamps
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Log a message with a timestamp
logging.info("This is a log message with a timestamp.")