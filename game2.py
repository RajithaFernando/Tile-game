from tkinter import*
import time
import random

selected = []
def match(num):
    # print(num)
    selected.append(num)
    print(selected)
    if num == 1:
        Button1["background"]="green"
        Button1.after(2000, lambda:colour(num))
    elif num == 2:
        Button2["background"]="green"
        Button2.after(2000, lambda:colour(num))
    elif num == 3:
        Button3["background"]="green"
        Button3.after(2000, lambda:colour(num))
    elif num == 4:
        Button4["background"]="green"
        Button4.after(2000, lambda:colour(num))
    elif num == 5:
        Button5["background"]="red"
        Button5.after(2000, lambda:colour(num))
    elif num == 6:
        Button6["background"]="red"
        Button6.after(2000, lambda:colour(num))
    elif num == 7:
        Button7["background"]="red"
        Button7.after(2000, lambda:colour(num))
    elif num == 8:
        Button8["background"]="red"
        Button8.after(2000, lambda:colour(num))
    elif num == 9:
        Button9["background"]="blue"
        Button9.after(2000, lambda:colour(num))
    elif num == 10:
        Button10["background"]="blue"
        Button10.after(2000, lambda:colour(num))
    elif num == 11:
        Button11["background"]="blue"
        Button11.after(2000, lambda:colour(num))
    elif num == 12:
        Button12["background"]="blue"
        Button12.after(2000, lambda:colour(num))
    if len(selected) ==2:
        return cheakvalue(num,selected)
        
    if len(selected) > 2:
        newselected = selected
        selected.pop(0)
        return cheakvalue(num,selected)
points = 0
def cheakvalue(num, sel):
    global points
    print(sel)
    lastclick = sel[:2]
    if lastclick[0] %3 == lastclick[1]%3:
        points = points + 20
    else:
        points = points -5
    print(points)

def colour(num):
    
    if num == 1:
        Button1["background"]="gray" 
    if num == 2:
        Button2["background"]="gray" 
    if num == 3:
        Button3["background"]="gray" 
    if num == 4:
        Button4["background"]="gray" 
    if num == 5:
        Button5["background"]="gray" 
    if num == 6:
        Button6["background"]="gray" 
    if num == 7:
        Button7["background"]="gray" 
    if num == 8:
        Button8["background"]="gray" 
    if num == 9:
        Button9["background"]="gray" 
    if num == 10:
        Button10["background"]="gray" 
    if num == 11:
        Button11["background"]="gray" 
    if num == 12:
        Button12["background"]="gray" 




#setting the game window
window = Tk()
# window.after(10000, lambda: aftertime())
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









