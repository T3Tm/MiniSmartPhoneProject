'''
320 x 640 크기


#첫 번째
전화를 눌렀을 때는

버튼 14개 만들어야 되고
Entry 칸 있어야함.

ctrl k , ctrl 0 전부 숨기기
ctrl k , ctrl j 전부 펼치기
계산기

a + b  아님
'''
from tkinter import *
def isMinusinsert(wordlen):
    if wordlen==3:return True
    elif wordlen==8:return True
    return False
def showone():
    global preword
    if isMinusinsert(len(preword)):
        preword+='-1'
        TextLabel.configure(text=preword)
    else:
        preword+='1'
        TextLabel.configure(text=preword)
def showtwo():
    global preword
    if isMinusinsert(len(preword)):
        preword+='-2'
        TextLabel.configure(text=preword)
    else:
        preword+='2'
        TextLabel.configure(text=preword)
def showthree():
    global preword
    if isMinusinsert(len(preword)):
        preword+='-3'
        TextLabel.configure(text=preword)
    else:
        preword+='3'
        TextLabel.configure(text=preword)
def showfour():
    global preword
    if isMinusinsert(len(preword)):
        preword+='-4'
        TextLabel.configure(text=preword)
    else:
        preword+='4'
        TextLabel.configure(text=preword)
def showfive():
    global preword
    if isMinusinsert(len(preword)):
        preword+='-5'
        TextLabel.configure(text=preword)
    else:
        preword+='5'
        TextLabel.configure(text=preword)
def showsix():
    global preword
    if isMinusinsert(len(preword)):
        preword+='-6'
        TextLabel.configure(text=preword)
    else:
        preword+='6'
        TextLabel.configure(text=preword)
def showseven():
    global preword
    if isMinusinsert(len(preword)):
        preword+='-7'
        TextLabel.configure(text=preword)
    else:
        preword+='7'
        TextLabel.configure(text=preword)
def showeight():
    global preword
    if isMinusinsert(len(preword)):
        preword+='-8'
        TextLabel.configure(text=preword)
    else:
        preword+='8'
        TextLabel.configure(text=preword)
def shownine():
    global preword
    if isMinusinsert(len(preword)):
        preword+='-9'
        TextLabel.configure(text=preword)
    else:
        preword+='9'
        TextLabel.configure(text=preword)
def showzero():
    global preword
    if isMinusinsert(len(preword)):
        preword+='-0'
        TextLabel.configure(text=preword)
    else:
        preword+='0'
        TextLabel.configure(text=preword)
def showstar():
    global preword
    if isMinusinsert(len(preword)):
        preword+='-*'
        TextLabel.configure(text=preword)
    else:
        preword+='*'
        TextLabel.configure(text=preword)
def showpound():
    global preword
    if isMinusinsert(len(preword)):
        preword+='-#'
        TextLabel.configure(text=preword)
    else:
        preword+='#'
        TextLabel.configure(text=preword)


def cal(a,b,token):
    try:
        calNumber=eval(a+token+b)
    except ZeroDivisionError:
        calNumber='오류'
    return f'{calNumber}'
def mulply():
    global token
    token='*'
def percent():
    preValue=TextLabel.cget('text')
    TextLabel.configure(text=cal(preValue,f'{0.01}','*'))
def divide():
    global token
    token='//'
def minus():
    global token
    token='-'
def plus():
    global token
    token='+'
def equls():
    global token,secondNumber,firstNumber
    if token:
        if secondNumber:
            value=cal(firstNumber,secondNumber,token)
            TextLabel.configure(text=value)
        else:
            secondNumber=firstNumber
            TextLabel.configure(text=cal(firstNumber,secondNumber,token))

     
def plusminus(): 
    global token,firstNumber,secondNumber
    preValue=TextLabel.cget('text')
    calnumber=cal(preValue,f'{-1}','*')
    if preValue!='0':
        TextLabel.configure(text=calnumber)
    if token:
        secondNumber=calnumber
    else:
        firstNumber=calnumber
def comma():
    global iscomma,firstNumber,secondNumber,token
    if iscomma==False:
        iscomma=True
        preValue=TextLabel.cget('text')
        TextLabel.configure(text=preValue+'.')
        if token:
            secondNumber+='.'
        else:
            firstNumber+='.'
def allclear():
    global iscomma,firstNumber,secondNumber,token
    token=None
    firstNumber='0'
    secondNumber=None
    iscomma=False
    TextLabel.configure(text='0',anchor='e')

def calzero():
    global firstNumber,secondNumber,token
    preValue= TextLabel.cget('text')
    num='0'
    if token==None:#token이 정해지기 전
        if preValue!='0':
            TextLabel.configure(text=preValue+num)
            firstNumber+=num
    else:#정해진 후
        if secondNumber!=None:
            TextLabel.configure(text=secondNumber+num)
            secondNumber+=num
        else:
            TextLabel.configure(text=num)
            secondNumber=num
def calone():
    global firstNumber,secondNumber,token
    preValue= TextLabel.cget('text')
    num='1'
    if token==None:#token이 정해지기 전
        if preValue!='0':
            TextLabel.configure(text=preValue+num)
            firstNumber+=num
        else:
            TextLabel.configure(text=num)
            firstNumber=num
    else:#정해진 후
        if secondNumber!=None:
            TextLabel.configure(text=secondNumber+num)
            secondNumber+=num
        else:
            TextLabel.configure(text=num)
            secondNumber=num
def caltwo():
    global firstNumber,secondNumber,token
    preValue= TextLabel.cget('text')
    num='2'
    if token==None:#token이 정해진 전
        if preValue!='0':
            TextLabel.configure(text=preValue+num)
            firstNumber+=num
        else:
            TextLabel.configure(text=num)
            firstNumber=num
    else:#정해지기 후
        if secondNumber!=None:
            TextLabel.configure(text=secondNumber+num)
            secondNumber+=num
        else:
            TextLabel.configure(text=num)
            secondNumber=num
def calthree():
    global firstNumber,secondNumber,token
    preValue= TextLabel.cget('text')
    num='3'
    if token==None:#token이 정해지기 전
        if preValue!='0':
            TextLabel.configure(text=preValue+num)
            firstNumber+=num
        else:
            TextLabel.configure(text=num)
            firstNumber=num
    else:#정해진 후
        if secondNumber!=None:
            TextLabel.configure(text=secondNumber+num)
            secondNumber+=num
        else:
            TextLabel.configure(text=num)
            secondNumber=num
def calfour():
    global firstNumber,secondNumber,token
    preValue= TextLabel.cget('text')
    num='4'
    if token==None:#token이 정해지기 전
        if preValue!='0':
            TextLabel.configure(text=preValue+num)
            firstNumber+=num
        else:
            TextLabel.configure(text=num)
            firstNumber=num
    else:#정해진 후
        if secondNumber!=None:
            TextLabel.configure(text=secondNumber+num)
            secondNumber+=num
        else:
            TextLabel.configure(text=num)
            secondNumber=num
def calfive():
    global firstNumber,secondNumber,token
    preValue= TextLabel.cget('text')
    num='5'
    if token==None:#token이 정해지기 전
        if preValue!='0':
            TextLabel.configure(text=preValue+num)
            firstNumber+=num
        else:
            TextLabel.configure(text=num)
            firstNumber=num
    else:#정해진 후
        if secondNumber!=None:
            TextLabel.configure(text=secondNumber+num)
            secondNumber+=num
        else:
            TextLabel.configure(text=num)
            secondNumber=num
def calsix():
    global firstNumber,secondNumber,token
    preValue= TextLabel.cget('text')
    num='6'
    if token==None:#token이 정해지기 전
        if preValue!='0':
            TextLabel.configure(text=preValue+num)
            firstNumber+=num
        else:
            TextLabel.configure(text=num)
            firstNumber=num
    else:#정해진 후
        if secondNumber!=None:
            TextLabel.configure(text=secondNumber+num)
            secondNumber+=num
        else:
            TextLabel.configure(text=num)
            secondNumber=num
def calseven():
    global firstNumber,secondNumber,token
    preValue= TextLabel.cget('text')
    num='7'
    if token==None:#token이 정해지기 전
        if preValue!='0':
            TextLabel.configure(text=preValue+num)
            firstNumber+=num
        else:
            TextLabel.configure(text=num)
            firstNumber=num
    else:#정해진 후
        if secondNumber!=None:
            TextLabel.configure(text=secondNumber+num)
            secondNumber+=num
        else:
            TextLabel.configure(text=num)
            secondNumber=num
def caleight():
    global firstNumber,secondNumber,token
    preValue= TextLabel.cget('text')
    num='8'
    if token==None:#token이 정해지기 전
        if preValue!='0':
            TextLabel.configure(text=preValue+num)
            firstNumber+=num
        else:
            TextLabel.configure(text=num)
            firstNumber=num
    else:#정해진 후
        if secondNumber!=None:
            TextLabel.configure(text=secondNumber+num)
            secondNumber+=num
        else:
            TextLabel.configure(text=num)
            secondNumber=num
def calnine():
    global firstNumber,secondNumber,token
    preValue= TextLabel.cget('text')
    num='9'
    if token==None:#token이 정해지기 전
        if preValue!='0':
            TextLabel.configure(text=preValue+num)
            firstNumber+=num
        else:
            TextLabel.configure(text=num)
            firstNumber=num
    else:#정해진 후
        if secondNumber!=None:
            TextLabel.configure(text=secondNumber+num)
            secondNumber+=num
        else:
            TextLabel.configure(text=num)
            secondNumber=num

def Allunmap():#모든 버튼 일시적으로 숨기기
    callButton.place_forget()
    contactsButton.place_forget()
    calculatorButton.place_forget()  
def AllButtonMap():#모든 버튼 나타나게 하기
    callButton.place(x=35,y = 495)
    contactsButton.place(x=130,y = 495)
    calculatorButton.place(x=230,y = 490)
def callActivate():
    global preword
    Allunmap()
    preword=''
    TextLabel.place(x=35,y=95,width=250,height=115)
    TextLabel.configure(anchor=CENTER)
    x_loc,y_loc=35,210
    for button in numbers:#버튼 배치
        button.place(x=x_loc,y=y_loc)
        x_loc+=85
        if x_loc == 290:
            x_loc=35
            y_loc+=83
    idx=0
    for define in defines:
        numbers[idx].configure(command=define)
        idx+=1
def contactsActivate():
    Allunmap()

def calculatorActivate():
    global token,secondNumber,firstNumber,iscomma
    Allunmap()
    TextLabel.place(x=35,y=95,width=250,height=115)
    TextLabel.configure(text='0', anchor='e')
    x_loc,y_loc=35,210
    for button in calculatornumber:
        button.place(x=x_loc,y=y_loc)
        x_loc+=63
        if x_loc==287:
            y_loc+=67
            x_loc=35
    idx=0
    for define in caldefine:
        calculatornumber[idx].configure(command=define)
        idx+=1
    firstNumber='0'
    token=None
    secondNumber=None
    iscomma=False


def homeButton():
    TextLabel.configure(text='')
    AllButtonMap()
    for button in numbers: #call에 버튼들 화면에서 지우기
        button.place_forget()
    TextLabel.place_forget() #Label 화면에서 지우기
    for button in calculatornumber: #계산기 버튼들 화면에서 지우기
        button.place_forget()
root=Tk()
root.title('small SmartPhone')

#사진
smart = PhotoImage(file="smartPhone.png")
call = PhotoImage(file="call.png")
contacts = PhotoImage(file="contacts.png")
calculator=PhotoImage(file='calculator.png')
bg=PhotoImage(file='bg.png')
home=PhotoImage(file='home.png')

#라벨
phoneLabel = Label(root,image=smart)
bgLabel = Label(root,image=bg)
TextLabel = Label(root,font=("굴림",22,'bold'))

phoneLabel.pack()
bgLabel.place(x=35,y=95)

#버튼
callButton = Button(root,text='전화',image=call,command=callActivate)
contactsButton = Button(root,text='주소록',image=contacts,command=contactsActivate)
calculatorButton = Button(root,text='계산기',image=calculator,command=calculatorActivate)
numbers=[]
for i in range(1,10):#숫자 1번부터 9번까지
    numbers.append(Button(root,width=8,height=6,text=f'{i}',font=("굴림",10,'bold')))
numbers.append(Button(root,width=8,height=6,text='*',font=("굴림",10,'bold')))
numbers.append(Button(root,width=8,height=6,text='0',font=("굴림",10,'bold')))
numbers.append(Button(root,width=8,height=6,text='#',font=("굴림",10,'bold')))

calculatornumber=[]
Buttonarr=['AC','+/-','%','/'
           ,'7','8','9','x'
           ,'4','5','6','-'
           ,'1','2','3','+'
           ,'0','.','=']
for i in Buttonarr:
    calculatornumber.append(Button(root,width=6,height=5,text=i,font=("굴림",10,'bold')))


homeButton = Button(root,image=home,command=homeButton)
homeButton.place(x=126,y=550)

#함수들
defines = [showone,showtwo,showthree,showfour,showfive,showsix,showseven
           ,showeight,shownine,showstar,showzero,showpound]
caldefine=[allclear,plusminus,percent,divide,
           calseven,caleight,calnine,mulply,
           calfour,calfive,calsix,minus,
           calone,caltwo,calthree,plus,
           calzero,comma,equls]


AllButtonMap()
root.mainloop()