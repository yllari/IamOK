from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
import warnings

from tree_manager import run_mode

def browse_button_in():
    # Allow user to select a directory and store it in global var
    # called folder_path
    filename = filedialog.askdirectory()
    folder_path_in.set(filename)

    return None

def browse_button_out():
    # Allow user to select a directory and store it in global var
    # called folder_path
    filename = filedialog.askdirectory()
    folder_path_out.set(filename)

    return None

def run_main():


    if len(folder_path_in.get()) == 0 or len(folder_path_out.get()) == 0:
        return 'Please enter out and in folders'


    return run_mode(folder_path_in.get(), folder_path_out.get(), sel_mode.get())

def run_main_wait():

    is_running.set('Running! Please wait')
    is_running.set(run_main())

modes = ['nocopy', 'docs', 'docs_images']

root = Tk()
default_font = tkFont.nametofont("TkDefaultFont")
default_font.configure(size=15)

# set minimum window size value
folder_path_in = StringVar()
folder_path_out = StringVar()
running = BooleanVar(value=False)

sel_mode = StringVar(value='nocopy')
lbl1 = Label(master=root, textvariable=folder_path_in)
lbl2 = Label(master=root, textvariable=folder_path_out)

is_running= StringVar(value='')
lbl_state = Label(master=root, textvariable=is_running)

# Specify Grid

for i in range(5):
    Grid.rowconfigure(root,i,weight=1)
    Grid.columnconfigure(root,i,weight=1)

lbl1.grid(row=0, column=1)
lbl2.grid(row=1, column=1)
lbl_state.grid(row=4, column=1)

# buttons buttons
button2 = Button(text="Browse in directory", command=browse_button_in)
button2.grid(row=0, column=2,sticky="NSEW")
button3 = Button(text="Browse out directory", command=browse_button_out)
button3.grid(row=1, column=2,sticky="NSEW")


## Setting dropdown menu
cb = ttk.Combobox(root, values=modes)
cb.set('Select run mode (nocopy as default)')
cb.grid(row=2, column=1, columnspan=2,sticky="NSEW")
cb.config(font=default_font)


## Setting run button
submit = ttk.Button(
    root,
    text="Run",
    command=run_main_wait
)
submit.grid(row=3, column=2, padx=5, pady=5, sticky='NSEW')

mainloop()
