from tkinter import *
import scogrub
root = Tk()
root.title("ScoreInq")
print('running')
def xianshi():
	mylist=Listbox(root)
	# for line in range(100):
		# mylist.insert(END,"this is line "+str(line))
	stunum= E1.get()
	# for line in range(100):
		# mylist.insert(END,"this is line "+str(line))
	mylist.insert(END,scogrub.DiffClass(stunum))
	mylist.grid(row=1,column=1)
InqButton = Button(root,text = '查询',command = xianshi)
InqButton.grid(row=1,column=0)
L1 = Label(root,text = 'id')
L1.grid(row=0,column=0)
E1 = Entry(root,bd = 5)
E1.grid(row=0,column=1)
# scrollbar = Scrollbar(root)
# scrollbar.grid(row=1,column=1)
d=scogrub.DiffClass(1301120172)
print (d)
root.mainloop()