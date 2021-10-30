'''复习界面 显示中文输入英语 比对后显示正确/错误 错误自动加入生词本
复习今日单词后再复习一遍生词本内容'''

from tkinter import *


flag = 0
count = 0
if_check = False
wrongWordList={}
reviewWordList={}

class ReviewWordsScreen():
    def __init__(self,reviewScreen,List):
        self.reviewScreen=reviewScreen
        self.List=List
        self.frame1 = Frame(self.reviewScreen)
        self.frame2 = Frame(self.reviewScreen)
        self.ans = ''

    def screen0(self):
        label1 = Label(self.frame1, text="恭喜你学完今日单词！\n\n下面来检查一下你的学习成果吧~", font=("Arial Bold", 20))
        label1.pack(pady=25)
        button1 = Button(self.frame1, text="OK！", font=("Arial Bold", 15), fg="green", command = self.screen1)
        button1.pack(pady=50)
        self.frame1.pack(padx=1, pady=1)

    def screen1(self):
        global reviewWordList
        reviewWordList = self.List

        self.frame1.destroy()
        self.frame2.pack(padx=10,pady=10)

        txt = Entry(self.frame2, width=30)
        txt.pack(ipady=10,padx=10, pady=5)

        label2 = Label(self.frame2, text="", font=("Arial Bold", 20))
        label2.pack(pady=5)
        label3 = Label(self.frame2, text="", font=("Arial Bold", 20))
        label4 = Label(self.frame2, text="", font=("Arial Bold", 20))
        label4.pack(pady=5)

        def check():
            global count
            global wrongWordList
            global reviewWordList
            global if_check
            if_check = True
            self.ans = txt.get()
            if (self.ans == reviewWordList[flag].word):
                label3.configure(text="正确")
                label3.pack(pady=5)
            if(self.ans != reviewWordList[flag].word):
                label3.configure(text="错误"+"\n"+"正确答案为："+reviewWordList[flag].word)
                label3.pack(pady=5)

                #判断这个单词是否已经在生词本中
                in_or_not = False
                for i in wrongWordList:
                    if(i==reviewWordList[flag]):
                        in_or_not = True
                if(in_or_not==False):
                    reviewWordList.append(reviewWordList[flag])
                    wrongWordList[count] = reviewWordList[flag]
                    count += 1

        label2.configure(text=reviewWordList[flag].chMeaning)
        button2 = Button(self.frame2, text="CHECK", font=("Arial Bold", 15), fg="green", command=check)
        button2.pack(pady=5)

        def next():
            global flag
            global count
            global if_check
            global wrongWordList
            global reviewWordList

            label3.configure(text="")

            if(flag==len(reviewWordList)-1):
                txt.delete(0, END)
                label2.destroy()
                label3.configure(text="恭喜你完成今日复习!")
                label3.pack(pady=5)
                button2.destroy()
                button3.destroy()
                txt.destroy()
                with open(".\\NewWords.txt", 'a')as m:
                    for j in range(len(wrongWordList)):
                        line = wrongWordList[j].word + " " + wrongWordList[j].chMeaning + "\n"
                        m.write(line)
                m.close()

            else:
                if(if_check==False):
                    label4.configure(text="Not check yet!")
                else:
                    flag += 1
                    if_check=False
                    txt.delete(0, END)
                    label2.configure(text=reviewWordList[flag].chMeaning)
                    label4.configure(text="")
                    button2.configure(command=check)
                    button3.configure(command=next)

        button3 = Button(self.frame2, text="NEXT", font=("Arial Bold", 15), fg="black", command=next)
        button3.pack(pady=5)

def main(reviewScreen,List):
    testReview = ReviewWordsScreen(reviewScreen=reviewScreen,List=List)
    testReview.screen0()
    
if __name__ == '__main__':
    main()
