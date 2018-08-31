

if __name__ == '__main__':
	with open('in.txt', 'r') as file,\
	open('out.csv', 'a', encoding='utf-8') as file1:
		for line in file:
			data = [x.strip() for x in line.split('	')]
			data1 = []
			data1.append(data[0])
			data1.append(data[1])
			data1.append(data[2])
			new_line = ', '.join(data1)
			print(new_line)
			file1.write(new_line + '\n')