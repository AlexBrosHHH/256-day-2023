#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from random import shuffle
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel,
    QPushButton, QRadioButton, QGroupBox, QButtonGroup)

#Создание главного окна
app = QApplication([])
win = QWidget()
win.setWindowTitle('Тестирование')
win.resize(500, 330)
win.setStyleSheet('background: rgb(151, 151, 151);')
#Создание класса для вопросов

class Question():
    def __init__(self, quest, right_ans, wrong_ans1, wrong_ans2, wrong_ans3):
        self.quest = quest 
        self.right_ans = right_ans
        self.wrong_ans1 = wrong_ans1
        self.wrong_ans2 = wrong_ans2
        self.wrong_ans3 = wrong_ans3
#Вопросы
question_list = []
question_list.append(Question(
    'Какое достоинство не относится к программистам?',
    'Хорошо понимать чужой код',
    'Лень',
    'Нетерпеливость',
    'Гордыня'))

question_list.append(Question(
    'Что не является языком программирования?',
    'HTML',
    'Java Script',
    'Python',
    'C++'))

question_list.append(Question(
    'На что чаще всего программист тратит время в проекте?',
    'Поиск бага',
    'Написание кода',
    'Гугл',
    '?'))

question_list.append(Question(
    'Кто делает сайт который мы видим?',
    'Фронтенд разработчик',
    'Бэкенд разработчик',
    'Мобильный разработчик',
    'Верстальщик'))

question_list.append(Question(
    'Самый любимый сайт программиста на работе?',
    'Stack Owerflow',
    'HTML book',
    'YouTube',
    'GitHub'))

app.setStyleSheet("QLabel{font-size: 18pt;} ")

#Создание интерфейса
question = QLabel('Здесь будет вопрос')
button = QPushButton('Ответить')
AnswerBox = QGroupBox('Варианты ответов')

rbtn_1 = QRadioButton('Ответ 1')
rbtn_2 = QRadioButton('Ответ 2')
rbtn_3 = QRadioButton('Ответ 3')
rbtn_4 = QRadioButton('Ответ 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


#Создание окна результата
ResultBox = QGroupBox('Результат теста')
result = QLabel('Правильно / неправильно')
correct = QLabel('Здесь будет правильный ответ')

#Выравнивани
#Выравнивание окна вопросов
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)

layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

AnswerBox.setLayout(layout_ans1)

#Выравнивание окна результатов
layout_res = QVBoxLayout()
layout_res.addWidget(result, alignment= Qt.AlignLeft)
layout_res.addWidget(correct, alignment= Qt.AlignCenter)
ResultBox.setLayout(layout_res)

layout_main = QVBoxLayout()
layout_main.addWidget(question, alignment = Qt.AlignCenter)
layout_main.addWidget(AnswerBox)
layout_main.addWidget(ResultBox)
layout_main.addWidget(button)
win.setLayout(layout_main)
AnswerBox.show()
ResultBox.hide()


#Создание функций


#Отображение результата
def show_result():
    AnswerBox.hide()
    ResultBox.show()
    button.setText('Следующий вопрос')
    


#Отображение вопросв
def show_questuon():
    AnswerBox.show()
    ResultBox.hide()
    button.setText('Ответить')
    button.setStyleSheet('background: rgb(94, 0, 255);')
    



#Функция загрузки вопросов и ответов

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_ans)
    answers[1].setText(q.wrong_ans1)
    answers[2].setText(q.wrong_ans2)
    answers[3].setText(q.wrong_ans3)
    question.setText(q.quest)
    correct.setText(q.right_ans)
    show_questuon()




#Функция проверки правильного ответа
def check_answer():
    if answers[0].isChecked():
        result.setText('Правильно')
        result.setStyleSheet('background: rgb(34, 255, 0);')
        show_result()
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            result.setText('Неправильно!')
            result.setStyleSheet('background: rgb(255, 0, 0);')
            show_result()


#Фунция перехода к следующему вопр
def next_question():
    win.cur_question = win.cur_question + 1
    if win.cur_question >= len(question_list):
        win.cur_question == 0
    q = question_list[win.cur_question]
    ask(q)

#Функция нажатия по кнопу
def b_click():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()
button.clicked.connect(b_click)
win.cur_question = -1
next_question()


#Создание сгрупированных вариантов ответа
#Запуск приложения
win.show()
app.exec()
