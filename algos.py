def power(n):
	p = 0
	if n == 0:
		return p
	elif n % 2 == 0 and n != 0.0:
		print(n)
		p = power(n/2)*power(n/2)
	else:
		p = 2*(power(n-1))

print(power(2))