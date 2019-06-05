from tkinter import*
import time
import random
import numpy as np
import numpy.random


#functions
click = []
t0 = time.time()

def aftertime ():
    Button1["background"]="black"
    Button2["background"]="black" 
    Button3["background"]="black" 
    Button4["background"]="black" 
    Button5["background"]="black" 
    Button6["background"]="black" 
    Button7["background"]="black" 
    Button8["background"]="black" 
    Button9["background"]="black" 
    Button10["background"]="black" 
    Button11["background"]="black" 
    Button12["background"]="black" 
    Button1.config(state="disabled")
    Button2.config(state="disabled")
    Button3.config(state="disabled")
    Button4.config(state="disabled")
    Button5.config(state="disabled")
    Button6.config(state="disabled")
    Button7.config(state="disabled")
    Button8.config(state="disabled")
    Button9.config(state="disabled")
    Button10.config(state="disabled")
    Button11.config(state="disabled")
    Button12.config(state="disabled")

def testfun():
    Button1["background"]="green" 
    Button1.config(state="disabled")
    
    testfun().after(1000, lambda:testfun2())

def testfun2():
    Button1["background"]="gray" 
    Button1.config(state="normal")
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
window.after(6000, lambda: aftertime())
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
    # if j == 0:
    #     Button1 = Button(topFrame,  height=5, width=12, bg="gray", command=lambda:match( num = 1))
    #     Button.pack(side = LEFT)
    # elif j == 1:
    #     Button5 = Button(topDown,  height=5, width=12, bg="gray" , command=lambda:match(num =5) )
    #     Button5.pack(side = LEFT)
    # else:
    #     Button11 = Button(topBottom,  height=5, width=12, bg="gray", command=lambda:match(num =11) )
    #     Button11.pack(side = LEFT)

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
        Button4 = Button(topFrame,  height=5, width=12, bg="gray", command=lambda:match(num =4))
        Button4.pack(side = LEFT)
        #second raw
    elif i==5:
        Button5 = Button(topDown,  height=5, width=12, bg="gray" , command=lambda:match(num =5) )
        Button5.pack(side = LEFT)
    elif i==6:
        Button6 = Button(topDown,  height=5, width=12, bg="gray" , command=lambda:match(num =6) )
        Button6.pack(side = LEFT)
    elif i==7:
        Button7 = Button(topDown,  height=5, width=12, bg="gray" , command=lambda:match(num =7) )
        Button7.pack(side = LEFT)
    elif i==8:
        Button8 = Button(topDown,  height=5, width=12, bg="gray" , command=lambda:match(num =8) )
        Button8.pack(side = LEFT)
        # Third row 
    elif i==9:
        Button9 = Button(topBottom,  height=5, width=12, bg="gray", command=lambda:match(num =9) )
        Button9.pack(side = LEFT)
    elif i==10:
        Button10 = Button(topBottom,  height=5, width=12, bg="gray", command=lambda:match(num =10) )
        Button10.pack(side = LEFT)
    elif i==11:
        Button11 = Button(topBottom,  height=5, width=12, bg="gray", command=lambda:match(num =11) )
        Button11.pack(side = LEFT)
    elif i==12  :
        Button12 = Button(topBottom,  height=5, width=12, bg="gray", command=lambda:match(num =12) )
        Button12.pack(side = LEFT)
    
    





window.mainloop()









