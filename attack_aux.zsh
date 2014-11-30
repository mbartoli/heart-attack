#!/bin/zsh

n=0
for num in 1 2 3 4 5 6 7 8
	do      
        n=$(($1+$num))
	python grab.py "segment$n.txt" 1000000 "res$n.txt"	
	done
