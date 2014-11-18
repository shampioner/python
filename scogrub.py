import urllib.request,urllib,re,_thread,time,datetime
classes = ["0022001","0022002","0721001","0721005","0821101","0721002","0122206","0121010","0421008","0821100","0122211","0222109","0121005","0122220","0221001","0121003","0121012","0741005","0241036","0241023","0821102","0821001","0821004","0821005"]#
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
        print ("姓名：%s\t科目：%s\t成绩：%s\t学分：%s"%(myName[0],mySub[0],myScore[0],classScore[0]))
    elif(len(mySub) == 2):
        print ("姓名：%s\t科目：%s\t成绩：%s\t学分：%s"%(myName[0],mySub[0],myScore[0],classScore[0]))
        print ("姓名：%s\t科目：%s\t成绩：%s\t学分：%s"%(myName[0],mySub[1],myScore[1],classScore[1]))
def DiffStu(first_num,count):
    for i in range(count):
        for classid in classes:
            ScoreGrub(str(first_num+i),classid)
def DiffClass(StuNum):
    for classid in classes:
        ScoreGrub(StuNum,classid)
def Hello():
	print ('hello world')
# DiffStu(1301120172,1)
DiffClass(1301120172)
# input('Enter')
