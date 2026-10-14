# Unix/Linux - File Permissions, Environment, and Basic Utilities (Printing & Email)

---

# Big Picture Context

These topics are fundamental parts of working with a Linux system.

```text
Linux
│
├── File System
├── File Management
├── Directories
│
├── File Permissions      ← You are Here
├── Environment           ← You are Here
├── Basic Utilities       ← You are Here
│     ├── Printing
│     └── Email
│
├── Users & Groups
├── Processes
├── Networking
├── Shell Scripting
└── System Administration
```

These concepts become especially important when working on shared servers, cloud instances, Docker containers, and production systems.

---

# Part 1: Unix/Linux File Permissions

## What are File Permissions?

File permissions define **who can access a file or directory and what actions they are allowed to perform**.

Every file and directory in Linux has a set of permissions.

Permissions control:

- Who can read a file
- Who can modify a file
- Who can execute a file
- Who can access a directory

Without permissions, Linux would not be a secure multi-user operating system.

---

## Why are Permissions Important?

Imagine a company server:

```text
Server
│
├── Employee A
├── Employee B
├── Employee C
└── Administrator
```

Suppose Employee A stores:

```text
salary.xlsx
```

Without permissions:

- Anyone could read it.
- Anyone could modify it.
- Anyone could delete it.

Permissions prevent unauthorized access.

---

## Permission Categories

Linux divides users into three categories.

```text
File
│
├── Owner (u)
├── Group (g)
└── Others (o)
```

### Owner

The user who created the file.

Example:

```text
rohan
```

---

### Group

A collection of users.

Example:

```text
developers
```

Members of this group can receive shared permissions.

---

### Others

Every user who is neither the owner nor part of the group.

---

## Types of Permissions

Linux has three basic permissions.

```text
Permission
│
├── Read (r)
├── Write (w)
└── Execute (x)
```

---

### Read (r)

Allows viewing the contents of a file.

Example:

```text
notes.txt
```

A user with read permission can:

```bash
cat notes.txt
```

or

```bash
less notes.txt
```

---

### Write (w)

Allows modifying the file.

Examples:

- Edit the contents
- Save changes
- Append text

---

### Execute (x)

Allows running a file as a program or script.

Example:

```bash
python app.py
```

or

```bash
./backup.sh
```

Without execute permission:

```bash
./backup.sh
```

returns:

```text
Permission denied
```

---

# Permission Display

Run:

```bash
ls -l
```

Example output:

```text
-rwxr-xr--
```

Break it into sections:

```text
- rwx r-x r--
```

| Part | Meaning            |
| ---- | ------------------ |
| -    | File type          |
| rwx  | Owner permissions  |
| r-x  | Group permissions  |
| r--  | Others permissions |

---

## File Types

First character:

```text
-
```

Regular file.

Other possibilities:

| Symbol | Meaning          |
| ------ | ---------------- |
| -      | Regular File     |
| d      | Directory        |
| l      | Symbolic Link    |
| c      | Character Device |
| b      | Block Device     |

Example:

```text
drwxr-xr-x
```

means it is a directory.

---

# Understanding Permission Strings

Example:

```text
-rwxrwxr-x
```

Split:

```text
Owner  Group  Others

rwx    rwx    r-x
```

Owner:

- Read
- Write
- Execute

Group:

- Read
- Write
- Execute

Others:

- Read
- Execute

---

# Numeric Permission Values

Each permission has a numeric value.

| Permission | Value |
| ---------- | ----- |
| Read       | 4     |
| Write      | 2     |
| Execute    | 1     |

Add them together.

Example:

```text
rwx

4+2+1 = 7
```

Examples:

| Permission | Number |
| ---------- | ------ |
| rwx        | 7      |
| rw-        | 6      |
| r-x        | 5      |
| r--        | 4      |
| ---        | 0      |

---

# Common Permission Sets

| Numeric | Symbolic  |
| ------- | --------- |
| 777     | rwxrwxrwx |
| 755     | rwxr-xr-x |
| 700     | rwx------ |
| 644     | rw-r--r-- |
| 600     | rw------- |

---

# Changing Permissions

Command:

```bash
chmod
```

Example:

```bash
chmod 755 script.sh
```

Now permissions become:

```text
rwxr-xr-x
```

---

Another example:

```bash
chmod 644 notes.txt
```

Permissions:

```text
rw-r--r--
```

---

# Symbolic chmod

Instead of numbers:

```bash
chmod u+x script.sh
```

Adds execute permission to owner.

Remove write:

```bash
chmod g-w file.txt
```

Add read:

```bash
chmod o+r file.txt
```

Symbols:

| Symbol | Meaning |
| ------ | ------- |
| u      | Owner   |
| g      | Group   |
| o      | Others  |
| a      | All     |

---

# Changing Ownership

Command:

```bash
chown
```

Example:

```bash
sudo chown rohan file.txt
```

Owner changes to:

```text
rohan
```

---

Change group:

```bash
chgrp developers file.txt
```

---

# Real Use Cases

### Python Script

```text
backup.sh
```

Needs execute permission.

```bash
chmod +x backup.sh
```

---

### Website

Web server needs permission to read HTML files.

Without read permission:

Website returns:

```text
403 Forbidden
```

---

### AI Model

Large model file:

```text
model.pt
```

Should only be writable by administrators.

Permission:

```text
644
```

---

# Part 2: Unix/Linux Environment

---

## What is the Environment?

The environment is a collection of variables and settings that affect how programs run.

Examples include:

- Username
- Home directory
- Current shell
- Search paths
- Language
- Terminal type

Programs read these variables to understand their execution context.

---

# Environment Variables

Examples:

```text
HOME

PATH

USER

PWD

SHELL

LANG
```

---

## HOME

Your home directory.

Example:

```text
/home/rohan
```

Display:

```bash
echo $HOME
```

---

## USER

Current logged-in user.

```bash
echo $USER
```

Output:

```text
rohan
```

---

## PWD

Current working directory.

```bash
echo $PWD
```

Example:

```text
/home/rohan/Documents
```

---

## SHELL

Current shell.

```bash
echo $SHELL
```

Example:

```text
/bin/bash
```

---

## PATH

One of the most important variables.

Example:

```text
/usr/local/bin
/usr/bin
/bin
```

Display:

```bash
echo $PATH
```

---

## Why PATH Matters

Suppose you type:

```bash
python
```

Linux searches each directory in `PATH`.

```text
PATH

↓

/usr/local/bin

↓

/usr/bin

↓

/bin
```

When it finds:

```text
python
```

it executes that program.

Without `PATH`, you would need to type the full location:

```bash
/usr/bin/python3
```

every time.

---

# Creating Environment Variables

Temporary variable:

```bash
export PROJECT=AI
```

Check it:

```bash
echo $PROJECT
```

Output:

```text
AI
```

It exists only in the current shell session.

---

# Permanent Variables

Stored in files like:

```text
~/.bashrc

~/.profile

~/.zshrc
```

Example:

```bash
export JAVA_HOME=/usr/lib/jvm/java-21
```

After reloading the shell:

```bash
source ~/.bashrc
```

the variable becomes available in future sessions.

---

# Viewing All Variables

```bash
env
```

or

```bash
printenv
```

---

# Real Use Cases

### Python Virtual Environment

```text
PATH
```

changes so that:

```text
python
```

points to the virtual environment instead of the system Python.

---

### Java Development

```text
JAVA_HOME
```

helps tools locate the Java installation.

---

### CUDA

AI frameworks use variables like:

```text
CUDA_HOME
```

to locate GPU libraries.

---

### API Keys

Applications often read secrets from environment variables.

Example:

```text
OPENAI_API_KEY
```

Instead of hardcoding keys into source code, storing them in environment variables improves security and makes deployment easier.

---

# Part 3: Unix/Linux Basic Utilities

---

# Printing

Modern Linux printing is usually managed by the Common UNIX Printing System (CUPS), but command-line utilities are still useful, especially on servers.

---

## Print a File

Command:

```bash
lp report.pdf
```

or

```bash
lpr report.pdf
```

Sends the document to the default printer.

---

## Show Printers

```bash
lpstat -p
```

Displays available printers.

---

## Show Print Queue

```bash
lpq
```

Displays pending print jobs.

---

## Cancel Print Job

```bash
cancel JOB_ID
```

Example:

```bash
cancel 15
```

---

# Real Use Cases

- Printing invoices
- Printing reports
- Printing shipping labels
- Printing certificates
- Office document workflows

Many server environments have no printers attached, so these commands are more common on desktop Linux systems or print servers.

---

# Email Utilities

Linux can send email directly from the command line.

Historically, this has been used for:

- System alerts
- Backup notifications
- Scheduled reports
- Error logs

---

## mail Command

Example:

```bash
mail user@example.com
```

After typing the command:

```text
Subject:
```

Enter:

```text
Backup Complete
```

Write the message.

Press:

```text
Ctrl + D
```

to send.

---

## Send a File

```bash
mail -s "Monthly Report" user@example.com < report.txt
```

---

## Send Output

```bash
df -h | mail -s "Disk Report" admin@example.com
```

This emails the disk usage report generated by `df -h`.

---

## Modern Alternatives

Many systems today use utilities such as:

- `mailx`
- `sendmail`
- `postfix`
- `msmtp`

or external email APIs and SMTP services for automated notifications.

---

# Real Use Cases

### Daily Backup

A cron job finishes.

Linux automatically emails:

```text
Backup completed successfully.
```

---

### Server Monitoring

Disk usage reaches 95%.

Linux sends:

```text
Disk space critically low.
```

---

# Summary

| Topic               | Description                                                    |
| ------------------- | -------------------------------------------------------------- |
| File Permissions    | Control who can read, write, and execute files and directories |
| Permission Types    | Read (`r`), Write (`w`), Execute (`x`)                         |
| User Categories     | Owner (`u`), Group (`g`), Others (`o`)                         |
| Numeric Permissions | 755, 644, 600, 777, etc.                                       |
| `chmod`             | Changes file permissions                                       |
| `chown`             | Changes file ownership                                         |
| `chgrp`             | Changes a file's group ownership                               |
| Environment         | Variables that influence program behavior                      |
| Common Variables    | `PATH`, `HOME`, `USER`, `PWD`, `SHELL`, `LANG`                 |
| `export`            | Creates or modifies environment variables                      |
| `env` / `printenv`  | Display environment variables                                  |
| Printing            | `lp`, `lpr`, `lpstat`, `lpq`, `cancel`                         |
| Email               | `mail`, `mailx`, `sendmail`, `postfix`                         |
