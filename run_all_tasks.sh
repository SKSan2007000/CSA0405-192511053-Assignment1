#!/bin/sh
set -eu
for d in Task01 Task02 Task03 Task04 Task08 Task09 Task11 Task12; do
  (cd "$d" && python3 main.py > output.txt)
done
(cd Task05 && ./run.sh > output.txt)
(cd Task06 && ./run.sh > output.txt)
(cd Task07 && ./run.sh > output.txt)
(cd Task07 && ./run_duplicate_output_experiment.sh > duplicate_output_experiment.txt)
(cd Task10 && ./run_all.sh)
echo "All task programs completed. See each Task folder's output.txt and Task10/results/."
