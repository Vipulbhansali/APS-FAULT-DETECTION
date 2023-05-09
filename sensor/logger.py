import logging
import os
from datetime import datetime

#Log file name
LOG_FILE_NAME = f"{datetime.now().strftime('%m%d_%Y__%H_%M_%S')}.log "

#Log Directory
LOG_FILE_DIR = os.path.join(os.getcwd(),"logs")


#Create folder if not available
o.makedirs(LOG_FILE_DIR,exist_ok=True)

#log file path

LOG_FILE_PATH = os.path.join(LOG_FILE_DIR,LOG_FILE_NAME,)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)