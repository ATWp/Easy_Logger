import os
from datetime import datetime

from logs.reader import READER


STATUS = {
    "prode":3,
    "error":2,
    "debug":1,
}


class Log():
    """
    Записываем логи
    @path -> logs_folder, где будут храниться все файлы логов
    @file_name -> file_name текущий файл дня для хранения логов, которые будут записаны сегодня
    """
    
    def __init__(self, path, file_name, status="debug", reader = READER):

        self.status = status
        self.logs_folder = path
        self.log_path = f"{path}\\{file_name}.txt"
        
        # Interface for saving data
        self.reader = reader()
        
        # format-datetime
        self.format_datetime = '%Y-%m-%d %H:%M:%S'
        self.short_format_time = '%H:%M:%S'
    
    def create_file(self):
        """Создаем файл текущего дня"""
        if not os.path.exists(self.log_path):
            first_message = f"Create logs at {datetime.now().strftime(self.format_datetime)}"
            self.reader.save(self.log_path,[first_message])
    
    def create_folder(self):
        """Создаем папку для логов"""
        if not os.path.exists(self.logs_folder): os.mkdir(self.logs_folder)
       
    def print(self, messages, status="debug"):
        """Сохраняем список строк в файл логов"""
        self.create_folder()
        self.create_file()
        time = datetime.now().strftime(self.short_format_time)
        line = f"{time}-{status}::{messages}"
        self.reader.awrite(self.log_path, [line])
        
        if STATUS[status] >= STATUS[self.status]: print(messages)