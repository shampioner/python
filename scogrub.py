#version 1.1
import urllib.request,urllib,re,_thread,time,datetime
from tkinter import *
root = Tk()
root.title("ScoreInq")
root.geometry('600x400+100+100')
classes = ["0022001","0022002","0721001","0721005","0821101","0721002","0122206","0121010","0421008","0821100","0122211","0222109","0121005","0122220","0221001","0121003","0121012","0741005","0241036","0241023","0821102","0821001","0821004","0821005"]#
infoList=[]
def ScoreGrub(StuNum,classid):
    stuid = str(int(StuNum)-8)[6:10]
    myUrl = "http://210.27.12.1:90/queryDegreeScoreAction.do?studentid=xdleess20130621zq"+stuid+"&degreecourseno="+classid
    req   = urllib.request.Request(myUrl)
    Page  = urllib.request.urlopen(req).read().decode('gbk','ignore')
    myName  = re.findall('<td width="15%">姓名：\s+(.*)\s+</td>',Page)
    mySub   = re.findall('<td width="7%" align="left">\d{4}[春秋]</td>\s<td width="16%" align="left">\s+(.*)\r',Page)
    myScore = re.findall('<td width="7%" align="left">\s+(.*)\s+</td>\s+<td width="7%" align="left">',Page)
    classScore  = re.findall('<td width="4%" align="left">(.*)</td>',Page) 
    if(len(mySub) == 1):
        infoList.append("姓名：%s  科目：%s  成绩：%s  学分：%s"%(myName[0],mySub[0],myScore[0],classScore[0]))
    elif(len(mySub) == 2):
        infoList.append("姓名：%s  科目：%s  成绩：%s  学分：%s"%(myName[0],mySub[0],myScore[0],classScore[0]))
        infoList.append("姓名：%s  科目：%s  成绩：%s  学分：%s"%(myName[0],mySub[1],myScore[1],classScore[1]))
def DiffStu(first_num,count):
    for i in range(count):
        for classid in classes:
            ScoreGrub(str(first_num+i),classid)
def DiffClass(StuNum):
    for classid in classes:
        ScoreGrub(StuNum,classid)
#tkinter
L1 = Label(root,text = '学号')
L1.grid(row=0,column=0)
E1 = Entry(root,bd = 5,width=40)
E1.grid(row=0,column=1)
def listBox():
    mylist=Listbox(root,width=80,height=20)
    stu_num=E1.get()
    DiffClass(stu_num)
    for num in range(len(infoList)):
        mylist.insert(END,infoList[0])
        del infoList[0]
    mylist.grid(row=1,column=1)
InqButton = Button(root,text = '查询',command = listBox)
InqButton.grid(row=1,column=0)

root.mainloop()