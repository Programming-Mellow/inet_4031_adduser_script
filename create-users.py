#!/usr/bin/python3

# INET4031
# Wendy Vang
# 10/24/2025 (Date Created)
# 10/24/2025 (Date Modified)

#OS is imported to allow interactions with the operating systems, re is imported to help with filtering through each line that we loop through, and sys helps us read our input file and process the contents of it as indicated in the code.
import os
import re
import sys

def main():
    for line in sys.stdin:

	#Taking a look at the code, it appears that the "^#" characters are being used to withhold a user from being created	#anytime the script is executed. It essentially acts like a comment, where commented code is not executed.
        match = re.match("^#",line)

        #It's using the ":" symbol to delimit and separate the fields from one another
	#so it is easier to process through the script and read.
        fields = line.strip().split(':')

	#This if statement checks to see if there is an instance of matching characters per the regular expression.
	#It also checks to see if all necessary fields are fulfilled (as the Python script separates each field into its
	#own index within the list/array. If all conditions are met (no match, and the length of that user's fields are 5)
	#then, the script will continue executing. Otherwise, if either conditions evaluate to true, then the script
	#will not perform the OS changes to add the users in and will continue to the next line/user.
        if match or len(fields) != 5:
            continue

	#In the passwd file, each user is stored a specific way. The python script attempts to mimic that and respect the format
	#in which the users are stored in the OS. The gecos field is just the full name, room number, work phone, etc..
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

	#Within the 4th index of the fields that are extracted, we want to be able to grab all of the groups the user
	#is associated with and process them one bit at a time so we can ensure that the user is added into all of the
	#the groups listed. These groups are separated by a "," symbol.
        groups = fields[4].split(',')

	#This print statement helps us understand what is happening throughout the loop and serves as a way to log actions
	#done by the script.
        print("==> Creating account for %s..." % (username))
	#This line of code helps build the Linux command that is used to create a new user through the system's
	#adduser. The variable CMD essentially just contains the Linux command.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #print cmd
	#This tells the operating system to execute the "cmd" variable that stores whatever command we're interested
	#in running.
        os.system(cmd)

        #Just like the last print statement, it allows us to see what exactly the script is doing and logs the actions
	#so we can evaluate them later if needed.
        print("==> Setting the password for %s..." % (username))
	#The variable "CMD" will store the following command. Essentially, it helps set the user's password by automatically
	#inputting the user's password. The various flags help mimic how a user would type the password twice when
	#they manually set it. The pipe "|" sends the output directly into the input to the next command.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #print cmd
	#The first time you run the code and don't want to make any modifications, you should scope out the code and
	#comment anything that has to do with interacting with the OS. So anything that starts with "os." is a good
	#idea to comment it so you can perform a dry run of the code and not modify anything.
        os.system(cmd)

        for group in groups:
	    #The if statement essentially checks to see if the user is assigned to any groups. If so, then it will assign them to the necessary groups.
	    #From there, it will execute the cmd variable that's been changed so that way the users can actually get
	    #assigned to their groups.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                os.system(cmd)

if __name__ == '__main__':
    main()

