# Author: Anni Li,
# Student ID: 30269776
# Start Date:  May 7
# Last Modification date: May
# Description:
# The following program imports function of parser and matplolib module to sort the data in inputfile.
# The visualizeWordDistribution function sorts given data by the vocabulary size and count the total number of each group.
# The visualizeWordDistribution function produces a bar chart of vocabulary size vs number of word count.
# The visualizePostNumberTrend function reads in the date and corresponding quater of input file.
# The visualizePostNumberTrend function also match the type of body content of input file to questions and answers.
# Finally, a line plot of numbers of question post and answer post is painted and exported as png.

import matplotlib.pyplot as plt
import parser_30269776 as parser

def visualizeWordDistribution(inputFile, outputImage):
	#write your code here
    readfile = open(inputFile,'r',encoding='utf-8')
    listVocab = [0]*11          #build a list to count different vocabulary size
    for line in readfile:
        if "Body" not in line:
            continue
        postparser = parser.Parser(line)
        postVocab = postparser.getVocabularySize()
        # divide the vocab size into different groups by value
        if postVocab >= 0 and postVocab < 10:
            listVocab[0] += 1
        elif postVocab >= 10 and postVocab < 20:
            listVocab[1] += 1
        elif postVocab >= 20 and postVocab < 30:
            listVocab[2] += 1
        elif postVocab >= 30 and postVocab < 40:
            listVocab[3] += 1
        elif postVocab >= 40 and postVocab < 50:
            listVocab[4] += 1
        elif postVocab >= 50 and postVocab < 60:
            listVocab[5] += 1
        elif postVocab >= 60 and postVocab < 70:
            listVocab[6] += 1
        elif postVocab >= 70 and postVocab < 80:
            listVocab[7] += 1
        elif postVocab >= 80 and postVocab < 90:
            listVocab[8] += 1
        elif postVocab >= 90 and postVocab < 100:
            listVocab[9] += 1
        else:
            listVocab[10] += 1

    # define a list for number of each size
    labelList = ['0~10','10~20','20~30','30~40','40~50','50~60','60~70','70~80','80~90','90~100','others']

    plt.bar(labelList, listVocab, fc='b')    # set axis data and bar color
    plt.xlabel('Vocabulary Size')  # add label to the x axis
    plt.ylabel('Number of posts with certain Vocabulary Size')  # add label to the y axis
    plt.title('Post Vocabulary Distribution')  # add title to the picture
    plt.savefig(outputImage)        # get output image

    readfile.close()

def visualizePostNumberTrend(inputFile, outputImage):
    # write your code here
    # open file and read by lines
    readfile = open(inputFile,'r',encoding='utf-8')
    listDate = []
    for line in readfile:
        if "Body" not in line:
            continue
        lineparser = parser.Parser(line)
        listDate.append(lineparser.dateQuarter)
    listDate = set(listDate)    # convert the list to set to exclude repeating items
    listDate = list(listDate)   # turn the set back to list after removing repeating items
    listDate.sort()
    readfile.close()

    readfile = open(inputFile,'r',encoding='utf-8')
    listQuestion = [0]*len(listDate)
    listAnswer = [0]*len(listDate)
    for line in readfile:
        if "row" not in line:
            continue
        lineparser = parser.Parser(line)
        linetype = lineparser.type
        linedate = lineparser.dateQuarter       # get line of date and quaters
        if linetype == 'question':              # count number of questions
            index = listDate.index(linedate)
            listQuestion[index]+=1
        if linetype == 'answer':            # count number of answers
            index = listDate.index(linedate)
            listAnswer[index]+=1
    readfile.close()


    plt.xlabel('Time Period')       # add label to x axis
    plt.ylabel('Number of Posts')   # add label to y axis
    plt.plot(listDate,listQuestion)     # plot the line of question by date
    plt.plot(listDate,listAnswer)       # plot the line of answer by date
    plt.legend(("question","answer"))   # plot legend of the two lines
    plt.title('Trend of post types')      # add plot titles
    plt.savefig(outputImage)        # get output image


if __name__ == "__main__":

	f_data = "data.xml"
	f_wordDistribution = "wordNumberDistribution.png"
	f_postTrend = "postNumberTrend.png"
	
	#visualizeWordDistribution(f_data, f_wordDistribution)
	visualizePostNumberTrend(f_data, f_postTrend)
