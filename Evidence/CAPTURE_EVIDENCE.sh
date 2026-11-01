#!/bin/sh
# Run from repository root after installing gcc, strace and time.
set -eu
mkdir -p Evidence Screenshots
{
  echo "DATE: $(date -Is)"
  echo "DISTRIBUTION:"; (lsb_release -a 2>&1 || cat /etc/os-release)
  echo "KERNEL:"; uname -a
  echo "GCC:"; gcc --version | head -n 1
  echo "PYTHON:"; python3 --version
  echo "STRACE:"; strace --version | head -n 1
} > Evidence/environment.txt
for d in Task01 Task02 Task03 Task04 Task08 Task09 Task11 Task12; do
  (cd "$d" && python3 main.py) > "Evidence/${d}_output.txt"
done
(cd Task05 && ./run.sh) > Evidence/Task05_output.txt
(cd Task06 && ./run.sh) > Evidence/Task06_output.txt
(cd Task06 && strace -c ./file_copy) 2> Evidence/Task06_strace_summary.txt
(cd Task06 && /usr/bin/time -v ./file_copy) 2> Evidence/Task06_time.txt
(cd Task07 && ./run.sh) > Evidence/Task07_output.txt
(cd Task07 && ./run_duplicate_output_experiment.sh) > Evidence/Task07_duplicate_output.txt
(cd Task10 && ./run_all.sh) > Evidence/Task10_output.txt
echo "Evidence captured. Now take real terminal screenshots and save them in Screenshots/."
