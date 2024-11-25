import pathlib
import hashlib

class File:

    def __init__(self, path):
        self.path = path

    @property
    def name(self):
        return self.__name

    @property
    def path(self):
        return self.__path
    
    @property
    def hash(self):
        return self.__hash

    @path.setter
    def path(self, value):
        self.__path = pathlib.Path(value)
        self.__name = self.__path.stem
        self.__hash = File.checksum_md5(self.__path)
        
    @staticmethod
    def cheksum_md5(file):
        with open(file, "rb") as file_to_check:
            file_hash = hashlib.md5()
            while chunk := file_to_check.read(8192):
                file_hash.update(chunk)
                chunk = file_to_check.read(8192)
            file_to_check.close()
        return file_hash.hexdigest()
    