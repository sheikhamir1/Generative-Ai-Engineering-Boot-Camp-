# Linux - File Management and Directories

---

# 1. Big Picture Context

Before learning file management, understand where it fits in Linux.

```text
Linux
│
├── Installation
├── Terminal
├── File System
│
├── File Management   ← You are Here
│
├── Directories       ← You are Here
│
├── Permissions
├── Users
├── Processes
├── Package Management
├── Networking
└── Shell Scripting
```

Everything you do in Linux revolves around files and directories.

When writing code, downloading datasets, installing software, editing configuration files, or deploying AI applications, you are constantly managing files.

---

# 2. What is a File?

A **file** is the smallest unit used to store data permanently on storage devices like SSDs or HDDs.

A file can contain:

- Text
- Images
- Videos
- Programs
- Configuration
- Database records
- Logs

Examples:

```text
notes.txt
photo.png
movie.mp4
main.py
config.yaml
database.db
```

Different files store different types of information.

---

# 3. What is File Management?

File Management means performing operations on files.

These operations include:

- Creating files
- Viewing files
- Editing files
- Renaming files
- Copying files
- Moving files
- Deleting files
- Searching files
- Compressing files
- Changing permissions
- Changing ownership

Every Linux administrator or developer performs these tasks daily.

---

# 4. Real World Examples

## AI Engineer

```text
Download Dataset

↓

Store Dataset

↓

Write Python Script

↓

Save Model

↓

Load Model

↓

Delete Old Checkpoints
```

Every step involves file management.

---

## Web Developer

```text
Create Project Folder

↓

Create HTML Files

↓

Create CSS Files

↓

Create JavaScript Files

↓

Upload to Server
```

---

## System Administrator

```text
Backup Configuration

↓

Copy Log Files

↓

Delete Temporary Files

↓

Archive Old Logs
```

---

# 5. What is a Directory?

A **directory** is a container that stores files and other directories.

It helps organize data.

Example:

```text
Documents/
    report.pdf
    notes.txt
```

The directory **Documents** contains two files.

Directories can also contain other directories.

```text
Projects/
    Website/
    AI/
    College/
```

---

# 6. Linux Directory Structure

Linux starts from one root directory.

```text
/
```

Everything exists under this root.

```text
/
├── home
├── etc
├── usr
├── var
├── boot
├── dev
├── proc
├── tmp
├── opt
└── media
```

Unlike Windows, Linux does **not** use drive letters like:

```text
C:
D:
E:
```

Everything belongs to one unified directory tree.

---

# 7. Root Directory (/)

The root directory is the top-most directory.

```text
/
```

Every file and every directory ultimately exists somewhere below `/`.

Example:

```text
/home/rohan/Documents

/etc/passwd

/usr/bin/python3
```

All begin from `/`.

---

# 8. Important Linux Directories

---

## /home

Stores user files.

Example:

```text
/home/rohan/

/home/ali/

/home/sara/
```

Inside your home directory:

```text
/home/rohan

Documents/

Downloads/

Pictures/

Videos/
```

This is where users usually keep their work.

---

## /root

Home directory of the root (administrator) user.

```text
/root
```

Do not confuse:

```text
/
```

with

```text
/root
```

They are different.

| Directory | Meaning              |
| --------- | -------------------- |
| /         | Root of filesystem   |
| /root     | Administrator's home |

---

## /etc

Stores system configuration files.

Examples:

```text
/etc/passwd

/etc/hostname

/etc/hosts
```

These files control how Linux behaves.

---

## /bin

Contains essential executable commands.

Examples:

```text
ls

cp

mv

cat

pwd

mkdir
```

When you type:

```bash
ls
```

Linux runs the executable stored in `/bin` (or `/usr/bin` on many modern systems).

---

## /usr

Contains installed software.

Example:

```text
Applications

Libraries

Documentation

Executables
```

Many installed programs are located here.

---

## /var

Stores changing data.

Examples:

```text
System Logs

Mail

Cache

Databases
```

Example:

```text
/var/log/
```

contains system log files.

---

## /tmp

Temporary files.

Applications often store temporary data here.

Linux may automatically clean this directory.

---

## /boot

Contains files required to start Linux.

Examples:

```text
Linux Kernel

Bootloader

Startup Files
```

Without these files Linux cannot boot properly.

---

## /dev

Represents hardware devices as files.

Examples:

```text
Hard Disk

USB Drive

Printer

Keyboard
```

Programs interact with hardware through these device files.

---

## /proc

A virtual directory containing information about:

- Running processes
- CPU
- Memory
- Kernel

Its contents are generated by the kernel while the system is running.

---

## /opt

Optional software installed outside the package manager.

Example:

```text
Google Chrome

Third-party Applications
```

---

## /media

Used when removable devices are mounted.

Example:

```text
USB Drive

DVD

External Hard Disk
```

---

# 9. Current Working Directory

Linux always knows where you are.

Example:

```text
/home/rohan/Documents
```

This location is called the **Current Working Directory (CWD)**.

To display it:

```bash
pwd
```

Output:

```text
/home/rohan/Documents
```

---

# 10. Absolute Path

An absolute path always starts from the root directory.

Example:

```text
/home/rohan/Documents/report.pdf
```

No matter where you currently are, this path always refers to the same file.

More examples:

```text
/etc/passwd

/usr/bin/python3

/var/log/syslog
```

---

# 11. Relative Path

A relative path starts from the current directory.

Suppose your current directory is:

```text
/home/rohan
```

You have:

```text
Documents/report.pdf
```

You can access it using:

```text
Documents/report.pdf
```

Instead of:

```text
/home/rohan/Documents/report.pdf
```

---

# 12. Special Directory Symbols

## Current Directory

```text
.
```

Means:

```text
Current directory
```

Example:

```bash
cp file.txt .
```

Copies the file into the current directory.

---

## Parent Directory

```text
..
```

Means:

```text
One directory above
```

Example:

Current location:

```text
/home/rohan/Documents
```

Parent directory:

```text
/home/rohan
```

Move there:

```bash
cd ..
```

---

## Home Directory

```text
~
```

Represents your home directory.

Example:

```text
~
```

Expands to:

```text
/home/rohan
```

Examples:

```bash
cd ~

cd ~/Downloads

cd ~/Documents
```

---

# 13. Hidden Files

Files beginning with a dot (`.`) are hidden by default.

Examples:

```text
.bashrc

.gitignore

.profile
```

These often store configuration settings.

To display hidden files:

```bash
ls -a
```

---

# 14. File Extensions

Linux does **not** rely on file extensions to determine file type.

Examples:

```text
photo.png

video.mp4

notes.txt

main.py
```

A program can still work even without an extension if its contents and permissions are correct.

---

# 15. Common File Management Commands

## List Files

```bash
ls
```

Lists files in the current directory.

---

## Show Current Directory

```bash
pwd
```

Displays the current working directory.

---

## Change Directory

```bash
cd Documents
```

Move into `Documents`.

---

## Create Directory

```bash
mkdir AI_Project
```

Creates:

```text
AI_Project/
```

---

## Create Empty File

```bash
touch notes.txt
```

Creates:

```text
notes.txt
```

---

## Copy File

```bash
cp notes.txt backup.txt
```

Result:

```text
notes.txt

backup.txt
```

---

## Move or Rename File

Rename:

```bash
mv notes.txt lecture.txt
```

Move:

```bash
mv notes.txt Documents/
```

The `mv` command performs both tasks depending on the destination.

---

## Delete File

```bash
rm notes.txt
```

Deletes the file permanently.

---

## Delete Directory

Empty directory:

```bash
rmdir Projects
```

Non-empty directory:

```bash
rm -r Projects
```

Use `rm -r` carefully, as it removes the directory and all its contents.

---

# 16. Viewing File Contents

Display an entire file:

```bash
cat notes.txt
```

Display page by page:

```bash
less notes.txt
```

First 10 lines:

```bash
head notes.txt
```

Last 10 lines:

```bash
tail notes.txt
```

These commands are especially useful for reading configuration files and logs.

---

# 17. Finding Files

Search by name:

```bash
find . -name "notes.txt"
```

Search from the root directory:

```bash
find / -name "python3"
```

This is useful when locating configuration files, scripts, or executables.

---

# 18. Real Developer Workflow

A common workflow for a Python project might look like this:

```bash
mkdir ai_project
cd ai_project

touch app.py
touch requirements.txt

mkdir data
mkdir models

cp dataset.csv data/

mv app.py src.py

ls

pwd
```

Project structure:

```text
ai_project/
│
├── src.py
├── requirements.txt
├── data/
│   └── dataset.csv
└── models/
```

This demonstrates how directory creation, file creation, copying, moving, and listing come together in everyday development.

---

# 19. Best Practices

- Use meaningful file and directory names.
- Group related files into dedicated directories.
- Avoid storing unrelated files together.
- Keep project structures consistent.
- Be cautious with `rm` and especially `rm -r`, as deleted files are not moved to a recycle bin by default.

---

# Summary

| Topic                     | Description                                                                                  |
| ------------------------- | -------------------------------------------------------------------------------------------- |
| File                      | Stores data such as text, images, code, or videos                                            |
| Directory                 | Organizes files and other directories                                                        |
| Root (`/`)                | Top-level directory of the filesystem                                                        |
| Home (`/home`)            | User-specific files and folders                                                              |
| Current Working Directory | The directory where your shell is currently operating                                        |
| Absolute Path             | Full path beginning with `/`                                                                 |
| Relative Path             | Path relative to the current directory                                                       |
| `.`                       | Current directory                                                                            |
| `..`                      | Parent directory                                                                             |
| `~`                       | Current user's home directory                                                                |
| Hidden Files              | Files beginning with `.`                                                                     |
| Common Commands           | `ls`, `pwd`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `rm`, `find`, `cat`, `less`, `head`, `tail` |
