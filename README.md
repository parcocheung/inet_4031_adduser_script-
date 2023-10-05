# inet_4031_adduser_script-
INET 4031 Lab 4 Part 2

Python Script for Adding Users/Groups to a System

 ## Description
 This Python Script reads user/group data from an input file, processes the file line-by-line, and adds each user to the system. 

 **Imports:**
   - os:Provides the use of operating system function
   - re:Check if a line in the input file starts with a #
   - sys:Allows access to some variables used

 **Regex:** 
 
 Regex is used to determine if a line in the input file starts with a #.

**Purpose of # in the input file:**

The script can skip the line that starts with a #.

## Operation
Input File Specification
The input file should have the following format:

*** username:default_password:last_name:first_name:comma_separated_list_of_groups

For example:

jdoe11:mypass:Doe:John:admins, reviewers

The name of the input file is up to the user. Convention is create-users.input

## Running the Script

Use **sudo ./create-users.py < create-users.input** to run the script. 

This script is designed for Python 3.


