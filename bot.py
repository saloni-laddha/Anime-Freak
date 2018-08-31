import sys
import random



def reply(sentence):
	index = int(random.randint(0, 99))
	print(index)
	count1 = 0
	with open('out.csv', 'r') as file:
		for line in file:
			if count1 == index:
				print(line)
				return (line)
			count1 += 1