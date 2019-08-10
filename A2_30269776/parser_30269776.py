# Author: Anni Li,
# Student ID: 30269776
# Start Date:  May 7
# Last Modification date: May 24
# Description:
# The program imports preprocess data and re to help modify input data.
# A string including post ID, type of post, post creation date, and the clean body of posts with unwanted signs or characters removed after extracton.
# The post ID, type of post, and post creation date are extracted with re.compile(), re.findall() and re.search().
# The post creation date is then sorted by quater of years in time sequence.
# Clean body is given by the preprocess data function imported
# The size of each line of clean body is given by getVocabularySize, where punctuation and replicated items are removed.


from preprocessData_30269776 import preprocessLine
import re

class Parser:
	"""docstring for ClassName"""
	def __init__(self, inputString):
		self.inputString = inputString
		self.ID = self.getID()
		self.type = self.getPostType()
		self.dateQuarter = self.getDateQuarter()
		self.cleanBody = self.getCleanedBody()

	def __str__(self):
		#print ID, Question/Answer/Others, creation date, the main content
		#write your code here
		return str(self.ID) + "," + str(self.type) + "," + str(self.dateQuarter) + "," + str(self.cleanBody)

	def getID(self):
		#write your code here
		rowId = re.compile(r'row Id=".+?"')   #get rowId of each post
		rowNum = rowId.findall(self.inputString)
		rNum = rowNum[0]
		rNum2 = re.search(r'\d+',rNum).group()
		return rNum2


	def getPostType(self):
		#write your code here
		postId = re.compile('PostTypeId=".+?"')  # Pattern to get postId of each post
		postType = postId.findall(self.inputString)		# get postId of each post
		pId = postType[0]
		pId2 = re.search(r'\d+',pId).group()

		if pId2 == '1':
			return "question"
		elif pId2 == '2':
			return "answer"
		else:
			return "other posts"


	def getDateQuarter(self):
		#write your code here
		dateQuater = re.compile('CreationDate=".+?"')  # get create date and time of each post
		dateQuater2 = dateQuater.findall(self.inputString)
		dateQuater2 = dateQuater2[0]
		dateQuater2 = dateQuater2.replace("CreationDate=\"", "")
		getQuater = dateQuater2[5:7]

		if getQuater == "01" or getQuater == "02" or getQuater == "03":
			return str(dateQuater2[0:4] + "Q1")
		elif getQuater == "04" or getQuater == "05" or getQuater == "06":
			return str(dateQuater2[0:4] + "Q2")
		elif getQuater == "07" or getQuater == "08" or getQuater == "09":
			return str(dateQuater2[0:4] + "Q3")
		elif getQuater == "10" or getQuater == "11" or getQuater == "12":
			return str(dateQuater2[0:4] + "Q4")


	def getCleanedBody(self):
		#write your code here
		clbody = preprocessLine(self.inputString)
		return clbody[1]

	def getVocabularySize(self):
		#write your code here
		lobody = self.cleanBody.lower()      #convert clean body in lower case
		newbody = re.sub('\W+', " ", lobody)
		bodylist = newbody.split()
		bodyset = set(bodylist)
		vocSize = len(bodyset)
		return vocSize





