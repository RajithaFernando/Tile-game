from tkinter import*
import time
import random
import numpy as np
import numpy.random
#setting the game window
window = Tk()
window.title("ABC pair game")

#setting the frame
topFrame = Frame(window)
topFrame.pack()
topDown = Frame(window)
topDown.pack()
topBottom = Frame(window)
topBottom.pack()

# Creating the buttons
# Button1 = Button(topFrame,  height=5, width=12, bg='lightblue')
# Button2 = Button(topFrame,  height=5, width=12, bg='lightblue' )
# Button3 = Button(topFrame,  height=5, width=12, bg='lightblue')
# Button4 = Button(topFrame,  height=5, width=12, bg='lightblue')
# Button5 = Button(topDown, height=5, width=12, bg='red')
# Button6 = Button(topDown, height=5, width=12,  bg='red'  )
# Button7 = Button(topDown, height=5, width=12,  bg='red')
# Button8 = Button(topDown, height=5, width=12,  bg='red')
# Button9 = Button(topBottom, height=5, width=12,  bg='green')
# Button10 = Button(topBottom, height=5, width=12, bg='green')
# Button11 = Button(topBottom, height=5, width=12, bg='green')
# Button12 = Button(topBottom, height=5, width=12, bg='green')


# Button1.pack(side = LEFT)
# Button2.pack(side = LEFT)
# Button3.pack(side = LEFT)
# Button4.pack(side = LEFT)
# Button5.pack(side = LEFT)
# Button6.pack(side = LEFT)
# Button7.pack(side = LEFT)
# Button8.pack(side = LEFT)
# Button9.pack(side = LEFT)
# Button10.pack(side = LEFT)
# Button11.pack(side = LEFT)
# Button12.pack(side = LEFT)

# nums1 = [1,2,3,4,5,6,7,8,9,10,11,12]

arr = np.arange(12)
np.random.shuffle(arr)
# print(arr)
# num2 = np.random.shuffle(nums1)
# print(num2)
# num = random.shuffle(nums1)

col = ["lightblue", "green", "red"]

# for j in col:
#     for i in nums:
#         if num <5:
#             Button1 = Button(topFrame,  height=5, width=12, bg=j)
#             Button1.pack(side = LEFT)
#         if num <9:
#             Button1 = Button(topDown,  height=5, width=12, bg=j)
#             Button1.pack(side = LEFT)

#         if num < 13:
#             Button1 = Button(topBottom,  height=5, width=12, bg=j)
#             Button1.pack(side = LEFT)
#     break
    
#     num = num + 1

for i in arr2:
    j = i %3
    if j == 0:
        Button1 = Button(topFrame,  height=5, width=12, bg=col[j])
        Button1.pack(side = LEFT)
    elif j==1:
        Button1 = Button(topDown,  height=5, width=12, bg=col[j])
        Button1.pack(side = LEFT)
    else:
        Button1 = Button(topBottom,  height=5, width=12, bg=col[j])
        Button1.pack(side = LEFT)
        

    


window.mainloop()









