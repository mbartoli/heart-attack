#!/bin/bash

MACHINES=(amazonia arden ash birnam bluebell broceliande clover columbine cosmos crocus delphinium dittany elm fangorn feverfew fir flax fleabane foxglove freesia gardenia godswood goldenrod heath heather hollyhock honeysuckle hundredacre hyacinth lavender lothlorien mallow menoa mirkwood mustard nettle oak olympia palm phlox pine poinsettia redwood sherwood terabithia truffula verbena violet walnut willow yarrow yggdrasil)

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

RESULTS=()
i=1
for machine in ${MACHINES[*]}
	do 
	echo "connecting to $machine"
	RESULTS+=($(source link.sh $machine $i &))
	echo "${RESULTS[*]}"
	i=$(($i+1))		
	done


