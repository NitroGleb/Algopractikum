from PyQt6 import uic, QtCore
from PyQt6.QtWidgets import QApplication
from random import *
from time import *

Form, Window = uic.loadUiType("Qt1better.ui")
def start():    
    global Form, Window, window, form
    window = Window()
    form = Form()
    form.setupUi(window)
    if form.pushButton.clicked.connect:
        Form, Window = uic.loadUiType("Qt2better.ui")
def next3():
    global Form, Window, window, form
    Form, Window = uic.loadUiType("Qt2better.ui")
    window = Window()
    form = Form()
    form.setupUi(window)


question = ["Вы любите физическую активность?",
"Вы увлекаетесь чтением?",
"Вы часто задумываетесь о смысле жизни",
"Вы обмениваетесь чем то?",
"Вы инересутесь командными играми?",
"Вы интересуетесь музыкой?",
"Вы умело собираете модели?",
"Вам нравиться играть в видео-игры?",
"Вы умеете выращивать растения?",
"Вы любите математику?",
"Вы любите работать сами?",
"Вам нравиться плавать на байдарке?",
"Вы любите работать в команде?",
"Вы увлекаетесь бизнесом?",
"Вы любите природу?",
"Вы любите гулять с друзьями?",
"Вы увлекаетесь пением?",
"Вы увлекаетесь разгадкой шифров или кроссвордов?",
"Вы часто изменяете что-то в себе или в чём то другом?",
"Вы думаете о том, кем хотели бы стать?",
"Вы увлекаетесь логическими задачами?",
"Вы интересуетесь танцами?",
"Вы часто конфликтуете?",
"Вы общительный человек?",
"Вы щедрый человек?",
"Вы стремитесь к справедливости?",
"Вы терпеливый человек?",
"Вы легко обучаетесь физическим навыкам?",
"Вы играете на музыкальных инструментах?",
"У вас есть домашнее животное?",
"Вы любите разгадывать головоломки?",
"Вы можете сразу узнать песню и отличить ее от другой?",
"Вы увлекаетесь стратегическими играми?",
"Вы хорошо запоминаете имена или факты?",
"Вы любите дарить что либо?",
"Вы часто задумываетесь о торговле?",
"Вы умете убеждать людей в чём либо?",
"Вы отстаиваете свои убеждения?",
"Вы любите отдавать что-то кому-то?",
"Вы доверяете людям?",
"Вы хорошо запоминаете лейт-мотив музыки?",	
"Вы любите гулять по лесу одному?",			
"Вы любите расказывать анекдоты?",
"Вы обдумываете что вы рисуете?",
"Вы любите рисовать пейзажи?",	
"Вы от скуки считаете до опр. числа?",
"Любите слушать звуки природы?",	
"Любите слушать звуки животных?",
"Вы умеете читать ноты?",
"Вы любите животных?",		
"Вы запоминаете школьный материал при помощи картинок и образов?",
"У вас большой словарный запас?",	
"Вас увлекают иностранные языки?",
"Вы сочиняете свою музыку или рэп?",
"Вы улавливаете ритм в окружающих тебя звука?",
"Вы любишь играть в спектаклях?",		
"У вас хорошая координация движений и реакция?",		
"Вы пишите без ошибок?",
"Ваш компьютер не только для игр?",
"Вы любите химию?",
"Вы любите делать зарядку?",		
"Любите смотреть оперы, спектакли и т.п.?",			
"Вы ходите по комнате, когда думаете?",		
"Движения помогают вам лучше запоминать информацию?",
"Вы умеете делать реалистичные и подробные зарисовки?",			
"Вы умело подмечаете различные детали в людях?",		
"Вы любите рисовать что-то у друга в тетради?"]
rofl_question = ["Вы из города Ещкерестан?", "Вы являетесь Владиславом Поляковым?", "Вам понравилось?"]

tipe = 0
tipe2 = 0
tipe3 = 0
tipe4 = 0

_translate = QtCore.QCoreApplication.translate
def randomiser():
    global Form, Window, window, form
    Form, Window = uic.loadUiType("Qt2better.ui")
    window = Window()
    form = Form()
    form.setupUi(window)
    shuffle(question)
    random_index = randint(0, len(question) - 1)
    random_element = question[random_index]
    question.pop(random_index)
    form.label_2.setText(_translate("Dialog", random_element))
    
def rofl_randomiser():
    global Form, Window, window, form
    Form, Window = uic.loadUiType("Qt2better.ui")
    window = Window()
    form = Form()
    form.setupUi(window)
    shuffle(rofl_question)
    random_index2 = randint(0, len(rofl_question) - 1)
    random_element2 = rofl_question[random_index2]
    rofl_question.pop(random_index2)
    form.label_2.setText(_translate("Dialog", random_element2))
    

def questions():   
    if next() and form.pushButton.clicked.connect or form.pushButton_2.clicked.connect:
        pass
        

def points():
    pass
def next2():
    global Form, Window, window, form
    Form, Window = uic.loadUiType("Qt3better.ui")
    window = Window()
    form = Form()
    form.setupUi(window)
    window.show()
def next():
    if question != []:
        randomiser()
        form.pushButton.clicked.connect(lambda: next())
        form.pushButton_2.clicked.connect(lambda: next())
        form.pushButton.clicked.connect(lambda: questions())
        form.pushButton_2.clicked.connect(lambda: questions())
        # form.pushButton.clicked.connect(lambda: result())
        # form.pushButton.clicked.connect(lambda: result())
    if question == [] and rofl_question != []:
        rofl_randomiser()
        form.pushButton.clicked.connect(lambda: next())
        form.pushButton_2.clicked.connect(lambda: next())
        form.pushButton.clicked.connect(lambda: questions())
        form.pushButton_2.clicked.connect(lambda: questions())
    if question == [] and rofl_question == []:
        next2()

    window.show()
 

# def choose():
#     if form.pushButton.clicked.connect:
#         if question[5] or question[10] or question[15] or question[20] or question[25] or question[30] or question[35] or question[40] or question[2]:
#             tipe += 1
#         if question[3] or question[4] or question[6] or question[7] or question[9] or question[11] or question[12] or question[13] or question[14] or question[8]:
#             tipe2 += 1
#         if question[16] or question[17] or question[18] or question[19] or question[21] or question[22] or question[23] or question[24] or question[26] or question[27]:
#             tipe3 += 1
#         if question[28] or question[29] or question[31] or question[32] or question[33] or question[34] or question[36] or question[37] or question[38] or question[39]:
#             tipe4 += 1                                                                                                                                                                                              

# def result():
#     if tipe>tipe2 and tipe>tipe3 and tipe>tipe4:
#         form.label_3.setText('dvbybfgj')
#     if tipe2>tipe and tipe2>tipe3 and tipe2>tipe4:
#         form.label_3.setText('dvbybfgj')
#     if tipe3>tipe and tipe3>tipe2 and tipe3>tipe4:
#         form.label_3.setText('dvbybfgj')
#     if tipe4>tipe and tipe4>tipe3 and tipe4>tipe2:
#         form.label_3.setText('dvbybfgj')

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)


form.pushButton.clicked.connect(lambda: next())
form.pushButton.clicked.connect(lambda: next2())
form.pushButton.clicked.connect(lambda: next2())
# form.pushButton.clicked.connect(lambda: result())
# form.pushButton.clicked.connect(lambda: result())


window.show()
app.exec()