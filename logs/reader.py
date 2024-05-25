class READER():
    
    def read(self, path):
        with open(path, "r", encoding="utf-8") as file:
            data = [line for line in file]
        return data
        
    def awrite(self, path, data):
        """Дозаписываем данные в файл по указанному пути"""
        with open(path, "a", encoding="utf-8") as file:
            for value in data:
                file.write(f"{value}\n")

    
    def save(self, path, data):
        # куда сохранять задачи, если нет ни одного загруженного файла?
        # в inbox, который рядом с этим файлом
        with open(path, "w", encoding="utf-8") as file:
            for value in data:
                file.write(f"{value}\n")