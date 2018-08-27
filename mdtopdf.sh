#!/bin/bash
if [ -z "$1" ]; then
    echo "Usage: `basename $0` [host]"
    exit
fi

IN=$1
OUT=$2
pandoc -s $IN -o $OUT
