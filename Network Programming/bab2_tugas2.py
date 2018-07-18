#!/usr/bin/python3

import sys
def main():
	if(len(sys.argv) == 2):
		filename = sys.argv[1]
		fo = open(filename,"r")
		readF = fo.read()
		readF = readF.lower()
		readF = readF.split()
		readF = [i.split('.',1)[0] for i in readF]
		readF = list(set(readF))
		readF = sorted(readF,reverse=True)
		print("Hasil dari split dan sorting:")
		print(readF)
	else:
		print("Format: ./tugas2.py [nama file text.txt]")

if __name__ == "__main__":
	main()
