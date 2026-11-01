#!/bin/sh
set -eu
gcc -std=c11 -Wall -Wextra file_copy.c -o file_copy
./file_copy
