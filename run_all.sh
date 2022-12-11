#!/bin/bash

for i in $(seq -f "%2g" 1 25)
do
    DIR="./day$i"
    if test -d "$DIR";
    then
        cd "$DIR"
        echo "Day $i:"
        python "p1.py"
        python "p2.py"
        printf "\n"
        cd ..
    fi
done