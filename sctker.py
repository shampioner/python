from tkinter import *
import scogrub
root = Tk()
root.title("ScoreInq")
print('running')
def xianshi():
    mylist=Listbox(root)
    mm=E1.get()
    scogrub.DiffClass(mm)
    for line in kgkg:
        mylist.insert(END,line)
    # mylist.bind('',scogrub.DiffClass(mm))
    # mylist.insert(END,tt)
    # mylist.insert(END,scogrub.DiffClass(stunum))
    mylist.grid(row=1,column=1)
InqButton = Button(root,text = '查询',command = xianshi)
InqButton.grid(row=1,column=0)
L1 = Label(root,text = 'id')
L1.grid(row=0,column=0)
E1 = Entry(root,bd = 5)
E1.grid(row=0,column=1)
# scrollbar = Scrollbar(root)
# scrollbar.grid(row=1,column=1)
root.mainloop()