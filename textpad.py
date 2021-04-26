from tkinter import *
from tkinter import filedialog
from tkinter import font

root = Tk()
root.title("Carter's text editor")
root.geometry("1200x600")


def new_file():
    my_text.delete("1.0", END)
    root.title("New file - TextPad!")
    status_bar.config(text='New file          ')


def open_file():
    my_text.delete("1.0", END)

    text_file = filedialog.askopenfilename(title="Open File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("JavaScript Files", "*.js"),("All Files","*.*")))
    name = text_file
    status_bar.config(text=f'{name}        ')
    root.title(f'{name} - TextPad!')

    text_file = open(text_file,"r")
    stuff = text_file.read()

    my_text.insert(END, stuff)

    text_file.close()


def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*", title="Save File", filetypes=(("Text Files", "*.txt"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("JavaScript Files", "*.js"),("All Files","*.*")))

    if text_file:
        name = text_file
        status_bar.config(text=f'Saved: {name}        ')
        root.title(f'{name} - TextPad!')

        text_file = open(text_file,"w")
        text_file.write(my_text.get(1.0, END))
        text_file.close()

my_frame = Frame(root)
my_frame.pack(pady=5)

text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT, fill=Y)



my_text = Text(my_frame, width=97,height=25,font=("Helvetica", 16), selectbackground="yellow",selectforeground="black",undo=True,yscrollcommand=text_scroll.set)
my_text.pack()

text_scroll.config(command=my_text.yview)



my_menu = Menu(root)

root.config(menu=my_menu)

file_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save")
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit" ,command=root.quit)


edit_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut")
edit_menu.add_command(label="Copy")
edit_menu.add_command(label="Paste")
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Redo")



status_bar = Label(root, text="Ready        ", anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)



root.mainloop()