""" next按钮&英文&中文 """

import tkinter
from tkinter.constants import X
from ReviewWordsScreen123 import main as reviewMain
import linecache
import random

wordList = []  # 英文单词列表，字符串类型
chineseMeaningList = []  # 中文意思列表，字符串类型
allWordList = []  # 今日所背所有单词的列表，wordStruct类型
sequenceNum = 0  # 计数器，用于next循环
todayWordsNum = 5  # 今日背单词总数
fileLocation = ".\\CET6Test.txt"  # CTE6txt文件位置


class wordStruct:
    def __init__(self, word, chMeaning):
        self.word = word  # 英语单词
        self.chMeaning = chMeaning  # 汉语意思


class processWordsIntoList:
    def __init__(self):
        with open(file=fileLocation) as txt:
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


class WordsMemorizingVersion1:
    def __init__(self, wordsMemoringScreen):
        self.wordsMemoringScreen = wordsMemoringScreen

        self.label1 = tkinter.Label(
            self.wordsMemoringScreen, text=wordList[sequenceNum], font=("Arial Bold", 20))
        self.label1.pack(fill=X, pady=30)

        self.label2 = tkinter.Label(
            self.wordsMemoringScreen, text=chineseMeaningList[sequenceNum], font=("Arial Bold", 20))
        self.label2.pack(fill=X, pady=30)

        self.nextButton = tkinter.Button(self.wordsMemoringScreen, text="Next", font=(
            "Arial Bold", 15), fg="green", command=lambda: self.pressed())
        self.nextButton.pack(pady=30)

    def pressed(self):
        global sequenceNum
        sequenceNum = sequenceNum+1

        if(sequenceNum == len(wordList)):
            self.label1.destroy()
            self.label2.destroy()
            self.nextButton.destroy()
            reviewMain(self.wordsMemoringScreen,allWordList)
        else:
            self.label1.configure(text=wordList[sequenceNum])
            self.label2.configure(text=chineseMeaningList[sequenceNum])

def deleteFirstNLines(sum):
    fileIn = open(fileLocation, 'r')
    a = fileIn.readlines()
    fileOut = open(fileLocation, 'w')
    b = ''.join(a[sum:])
    fileOut.write(b)

def main(testStartScreen):
    processWordsIntoList()
    deleteFirstNLines(todayWordsNum)
    test = WordsMemorizingVersion1(wordsMemoringScreen=testStartScreen)


# def main():
#     processWordsIntoList()
#     testStartScreen = tkinter.Tk()
#     testStartScreen.geometry("600x400")
#     WordsMemorizingVersion1(wordsMemoringScreen=testStartScreen)
#     testStartScreen.mainloop()


if __name__ == "__main__":
    main()
