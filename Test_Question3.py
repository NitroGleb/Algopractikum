import sys
from PyQt6 import QtWidgets, uic, QtCore, QtGui
from PyQt6.sip import sipPyTypeRectRef

class Window1(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window1, self).__init__()
        uic.loadUi('Qt1.ui', self)

        # Добавление кнопки для перехода к следующему окну
        self.nextButton = self.findChild(QtWidgets.QPushButton, 'OK')
        self.nextButton.clicked.connect(self.goToNextWindow)

    def goToNextWindow(self):
        # Переход к следующему окну
        w = Window2()
        w.show()
        self.close()

# Загрузка второго окна
class Window2(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window2, self).__init__()
        uic.loadUi('Qt2.ui', self)

        # Изменение текста вопроса
        questionLabel = self.findChild(QtWidgets.QLabel, 'Вопрос № 1')
        questionLabel.setText("Новый вопрос для второго окна")

        # Добавление кнопки для перехода к следующему окну
        self.nextButton = self.findChild(QtWidgets.QPushButton, 'Cancel')
        self.nextButton.clicked.connect(self.goToNextWindow)

    def goToNextWindow(self):
        # Переход к следующему окну
        w = Window3()
        w.show()
        self.close()

# Загрузка третьего окна
class Window3(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window3, self).__init__()
        uic.loadUi('Qt3.ui', self)

        # Здесь можно добавить логику для последнего окна, включая вывод результатов теста
        resultLabel = self.findChild(QtWidgets.QLabel, 'Результаты теста')
        resultLabel.setText("Результаты теста")

# Главный класс, который запускает тест
class Main(QtWidgets.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.centralWidget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.centralWidget)

        # Добавление окон в стек
        self.addWindow(Window1())
        self.addWindow(Window2())
        self.addWindow(Window3())

        # Начало с первого окна
        self.centralWidget.setCurrentIndex(0)

    def addWindow(self, window):
        self.centralWidget.addWidget(window)

# Запуск приложения
app = QtWidgets.QApplication(sys.argv)
w = Main()
w.show()
sys.exit(app.exec_())