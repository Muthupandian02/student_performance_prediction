import logging
import os
from datetime import datetime

log_path=os.path.join(os.getcwd(),'logs',f'{datetime.now().strftime('%d_%m_%Y')}') #joining the path D:\Mlops\logs\12_30_2025 
LOG_FILE=f'{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log'
os.makedirs(log_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] line: %(lineno)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

