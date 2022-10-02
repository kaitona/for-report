python3 2022problemA.py < 2022A.in > 2022A.out
value=`diff 2022A.out 2022A.ans`
if [[ -n $value ]]; then
	rm 2022A.out
	echo failed...
else
	echo Clear!
fi

