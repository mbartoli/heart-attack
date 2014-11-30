#!/bin/zsh
cleanup()
{
	rm -f /tmp/tempfile
	return $?
}

control_c()
{
	echo "exiting"
	cleanup
	exit $?
}

trap control_c SIGINT


n=0
echo "welcome to attack_aux"
for num in 1 2 3 4
	do      
        n=$(($1+$num))
	python "grab.py" "segment$n.txt" 1000000 "vuln$n.txt"
	done
