from os import listdir, path


class FileManager:
    def __init__(self, path):
        self.path = path

    def get_file_names(self):
        file_names = [f for f in listdir(self.path) if path.isfile(path.join(self.path, f)) and not f.startswith(".")]
        return file_names

    def read_file(self, file_name):
        try:
            f = open(path.join(self.path, file_name))
            return f.read()
        except FileNotFoundError:
            return "Error: File not found!"
        except UnicodeDecodeError:
            return "Error: This is not a text file!"
