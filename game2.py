from tkinter import*
import time
import random

selected = []
def match(num):
    # print(num)
    selected.append(num)
    print(selected)
    if len(selected) == 1:
        if num == 1:
            Button1["background"]="green"
            Button1.after(2000, lambda:col1(num))
        elif num == 2:
            Button2["background"]="red"
            Button2.after(2000, lambda:col1(num))
        elif num == 3:
            Button3["background"]="blue"
            Button3.after(2000, lambda:col1(num))
        elif num == 4:
            Button4["background"]="green"
            Button4.after(2000, lambda:col1(num))
        elif num == 5:
            Button5["background"]="red"
            Button5.after(2000, lambda:col1(num))
        elif num == 6:
            Button6["background"]="blue"
            Button6.after(2000, lambda:col1(num))
        elif num == 7:
            Button7["background"]="green"
            Button7.after(2000, lambda:col1(num))
        elif num == 8:
            Button8["background"]="red"
            Button8.after(2000, lambda:col1(num))
        elif num == 9:
            Button9["background"]="blue"
            Button9.after(2000, lambda:col1(num))
        elif num == 10:
            Button10["background"]="green"
            Button10.after(2000, lambda:col1(num))
        elif num == 11:
            Button11["background"]="red"
            Button11.after(2000, lambda:col1(num))
        elif num == 12:
            Button12["background"]="blue"
            Button12.after(2000, lambda:col1(num))

    elif len(selected) >=2:
        if (selected[len(selected)-1] )!= (selected[len(selected)-2]):
            if len(selected) ==2 :
                sel = selected[0]
                return cheakvalue(num,sel)

                
            elif len(selected) >= 3 and (selected[0] != selected[1]):
                firstclick = len(selected)-2
                sel = selected[firstclick]
                selected.pop(0)
                return cheakvalue(num,sel)
                print('Array got bigger')
        else:
            selected.pop(0)
            selected.pop(len(selected)-2)
points = 0
matched = []

def col1 (num):
    
    if num == 1:
        Button1["background"]="gray"
    elif num == 2:
        Button2["background"]="gray"
    elif num == 3:
        Button3["background"]="gray"
    elif num == 4:
        Button4["background"]="gray"
    elif num == 5:
        Button5["background"]="gray"
    elif num == 6:
        Button6["background"]="gray"
    elif num == 7:
        Button7["background"]="gray"
    elif num == 8:
        Button8["background"]="gray"
    elif num == 9:
        Button9["background"]="gray"
    elif num == 10:
        Button10["background"]="gray"
    elif num == 11:
        Button11["background"]="gray"
    elif num == 12:
        Button12["background"]="gray"


def cheakvalue(num,sel):
    global points
    global matched  
    print(sel)
    # lastclick = sel[:2]
    # a = lastclick[0]
    # b = lastclick[1]
    a = num
    b = sel
    print(a,b)
    if a%3 == b%3:
        matched.append(num)
        points = points + 20

        if a == 1 or b==1:
            Button1.config(state="disabled")
            #Button1["background"]="white" 
        if a == 2 or b==2:
            Button2.config(state="disabled")
            #Button2["background"]="white" 
        if a == 3 or b==3:
            Button3.config(state="disabled")
            #Button3["background"]="white" 
        if a == 4 or b==4:
            Button4.config(state="disabled")
            #Button4["background"]="white" 
        if a == 5 or b==5:
            Button5.config(state="disabled")
            #Button5["background"]="white" 
        if a == 6 or b==6:
            Button6.config(state="disabled")
            #Button6["background"]="white" 
        if a == 7 or b==7:
            #Button7["background"]="white" 
            Button7.config(state="disabled")
        if a == 8 or b==8:
            #Button8["background"]="white" 
            Button8.config(state="disabled")
        if a == 9 or b==9:
            #Button9["background"]="white" 
            Button9.config(state="disabled")
        if a == 10 or b==10:
            #Button10["background"]="white" 
            Button10.config(state="disabled")
        if a == 11 or b==11:
            #Button11["background"]="white" 
            Button11.config(state="disabled")
        if a == 12 or b==12:
            #Button12["background"]="white" 
            Button12.config(state="disabled")
        
        
    else:
        points = points -5
        return 0
    
    print(points)

def colour(num):
    
    if num == 1 and num not in matched:
        Button1["background"]="gray" 
    elif num == 2 and num not in matched:
        Button2["background"]="gray" 
    elif num == 3 and num not in matched:
        Button3["background"]="gray" 
    elif num == 4 and num not in matched:
        Button4["background"]="gray" 
    elif num == 5 and num not in matched:
        Button5["background"]="gray" 
    elif num == 6 and num not in matched:
        Button6["background"]="gray" 
    elif num == 7 and num not in matched:
        Button7["background"]="gray" 
    elif num == 8 and num not in matched:
        Button8["background"]="gray" 
    elif num == 9 and num not in matched:
        Button9["background"]="gray" 
    elif num == 10 and num not in matched:
        Button10["background"]="gray" 
    elif num == 11 and num not in matched:
        Button11["background"]="gray" 
    elif num == 12 and num not in matched:
        Button12["background"]="gray" 

def aftertime():
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



#setting the game window
window = Tk()
window.after(100000, lambda: aftertime())
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









