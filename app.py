from gui import GUI

from os.path import isfile
import pathlib
from file import File
import os

class App:

  def __init__(self):
    self.__gui = GUI(self)
    self.__gui.mainloop()

  def compare_files(self, file_list, erase=False):
    if self.valid_paths(file_list):
      files = []
      hash = File(file_list[0].replace("\"", "")).hash
      for i in range(1, len(file_list)):
        try: file = File(file_list[i].replace("\"", ""))
        except Exception: return None
        files.append(file)
        if file.hash != hash: return False
      if erase: 
        for file in files: os.remove(file.path)
      return True
    return None
  
  def valid_paths(self, path_list):
    if len(path_list) > 1: return True
    return False