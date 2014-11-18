'''class Student(object):
    def __init__(self,name,score):
        self.__name = name
        self.__score = score
        
    def print_score(self):
        print '%s:%s' %(self.__name,self.__score)

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('bart simpon',98)
#bart.score = 50
bart.print_score()
print '%s''s grade is %s' %(bart.name,bart.get_grade())
lisa = Student('lisa simoj',87)
lisa.print_score()'''

'''
class Animal(object):
    def run(self):
        print 'Animal is running...'

class Dog(Animal):
    def run(self):
        print 'Dog is running...'
    def eat(self):
        print 'Eating meat'
class Cat(Animal):
    def run(self):
        print 'Cat is running...'

class Tortoise(Animal):
    def run(self):
        print 'Tortoise is running slowly...'
def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Tortoise())'''
'''
class Student(object):
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer!')
        if value < 0 or value >100:
            raise ValueError('score must be 0~100!')
        self._score = value
s= Student()
s.score=60
print s.score'''
'''
#animal
class Animal(object):
    pass
#大类
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
#各种动物
class Dog(Mammal):
    pass
class Bat(Mammal):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass
class Runnable(object):
    def run(self):
        print 'running...'
class Flyable(object):
    def fly(self):
        print 'flying...'
class Dog(Mammal,Runnable):
    pass
class Bat(Mammal,Flyable):
    pass
'''
'''
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1
    def __iter__(self):
        return self
    def next(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>1000000:
            raise StopIteration()
        return self.a

for n in Fib():
    print n
'''
'''
#urllib2
from urllib2 import Request, urlopen, URLError, HTTPError  
old_url = 'http://www.baidu.com/'
req = Request(old_url)
response = urlopen(req)
print 'Info():'
print response.info()
'''
'''
import string,urllib2

def baidu_tieba(url,begin_page,end_page):
    for i in range(begin_page,end_page+1):
        sName = string.zfill(i,5)+'.html'
        print '正在下载第' + str(i) + '个网页，并存储为'+sName
        f=open(sName,'w+')
        m=urllib2.urlopen(url+str(i)).read()
        f.write(m)
        f.close()

begin_page = 1
end_page = 6
burl= 'http://tieba.baidu.com/p/2296017831?pn='
baidu_tieba(burl,begin_page,end_page)
'''

import urllib.request,urllib,re,_thread,time

class Spider_Model:
    def __init__(self):
        self.page=1
        self.pages=[]
        self.enable=False

    def GetPage(self,page):
        myUrl="http://m.qiushibaike.com/hot/page/"+page
        user_agent='Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
        headers={'User-Agent':user_agent}
        req=urllib.request.Request(myUrl,headers=headers)
        myResponse=urllib.request.urlopen(req)
        myPage=myResponse.read()
        unicodePage=myPage.decode("utf-8")

        myItems=re.findall('<div.*?class="content".*?title="(.*?)">(.*?)</div>',unicodePage,re.S)
        items=[]
        for item in myItems:
            print (items)
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
                page += 1

print ("""
------------------------------------
    程序 糗百爬虫
    版本 v1.0
    操作：输入quit退出
    功能：按下回车依次浏览
------------------------------------
""")
print ('请按下回车浏览今日的糗百内容：')
input('')
myModel=Spider_Model()
myModel.Start()
