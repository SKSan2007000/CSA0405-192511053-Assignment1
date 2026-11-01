# CSA04-192511053-Assignment1
**Student:** B. Santhosh Kumar  
**Register Number:** 192511053  
**Course:** CSA04 – Operating Systems  
**Assignment:** Evaluate and Justify the Operating-System Design of a Smart Hospital

## Environment record (fill after running on your own Ubuntu/WSL2)
- Linux distribution/version: `lsb_release -a`
- Kernel: `uname -a`
- Compiler/version: `gcc --version`
- Python version: `python3 --version`
- Tools: `strace --version`, `/usr/bin/time --version`
- Execution date: __________________

## Repository structure
`Task01` through `Task12` each contain a task brief/analysis and a runnable implementation, demonstration or reproducible calculation. C programs are used where the assignment explicitly requires system calls/process control/benchmarking; Python scripts provide repeatable calculations and decision tables for analytical tasks.

## Setup on Ubuntu / WSL2
```bash
sudo apt update
sudo apt install -y build-essential git python3 strace time
```

## Run every task
```bash
for d in Task{01..04} Task08 Task09 Task11 Task12; do
  (cd "$d" && python3 main.py)
done
(cd Task05 && gcc -std=c11 -Wall -Wextra syscall_demo.c -o syscall_demo && printf 'abnormal reading\n' | ./syscall_demo)
(cd Task06 && gcc -std=c11 -Wall -Wextra file_copy.c -o file_copy && ./file_copy)
(cd Task07 && gcc -std=c11 -Wall -Wextra process_control.c -o process_control && ./process_control)
(cd Task10 && gcc -std=c11 -Wall -Wextra -pthread process_thread_benchmark.c -o benchmark && ./benchmark)
```
Each task has its own README with exact commands and the result to verify.

## Task 6 system-call and timing evidence
```bash
cd Task06
strace -c ./file_copy
/usr/bin/time -v ./file_copy
```
The program itself reports the read() calls made by its copy loop. `strace -c` reports all traced process calls, including runtime/stdio activity, so compare the `read` row carefully rather than expecting every traced read to equal the program's counter.

## Task 7 required buffered-output experiment
```bash
cd Task07
./run_duplicate_output_experiment.sh
```
This demonstrates the effect of stdio buffering across `fork()` when stdout is redirected to a file.

## Task 10 measurements
```bash
cd Task10
./run_all.sh
```
Run at least five trials on your own Ubuntu/WSL2. Keep raw outputs in `results/`; report medians and note the system load/cache conditions. Timings from another machine are not a substitute for your own measurements.

## GitHub submission
Create a GitHub repository named `CSA04-192511053-Assignment1`. Then, from this extracted folder:
```bash
git init
git branch -M main
git add .
git commit -m "Add task-wise OS assignment implementation"
git remote add origin https://github.com/YOUR-USERNAME/CSA04-192511053-Assignment1.git
git push -u origin main
```
Replace `YOUR-USERNAME`. Add at least one meaningful commit for each task (instructions in `GITHUB_COMMIT_PLAN.md`). If private, invite the course faculty as collaborator. Paste the actual repository URL in the Word report and share it with faculty.

## Evidence integrity
Files named `output.txt` are reproducible run logs generated while preparing this package. The `Screenshots/` directory contains no fabricated desktop screenshots. Capture your own Ubuntu terminal screenshots after running each required program and commit them. Replace the environment placeholders with your actual machine details. Do not upload real patient information.
