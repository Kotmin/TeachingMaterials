import logging

# Define a custom formatter class to add colors
class CustomFormatter(logging.Formatter):
    color_codes = {
        logging.DEBUG: "\033[0;37m",  # Grey
        logging.INFO: "\033[0;34m",   # Blue
        logging.WARNING: "\033[0;33m",  # Yellow
        logging.ERROR: "\033[0;31m",   # Red
        logging.CRITICAL: "\033[1;31m"  # Bright Red
    }

    def format(self, record):
        color_code = self.color_codes.get(record.levelno, "\033[0m")  # Default to no color
        formatter = logging.Formatter(f"{color_code}%(asctime)s - %(levelname)s - %(message)s\033[0m")
        return formatter.format(record)

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Set the logging level

# Ensure there are no duplicate handlers
if not logger.handlers:
    # Create a stream handler and set the custom formatter
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(CustomFormatter())
    logger.addHandler(stream_handler)

# Example log messages
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
