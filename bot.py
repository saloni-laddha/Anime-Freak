import sys
import random



def reply(sentence):
	index = int(random.randint(0, 49))
	print(index)
	count1 = 0
	with open('out.csv', 'r') as file:
		for line in file:
			if count1 == index:
				data = [x.strip() for x in line.split(',')]
				line = str(data[0]) + ' with IMDb of ' + str(data[1]) + '.'
				print(line)
				return (line)
			count1 += 1