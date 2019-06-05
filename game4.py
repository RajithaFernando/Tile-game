from tkinter import*
import time
import random

selected = []
clickcount = 0
points = 0
matched = []
clickButton = []
def showText(num):
    print("ShowText")
    if num == 1:
        Button1["text"] = "A"
    if num == 2:
        Button2["text"] = "B"
    if num ==3:
        Button3["text"] = "C"
    if num ==4:
        Button4["text"] = "A"
    if num ==5:
        Button5["text"] = "B"
    if num ==6:
        Button6["text"] = "C"
    if num ==7:
        Button7["text"] = "A"
    if num ==8:
        Button8["text"] = "B"
    if num == 9:
        Button9["text"] = "C"
    if num == 10:
        Button10["text"] = "A"
    if num == 11:
        Button12["text"] = "B"
    if num == 12:
        Button12["text"] = "C"

def succes(a,b):
    print("success")
    if a == 1 or b==1:
        Button1.config(state="disabled")
    if a == 2 or b==2:
        Button2.config(state="disabled")
    if a == 3 or b==3:
        Button3.config(state="disabled")
    if a == 4 or b==4:
        Button4.config(state="disabled")
    if a == 5 or b==5:
        Button5.config(state="disabled")
    if a == 6 or b==6:
        Button6.config(state="disabled")
    if a == 7 or b==7: 
        Button7.config(state="disabled")
    if a == 8 or b==8: 
        Button8.config(state="disabled")
    if a == 9 or b==9:
        Button9.config(state="disabled")
    if a == 10 or b==10:
        Button10.config(state="disabled")
    if a == 11 or b==11:
        Button11.config(state="disabled")
    if a == 12 or b==12:
        Button12.config(state="disabled")
    return showText(a)
    return showText(b)

def missmatch(a,b):
    print("Missmatch")
    if a == 1 or b==1:
        Button1.config(state="disabled")
        Button1["text"] = "A"
        Button1.after(2000, lambda:normalState(a,b))
    if a == 2 or b==2:
        Button2.config(state="disabled")
        Button2["text"] = "B"
        Button2.after(2000, lambda:normalState(a,b))
    if a == 3 or b==3:
        Button3.config(state="disabled")
        Button3["text"] = "C"
        Button3.after(2000, lambda:normalState(a,b))
    if a == 4 or b==4:
        Button4.config(state="disabled")
        Button4["text"] = "A"
        Button4.after(2000, lambda:normalState(a,b))
    if a == 5 or b==5:
        Button5.config(state="disabled")
        Button5["text"] = "B"
        Button5.after(2000, lambda:normalState(a,b))
    if a == 6 or b==6:
        Button6.config(state="disabled")
        Button6["text"] = "C"
        Button6.after(2000, lambda:normalState(a,b))
    if a == 7 or b==7: 
        Button7.config(state="disabled")
        Button7["text"] = "A"
        Button7.after(2000, lambda:normalState(a,b))
    if a == 8 or b==8: 
        Button8.config(state="disabled")
        Button8["text"] = "B"
        Button8.after(2000, lambda:normalState(a,b))
    if a == 9 or b==9:
        Button9.config(state="disabled")
        Button9["text"] = "C"
        Button9.after(2000, lambda:normalState(a,b))
    if a == 10 or b==10:
        Button10.config(state="disabled")
        Button10["text"] = "A"
        Button10.after(2000, lambda:normalState(a,b))
    if a == 11 or b==11:
        Button11.config(state="disabled")
        Button11["text"] = "B"
        Button11.after(2000, lambda:normalState(a,b))
    if a == 12 or b==12:
        Button12.config(state="disabled")
        Button12["text"] = "C"
        Button12.after(2000, lambda:normalState(a,b))

def normalState(a,b):
    print("Normal State")

    if a == 1 or b==1:
        Button1.config(state="normal")
        Button1["text"] = ""
    if a == 2 or b==2:
        Button2.config(state="normal")
        Button2["text"] = ""
    if a == 3 or b==3:
        Button3.config(state="normal")    
        Button3["text"] = "" 
    if a == 4 or b==4:
        Button4.config(state="normal")
        Button4["text"] = "" 
    if a == 5 or b==5:
        Button5.config(state="normal")
        Button5["text"] = "" 
    if a == 6 or b==6:
        Button6.config(state="normal")
        Button6["text"] = "" 
    if a == 7 or b==7: 
        Button7.config(state="normal")
        Button7["text"] = "" 
    if a == 8 or b==8: 
        Button8.config(state="normal")
        Button8["text"] = "" 
    if a == 9 or b==9:
        Button9.config(state="normal")
        Button9["text"] = "" 
    if a == 10 or b==10:
        Button10.config(state="normal")
        Button10["text"] = "" 
    if a == 11 or b==11:
        Button11.config(state="normal")
        Button11["text"] = "" 
    if a == 12 or b==12:
        Button12.config(state="normal")
        Button12["text"] = "" 

def match(num):
    print("match")
    global clickButton
    clickButton.append(num)
    global clickcount
    clickcount = clickcount + 1
    if clickcount < 2:
        return showText(num)
        print("Match - clickcount<1")
    else:
        prevNum = clickButton[-2]
        a = num % 3
        b = prevNum % 3
        print("Match - clickcount>1")
        if a == b:
            return succes(prevNum,num)
            clickcount = 0
        else:
            print("missmatch")
            return missmatch(prevNum,num)
            
def aftertime():
    print("aftertime")
    Button1["text"] = "Game Over"
    Button2["text"] = "Game Over" 
    Button3["text"] = "Game Over" 
    Button4["text"] = "Game Over" 
    Button5["text"] = "Game Over" 
    Button6["text"] = "Game Over" 
    Button7["text"] = "Game Over" 
    Button8["text"] = "Game Over" 
    Button9["text"] = "Game Over" 
    Button10["text"] = "Game Over" 
    Button11["text"] = "Game Over" 
    Button12["text"] = "Game Over"  
    # Button1.config(state="disabled")
    # Button2.config(state="disabled")
    # Button3.config(state="disabled")
    # Button4.config(state="disabled")
    # Button5.config(state="disabled")
    # Button6.config(state="disabled")
    # Button7.config(state="disabled")
    # Button8.config(state="disabled")
    # Button9.config(state="disabled")
    # Button10.config(state="disabled")
    # Button11.config(state="disabled")
    # Button12.config(state="disabled")



#setting the game window
window = Tk()
window.after(10000, lambda: aftertime())
# limited 10 seconds , then buttons become grray
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


count =0
# print(arr)
for i in arr:
    # j = i %3
    if count < 4:

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
        elif i==5:
            Button5 = Button(topFrame,  height=5, width=12, bg="gray" , command=lambda:match(num =5) )
            Button5.pack(side = LEFT)
        elif i==6:
            Button6 = Button(topFrame,  height=5, width=12, bg="gray" , command=lambda:match(num =6) )
            Button6.pack(side = LEFT)
        elif i==7:
            Button7 = Button(topFrame,  height=5, width=12, bg="gray" , command=lambda:match(num =7) )
            Button7.pack(side = LEFT)
        elif i==8:
            Button8 = Button(topFrame,  height=5, width=12, bg="gray" , command=lambda:match(num =8) )
            Button8.pack(side = LEFT)
        elif i==9:
            Button9 = Button(topFrame,  height=5, width=12, bg="gray", command=lambda:match(num =9) )
            Button9.pack(side = LEFT)
        elif i==10:
            Button10 = Button(topFrame,  height=5, width=12, bg="gray", command=lambda:match(num =10) )
            Button10.pack(side = LEFT)
        elif i==11:
            Button11 = Button(topFrame,  height=5, width=12, bg="gray", command=lambda:match(num =11) )
            Button11.pack(side = LEFT)
        elif i==12  :
            Button12 = Button(topFrame,  height=5, width=12, bg="gray", command=lambda:match(num =12) )
            Button12.pack(side = LEFT)
    elif count < 8:

        if i == 1:
            Button1 = Button(topDown,  height=5, width=12, bg="gray", command=lambda:match( num = 1))
            Button1.pack(side = LEFT)
        elif i==2:
            Button2 = Button(topDown,  height=5, width=12, bg="gray", command=lambda:match(num =2))
            Button2.pack(side = LEFT)
        elif i==3:
            Button3 = Button(topDown,  height=5, width=12, bg="gray", command=lambda:match(num =3))
            Button3.pack(side = LEFT)
        elif i==4:
            Button4 = Button(topDown,  height=5, width=12, bg="gray", command=lambda:match(num =4))
            Button4.pack(side = LEFT)
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
        elif i==9:
            Button9 = Button(topDown,  height=5, width=12, bg="gray", command=lambda:match(num =9) )
            Button9.pack(side = LEFT)
        elif i==10:
            Button10 = Button(topDown,  height=5, width=12, bg="gray", command=lambda:match(num =10) )
            Button10.pack(side = LEFT)
        elif i==11:
            Button11 = Button(topDown,  height=5, width=12, bg="gray", command=lambda:match(num =11) )
            Button11.pack(side = LEFT)
        elif i==12  :
            Button12 = Button(topDown,  height=5, width=12, bg="gray", command=lambda:match(num =12) )
            Button12.pack(side = LEFT)
    elif count < 12:

        if i == 1:
            Button1 = Button(topBottom,  height=5, width=12, bg="gray", command=lambda:match( num = 1))
            Button1.pack(side = LEFT)
        elif i==2:
            Button2 = Button(topBottom,  height=5, width=12, bg="gray", command=lambda:match(num =2))
            Button2.pack(side = LEFT)
        elif i==3:
            Button3 = Button(topBottom,  height=5, width=12, bg="gray", command=lambda:match(num =3))
            Button3.pack(side = LEFT)
        elif i==4:
            Button4 = Button(topBottom,  height=5, width=12, bg="gray", command=lambda:match(num =4))
            Button4.pack(side = LEFT)
        elif i==5:
            Button5 = Button(topBottom,  height=5, width=12, bg="gray" , command=lambda:match(num =5) )
            Button5.pack(side = LEFT)
        elif i==6:
            Button6 = Button(topBottom,  height=5, width=12, bg="gray" , command=lambda:match(num =6) )
            Button6.pack(side = LEFT)
        elif i==7:
            Button7 = Button(topBottom,  height=5, width=12, bg="gray" , command=lambda:match(num =7) )
            Button7.pack(side = LEFT)
        elif i==8:
            Button8 = Button(topBottom,  height=5, width=12, bg="gray" , command=lambda:match(num =8) )
            Button8.pack(side = LEFT)
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
    
    # print(i)
    count = count +1






window.mainloop()









