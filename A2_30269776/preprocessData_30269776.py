# Author: Anni Li,
# Student ID: 30269776
# Start Date:  May 7
# Last Modification date: May 24
# Description:
#This program read an input file by lines.
#The main body of data is extracted and filter with special reference characters removed and replaced with space.
#The content of clean body is sorted into a file of question and a file of answer.The files are exported as txt.



import re

def preprocessLine(inputLine):
    #preprocess the data in each line
    #write your code here
    old_line = inputLine
    # perform data processing of character reference
    initInput = re.compile(r'Body=".+?"')   # set the pattern to extract body part of each line
    inputLine = initInput.findall(inputLine)    # detach body part of each line with row ID etc, where "Body=" remain
    if len(inputLine) < 1:      # sort lines with no body part of posts to another tuple
        return(0,'')
    inputLine = inputLine[0]                # extract the body part from the list produced by .findall
    inputLine = inputLine.replace("&amp;", "&")  # replace the character reference of '&'
    inputLine = inputLine.replace("&amp;", "&")  # replace the character reference of '&'
    inputLine = inputLine.replace("&quot;", "\"")  # replace the character reference of '"'
    inputLine = inputLine.replace("&apot;", "\'")  # replace the character reference of '''
    inputLine = inputLine.replace("&gt;", ">")  # replace the character reference of '>'
    inputLine = inputLine.replace("&lt;", "<")  # replace the character reference of '<'
    inputLine = inputLine.replace("&#xA;", " ")  # replace "&#xA;" with space
    inputLine = inputLine.replace("&#xD;", " ")  # replace "&#xD;" with space
    inputLine = re.sub('<[^ =].*?>', "", inputLine)  # remove all HTML tags in file
    inputLine = inputLine.replace("Body=\""," ")  # remove "Body=" in file
    inputLine = inputLine[:-1]

    if "PostTypeId=\"1\"" in old_line:      #sort the input of questions into a tuple
        return(1,inputLine)
    if "PostTypeId=\"2\"" in old_line:      #sort the input of answers into a tuple
        return(2,inputLine)
    return (0,inputLine)

def splitFile(inputFile, outputFile_question, outputFile_answer):
    #preprocess the original file, and split them into two files.
    #please call preprocessLine() function within this function
    #write you code here

    # open data.xml file for reading
    dtFile = open(inputFile, 'r', encoding='utf-8')                 # open input file
    quesOutput = open(outputFile_question,'w',encoding='utf-8')      #open file for question output
    answerOutput = open(outputFile_answer,'w',encoding='utf-8')      #open file for answer output

    for line in dtFile:     # read original data by line
        cl = preprocessLine(line)  # call preprocessLine() to return clean body text


        if cl[0] == 1:
            quesOutput.write(cl[1])  # open question.txt for writing

        if cl[0] == 2:
            answerOutput.write(cl[1])  # open answer.txt for writing

    dtFile.close()
    quesOutput.close()
    answerOutput.close()

if __name__ == "__main__":

    f_data = "data.xml"
    f_question = "question.txt"
    f_answer = "answer.txt"

    splitFile(f_data, f_question, f_answer)
