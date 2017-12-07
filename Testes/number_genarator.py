from sys import stdin
import random
L = 40000
m_max = 4000
x = 0


print (L)
print (m_max)
for i in range(0, m_max):
	x += random.randint(1, 10)
	print(x, end = '')
	print(' ', end = '')

print()
print('0')