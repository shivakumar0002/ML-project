import logging 
import os
from datetime import datetime

# Log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Directory path for logs
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Full path for the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Basic configuration for logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)  


