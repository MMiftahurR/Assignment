#!/usr/bin/python3

import sys
prime = []
def main():
	if(len(sys.argv) == 3):
		low = int(sys.argv[1])
		hi = int(sys.argv[2])
		while(low <= hi):
			if(isPrime(low)):
				prime.append(low)
			low += 1
	else:
		print("Format : ./tugas1.py [batas bawah] [batas atas]")

def isPrime(n):
	if n < 2:
		return False
	if n % 2 == 0:
		if n > 2:
			return False
	for i in range (3,int(n**0.5)+1,2):
		if n % i == 0:
			return False
	return True

if __name__ == "__main__":
	main()
	print("Bilangan prima antara %s dan %s adalah : " %(sys.argv[1], sys.argv[2]))
	print(prime)
