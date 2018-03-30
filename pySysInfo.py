#!/usr/bin/env python
#A System Information Gathering Script
#Command usage: subprocess.call(["some_command", "some_argument", "another_argument_or_path"]) 
import subprocess

def uname_func():

	uName="uname"
	uName_arg="-a"
	print "-------------------------------------------------"
	print "Gathering syetem info"
	print "-------------------------------------------------"
	print "Type 1"
	subprocess.call([uName,uName_arg])

	print "-------------------------------------------------"
	print "Gathering syetem info"
	print "-------------------------------------------------"
	print "Type 2"
	subprocess.call(["uname","-a"])

def disk_func():

	diskSpace="df"
	diskSpace_arg="-h"
        print "-------------------------------------------------"
        print "Gathering disk info"
        print "-------------------------------------------------"
        print "Type 1"
        subprocess.call([diskSpace,diskSpace_arg])

        print "-------------------------------------------------"
        print "Gathering disk info"
        print "-------------------------------------------------"
        print "Type 2"
        subprocess.call(["df","-h"])


def main():
	uname_func()
	disk_func()

if __name__ == "__main__":
main()
