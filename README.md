# Cyber301-Automation-Project

## Project Selected

Security Log Analyzer, inspired by file-handling concepts from Automate the Boring Stuff with Python.

## What the Script Does

This Python program reads a sample security log file and:

- Counts failed login attempts.
- Counts failed attempts for each username.
- Identifies accounts with three or more failed login attempts.
- Displays a security report in the terminal.
- Saves the report to a text file.

This project demonstrates how Python can be used to analyze security logs.

## How to Run

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Keep the Python script and sample log file in the same folder.
4. Open a terminal or command prompt in that folder.
5. Run the following command:

   ```bash
   python security_log_analyzer.py
   ```

   On Windows, you can also use:

   ```bash
   py security_log_analyzer.py
   ```

6. The program will display the security report and create a file called `security_report.txt`.

## Challenges Encountered

One challenge was learning how to read a text file and identify specific information within each line. I used Python's `split()` method to separate the information and find usernames.

Another challenge was making sure the program could handle a missing log file without crashing.

## Improvements and Modifications

I adapted the file-reading concepts from the book into a cybersecurity project.

My modifications included:

- Counting failed login attempts by username.
- Adding a warning threshold for repeated failed logins.
- Creating a readable security report.
- Saving the report to a separate text file.
- Adding error handling for missing files.

## Sample Output

```text
SECURITY LOG ANALYSIS REPORT
============================
Total failed login attempts: 6

Failed attempts by account:
- admin: 3
- guest: 3

Accounts with 3 or more failed attempts:
WARNING: admin had 3 failed attempts.
WARNING: guest had 3 failed attempts.

Report saved to security_report.txt
```

## Limitations

This is a beginner-level educational project that uses sample security logs. It does not connect to real systems or automatically block accounts.
