#!/usr/bin/python3

from sys import argv

script, filename = argv
fo = open(filename,"r")
txt = fo.read()
txt = txt.split()
txt = [i.lower() for i in txt]
txt = [i.split('.',1)[0] for i in txt]
txt = [i.split(',',1)[0] for i in txt]
txt = list(set(txt))
txt = sorted(txt,reverse=True)
print("Daftar kata yang sudah dilakukan reverse sorting, tanpa duplikasi dan dimasukkan list :")
print(txt)
