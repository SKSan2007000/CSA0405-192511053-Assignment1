#!/bin/sh
set -eu
# Run only after `git init` and after setting your verified Git email.
for spec in \
"Task01|Complete Task 1 requirements evaluation" \
"Task02|Complete Task 2 operating system types" \
"Task03|Complete Task 3 OS structures" \
"Task04|Complete Task 4 OS services" \
"Task05|Implement Task 5 system call demonstration" \
"Task06|Complete Task 6 file copy system call program" \
"Task07|Complete Task 7 process control program" \
"Task08|Complete Task 8 CPU protection model" \
"Task09|Complete Task 9 memory and DMA analysis" \
"Task10|Add Task 10 process and thread benchmarks" \
"Task11|Complete Task 11 hospital OS recommendation" \
"Task12|Complete Task 12 remote and cloud design challenge"; do
  folder=${spec%%|*}
  message=${spec#*|}
  git add "$folder"
  git commit -m "$message"
done
git add README.md GITHUB_COMMIT_PLAN.md Diagrams Evidence Screenshots
git commit -m "Add documentation diagrams and execution evidence"
