from tkinter import *
from solver import solvr
root = Tk()
root.title("Sudoku Solver")
root.geometry("324x550")

label = Label(root,text="Fill in the numbers and click solve").grid(row=0,column = 1,columnspan = 10)

errlabel = Label(root,text = "",fg = "red")
errlabel.grid(row = 15,column = 0,columnspan = 15, pady = 5)
solvedlabel = Label(root,text = "",fg = "green")
solvedlabel.grid(row = 15,column = 0,columnspan = 15,pady = 5)

cell = {}
def ValidateNum(P):
    out = (P.isdigit() or P == "") and len(P)<2
    return out

reg = root.register(ValidateNum)

def draw3X3(row,column,bgcolor):
    for i in range(3):
        for j in range(3):
            e = Entry(root,width = 5,bg = bgcolor,justify="center",validate ="key",validatecommand=(reg,"%P"))
            e.grid(row = row+i+1,column = column+j+1,sticky ="nsew",padx = 1,pady=1,ipady =5)
            cell[(row+i+1),column+j+1] = e

def draw9X9():
    color = "#D0ffff"
    for rowno in range(1,10,3):
        for colno in range(0,9,3):
            draw3X3(rowno,colno,color)
            if color =="#D0ffff":
                color = "#ffffd0"
            else:
                color = "#D0ffff"
def clearValues():
    errlabel.configure(text = "")
    solvedlabel.configure(text="")
    for row in range(2,11):
        for col in range(1,10):
            c = cell[(row,col)]
            c.delete(0,"end")

def getValues():
    board =[]
    errlabel.configure(text = "")
    solvedlabel.configure(text = "")
    for row in range(2,11):
        rows = []
        for col in range(1,10):
            val = cell[(row,col)].get()
            if val =="":
                rows.append(0)
            else:
                rows.append(int(val))
        board.append(rows)
    updateValues(board)
btn1 = Button(root,command =getValues,text = "Solve",width = 10).grid(row =20,column=1,columnspan = 5,pady =20)
btn2 = Button(root,command =clearValues,text = "Clear",width = 10).grid(row =20,column=5,columnspan = 5,pady =20)

def updateValues(s):
    sol = solvr(s)
    if sol!="no":
        for rows in range(2,11):
            for col in range(1,10):
                cell[(rows,col)].delete(0,"end")
                cell[(rows,col)].insert(0,sol[rows-2][col-1])
        solvedlabel.configure(text = "Sudoku Solved!")
    else:
        errlabel.configure(text = "No solution ")

draw9X9()
root.mainloop()
