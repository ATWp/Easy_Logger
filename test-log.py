from datetime import datetime

from logs.logs import Log

path = "C:\\Users\\1\\Desktop\\git-log"
url = datetime.now().strftime("%Y-%m-%d")
status = "prode" # all-status-level: prode | error | debug
log = Log(path, url, status=status)

log.print(f"Какая-то информация...{path}")