
#from playsound import playsound
from PySide2.QtWidgets import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from pygame import mixer
import os
#from ui import main
def play():
    print("点击了按钮")

# app = QApplication([])
# window = QMainWindow()
# window.resize(600,600)
# window.move(300,310)
# window.setWindowTitle("piano")
# textEdit = QPlainTextEdit(window)
# textEdit.setPlaceholderText("输入")
# textEdit.move(300,25)
# textEdit.resize(300,500)
# button=QPushButton("按钮",window)
# button.move(100,100)
# button.resize(100,100)
# button.clicked.connect(play)
# window.show()
# app.exec_() #暂停


class Guitar():
    def __init__(self):
        mixer.init()
        C=mixer.Sound("./Yamaha/C.wav")
        D = mixer.Sound("./Yamaha/D.wav")
        G = mixer.Sound("./Yamaha/G.wav")
        Em = mixer.Sound("./Yamaha/Em.wav")
        Am = mixer.Sound("./Yamaha/Am.wav")
        Bm7 = mixer.Sound("./Yamaha/Bm7.wav")

       # 添加ui文件
        qfile = QFile("./ui/guitar.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.window = QUiLoader().load(qfile)
       #  a=ui.Ui_Form()
       #  self.window = a
        def Myclick():
            print("点击了按钮")
        def click_C():
            #playsound("Yamaha/C.mp3")
            C.play()

        def click_D():
            #playsound("Yamaha/D.mp3")
            D.play()
        def click_G():
            #playsound("Yamaha/G.mp3")
            G.play()
        def click_Am():
            #playsound("Yamaha/Am.mp3")
            Am.play()
        def click_Em():
            #playsound("Yamaha/Em.mp3")
            Em.play()
        def click_Bm7():
            #playsound("Yamaha/Bm7.mp3")
            Bm7.play()
        # self.window=QMainWindow()
        # self.window.resize(400,400)
        # self.window.move(100,100)
        # self.window.setWindowTitle("TangYijun_guitar")
        #self.button_C=QPushButton("C",self.window)
        self.window.button_C.clicked.connect(click_C)


        #self.button_D = QPushButton("D", self.window)
        self.window.button_D.clicked.connect(click_D)
       # self.button_D.move(100,0)

        #self.button_G = QPushButton("G", self.window)
        self.window.button_G.clicked.connect(click_G)
        #self.button_G.move(200, 0)

        #self.button_Am = QPushButton("Am", self.window)
        self.window.button_Am.clicked.connect(click_Am)
        #self.button_Am.move(300, 0)

        #self.button_Em = QPushButton("Em", self.window)
        self.window.button_Em.clicked.connect(click_Em)
        #self.button_Em.move(400, 0)

        #self.button_Bm7 = QPushButton("Bm7", self.window)
        self.window.button_Bm7.clicked.connect(click_Bm7)
        #self.button_Bm7.move(500, 0)

class Piano1():
    def __init__(self):
        mixer.init()
        one = mixer.Sound("./piano_High/1.wav")
        b_two = mixer.Sound("./piano_High/b2.wav")
        two = mixer.Sound("./piano_High/2.wav")
        b_three = mixer.Sound("./piano_High/b3.wav")
        three = mixer.Sound("./piano_High/3.wav")
        four = mixer.Sound("./piano_High/4.wav")
        b_five = mixer.Sound("./piano_High/b5.wav")
        five = mixer.Sound("./piano_High/5.wav")
        b_six = mixer.Sound("./piano_High/b6.wav")
        six = mixer.Sound("./piano_High/6.wav")
        b_seven = mixer.Sound("./piano_High/b7.wav")
        seven = mixer.Sound("./piano_High/7.wav")
        oneone = mixer.Sound("./piano_High/11.wav")
        #按钮
        def click_one():
            one.play()
        def click_b_two():
            b_two.play()
        def click_two():
            two.play()
        def click_b_three():
            b_three.play()
        def click_three():
            three.play()
        def click_four():
            four.play()
        def click_b_five():
            b_five.play()
        def click_five():
            five.play()
        def click_b_six():
            b_six.play()
        def click_six():
            six.play()
        def click_b_seven():
            b_seven.play()
        def click_seven():
            seven.play()
        def click_oneone():
            oneone.play()
        #添加ui文件
        qfile= QFile("./ui/piano.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui=QUiLoader().load(qfile)
        self.ui.one.clicked.connect(click_one)
        self.ui.b_two.clicked.connect(click_b_two)
        self.ui.two.clicked.connect(click_two)
        self.ui.b_three.clicked.connect(click_b_three)
        self.ui.three.clicked.connect(click_three)
        self.ui.four.clicked.connect(click_four)
        self.ui.b_five.clicked.connect(click_b_five)
        self.ui.five.clicked.connect(click_five)
        self.ui.b_six.clicked.connect(click_b_six)
        self.ui.six.clicked.connect(click_six)
        self.ui.b_seven.clicked.connect(click_b_seven)
        self.ui.seven.clicked.connect(click_seven)
        self.ui.oneone.clicked.connect(click_oneone)
        #self.ui.show()
class Piano2():
    def __init__(self):
        # 低声部
        lone = mixer.Sound("./piano_low/1.wav")
        lb_two = mixer.Sound("./piano_low/b2.wav")
        ltwo = mixer.Sound("./piano_low/2.wav")
        lb_three = mixer.Sound("./piano_low/b3.wav")
        lthree = mixer.Sound("./piano_low/3.wav")
        lfour = mixer.Sound("./piano_low/4.wav")
        lb_five = mixer.Sound("./piano_low/b5.wav")
        lfive = mixer.Sound("./piano_low/5.wav")
        lb_six = mixer.Sound("./piano_low/b6.wav")
        lsix = mixer.Sound("./piano_low/6.wav")
        lb_seven = mixer.Sound("./piano_low/b7.wav")
        lseven = mixer.Sound("./piano_low/7.wav")
        loneone=mixer.Sound("./piano_low/11.wav")
        def click_lone():
            lone.play()
        def click_lb_two():
            lb_two.play()
        def click_ltwo():
            ltwo.play()
        def click_lb_three():
            lb_three.play()
        def click_lthree():
            lthree.play()
        def click_lfour():
            lfour.play()
        def click_lb_five():
            lb_five.play()
        def click_lfive():
            lfive.play()
        def click_lb_six():
            lb_six.play()
        def click_lsix():
            lsix.play()
        def click_lb_seven():
            lb_seven.play()
        def click_lseven():
            lseven.play()
        def click_loneone():
            loneone.play()
        # 添加ui文件
        qfile = QFile("./ui/piano2.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui = QUiLoader().load(qfile)
        self.ui.one.clicked.connect(click_lone)
        self.ui.b_two.clicked.connect(click_lb_two)
        self.ui.two.clicked.connect(click_ltwo)
        self.ui.b_three.clicked.connect(click_lb_three)
        self.ui.three.clicked.connect(click_lthree)
        self.ui.four.clicked.connect(click_lfour)
        self.ui.b_five.clicked.connect(click_lb_five)
        self.ui.five.clicked.connect(click_lfive)
        self.ui.b_six.clicked.connect(click_lb_six)
        self.ui.six.clicked.connect(click_lsix)
        self.ui.b_seven.clicked.connect(click_lb_seven)
        self.ui.seven.clicked.connect(click_lseven)
        self.ui.oneone.clicked.connect(click_loneone)

# def show_Guitar():
#     a = guitar()
#     a.window.show()
#     app.exec_()  # 暂停
#     #aa=input("获取输入，暂停")
# #钢琴低声部
# def show_Piano1():
#     piano=Piano1()
#     #aa=input("获取输入，暂停")
# def show_Piano2():
#     print()

class main_W():
    def __init__(self):
        # 添加ui文件
        qfile = QFile("./ui/main.ui")
        qfile.open(QFile.ReadOnly)
        qfile.close()
        self.ui = QUiLoader().load(qfile)
        #self.ui=main.Ui_widget()







app = QApplication([])
Main_Window=main_W()
piano1=Piano1()
piano2=Piano2()
guitar=Guitar()
Main_Window.ui.guitar.clicked.connect(guitar.window.show)
Main_Window.ui.piano1.clicked.connect(piano2.ui.show)
Main_Window.ui.piano2.clicked.connect(piano1.ui.show)

Main_Window.ui.show()
app.exec_() #暂停

