import random
import re

def isValidChoice(c):
	if type(c) != str:
		return False
	elif len(c) > 1 or not c:
		return False
	elif re.match('[^A-Da-d]', c):
		return False
	else:
		return True

def generatePool():
	myfile = open("TechPool.txt", 'r')
	contents = []
	questionIndex = []
	binIndex = []
	for line in myfile:
		contents.append(line)
	myfile.close()
	for i in range(len(contents)):
		if contents[i] == '~~\n':
			questionIndex.append(i-6)
	for i in range(len(questionIndex)):
		currentMetaInfo = contents[questionIndex[i]].split(" ")
		previousMetaInfo = contents[questionIndex[i-1]].split(" ")
		if currentMetaInfo[0][0:3] != previousMetaInfo[0][0:3]:
			binIndex.append(questionIndex[i])
	return [binIndex, questionIndex]


def chooseQuestions():
	main = generatePool()
	picked = []
	for i in range(len(main[0])):
		try:
			choice = main[1][random.randint(main[1].index(main[0][i]), main[1].index(main[0][i+1])-1)]
			picked.append(choice)
		except IndexError:
			pass
	return picked

def administerExam():
	myfile = open("TechPool.txt", 'r')
	contents = []
	pointCount = 0
	for line in myfile:
		contents.append(line)
	myfile.close()
	questionList = chooseQuestions()
	for i in range(len(questionList)):
		pointCheck = True
		print "--"+contents[questionList[i]][0:5]+"--"
		print ""
		print contents[questionList[i]+1]
		print contents[questionList[i]+2]
		print contents[questionList[i]+3]
		print contents[questionList[i]+4]
		print contents[questionList[i]+5]
		choice = raw_input("> ")
		while not isValidChoice(choice):
			print ("> That choice is invalid. Please choose either A, B, C, or D as your answer.")
			choice = raw_input("> ")
		while (ord(choice) != ord(contents[questionList[i]][7:8]) and ord(choice) != ord(contents[questionList[i]][7:8])+32):
			print "> That is incorrect. Please try again."
			choice = raw_input("> ")
			pointCheck = False
			while not isValidChoice(choice):
				print ("> That choice is invalid. Please choose either A, B, C, or D as your answer.")
				choice = raw_input("> ")
		if ord(choice) == ord(contents[questionList[i]][7:8]) or ord(choice) == ord(contents[questionList[i]][7:8])+32:
			print "> That is correct!"
			print ""
		if pointCheck == True:
			pointCount = pointCount+1
	return pointCount	

def main():
	print "Please enter your name."
	studentName = raw_input("> ")
	print ""
	print "> "+studentName+", the exam will now begin. Are you ready? Please indicate with Y/N."
	beginCheck = raw_input("> ")
	print ""
	if beginCheck == "Y" or beginCheck == "y":
		finalScore = administerExam()
	elif beginCheck == "N" or beginCheck == "n":
		print "The program will now exit."
	else:
		print "That is an invalid choice. The program will now exit."
	try:
		if finalScore >= 26:
			print "> Exam Summary"
			print "> Congratulations! You have passed this exam. Your scored a total of "+str(finalScore)+" out of 34 possible points."
		else:
			print "> Exam Summary"
			print "> You scored a total of "+str(finalScore)+" out of 34 possible points. Unfortunately, you did not reach the minimum 26 points needed to pass this exam."
	except UnboundLocalError:
		pass	

if __name__ == '__main__':
	main()
