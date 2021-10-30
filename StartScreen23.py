""" 设置数量输入框（+/-）（不点就默认） """
from tkinter import IntVar, font
from tkinter.constants import LEFT,  X
import tkinter
#from WordsMemorizing2 import main as wordsMain
from WordsMemorizing3 import main as wordsMain
todayWordsNum = 20


class StartScreenVersion23:
    def __init__(self):
        self.startScreen = tkinter.Tk()
        self.startScreen.title("WordsApp -- by Wang&Cheng")
        self.startScreen.geometry("600x400")

        self.label1 = tkinter.Label(
            self.startScreen, text="Words Memorize", font=("Arial Bold", 30), fg="orange")
        self.label1.pack(fill=X, pady=30)

        self.label2 = tkinter.Label(
            self.startScreen, text="--Programmed by Wang Sirui & Cheng Yuan", font=("Arial Bold", 20))
        self.label2.pack(fill=X, pady=30)

        self.__button = tkinter.Button(self.startScreen, text="Go!", font=(
            "Arial Bold", 15), fg="green", command=self.__pressed)
        self.__button.pack(pady=30)

        self.label3 = tkinter.Label(
            self.startScreen, text="    how many words to recite:", font=("Arial Bold", 15))
        self.label3.pack(side=LEFT, pady=30)

        self.v = IntVar()
        self.v.set(20)
        self.spin = tkinter.Spinbox(
            self.startScreen, from_=5, to=100, font=("Arial Bold", 15), textvariable=self.v)
        self.spin.pack(pady=30)

    def __pressed(self):
        global todayWordsNum
        todayWordsNum = int(self.spin.get())
        print(todayWordsNum)

        self.label1.destroy()
        self.label2.destroy()
        self.__button.destroy()
        self.label3.destroy()
        self.spin.destroy()

        wordsMain(self.startScreen,todayWordsNum)


def main():
    testStartScreen = StartScreenVersion23().startScreen
    testStartScreen.mainloop()


if __name__ == "__main__":
    main()
