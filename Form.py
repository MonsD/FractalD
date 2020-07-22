import os
import time

def Registration():
	time.sleep(1)
	loggin = str(input("Введите новый логин\n"))
	password = str(input("Введите новый пароль\n"))
	f = open('loggin.txt', 'r')
	f.close()
	if loggin in loglist:
		time.sleep(1)
		print("Такой логин уже существует")
		Registration()
	else:
		f = open('loggin.txt', 'a')
		f.write(loggin + ',')
		f.close()
		g = open('password.txt', 'a')
		g.write(password + ',')
		g.close()
	Terminal()

def Autorisation():
	time.sleep(1)
	loggin = str(input("Введите логин\n"))
	password = str(input("Введите пароль\n"))
	try:
		if password == database[loggin]:
			time.sleep(1)
			print("Приветствую!")
			Application()
		else:
			time.sleep(1)
			print("Неверный логин или пароль")
			Terminal()
	except KeyError: #Обход ошибок (try - except).
		time.sleep(1)
		print("Неверный логин или пароль")
		Terminal()

def Terminal():
	command = input("Авторизация, регистрация или удаление аккаунта?\n")
	if command == "Авторизация":
		Autorisation()
	elif command== "Регистрация":
		Registration()
	elif command== "Удаление":
		Remove()
	elif command == "Изменить логин":
		Rename()
def Remove():
	time.sleep(1)
	global loglist
	global passlist
	loggin = str(input("Введите логин\n"))
	if loggin == "Default":
		time.sleep(2)
		print("Запрещено")
		time.sleep(1)
		Terminal()
	number = loglist.index(loggin)
	loglist[number] = 'Deleted'
	f = open('loggin.txt', 'w')
	lenlog = len(loglist)
	for i in range(0, lenlog):
		f.write(loglist[i] + ',')
	f.close()
def Rename():
	global loglist
	global passlist
	global database
	time.sleep(1)
	loggin = str(input("Введите логин\n"))
	password = str(input("Введите пароль\n"))
	try:
		if password == database[loggin]:
			time.sleep(1)
			loggin1 = str(input("Введи желаемый логин"))
			if loggin1 in loglist:
				time.sleep(1)
				print("Такой логин уже существует")
				Rename()
			elif loggin1 not in loglist:
				number = loglist.index(loggin)
				loglist[number] = loggin1
				f = open('loggin.txt', 'w')
				lenlog = len(loglist)
				for i in range(0, lenlog):
					f.write(loglist[i] + ',')
				f.close()
		else:
			time.sleep(1)
			print("Неверный логин или пароль")
			Terminal()
	except KeyError:  # Обход ошибок (try - except).
		time.sleep(1)
		print("Неверный логин или пароль")
		Terminal()

def Application():
	os.startfile()

f = open('loggin.txt', 'r')
loglist = f.read().split(",")
f.close()
g = open('password.txt', 'r')
passlist = g.read().split(",")
g.close()
mainlist = zip(loglist, passlist)
database = dict(mainlist)

Terminal()
