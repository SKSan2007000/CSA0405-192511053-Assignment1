#!/bin/sh
set -eu
gcc -std=c11 -Wall -Wextra syscall_demo.c -o syscall_demo
printf 'abnormal reading\n' | ./syscall_demo
