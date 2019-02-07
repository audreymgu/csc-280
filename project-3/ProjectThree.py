# Project 3 - The 15 Game
# NAME: Audrey Gu
# DUE DATE:
# OTHER COMMENTS: Wheeeeee! Conditionals!

import re

def greetPlayers():
	playerList = []
	playerList.append(raw_input("Hi! Player One, what is your name? > "))
	playerList.append(raw_input("Hi! Player Two, what is your name? > "))
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


def getMoveFromPlayer(player, moves):
	choice = raw_input(str(player)+", what is your next move? > ")
	while (not isInRange(choice)) or (not int(choice) in moves):
		choice = raw_input(str(player)+", that choice is invalid. Input another move. > ")
	return int(choice)


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


def makeMove(choice, playerSet, moveSet):
	playerSet.append(moveSet.pop(moveSet.index(choice)))


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


def main():
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
			print "---- Time to strategize! ----".center(40)
			print "\n"
			print "-- Chosen Moves --".center(40)
			print ('%s %s' % ('%-16s' % ('%.6s' % (str(playerList[0]),)+" has:",), str(zeroSet))).center(40)
			print ('%s %s' % ('%-16s' % ('%.6s' % (str(playerList[1]),)+" has:",), str(oneSet))).center(40)
			print "\n"
			print "-- Available Moves --".center(40)
			print str(moveSet).center(40)
			print "\n"

		# Tie Exception
		if not zeroWinCheck[0] and not oneWinCheck[0] and not moveSet:
			zeroWinCheck.append(str(zeroSet))
			oneWinCheck.append(str(oneSet))

		# Verbose Debug
		# print str(zeroWinCheck)+str(zeroSet)+str(oneWinCheck)+str(oneSet)

	# Final Sign-off!
	signoff(playerList, zeroWinCheck, oneWinCheck)


if __name__ == '__main__':
	main()
