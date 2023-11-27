# Project 0x05-processes_and_signals

This project contains a collection of Bash scripts that demonstrate various tasks related to processes and signals. Each script addresses a specific task and has its own requirements. Below is a list of tasks and their respective scripts.

## Task 0: What is my PID
**Script:** `0-what-is-my-pid.sh`

This script displays its own Process ID (PID).

## Task 1: List your processes
**Script:** `1-list-your-processes.sh`

This script displays a list of currently running processes with the following requirements:
- Shows all processes, for all users, including those without a TTY.
- Displays the information in a user-oriented format.
- Shows the process hierarchy.

## Task 2: Show your Bash PID
**Script:** `2-show-your-bash-pid.sh`

This script displays lines containing the word "bash" to easily get the PID of the Bash process. It cannot use `pgrep`, and the third line of the script disables the ShellCheck error SC2009.

## Task 3: Show your Bash PID made easy
**Script:** `3-show-your-bash-pid-made-easy.sh`

This script displays the PID and process name of processes whose name contains the word "bash" without using `ps`.

## Task 4: To infinity and beyond
**Script:** `4-to-infinity-and-beyond.sh`

This script displays "To infinity and beyond" indefinitely with a sleep of 2 seconds between each iteration.

## Task 5: Don't stop me now!
**Script:** `5-dont-stop-me-now.sh`

This script stops the `4-to-infinity-and-beyond` process using the `kill` command.

## Task 6: Stop me if you can
**Script:** `6-stop-me-if-you-can.sh`

This script stops the `4-to-infinity-and-beyond` process without using the `kill` or `killall` commands.

## Task 7: Highlander
**Script:** `7-highlander.sh`

This script displays "To infinity and beyond" indefinitely with a sleep of 2 seconds between each iteration. It also prints "I am invincible!!!" when receiving a SIGTERM signal.

**Additional Script:** `67-stop-me-if-you-can.sh`

This script is a copy of `6-stop-me-if-you-can.sh` and is used to kill the `7-highlander` process instead of the `4-to-infinity-and-beyond` one.

## Task 8: Beheaded process
**Script:** `8-beheaded-process.sh`

This script kills the `7-highlander` process.

Each script is designed to fulfill its specific task, and you can run them individually to observe their behavior and functionality.
