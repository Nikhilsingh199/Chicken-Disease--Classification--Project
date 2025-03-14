import os
import sys
import logging

logging_str ="[%(asctime)s]: %(levelname)s: %(module)s %(message)s]"

login_dir ="logs"
log_filepath =os.path.join(login_dir,"running_logs.log")
os.makedirs(login_dir,exist_ok=True)

logging.basicConfig(level=logging.INFO,format=logging_str
                    ,handlers=[logging.FileHandler(log_filepath),
                                logging.StreamHandler(sys.stdout)])
logger =logging.getLogger("cnnClassifierLogger")