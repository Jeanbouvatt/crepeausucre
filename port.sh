#Give corresponding port
if [ "$1" == "i" ]
then
	RES=8091
fi
if [ "$1" == "s" ]
then
	RES=8092
fi
if [ "$1" == "w" ]
then
	RES=8090
fi
if [ "$1" == "b" ]
then
	RES=8093
fi
if [ "$1" == "p" ]
then
	RES=8094
fi
echo $RES

echo "$1=0.0.0.0:$RES" >> loltext
