import random

class Counter():
	def __init__(self, low, high):
		self.current = low
		self.high = high

	def __iter__(self):
		return self

	def __next__(self):
		if self.current > self.high:
			raise StopIteration
		else:
			self.current += 1
			return self.current - 1


a = random.randint(0, 8)
x = [i for i in range (1, 6)]
print(x)

def factorial_rec(n):
	return 1 if n == 1 else n * factorial_rec(n-1)

def square(n):
	return pow(n, 2)

# print(factorial_rec(a))

for c in Counter(3, 8):
	print(c)

print(list(map(square, x)))