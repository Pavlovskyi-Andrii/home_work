#!/bin/bash

echo "Ugadai chislo vid 1 do 100 za 5 sprob"

random_number=$((RANDOM % 100 + 1))
count=5
for ((i=1; i<=count; i++ )); do	
	echo "Спроба № "$i" напишіть число"
	read chislo


	if [[ "$random_number" > "$chislo" ]]; then
	echo "Random number biger than your number. try agen "
	elif [[ "$random_number" < "$chislo" ]]; then 
		echo "Random number less than your number. try agen "
	elif [[ "$random_number" == "$chislo" ]]; then 
        	echo "You right correct number is $chislo"
  		exit 0
	fi
done
echo "Вы проиграли! Загаданное число было: $random_number"
