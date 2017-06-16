#!/usr/bin/env python
import sys
import random
from Way2SMS  import *
from perf import *
import time
file = open('to.txt', 'r').readlines() if os.path.isfile('./to.txt') else raw_input('[?] Enter , Separted Mobile Numbers: ').split(',')
log = login()
print '''

	+++++++++++++++++++++++++++++++++++++++
	{ Way 2 SMS Automatic Tool - Ver 1.0  }
	+++++++++++++++++++++++++++++++++++++++
	|#Author: CodeCowBoy aka Gowtham      |
	|#Date: 24-03-2015                    |
	|#Contact: fb.com/Gowtham95india      |
	|#Mail: Gowtham95india@gmail.com      |
	|#Changing name never makes you       |
	|coder.^_^			      |
	|#Respect Coders ^_^ 		      |	
	+++++++++++++++++++++++++++++++++++++++
	{ Love it ? Please feed me            }
	+++++++++++++++++++++++++++++++++++++++

'''	
if log != False:
	print "[+] Way2SMS Automatic Script Intialized"
	print "[+] Author : 7H3 !N5ID3R AKA Gowtham"
	print "[+] Login Successful..."
	print "[+] Token Obtained: ", log
	print "[+] Initializing Sending Messages"

def start():
	msgs = wilc(log)
	msg = random.choice(msgs)
	msg = msg.strip()
	msg = msg.rstrip('</p>')
#	msg = msg.rstrip('...')
	msg = msg.rstrip('Div')
	p = "</p>"
	if p in msg:
		n = msg.index(p)
		msg = msg[:n]
	msg = msg[:140]	
	print "[+] Message length: ",len(msg)
	print "[+] Message Body : ", "\n\n", msg, "\n"
	ok(msg)
def ok(msg):
	for line in file:
		no = line.strip()
		status = send(no,msg)
		if status == True:
			print "[+] Message sent successfully to %s" %no
		else:
			print "[-] Sending message failed to %s" %no
if __name__ == '__main__':
	start()
