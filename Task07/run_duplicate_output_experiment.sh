#!/bin/sh
set -eu
gcc -std=c11 -Wall -Wextra duplicate_output.c -o duplicate_output
./duplicate_output > duplicate_output.txt
echo "Contents of redirected output:"
cat duplicate_output.txt
echo "The pre-fork buffered line is flushed once by child exit() and once by parent exit()."
