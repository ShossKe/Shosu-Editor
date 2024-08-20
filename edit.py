import sys
import tkinter as tk
import tkinter.scrolledtext as sk
data = open(sys.argv[1],'r+',encoding='utf-8')

def text():
    label.insert('end',''.join(data.readlines()))
def save():
    data.write(label.get('1.0','end'))    
root = tk.Tk()
root.geometry('500x300')
root.title('Text Editor Shosu v0')

men = tk.Menu(root,tearoff=False)
root.config(menu=men)
mend = tk.Menu(root,tearoff=False)
men.add_cascade(label='メニュー',menu=mend)
mend.add_command(label='保存',command=save)
label = sk.ScrolledText(root,width=55,height=27)


label.pack()

text()
root.mainloop()   
