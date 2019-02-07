# Project Seven - Heap Sort
# NAME: Audrey Gu
# OTHER COMMENTS: Eheh, hacky implemention it is :P

from copy import deepcopy


def isAHeap(H):
	# We begin with the assumption that H is a heap.
	checkVar = True

	# We then test to see whether each parent-child ordering fulfills the heap property.
	for i in range(len(H)):
		# If a given node has children within the range of the list as a whole, and the heap has not yet been shown to be invalid, evaluate whether the three numbers are heaped. Store the boolean result.
		if 2*i+1 <= (len(H)-1) and 2*i+2 <= (len(H)-1) and checkVar:
			sCheckVar = checkTree(H[i], H[2*i+1], H[2*i+2])
		# Otherwise, if a node has only one child (meaning that that child is the last value in the heap) and this child is shown to be larger than its parent, note this failure.
		elif 2*i+1 == (len(H)-1) and H[2*i+1] > H[i]:
			sCheckVar = False
		# If any parent-child combination has been noted to fail the heap property, designate the whole list as failing to uphold the ehap property.
		if not(sCheckVar):
			checkVar = False

	# Return the true/false result.
	return checkVar


def checkTree(p, lChild, rChild):
	if p >= lChild and p >= rChild:
		return True
	else:
		return False


def singleSwap(p, lChild, rChild, L):
	checkVar = [0, 0]
	try:
		# If the left child is the greatest value of the three, swap with the parent. Note the swap in checkVar.
		if L[lChild] > L[p] and L[lChild] >= L[rChild]:
			(L[p], L[lChild]) = (L[lChild], L[p])
			checkVar[0] = 1
		# If the right child is the greatest value of the three, swap with the parent. Note the swap in checkVar.
		elif L[rChild] > L[p] and L[rChild] >= L[lChild]:
			(L[p], L[rChild]) = (L[rChild], L[p])
			checkVar[1] = 1
		# If the parent has the last list value as its left child and is lesser than it, swap the two. Note the swap in checkVar.
		elif lChild == len(L)-1 and L[lChild] > L[p]:
			(L[p], L[lChild]) = (L[lChild], L[p])
			checkVar[0] = 1
	except IndexError:
		pass
	return checkVar


def checkSwap(p, L):
	checkVar = singleSwap(p, p*2+1, p*2+2, L)
	try:
		if checkVar[0]:
			checkSwap(p*2+1, L)
		elif checkVar[1]:
			checkSwap(p*2+2, L)
	except IndexError:
		pass


def listToHeap(L):
	# In reverse order starting from the highest index value:
	for i in range(len(L), -1, -1):
		# Evaluate whether or not a parent needs to be swapped with its children.
		initialSwap = singleSwap(i, 2*i+1, 2*i+2, L)
		# If a swap has occurred and the new left child has at least one child of its own, call checkSwap to check the child's children.
		if initialSwap[0] and 2*(2*i+1)+1 <= len(L)-1:
			checkSwap(2*i+1, L)
		# If a swap has occurred and the new right child has at least one child of its own, call checkSwap to check the child's children.
		if initialSwap[1] and 2*(2*i+1)+1 <= len(L)-1:
			checkSwap(2*i+2, L)


def sortHeap(H):
	i = len(H)-1
	while i > 0:
		(H[0], H[i]) = (H[i], H[0])
		duplicate = deepcopy(H[0:i])
		checkSwap(0, duplicate)
		H[0:i] = duplicate
		i = i-1
	if H[0] > H[1]:
		(H[0], H[1]) = (H[1], H[0])


def sortList(L):
	listToHeap(L)
	sortHeap(L)
