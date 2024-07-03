from gui import GUI

from os.path import isfile
import pathlib
import hashlib

class App:

  def __init__(self):
    self._gui = GUI(self)
    self._gui.mainloop()

  def compare_files(self, path_list):
    hash = ""
    equal = True
    for i in range(len(path_list)):
      file_hashi = hashlib.md5(open(path_list[i], 'rb').read()).hexdigest()
      if i == 0:
        hash = file_hashi
      else:
        equal &= file_hashi == hash
    return equal
    
  def convert_paths(self, file_list):
    path_list = []
    for i in range(len(file_list)):
      current_path = pathlib.Path(r"%s" %file_list[i].replace("\"", ""))
      path_list.append(current_path)
    return path_list
  
  def verify_paths(self, path_list):
    valid = True
    if len(path_list) > 1:
      for i in range(len(path_list)):
        valid &= path_list[i].is_absolute() & isfile(path_list[i])
        if not valid: 
          return False
      return True
    return False
      #if valid:
      #  self.compare_files(path_list)
      #  