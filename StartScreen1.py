""" 显示“欢迎进入”&开始按钮&默认每天背单词30 """
import tkinter
from tkinter.constants import X
from WordsMemorizing1 import main as wordsMain


class StartScreenVersion1:
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
        
        enterButton(self.startScreen, self.label1, self.label2)


class enterButton:
    def __init__(self, startScreen, label1, label2):
        self.label1 = label1
        self.label2 = label2
        self.button = tkinter.Button(startScreen, text="Go!", font=(
            "Arial Bold", 15), fg="green", command=lambda: self.__pressed(startScreen=startScreen))
        self.button.pack(pady=30)

    def __pressed(self,startScreen):
        self.label1.destroy()
        self.label2.destroy()
        self.button.destroy()
        wordsMain(startScreen)


def main():
    test = StartScreenVersion1()
    teststartScreen = test.startScreen
    teststartScreen.mainloop()


if __name__ == "__main__":
    main()
