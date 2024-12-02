#!/bin/bash

if [[ $# -eq 0 ]]
then
    echo "Usage: ./$0 day_number"
fi

mkdir "day$1"
curl "https://adventofcode.com/2024/day/$1/input" -o "day$1/input.txt"