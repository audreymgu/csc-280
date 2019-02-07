# Project Four - The 15 Game, Tournament Version
# NAME: Audrey Gu
# DUE DATE: 10/25/16
# OTHER COMMENTS: 3y3 @m 1337 haxx0r g@wd (just kidding)


import random
import copy
import re


def greetPlayer():
	print ("Enter your name.").center(100)
	playerName = raw_input("> ")
	return playerName


def greetPlayers():
	playerList = []
	print "Hi! Player One, what is your name?".center(100)
	playerList.append(raw_input("> "))
	print "Hi! Player Two, what is your name?".center(100)
	playerList.append(raw_input("> "))
	return playerList


def isInRange(v):
	if type(v) != str:
		return False
	elif len(v) > 1 or not v:
		return False
	elif re.match('[0-9]', v):
		v = int(v)
		return v
	else:
		return False


def findMoveToWin(ownSet, moveSet):
	winChoice = False
	for i in range(0, len(ownSet)-1):
		for j in range(i+1, len(ownSet)):
			for k in range(0, len(moveSet)):
				if ownSet[i] + ownSet[j] + moveSet[k] == 15:
					winChoice = int(moveSet[k])
	return winChoice


def pickRandomly(moveSet):
	randChoice = random.choice(moveSet)
	return randChoice

# Because melting things is cool.
def melt(l):
	l = [item for sublist in l for item in sublist]
	return l


def bestChoice(set):
	highestCount = [0, 0]
	for i in range(len(set)):
		if set[i] == highestCount[1]:
			pass
		else:
			counter = set.count(set[i])
		if counter > highestCount[0]:
			highestCount = [counter, set[i]]
	return highestCount[1]


def choiceEval(option, solutions):
	counter = 0
	for i in range(len(solutions)):
		counter = counter + solutions[i-1].count(option)
	return counter


def solnEval(reqSet, moveSet):
	startingSolutions = [[1, 5, 9], [1, 6, 8], [2, 4, 9], [2, 5, 8], [2, 6, 7], [3, 4, 8], [3, 5, 7], [4, 5, 6]]
	validSolutions = []
	temp1 = []
	temp2 = []
	win = []
	pool = []
	highestCount = [0, 0]

	# If a solution in startingSolutions contains one of the moves remaining in the moveset, append it to validSolutions. Remove duplicates.
	# This filters out solutions that do not have the potential to be advanced in the next move.
	for i in range(len(moveSet)):
		for j in range(len(startingSolutions)):
			if startingSolutions[j].count(moveSet[i]):
				validSolutions.append(startingSolutions[j])
	for i in range(len(validSolutions)):
		if validSolutions[i] not in temp1:
			temp1.append(validSolutions[i])
	validSolutions = temp1

	# If a solution in validSolutions contains one of the moves in the requested set (reqSet), append it to temp. Allow for multiple appends of the same solution. Replace the existing validSolutions with temp after the search is complete.
	# This filters validSolutions further, while also using a double append to indicate immediate victory (a double append means that the requested set already owns two of the three numbers to win.)
	for i in range(len(reqSet)):
		for j in range(len(validSolutions)):
			if validSolutions[j].count(reqSet[i]):
				temp2.append(validSolutions[j])
	validSolutions = temp2

	# If a solution has been appended to validSolutions more than once, append that solution to win.
	for i in range(len(validSolutions)):
		if validSolutions.count(validSolutions[i]) > 1 and not win:
			win.append(validSolutions[i])

	# If the win condition has been satisfied...
	if win:
		winChoice = [x for x in win[0] if x not in reqSet]
		victoryMove = [True, winChoice[0]]
		return victoryMove

	# Otherwise, if there are valid strategic moves, given an existing set...
	elif validSolutions:
		pool = [x for x in melt(validSolutions) if x not in reqSet]
		bestMove = [False, bestChoice(pool)]
		# print validSolutions
		# print pool
		return bestMove

	# Otherwise, if the computer has not yet made any moves...
	else:
		for i in range(len(moveSet)):
			counter = choiceEval(moveSet[i], startingSolutions)
			if counter > highestCount[0]:
				highestCount = [counter, moveSet[i]]
		firstMove = [False, highestCount[1]]
		return firstMove


def childChoice(ownSet, oppSet, moveSet):
	oppWinCheck = findMoveToWin(oppSet, moveSet)
	ownWinCheck = findMoveToWin(ownSet, moveSet)
	if oppWinCheck and not ownWinCheck:
		return oppWinCheck
	elif ownWinCheck:
		return ownWinCheck
	else:
		random = pickRandomly(moveSet)
		return random


def computerChoice(ownSet, oppSet, moveSet):
	opponentCheck = solnEval(oppSet, moveSet)
	selfCheck = solnEval(ownSet, moveSet)
	if opponentCheck[0] is True:
		return opponentCheck[1]
	elif selfCheck[0] is True:
		return selfCheck[1]
	else:
		return selfCheck[1]


def getMoveFromPlayer(player, moves):
	print (str(player)+", what is your next move?").center(100)
	choice = raw_input("> ")
	while (not isInRange(choice)) or (not int(choice) in moves):
		print (str(player)+", that choice is invalid. Input another move.").center(100)
		choice = raw_input("> ")
	return int(choice)


def makeMove(choice, playerSet, moveSet):
	playerSet.append(moveSet.pop(moveSet.index(choice)))


def winner(l):
	final = []
	for i in range(0, len(l)-2):
		for j in range(i+1, len(l)-1):
			for k in range(j+1, len(l)):
				if l[i] + l[j] + l[k] == 15:
					result = str(l[i])+" + "+str(l[j])+" + "+str(l[k])+" = 15"
					final = [True, result]
	if not final:
		final = [False]
		return final
	else:
		return final


def signoff(playerList, zeroSetFinal, oneSetFinal):
	print "\n"
	print str(playerList[0])+" and "+str(playerList[1])+", thank you for playing!"
	if zeroSetFinal[0]:
		print "\n"
		print str(playerList[0])+" has won the game, with a winning combination of: "+str(zeroSetFinal[1])
	if oneSetFinal[0]:
		print "\n"
		print str(playerList[1])+" has won the game, with a winning combination of: "+str(oneSetFinal[1])
	if not zeroSetFinal[0] and not oneSetFinal[0]:
		print "The game has ended in a tie. "+str(playerList[0])+" has a final set of "+str(zeroSetFinal[1])+", and "+str(playerList[1])+" has a final set of "+str(oneSetFinal[1])+"."


def hvh():
	print "---------- Begin Turn ----------".center(100)

	# Move lists
	moveSet = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	zeroSet = []
	oneSet = []

	# Initial win condition checks
	zeroWinCheck = winner(zeroSet)
	oneWinCheck = winner(oneSet)

	# Greet players
	playerList = greetPlayers()

	# While neither player has won and there are remaining available moves...
	while not zeroWinCheck[0] and not oneWinCheck[0] and moveSet:

		# If player one has not yet won and there are remaining available moves...
		if not oneWinCheck[0] and moveSet:
			# Get move from player zero
			zeroChoice = getMoveFromPlayer(playerList[0], moveSet)
			# Apply move choice
			makeMove(zeroChoice, zeroSet, moveSet)
			# Update win condition check for player zero
			zeroWinCheck = winner(zeroSet)

		# If player zero has not yet won and there are remaining available moves...
		if not zeroWinCheck[0] and moveSet:
			# Get move from player one
			oneChoice = getMoveFromPlayer(playerList[1], moveSet)
			# Apply move choice
			makeMove(oneChoice, oneSet, moveSet)
			# Update win condition check for player one
			oneWinCheck = winner(oneSet)

		# Real-time List Updates...
		if not zeroWinCheck[0] and not oneWinCheck[0] and moveSet:
			print "\n"
			print "--------- Turn Summary ---------".center(100)
			print "\n"
			print "-- Chosen Moves --".center(100)
			print ('%s %s' % ('%-16s' % ('%.6s' % (str(playerList[0]),)+" has:",), str(zeroSet))).center(100)
			print ('%s %s' % ('%-16s' % ('%.6s' % (str(playerList[1]),)+" has:",), str(oneSet))).center(100)
			print "\n"
			print "-- Available Moves --".center(100)
			print str(moveSet).center(100)
			print "\n"

		# Tie Exception
		if not zeroWinCheck[0] and not oneWinCheck[0] and not moveSet:
			zeroWinCheck.append(str(zeroSet))
			oneWinCheck.append(str(oneSet))

		# Verbose Debug
		# print str(zeroWinCheck)+str(zeroSet)+str(oneWinCheck)+str(oneSet)

	# Final Sign-off!
	signoff(playerList, zeroWinCheck, oneWinCheck)


def cvh():
	# Move lists
	moveSet = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	cpSet = []
	hmSet = []

	# Initial win condition checks
	cpWinCheck = winner(cpSet)
	hmWinCheck = winner(hmSet)

	# Greet player
	playerList = ["CPU-00", greetPlayer()]

	# While neither player has won and there are remaining available moves...
	while not cpWinCheck[0] and not hmWinCheck[0] and moveSet:
		print "---------- Begin Turn ----------".center(100)

		# If the human player has not yet won and there are remaining available moves...
		if not hmWinCheck[0] and moveSet:
			# Get move from the computer
			cpChoice = computerChoice(cpSet, hmSet, moveSet)
			# Apply move choice
			makeMove(cpChoice, cpSet, moveSet)
			# Update win condition check for the computer
			cpWinCheck = winner(cpSet)
			# Inform player of computer's choice
			print ("CPU-OO has chosen "+str(cpChoice)+".").center(100)

		# If the computer has not yet won and there are remaining available moves...
		if not cpWinCheck[0] and moveSet:
			# Get move from human player
			hmChoice = getMoveFromPlayer(playerList[1], moveSet)
			# Apply move choice
			makeMove(hmChoice, hmSet, moveSet)
			# Update win condition check for human player
			hmWinCheck = winner(hmSet)

		# Real-time List Updates...
		if not cpWinCheck[0] and not hmWinCheck[0] and moveSet:
			print "\n"
			print "--------- Turn Summary ---------".center(100)
			print "\n"
			print "-- Chosen Moves --".center(100)
			print ('%s %s' % ('%-16s' % ('%.6s' % ("CPU-00",)+" has:",), str(cpSet))).center(100)
			print ('%s %s' % ('%-16s' % ('%.6s' % (str(playerList[1]),)+" has:",), str(hmSet))).center(100)
			print "-- Available Moves --".center(100)
			print str(moveSet).center(100)
			print "\n"

		# Tie Exception
		if not cpWinCheck[0] and not hmWinCheck[0] and not moveSet:
			cpWinCheck.append(str(cpSet))
			hmWinCheck.append(str(hmSet))

	# Final Sign-off!
	signoff(playerList, cpWinCheck, hmWinCheck)


def hvc():
	# Move lists
	moveSet = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	hmSet = []
	cpSet = []

	# Initial win condition checks
	hmWinCheck = winner(hmSet)
	cpWinCheck = winner(cpSet)

	# Greet player
	playerList = [greetPlayer(), "CPU-00"]

	# While neither player has won and there are remaining available moves...
	while not hmWinCheck[0] and not cpWinCheck[0] and moveSet:
		print "---------- Begin Turn ----------".center(100)

		# If the computer has not yet won and there are remaining available moves...
		if not cpWinCheck[0] and moveSet:
			# Get move from human player
			hmChoice = getMoveFromPlayer(playerList[0], moveSet)
			# Apply move choice
			makeMove(hmChoice, hmSet, moveSet)
			# Update win condition check for human player
			hmWinCheck = winner(hmSet)

		# If the human player has not yet won and there are remaining available moves...
		if not hmWinCheck[0] and moveSet:
			# Get move from the computer
			cpChoice = computerChoice(cpSet, hmSet, moveSet)
			# Apply move choice
			makeMove(cpChoice, cpSet, moveSet)
			# Update win condition check for the computer
			cpWinCheck = winner(cpSet)
			# Inform player of computer's choice
			print ("CPU-OO has chosen "+str(cpChoice)+".").center(100)

		# Real-time List Updates...
		if not hmWinCheck[0] and not cpWinCheck[0] and moveSet:
			print "\n"
			print "--------- Turn Summary ---------".center(100)
			print "\n"
			print "-- Chosen Moves --".center(100)
			print ('%s %s' % ('%-16s' % ('%.6s' % (str(playerList[0]),)+" has:",), str(hmSet))).center(100)
			print ('%s %s' % ('%-16s' % ('%.6s' % ("CPU-00",)+" has:",), str(cpSet))).center(100)
			print "-- Available Moves --".center(100)
			print str(moveSet).center(100)
			print "\n"

		# Tie Exception
		if not hmWinCheck[0] and not cpWinCheck[0] and not moveSet:
			hmWinCheck.append(str(hmSet))
			cpWinCheck.append(str(cpSet))

	# Final Sign-off!
	signoff(playerList, hmWinCheck, cpWinCheck)


def cvc():
	# Move lists
	moveSet = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	cp1Set = []
	cp2Set = []

	# Initial win condition checks
	cp1WinCheck = winner(cp1Set)
	cp2WinCheck = winner(cp2Set)

	# Computer Opponent List
	playerList = ["CPU-00", "CPU-01"]

	# While neither computer player has won and there are remaining available moves...
	while not cp1WinCheck[0] and not cp2WinCheck[0] and moveSet:
		print "---------- Begin Turn ----------".center(100)

		if not cp2WinCheck[0] and moveSet:
			# Get move from the computer
			cp1Choice = computerChoice(cp1Set, cp2Set, moveSet)
			# Apply move choice
			makeMove(cp1Choice, cp1Set, moveSet)
			# Update win condition check the computer
			cp1WinCheck = winner(cp1Set)
			# Inform user of computer's choice
			print (str(playerList[0])+" has chosen "+str(cp1Choice)+".").center(100)

		if not cp1WinCheck[0] and moveSet:
			# Get move from the computer
			cp2Choice = computerChoice(cp2Set, cp1Set, moveSet)
			# Apply move choice
			makeMove(cp2Choice, cp2Set, moveSet)
			# Update win condition check the computer
			cp2WinCheck = winner(cp2Set)
			# Inform user of computer's choice
			print (str(playerList[1])+" has chosen "+str(cp2Choice)+".").center(100)

		# Real-time List Updates...
		if not cp1WinCheck[0] and not cp2WinCheck[0] and moveSet:
			print "\n"
			print "--------- Turn Summary ---------".center(100)
			print "\n"
			print "-- Chosen Moves --".center(100)
			print ('%s %s' % ('%-16s' % ('%.6s' % (str(playerList[0]),)+" has:",), str(cp1Set))).center(100)
			print ('%s %s' % ('%-16s' % ('%.6s' % (str(playerList[1]),)+" has:",), str(cp2Set))).center(100)
			print "-- Available Moves --".center(100)
			print str(moveSet).center(100)
			print "\n"

		# Tie Exception
		if not cp1WinCheck[0] and not cp2WinCheck[0] and not moveSet:
			cp1WinCheck.append(str(cp1Set))
			cp2WinCheck.append(str(cp2Set))

		# Verbose Debug
		# print str(zeroWinCheck)+str(zeroSet)+str(oneWinCheck)+str(oneSet)

	# Final Sign-off!
	signoff(playerList, cp1WinCheck, cp2WinCheck)


def main():
	print "Welcome to Fifteen.".center(100)
	print "\n"
	print "Select a game mode by typing one of the following options below:".center(100)
	print "-hvh-  -cvh-  -cvc-".center(100)
	selection = raw_input("> ")
	if selection == "hvh" or selection == "-hvh-":
		hvh()
	elif selection == "cvh" or selection == "-cvh-":
		coinFlip = 8
		print "Would you like to go first? Please indicate your choice with Y or N.".center(100)
		print "Type R to have the turn order to be randomly decided.".center(100)
		youFirst = raw_input("> ")
		if youFirst == "Y" or youFirst == "y":
			print "You will go first.".center(100)
			hvc()
		if youFirst == "N" or youFirst == "n":
			print "The computer will go first.".center(100)
			cvh()
		if youFirst == "R" or youFirst == "r":
			coinFlip = random.randrange(2)
		if coinFlip == 0:
			print "You will go first.".center(100)
			hvc()
		if coinFlip == 1:
			print "The computer will go first.".center(100)
			cvh()
	elif selection == "cvc" or selection == "-cvc-":
		cvc()
	else:
		print "That option is invalid. The game will now exit.".center(100)


if __name__ == '__main__':
	main()
