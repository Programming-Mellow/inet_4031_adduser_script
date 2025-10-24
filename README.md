# INET4031 Add Users Script and User List

## Program Description
Detailed and helpful description paragraph goes here.  Describe how the program will help the user.  It should talk about how the program is an automated way for the user to accomplish the manual task of adding users. Also include a description of what commands a user would normally use to add a user and then describe how those ***SAME COMMANDS*** are used by the script and automated.

This program provides an automated solution for adding (or removing) multiple users on a Linux system by reading structured input from a file. Instead of manually creating each user using terminal commands, the script processes an input list and performs all account creation, password setup, and group assignments automatically.

A system administrator would usually have to run a series of commands like adduser username, passwd username, and adduser username groupname one at a time for each new user. This program automates that process, creating and executing those same system commands in sequence for multiple users. Each command follows the standard Linux syntax and leverages Python’s os.system() function to execute them.

Additionally, the program includes a “dry-run” mode, allowing users to preview what commands would run without making any system changes. This feature is helpful for verifying that the input file is correct before performing real operations.

## Program User Operation
This Python script reads user information from an input file and automates user account operations based on that data. When the script runs, it first prompts the user to choose whether to perform a dry-run or an actual run.

If the user selects dry-run mode, the script prints the Linux commands that would be executed but does not make any changes to the system.
If the user chooses a normal run, the script executes the commands to add or delete users, assign groups, and set passwords as indicated in the input file.

### Input File Format
Each line of the input file represents a single user record, containing five fields separated by colons (:):

username:password:last_name:first_name:groups

If you wish to skip a line, place a # character at the beginning of it. Any line starting with # is treated as a comment and ignored by the program.

If a user should not belong to any additional groups, simply enter a dash (-) in the groups field.

### Command Excuction
To run the script, navigate to the directory containing both the Python file and your input file, then ensure the Python script is executable using:

bash
chmod +x create-users.py

You can execute the script using standard input redirection:

bash
./create-users.py < create-users.input

This feeds the contents of create-users.input into the script line by line.
Alternatively, you can call the file directly and modify the script to open the input file from an argument.

During a normal (non-dry-run) execution, the script performs these automated system tasks:

- Creates a user with /usr/sbin/adduser --disabled-password --gecos 'First Last,,,' username
- Sets the user’s password via /bin/echo -ne 'password\npassword' | sudo passwd username
- Adds the user to the appropriate groups with /usr/sbin/adduser username groupname

All commands are logged to the terminal for transparency.

### "Dry Run"
If the user selects the dry-run option when prompted (Run in dry-run mode? (Y/N):), the script does not actually execute any os.system() commands.

Instead, it prints statements showing exactly what commands would have run. This allows the user to confirm the script’s actions before making any changes to the system.

In dry-run mode, the program also:

- Prints error messages for invalid or incomplete lines in the input file.
- Displays which lines were skipped (such as comments starting with #).

When a normal (non-dry-run) run is chosen, those informational messages are suppressed, and the commands are executed directly on the system.
