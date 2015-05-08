
#Function that removes repetitions in a list and returns a new list without repetitions
#by Sabastian Mugazambi

def main():
	list = [4,5,6]
	for i in range(0,10):
		list.append(i)
	print list
	
	finalList = []
	
	for i in list:
		if i in finalList:
			finalList.remove(i)
		else:
			finalList.append(i)
	print finalList
	
main()
