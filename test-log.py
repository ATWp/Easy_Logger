from datetime import datetime

from logs.logs import Log

# In production it's worth loading data from an *.env file
path = "Write your folder to save logs"
file_name = datetime.now().strftime("%Y-%m-%d")
status = "prode" # all-status-level: prode | error | debug

# init log
log = Log(path, file_name, status=status)

# use log
log.print(f"Какая-то информация...{path}")