# Security Log Analyzer
# Inspired by file-handling examples in Automate the Boring Stuff with Python.
# This program reads a sample log, counts failed logins,
# flags accounts with repeated failures, and saves a report.

from collections import defaultdict

# Name of the input file.
LOG_FILE = "sample_security_log.txt"

# Accounts with 3 or more failed logins will be flagged.
FAILED_LOGIN_THRESHOLD = 3


def analyze_log(file_name):
    """Read the log file and count failed login attempts by account."""
    failed_attempts = defaultdict(int)
    total_failed = 0

    # Open the file in read mode.
    with open(file_name, "r", encoding="utf-8") as log_file:
        for line in log_file:

            # Remove extra spaces and ignore blank lines.
            line = line.strip()
            if not line:
                continue

            # Check whether the line contains a failed login.
            if "FAILED_LOGIN" in line:
                total_failed += 1

                # Find the username in the log entry.
                for part in line.split():
                    if part.startswith("username="):
                        username = part.split("=", 1)[1]
                        failed_attempts[username] += 1
                        break

    return total_failed, failed_attempts


def create_report(total_failed, failed_attempts):
    """Create a readable security report."""
    report_lines = [
        "SECURITY LOG ANALYSIS REPORT",
        "============================",
        f"Total failed login attempts: {total_failed}",
        "",
        "Failed attempts by account:"
    ]

    # Display the failed login count for each account.
    for username in sorted(failed_attempts):
        count = failed_attempts[username]
        report_lines.append(f"- {username}: {count}")

    report_lines.append("")
    report_lines.append(
        f"Accounts with {FAILED_LOGIN_THRESHOLD} or more failed attempts:"
    )

    # Find accounts that reached the warning threshold.
    flagged_accounts = []

    for username, count in failed_attempts.items():
        if count >= FAILED_LOGIN_THRESHOLD:
            flagged_accounts.append((username, count))

    # Display warnings for accounts with repeated failures.
    if flagged_accounts:
        for username, count in sorted(flagged_accounts):
            report_lines.append(
                f"WARNING: {username} had {count} failed attempts."
            )
    else:
        report_lines.append("No accounts reached the warning threshold.")

    return "\n".join(report_lines)


def main():
    """Run the analysis and save the report."""
    try:
        total_failed, failed_attempts = analyze_log(LOG_FILE)

    except FileNotFoundError:
        print(f"Error: Could not find '{LOG_FILE}'.")
        print("Make sure the log file is in the same folder as this script.")
        return

    # Create the report.
    report = create_report(total_failed, failed_attempts)

    # Display the report in the terminal.
    print(report)

    # Save the report to a separate text file.
    with open("security_report.txt", "w", encoding="utf-8") as report_file:
        report_file.write(report)

    print("\nReport saved to security_report.txt")


# Run the program when the script is executed.
if __name__ == "__main__":
    main()
