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


verbalniy = "Вы увлекаетесь чтением?", "Вы инересуютесь командными играми?", "Вы увлекаетесь разгадкой шифров или кроссвордов?", "Вы хорошо запоминаете имена или факты?", "Вы умете убеждать людей в чём либо?", "Вы любите расказывать анекдоты?", "Вы от скуки считаете до опр. числа?", "Вы умеете читать ноты?", "У вас большой словарный запас?", "Вы пишете без ошибок?"
musical = "Вы интересуетесь музыкой?", "Вы увлекаетесь пением?", "Вы играете на музыкальных инструментах?", "Вы хорошо запоминаете лейт-мотив музыки?", "Любите слушать звуки природы?", "Любите слушать звуки животных?", "Вы умеете читать ноты?", "Вы сочиняете свою музыку или рэп?", "Вы улавливаете ритм в окружающих тебя звука", "ы можете сразу узнать песню и отличить ее от другой?"
logicheskiy = "Вы увлекаетесь разгадкой шифров или кроссвордов?", "Вы увлекаетесь логическими задачами?", "Вы любите математику?", "Вы любите разгадывать головоломки?", "Вы увлекаетесь стратегическими играми?", "Вы от скуки считаете до опр. числа?", "Вы умеете читать ноты?", "Вы запоминаете материал лучше с картинками?", "Ваш компьютер не только для игр?", "Вы любите химию?"
obrazniy = "Вы умело собираете модели?", "Вам нравится играть в видео-игры?", "Вы любите дарить что либо?", "Вы скрываете свои рисунки от других?", "Вы обдумываете что вы рисуете?","Вы любите рисовать пейзажи?", "Вы запоминаете материал лучше с картинками?", "Вы умеете делать реалистичные и подробные зарисовки?", "Вы умело подмечаете различные детали в людях?", "Вы любите рисовать что-то у друга в тетради?;)"
telesniy = "Вы любите физическую активность?", "Вам нравиться плавать на байдарке?", "Вы интересуетесь танцами?", "Вы легко обучаетесь физическим навыкам?", "Вы любишь играть в спектаклях?","У вас хорошая координация движений и реакция?", "Вы любите делать зарядку?", "Любите смотреть оперы, спектакли и т.п.?", "Вы ходите по комнате, когда думаете?", "Движения помогают вам лучше запоминать информацию?"
socialniy = "Вы обмениваетесь чем то?", "Вам нравится играть в видео-игры?", "Вы любите работать в команде?", "Вы любите гулять с друзьями?", "Вы часто конфликтуете?","Вы общительный человек?", "Вы хорошо запоминаете имена или факты?", "Вы любите дарить что либо?", "Вы доверяете людям?", "Вы любите расказывать анекдоты?"
vnutreniy = "Вы часто задумываетесь о смысле жизни", "Вы любите работать сами?", "Вы часто изменяете что-то в себе или в чём то другом?", "Вы думаете о том, кем хотели бы стать?", "Вы стремитесь к справедливости?","Вы терпеливый человек?", "Вы отстаиваете свои убеждения?", "Вы скрываете свои рисунки от других?", "Вы любите гулять по лесу одному?", "Вы любите животных?"
nature = "Вы умеете выращивать растения?", "Вам нравиться плавать на байдарке?", "Вы любите природу?", "У вас есть домашнее животное?", "Вы любите гулять по лесу одному?","Вы любите рисовать пейзажи?", "Любите слушать звуки природы?", "Любите слушать звуки животных?", "Вы любите животных?", "Вы любите химию?"
filosovskiy = "Вы часто задумываетесь о смысле жизни", "Вы любите математику?", "Вы думаете о том, кем хотели бы стать?", "Вы увлекаетесь логическими задачами?", "Вы часто задумываетесь о торговле?","Вы хорошо запоминаете лейт-мотив музыки?", "Вы любите расказывать анекдоты?", "Вы обдумываете что вы рисуете?", "Вы запоминаете материал лучше с картинками?", "У вас большой словарный запас?"


teacher = "Вы увлекаетесь чтением?", "Вы часто задумываетесь о смысле жизни", "Вы интересуетесь музыкой?", "Вы любите работать в команде?", "Вы увлекаетесь разгадкой шифров или кроссвордов?","Вы думаете о том, кем хотели бы стать?", "Вы увлекаетесь логическими задачами?", "Вы играете на музыкальных инструментах?", "Вы любите разгадывать головоломки?", "Вы хорошо запоминаете имена или факты?"
warrior = "Вы любите физическую активность?", "Вы инересутесь командными играми?", "Вам нравится играть в видео-игры?", "Вы любите работать сами?", "Вы часто конфликтуете?","Вы стремитесь к справедливости?", "Вы увлекаетесь стратегическими играми?", "Вы умете убеждать людей в чём либо?", "Вы отстаиваете свои убеждения?", "Вы доверяете людям?"
torgovec = "Вы обмениваетесь чем то?", "Вы увлекаетесь бизнесом?", "Вы любите гулять с друзьями?", "Вы часто изменяете что-то в себе или в чём то другом?", "Вы общительный человек?","Вы щедрый человек?", "Вы можете сразу узнать песню и отличить ее от другой?", "Вы любите дарить что либо?", "Вы часто задумываетесь о торговле?", "Вы скрываете свои рисунки от других?"
master = "Вы любите физическую активность?", "Вы умело собираете модели?", "Вы умеете выращивать растения?", "Вы любите математику?", "Вам нравиться плавать на байдарке?","Вы увлекаетесь пением?", "Вы интересуетесь танцами?", "Вы терпеливый человек?", "Вы легко обучаетесь физическим навыкам?", "У вас есть домашнее животное?"


questionsdict = {"verbalniy": verbalniy, "musical": musical, "logicheskiy": logicheskiy,"obrazniy":obrazniy,"telesniy":telesniy,"socialniy":socialniy,"vnutreniy":vnutreniy,"nature":nature,"filosovskiy":filosovskiy, "teacher":teacher, "warrior":warrior, "torgovec":torgovec, "master":master}
question = ["Вы любите физическую активность?",
"Вы увлекаетесь чтением?",
"Вы часто задумываетесь о смысле жизни",
"Вы обмениваетесь чем то?",
"Вы инересуютесь командными играми?",
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
"Вы запоминаете материал лучше с картинками?",
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
tipe4 = 0
intelect = 0
intelect1 = 0
intelect2 = 0
intelect3 = 0
intelect4 = 0
intelect5 = 0
intelect6 = 0
intelect7 = 0
intelect8 = 0
intelect9 = 0
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
        form.pushButton.clicked.connect(next)
        form.pushButton_2.clicked.connect(next)
    if question == [] and rofl_question != []:
        rofl_randomiser()
        form.pushButton.clicked.connect(next)
        form.pushButton_2.clicked.connect(next)
    if question == [] and rofl_question == []:
        next2()

    window.show()
                                                                                                                   

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)


form.pushButton.clicked.connect(lambda: next())
form.pushButton.clicked.connect(lambda: next2())
form.pushButton.clicked.connect(lambda: next2())


window.show()
app.exec()