from tkinter import *

root = Tk()
root.title("Nado GUI")

label1 =Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="gui_basic/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요")

    global photo2
    photo2=PhotoImage(file="gui_basic/img2.png")
    label2.config(image=photo2)

btn7 = Button(root, text="클릭", command=change)
btn7.pack()

root.mainloop()