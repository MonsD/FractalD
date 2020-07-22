import os
import time

def Registration():
	time.sleep(1)
	login = str(input("Enter a new login\n"))
	password = str(input("Enter a new password\n"))
	f = open('login.txt', 'r')
	f.close()
	if login in loglist:
		time.sleep(1)
		print("This login is already taken")
		Registration()
	else:
		f = open('login.txt', 'a')
		f.write(login + ',')
		f.close()
		g = open('password.txt', 'a')
		g.write(password + ',')
		g.close()
	Terminal()

def Autorisation():
	time.sleep(1)
	login = str(input("Enter login\n"))
	password = str(input("Enter password\n"))
	try:
		if password == database[login]:
			time.sleep(1)
			print("Hello!")
			Application()#Logical continue code
		else:
			time.sleep(1)
			print("Wrong password or login")
			Terminal()
	except KeyError: # Workaround (try - except).
		time.sleep(1)
		print("Wrong password or login")
		Terminal()

def Terminal():
	command = input("Authorization, registration, rename or remove user??\n")
	if command == "Autorisation":
		Autorisation()
	elif command== "Registration":
		Registration()
	elif command== "Remove":
		Remove()
	elif command == "Rename":
		Rename()
def Remove():
	time.sleep(1)
	global loglist
	global passlist
	login = str(input("Enter login\n"))
	if login == "Default":
		time.sleep(2)
		print("Prohibited")
		time.sleep(1)
		Terminal()
	number = loglist.index(login)
	loglist[number] = 'Deleted'
	f = open('login.txt', 'w')
	lenlog = len(loglist)
	for i in range(0, lenlog):
		f.write(loglist[i] + ',')
	f.close()
def Rename():
	global loglist
	global passlist
	global database
	time.sleep(1)
	login = str(input("Enter login\n"))
	password = str(input("Enter password\n"))
	try:
		if password == database[login]:
			time.sleep(1)
			login1 = str(input("Enter new login"))
			if login1 in loglist:
				time.sleep(1)
				print("This login is already taken")
				Rename()
			elif login1 not in loglist:
				number = loglist.index(login)
				loglist[number] = login1
				f = open('login.txt', 'w')
				lenlog = len(loglist)
				for i in range(0, lenlog):
					f.write(loglist[i] + ',')
				f.close()
		else:
			time.sleep(1)
			print("Wrong login or password")
			Terminal()
	except KeyError:  # Workaround (try - except).
		time.sleep(1)
		print("Wrong login or password")
		Terminal()

def Application():
	os.startfile()

f = open('login.txt', 'r')
loglist = f.read().split(",")
f.close()
g = open('password.txt', 'r')
passlist = g.read().split(",")
g.close()
mainlist = zip(loglist, passlist) #Pairwise indexing of sheets
database = dict(mainlist)

Terminal()
