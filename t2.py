from sys import stdin

#really high value
infinite = 12345678

#matrix used for memorization in dp
memo_table = [[0]*51 for i in range(51)]

# actual problem solving
while True:
	#reading stick length
	length = int(stdin.readline())

	if length == 0:
		break

	#reading number of stick cuts
	ncuts = int(stdin.readline())

	#reading stick cuts
	cuts = [0]
	for x in stdin.readline().rstrip().split(' '):
		cuts.append(int(x))
	cuts.append(length)

	#calculating costs for every cut
	for j in range(1,len(cuts)):
		for i in reversed(range(0,j)):
			#if we cut a stick with length 0, its cost will be 0
			if(i+1 == j):
				memo_table[i][j] = 0
			else:
				#the current cut value is maximum
				memo_table[i][j] = infinite

				#now im searching for the minimal cost for the previous calculated cuts
				for k in range(i+1,j):
					calculated_value = memo_table[i][k] + memo_table[k][j]
					if(calculated_value < memo_table[i][j]):
						memo_table[i][j] = calculated_value

				#this cut should have the previous costs plus the current cut cost
				current_cut_price = cuts[j] - cuts[i]
				memo_table[i][j] += current_cut_price

	#printing the result
	print('The minimum cutting is {0}.'.format(memo_table[0][ncuts+1]))