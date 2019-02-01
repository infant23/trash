min = 316				# 100 <= min <= sqrt(100000)
max = 999				# 999 <= max <= sqrt(999999)
# start = 990
n = 0					# main iteration counter
solution = [0, 0, 0]	# number's pair x, y and their palindrome


x = max
while x >= min:
	y = x
	while y >= min:
		if x % 11 == 0 or y % 11 == 0:
			tmp = x * y
			poli = [tmp // 10 ** x % 10 for x in range(6)]
			if (all([poli[i] == poli[5 - i] for i in range(3)])):
				min = y
				print('--Checking pair:', x, ':', y, ', palindrome:', tmp, ', iteration: ', n, ', bellow limit is:', min)
				if tmp > solution[2]:
					solution = [x, y, tmp]
			n += 1
		y -= 1
	x -= 1
if solution[2] > 0:
	print('Desired pair:', solution[0], ':', solution[1], ', palindrome:', solution[2], ', number of iterations: ', n)
else:
	print('There are not numbers that can create a palindrome.')


# for x in range(max, min, -1):
# 	for y in range(x, min, -1):
# 		if x % 11 == 0 or y % 11 == 0:
# 			n += 1
# 			tmp = x * y
# 			poli = [tmp // 10 ** x % 10 for x in range(6)]
# 			if (all([poli[i] == poli[5 - i] for i in range(3)])):
# 				min = y
# 				print('--Checking pair:', x, ':', y, ', palindrome:', tmp, ', iteration: ', n, ', bellow limit is:', min)
# 				if tmp > solution[2]:
# 					solution = [x, y, tmp]
# if solution[2] > 0:
# 	print('Desired pair:', solution[0], ':', solution[1], ', palindrome:', solution[2], ', number of iterations: ', n)
# else:
# 	print('There are not numbers that can create a palindrome.')

# for x, y in ((x, y) for x in range(start, min, -11) for y in range(max, min, -1)):
# 	n += 1
# 	tmp = x * y
# 	poli = [tmp // 10 ** x % 10 for x in range(6)]
# 	if (all([poli[i] == poli[5 - i] for i in range(3)])):
# 		print('--Checking pair:', x, ':', y, ', palindrome:', tmp, ', iteration: ', n, ', bellow limit is:', min)
# 		if tmp > solution[2]:
# 			solution = [x, y, tmp]
# if solution[2] > 0:
# 	print('Desired pair:', solution[0], ':', solution[1], ', palindrome:', solution[2], ', number of iterations: ', n)
# else:
# 	print('There are not numbers that can create a palindrome.')


# for x, y in ((x, y) for x in range(max, min, -1) for y in range(x, min, -1)):
# 	if x % 11 == 0 or y % 11 == 0:
# 		n += 1
# 		tmp = x * y
# 		poli = [tmp // 10 ** x % 10 for x in range(6)]
# 		if (all([poli[i] == poli[5 - i] for i in range(3)])):
# 			min = y
# 			print('--Checking pair:', x, ':', y, ', palindrome:', tmp, ', iteration: ', n, ', bellow limit is:', min)
# 			if tmp > solution[2]:
# 				solution = [x, y, tmp]
# if solution[2] > 0:
# 	print('Desired pair:', solution[0], ':', solution[1], ', palindrome:', solution[2], ', number of iterations: ', n)
# else:
# 	print('There are not numbers that can create a palindrome.')
