# import cv2
# import pyautogui as p
# import numpy as np

# rs=p.size()
# inp = input("enter the path")
# fps=30.0
# fourcc = cv2.VideoWriter_fourcc(*"xvid")
# output= cv2.VideoWriter(inp,fourcc,fps,rs)
# cv2.namedwindow("live_recording",cv2.WINDOW_NORMAL)
# cv2.resizeWindow("live_recording",(600,500))
# while True:
#     img=p.screenshot()
#     f=np.array(img)
#     f=cv2.cvtColor(f,cv2.COLOR_BGR2RGB)
#     output.write(f)
#     cv2.imshow("live-recording",f)
#     if cv2.waitKey(1)==ord('q'):
#         break
# output.release()
# cv2.destroyAllWindows()

from tkinter import *

import cv2
import pyautogui as p
import numpy as np

root=Tk()

width= root.winfo_screenwidth() 
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))

def f():
    rs=p.size()
    inp = addressvalue.get()
    fps=10.0
    fourcc = cv2.VideoWriter_fourcc(*"xvid")
    output= cv2.VideoWriter(inp,fourcc,fps,rs)
    cv2.namedWindow("live_recording",cv2.WINDOW_NORMAL)
    cv2.resizeWindow("live_recording",(600,500))
    while True:
        img=p.screenshot()
        f=np.array(img)
        f=cv2.cvtColor(f,cv2.COLOR_BGR2RGB)
        output.write(f)
        # cv2.imshow("live-recording",f)
        
        if cv2.waitKey(1)==ord('q'):
            break
    output.release()
    cv2.destroyAllWindows()

def exits():
    exit()
    cv2.destroyAllWindows()

Label(root,text="Screen Recorder",font=("Georgia",40,"bold"),pady=40,fg="purple").pack(pady=10)

addressvalue=StringVar()
l1=Label(root,text="Enter the path to save the video :",font=("serif",15,"bold")).pack()
address=Entry(root,textvariable=addressvalue,width=50)
address.pack(pady=10,ipady=10)

btn=Button(root,text="Start Recording",command=f,padx=150,pady=15,relief=RAISED,bg="gray",fg="white",font=("serif",15,"bold")).pack(pady=10)

btn_quit=Button(root,text="Exit",command=exits,padx=150,pady=15,relief=RAISED,bg="gray",fg="white",font=("serif",15,"bold")).pack(pady=10)



l3=Label(root,text="Press 'q' to stop the screen recording").pack(pady=60)
root.mainloop()
