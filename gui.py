from tkinter import Tk, IntVar, Grid, Frame, Checkbutton, Label, Text, Button, W, NSEW, messagebox

class GUI(Tk):

  messages = {
    True: ["Compare Result", "The files are the same", messagebox.showinfo],
    False: ["Compare Result", "The files aren't the same", messagebox.showerror],
    None: ["Invalid Path", "The path entered is not valid", messagebox.showerror]
  }

  def __init__(self, root, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.__root = root
    self.iconbitmap("icon.ico")
    self.title("Compare Files")
    self.resizable(True, False)
    self.__var_ck_auto_clear = IntVar()
    self.__var_ck_auto_clear.set(1)
    self.__var_ck_delete_duplicates = IntVar()
    self.__var_ck_delete_duplicates.set(1)
    self.columnconfigure(0, weight=1)
    lb_files_list = Label(self, text="Files List", anchor=W)
    lb_files_list.grid(column=0, row=0, padx=(10, 10), sticky=NSEW, pady=(10, 0))
    self.__tx_files_list = Text(self, height=5)
    self.__tx_files_list.grid(column=0, row=1, padx=(10, 10), sticky=NSEW)
    ck_auto_clear = Checkbutton(self, text="Auto Clear", variable=self.__var_ck_auto_clear, anchor=W)
    ck_auto_clear.grid(column=0, row=2, padx=(10, 10), sticky=NSEW)
    ck_delete_duplicates = Checkbutton(self, text="Delete File If Duplicated", variable=self.__var_ck_delete_duplicates, anchor=W)
    ck_delete_duplicates.grid(column=0, row=3, padx=(10, 10), sticky=NSEW)
    frame_bottom = Frame(self)
    frame_bottom.grid(column=0, row=4, padx=(10, 10), pady=(10, 10))
    bt_compare = Button(frame_bottom, text="Compare")
    bt_compare.grid(column=0, row=0, padx=(0, 5))
    bt_compare.bind("<ButtonRelease-1>", lambda event: self.bt_compare_click(event))
    bt_compare = Button(frame_bottom, text="Clear")
    bt_compare.grid(column=1, row=0, padx=(5, 0))
    bt_compare.bind("<ButtonRelease-1>", lambda event: self.bt_clear_click(event))
  
  @property
  def path_list(self):
    return self.__tx_files_list.get("1.0", "end-1c").split("\n")
  
  def bt_clear_click(self, event):
    self.tx_clear_text()
    
  def bt_compare_click(self, event):
    equal = self.__root.compare_files(self.path_list, self.__var_ck_delete_duplicates.get())
    self.show_message(equal)
    if self.__var_ck_auto_clear.get():
      self.tx_clear_text()

  def tx_clear_text(self):
    self.__tx_files_list.delete("1.0", "end")

  def show_message(self, value):
    message = GUI.messages[value]
    title = message[0]
    text = message[1]
    fn = message[2]
    fn(title=title, message=text)
    
