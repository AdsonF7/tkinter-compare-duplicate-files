from tkinter import Tk, IntVar, Grid, Frame, Checkbutton, Label, Text, Button, W, NSEW, messagebox

class GUI(Tk):

  def __init__(self, root, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.root = root
    self.iconbitmap("icon.ico")
    self.title("Compare Files")
    self.resizable(True, False)
    self.var_ck_auto_clear = IntVar()
    self.var_ck_auto_clear.set(1)
    self.columnconfigure(0, weight=1)
    self.lb_files_list = Label(self, text="Files List", anchor=W)
    self.lb_files_list.grid(column=0, row=0, padx=(10, 10), sticky=NSEW, pady=(10, 0))
    self.tx_files_list = Text(self, height=5)
    self.tx_files_list.grid(column=0, row=1, padx=(10, 10), sticky=NSEW)
    self.ck_auto_clear = Checkbutton(self, text="Auto Clear", variable=self.var_ck_auto_clear, anchor=W)
    self.ck_auto_clear.grid(column=0, row=2, padx=(10, 10), sticky=NSEW)
    self.frame_bottom = Frame(self)
    self.frame_bottom.grid(column=0, row=3, padx=(10, 10), pady=(10, 10))
    bt_compare = Button(self.frame_bottom, text="Compare")
    bt_compare.grid(column=0, row=0, padx=(0, 5))
    bt_compare.bind("<ButtonRelease-1>", lambda event: self.bt_compare_click(event))
    bt_compare = Button(self.frame_bottom, text="Clear")
    bt_compare.grid(column=1, row=0, padx=(5, 0))
    bt_compare.bind("<ButtonRelease-1>", lambda event: self.bt_clear_click(event))
    
  def bt_clear_click(self, event):
    self.clear_text()
    
  def bt_compare_click(self, event):
    text = self.tx_files_list.get("1.0", "end-1c")
    files_list = text.split("\n")
    path_list = self.root.convert_paths(files_list)
    if self.root.verify_paths(path_list):
      if self.var_ck_auto_clear.get():
        self.clear_text()
      if self.root.compare_files(path_list):
        messagebox.showinfo(title="Compare result", message="The files are the same")
      else:
        messagebox.showerror(title="Compare result", message="The files aren't the same")
    else:
      messagebox.showerror(title="Invalid Path", message="The path entered is not valid")
      
  def clear_text(self):
    self.tx_files_list.delete("1.0", "end")
  
    
