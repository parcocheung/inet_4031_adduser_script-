#!/usr/bin/python3

import os
import re
import sys


def main():
    for line in sys.stdin:
        # Check for the presence of a # at the start of a line.
        match = re.match(r'^#', line)

        # Strip any whitespace and split into an array
        fields = line.strip().split(':')
        # Check if the line starts with a
        # or does NOT have 5 fields. otherwise, skip it.
        if match or len(fields) != 5:
            continue

        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3], fields[2])

        # Split the field by ',', which represents different groups.
        groups = fields[4].split(',')

        print(f"==> Creating account for {username}...")
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (
            gecos, username)
        # Executes the cmd string as a system command.
        os.system(cmd)

        print(f"==> Setting the password for {username}...")
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (
            password, password, username)

        # print cmd
        os.system(cmd)
        # This loop iterates over the groups and assigns the user to each valid group.
        for group in groups:
            if group != '-':
                print(f"==> Assigning {username} to the {group} group...")
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                # print cmd
                os.system(cmd)


if __name__ == '__main__':
    main()
