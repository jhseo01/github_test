from tkinter import *
import datetime
import os
import glob
from pathlib import Path
from PIL import ImageTk

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
root = Tk()
root.title("GECD_Agent V1.0")
#root.geometry("640x480") # 가로 * 세로
root.geometry("640x480+300+100") # 가로 * 세로 + x좌표 + y좌표

root.resizable(False, False) # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)

base_dir = "C:\J"
now = datetime.datetime.now()
Y_dir = now.strftime("%Y")
M_dir = now.strftime("%m")
D_dir = now.strftime("%d")

path_dir = base_dir + "\\" + Y_dir + "\\" + M_dir  + "\\" + D_dir 

if [f for f in os.listdir(path_dir) if not f.startswith('.')] == []:
    pass
else: 
    global lbl_path 
    lbl_path = max(glob.glob(path_dir+"\\*"), key=os.path.getctime) + "\\Crack\\"

lbl_gid = Label(root, text="GLASS ID: ")
lbl_gid.pack()
lbl_gid.place(x=10, y=10)

lbl_glsid =Label(root, text=lbl_path)
lbl_glsid.pack()
lbl_glsid.place(x=70,y=10)

lbl_gmt = Label(root, text="판정 결과: ")
lbl_gmt.pack()
lbl_gmt.place(x=300, y=10)

lbl_gmt_result =Label(root, text="결과 출력")
lbl_gmt_result.pack()
lbl_gmt_result.place(x=370,y=10)

img_path = lbl_path + 'cr01.jpg'


def change():

    global photo2
    photo2=ImageTk.PhotoImage(file=img_path)
    label2 = Label(root, image=photo2)
    label2.pack()
    label2.place(x=100, y=100)
    #label2.config(image=photo2)

btn7 = Button(root, text="클릭", command=change)
btn7.pack()
btn7.place(x=500, y=10)




#-------------------
class Watcher:
    base_dir = "C:\J"
    now = datetime.datetime.now()
    Y_dir = now.strftime("%Y")
    M_dir = now.strftime("%m")
    D_dir = now.strftime("%d")

    path_dir = base_dir + "\\" + Y_dir + "\\" + M_dir  + "\\" + D_dir 

    if [f for f in os.listdir(path_dir) if not f.startswith('.')] == []:
        pass
    else: 
        global lbl_path 
        lbl_path = max(glob.glob(path_dir+"\\*"), key=os.path.getctime) + "\\Crack\\"
    print(lbl_path)
    DIRECTORY_WATCH =lbl_path # "./logDir"
    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")
            self.observer.join()


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_moved(event):
        print("move 발생")

    def on_created(shelf,event):
       print("move 발생")

    def on_deleted(shelf,event):
        print("delete 발생")

    def on_modified(shelf,event):
        print("modified 발생")

    def on_any_event(shelf,event):
        print("특정 event 발생")

print("test ")

if __name__ == "__main__":
    w = Watcher()
    w.run()

root.mainloop()