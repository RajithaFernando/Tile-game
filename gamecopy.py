from tkinter import*
import time
import random
import numpy as np
import numpy.random


#functions
click = []
t0 = time.time()

def aftertime ():
    Button1["background"]="gray" 
    Button2["background"]="gray" 
    Button3["background"]="gray" 
    Button4["background"]="gray" 
    Button5["background"]="gray" 
    Button6["background"]="gray" 
    Button7["background"]="gray" 
    Button8["background"]="gray" 
    Button9["background"]="gray" 
    Button10["background"]="gray" 
    Button11["background"]="gray" 
    Button12["background"]="gray" 

def testfun():
    Button1["background"]="green" 
    Button1.config(state="disabled")
def match(num):
    points = 0
    click.append(num)
    
    # print(num)
    # print(click)
    

    if len(click) < 12:
        # print('abc')
        print(t0)
        if num == 1:
            Button1.config(state="disabled")
            Button1.after(1000, lambda:testfun())
            
        elif num==2:
            Button2.config(state="disabled")
            Button1.after(1000, lambda:testfun())
        elif num==3:
            Button3.config(state="disabled")
            Button1.after(1000, lambda:testfun())
        elif num==4:
            Button4.config(state="disabled")
            Button1.after(1000, lambda:testfun())
        #second raw
        elif num==5:
            Button5.config(state="disabled")
            Button1.after(1000, lambda:testfun())
        elif num==6:
            Button6.config(state="disabled")
            Button1.after(1000, lambda:testfun())
        elif num==7:
            Button7.config(state="disabled")
            Button1.after(1000, lambda:testfun())
        elif num==8:
            Button8.config(state="disabled")
            Button1.after(1000, lambda:testfun())
        # Third row 
        elif num==9:
            Button9.config(state="disabled")
            Button1.after(1000, lambda:testfun())
        elif num==10:
            Button10.config(state="disabled")
            Button1.after(1000, lambda:testfun())
        elif num==11:
            Button11.config(state="disabled")
            Button1.after(1000, lambda:testfun())
        elif num ==12 :
            Button12.config(state="disabled")
            Button1.after(1000, lambda:testfun())
    else:
        a = click[:2] 
        b = click[2:4]
        d = click[4:6]
        e = click[6:8]
        f = click[8:10]
        g = click[10:]
       

        for r in range (6):
            if (click[r*2] %3 == click[r*2+1] %3):
                points = points +20
                print(points) 
            else:
                points = points -5
                print(points)

    


#setting the game window
window = Tk()
window.after(10000, lambda: aftertime())
# limited 10 seconds , then buttons become gray
window.title("ABC pair game")

#setting the frame
topFrame = Frame(window)
topFrame.pack()
topDown = Frame(window)
topDown.pack()
topBottom = Frame(window)
topBottom.pack()


col = ["lightblue", "green", "red"]
arr = [7,2,9,3,1,12,4,6,8,11,10,5]
random.shuffle(arr)


for i in arr:
    j = i %3
    if i == 1:
        Button1 = Button(topFrame,  height=5, width=12, bg="gray", command=lambda:match( num = 1))
        Button1.pack(side = LEFT)

    elif i==2:
        Button2 = Button(topFrame,  height=5, width=12, bg="gray", command=lambda:match(num =2))
        Button2.pack(side = LEFT)
    elif i==3:
        Button3 = Button(topFrame,  height=5, width=12, bg="gray", command=lambda:match(num =3))
        Button3.pack(side = LEFT)
    elif i==4:
        Button4 = Button(topFrame,  height=5, width=12, bg=col[j], command=lambda:match(num =4))
        Button4.pack(side = LEFT)
        #second raw
    elif i==5:
        Button5 = Button(topDown,  height=5, width=12, bg=col[j] , command=lambda:match(num =5) )
        Button5.pack(side = LEFT)
    elif i==6:
        Button6 = Button(topDown,  height=5, width=12, bg=col[j] , command=lambda:match(num =6) )
        Button6.pack(side = LEFT)
    elif i==7:
        Button7 = Button(topDown,  height=5, width=12, bg=col[j] , command=lambda:match(num =7) )
        Button7.pack(side = LEFT)
    elif i==8:
        Button8 = Button(topDown,  height=5, width=12, bg=col[j] , command=lambda:match(num =8) )
        Button8.pack(side = LEFT)
        # Third row 
    elif i==9:
        Button9 = Button(topBottom,  height=5, width=12, bg=col[j], command=lambda:match(num =9) )
        Button9.pack(side = LEFT)
    elif i==10:
        Button10 = Button(topBottom,  height=5, width=12, bg=col[j], command=lambda:match(num =10) )
        Button10.pack(side = LEFT)
    elif i==11:
        Button11 = Button(topBottom,  height=5, width=12, bg=col[j], command=lambda:match(num =11) )
        Button11.pack(side = LEFT)
    elif i==12  :
        Button12 = Button(topBottom,  height=5, width=12, bg=col[j], command=lambda:match(num =12) )
        Button12.pack(side = LEFT)
    
    





window.mainloop()









