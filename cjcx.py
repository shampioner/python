import urllib.request,urllib,re,_thread,time

class Spider_Model:
    def __init__(self):
        print ('running...')
        '''self.page=1
        self.pages=[]
        self.enable=False'''

    def GetPage(self):#,page):
        myUrl="http://210.27.12.1:90/queryDegreeScoreAction.do?studentid=xdleess20130621zq0164&degreecourseno=0821005"#+page
        #user_agent='Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
        #headers={'User-Agent':user_agent}
        req=urllib.request.Request(myUrl)#,headers=headers)
        myResponse=urllib.request.urlopen(req)
        myPage=myResponse.read()
        unicodePage=myPage.decode('utf-8','ignore')
        #print (5)
        
        #p=re.compile(r'\r\n                                \d+\r\n                            \r\n')
        #myItems=re.findall('<td width="7%" align="left">\s+(\d+\.?\d?)\s+</td>',myPage,re.S)
        #myItems=re.findall('<td width="7%" align="left">\s+(.*?)\s+</td>',myPage,re.S)

       '''items=[]
        for item in myItems:
            #print (items)
            items.append([item[0].replace("\n",""),item[1].replace("\n","")])
        return items     
    def LoadPage(self):
        while self.enable:
            if len(self.pages)<2:
                try:
                    myPage=self.GetPage(str(self.page))
                    self.page += 1
                    self.pages.append(myPage)
                except:
                    print ('无法连接糗事百科')
            else:
                time.sleep(1)

    def ShowPage(self,nowPage,page):
        for items in nowPage:
            print ('第%d页'%page,items[0],items[1])
            myInput=input()
            if myInput == "quit":
                self.enable = False
                break

    def Start(self):
        self.enable=True
        page=self.page
        print ('正在加载中请稍后......')
        _thread.start_new_thread(self.LoadPage,())

        while self.enable:
            if self.pages:
                nowPage=self.pages[0]
                del self.pages[0]
                self.ShowPage(nowPage,page)
                page += 1'''

print ("""
------------------------------------
    程序 糗百爬虫
    版本 v1.0
    操作：输入quit退出
    功能：按下回车依次浏览
------------------------------------
""")
#print ('请输入学号：')
#input('')
print ('start')
myModel=Spider_Model()
#myModel.Start()
myModel.GetPage()
