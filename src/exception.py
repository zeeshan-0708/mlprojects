import sys
import logging
import os
from datetime import datetime
from src.logger import logging
# Configure logging to include timestamps and log level
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(levelname)s in %(filename)s at line %(lineno)d: %(message)s",
    level=logging.INFO,
)

# Function to generate detailed error messages
def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message

# Custom exception class
class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message

# # Main code block to trigger the exception and log it
# if __name__ == "__main__":
#     try:
#         # This line will cause a ZeroDivisionError
#         a = 1 / 0
#     except Exception as e:
#         # Log and raise a custom exception with details
#         custom_exception = CustomException(e, sys)
#         logging.error(custom_exception)  # Log the custom exception message only
