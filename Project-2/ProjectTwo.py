# Project Two - Perpetual Calendar
# NAME: George Gu
# DUE DATE: 09/23/16
# OTHER COMMENTS: To the next leap year, and beyond!


def intToDayOfWeek(n):
	days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
	if n < 7:
		return days[n]
	else:
		return "ERROR"


def isValidDate(y, m, d):
	if(m < 1 or m > 12 or d < 1 or d > 31 or y < 1800 or y > 2099):
		return False
	elif((d > 30) and (m == 4 or m == 6 or m == 9 or m == 11)) or (d > 29 and m == 2):
		return False
	elif(d > 28 and m == 2) and isALeapYear(y) is False:
		return False
	else:
		return True

				
def isALeapYear(n):
	# A year is a leap year if it is:
	# Divisible by 4, but not by 100
	# Divisible by 400 (and, by implication, 100 and 4)
	if n % 400 == 0:
		return True
	elif(n % 100 != 0 and n % 4 == 0):
		return True
	else:
		return False
		
def countLeapYear(y):
	if y >= 1800 and y < 1900:
		leapCount = (y - 1800)/4
		return int(leapCount)
	else:
		leapCount = ((y - 1800)/4)-1
		return int(leapCount)

def computeDayOfWeek(y, m, d):
	monthOffset = [3, 6, 6, 2, 4, 0, 2, 5, 1, 3, 6, 1]
	if not(isValidDate(y, m, d)):
		return 999
	elif m > 2 or y == 1800:
		day = (monthOffset[m - 1] + (y - 1800) + countLeapYear(y) + d) % 7
		return day
	else:
		day = (monthOffset[m - 1] + (y - 1800) + countLeapYear(y - 1) + d) % 7
		return day
