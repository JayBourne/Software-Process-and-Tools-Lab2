# 添加生词本按钮（+/-）

import tkinter
from tkinter.constants import ACTIVE, DISABLED,  X
from ReviewWordsScreen123 import main as reviewMain
import linecache
import random

wordList = []  # 英文单词列表，字符串类型
chineseMeaningList = []  # 中文意思列表，字符串类型
allWordList = []  # 今日所背所有单词的列表，wordStruct类型
sequenceNum = 0  # 计数器，用于next循环
fileLocation = ".\\CET6Test.txt"  # CTE6txt文件位置
newWordsFileLocation = ".\\NewWords.txt"  # 生词本位置


class wordStruct:
    def __init__(self, word, chMeaning):
        self.word = word  # 英语单词
        self.chMeaning = chMeaning  # 汉语意思


class processWordsIntoList:
    def __init__(self, todayWordsNum):
        with open(fileLocation) as txt:
            line = txt.readline()
            lineNum = 0
            while line and lineNum < todayWordsNum:
                english = line.split()[0]
                chinese = line.split()[1]

                word = wordStruct(word=english, chMeaning=chinese)
                allWordList.append(word)

                wordList.append(english)
                chineseMeaningList.append(chinese)

                lineNum = lineNum+1
                line = txt.readline()
            txt.close()


class WordsMemorizingVersion3:
    def __init__(self, wordsMemoringScreen, todayWordsNum):
        self.wordsMemoringScreen = wordsMemoringScreen
        self.todayWordsNum = todayWordsNum
        self.label1 = tkinter.Label(
            self.wordsMemoringScreen, text=wordList[sequenceNum], font=("Arial Bold", 20))
        self.label1.pack(fill=X, pady=20)

        self.label2 = tkinter.Label(
            self.wordsMemoringScreen, text=chineseMeaningList[sequenceNum], font=("Arial Bold", 20))
        self.label2.pack(fill=X, pady=20)

        self.nextButton = tkinter.Button(self.wordsMemoringScreen, text="Next", font=(
            "Arial Bold", 15), fg="green", command=lambda: self.nextPressed())
        self.nextButton.pack(pady=20)

        self.addButton = tkinter.Button(self.wordsMemoringScreen, text="Add to NewWordsBook", font=(
            "Arial Bold", 15), fg="green", command=lambda: self.addPressed())
        self.addButton.pack(pady=20)

        self.label3 = tkinter.Label(self.wordsMemoringScreen, text="you have recite:"+str(
            sequenceNum)+"/"+str(self.todayWordsNum), font=("Arial Bold", 20))
        self.label3.pack(fill=X, pady=20)

    def nextPressed(self):
        global sequenceNum
        sequenceNum = sequenceNum+1

        if(sequenceNum == len(wordList)):
            self.label1.destroy()
            self.label2.destroy()
            self.nextButton.destroy()
            self.addButton.destroy()
            self.label3.destroy()
            reviewMain(self.wordsMemoringScreen, allWordList)
        else:
            self.label1.configure(text=wordList[sequenceNum])
            self.label2.configure(text=chineseMeaningList[sequenceNum])
            self.label3.configure(
                text="you have recite:"+str(sequenceNum)+"/"+str(self.todayWordsNum))
            self.addButton.configure(text="Add to NewWordsBook", state=ACTIVE)

    def addPressed(self):
        with open(newWordsFileLocation, 'a') as txt:
            line = self.label1.cget("text")+" "+self.label2.cget("text")+"\n"
            txt.write(line)
            self.addButton.configure(text="ADDED", state=DISABLED)
        txt.close()
        

        
def deleteFirstNLines(sum):
    fileIn = open(fileLocation, 'r')
    a = fileIn.readlines()
    fileOut = open(fileLocation, 'w')
    b = ''.join(a[sum:])
    fileOut.write(b)

def main(testStartScreen, todayWordsNum):
    with open(newWordsFileLocation, 'w') as txt:
        txt.write("")
    txt.close()
    processWordsIntoList(todayWordsNum)
    deleteFirstNLines(todayWordsNum)
    test = WordsMemorizingVersion3(
        wordsMemoringScreen=testStartScreen, todayWordsNum=todayWordsNum)


# def main():
#     with open(newWordsFileLocation, 'w') as txt:
#         txt.write("")
#     txt.close()
#     processWordsIntoList(todayWordsNum=3)
#     testStartScreen = tkinter.Tk()
#     testStartScreen.geometry("600x400")
#     WordsMemorizingVersion3(
#         wordsMemoringScreen=testStartScreen, todayWordsNum=3)
#     testStartScreen.mainloop()


# if __name__ == "__main__":
#     main()
