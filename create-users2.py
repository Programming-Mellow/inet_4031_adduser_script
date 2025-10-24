#!/usr/bin/python3

# INET4031
# Wendy Vang
# 10/24/2025 (Date Created)
# 10/24/2025 (Date Modified)
# Modified version to delete users instead of creating them.
# Adds dry-run interactivity to allow previewing all system commands before execution.

import os
import re
import sys

def main():
    # Ask the user whether to perform a dry-run (no system changes)
    dry_run_input = input("Run in dry-run mode? (Y/N): ").strip().lower()

    if dry_run_input == "y":
	dry_run = True
    else:
	dry_run = False

    for line in sys.stdin:
        # Skip comment lines or empty lines
        match = re.match("^#", line)
        fields = line.strip().split(':')

        # Check for valid field structure (5 expected fields, like username:password:first:last:groups)
        if match or len(fields) != 5:
            if dry_run:
                if match:
                    print(f"Skipped commented line: {line.strip()}")
                elif len(fields) != 5:
                    print(f"Error: Invalid line format (expected 5 fields): {line.strip()}")
            continue

        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])
        groups = fields[4].split(',')

        ####################################################
        # DELETE USER ACCOUNT
        ####################################################
        print(f"==> Deleting account for {username}...")

        cmd = f"/usr/sbin/deluser --remove-home {username}"

        if dry_run:
            print(f"[DRY-RUN] Would run: {cmd}")
        else:
            os.system(cmd)

        ####################################################
        # REMOVE USER FROM GROUPS
        ####################################################
        for group in groups:
            if group != '-':
                cmd = f"/usr/sbin/deluser {username} {group}"
                if dry_run:
                    print(f"[DRY-RUN] Would remove {username} from group {group}: {cmd}")
                else:
                    print(f"==> Removing {username} from {group} group...")
                    os.system(cmd)

    ####################################################
    # DRY-RUN SUMMARY NOTE
    ####################################################
    if dry_run:
        print("\nDry-run completed. No system changes were made.")
    else:
        print("\nActual deletion process completed for all valid users.")


if __name__ == '__main__':
    main()
