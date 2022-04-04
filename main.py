#!/usr/bin/python3
from requests import get
from modules import ipInfo, hackertarget
import os, time

red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
cls = '\033[m'

op22 = 'https://api.hackertarget.com/reverseiplookup/?q='
op33 = 'https://api.hackertarget.com/nmap/?q='
op44 = 'https://api.hackertarget.com/whois/?q='

def menu():
	os.system('clear && clear && clear')
	print(blue, 6*' ','}---------', green, 'IP-Check', blue, '---------{', cls)
	print()
	os.system('''ip=$(curl -s https://ipinfo.io/ip) 
	echo '\033[1;31m'IP: '\033[1;32m'$ip '\033[m' | cowsay''')
	print()
	print(blue, 4*' ','}-- Created by:', red, 'Visto-Preto', blue,'--{')
	print(15*' ', 'Version: ', red, '1.1', blue)
	print()
	print(2*'', 'Visit', red, ' https://github.com/Visto-Preto/IP-Check', blue)
	print(cls, '''
Select from the menu:

  1) IP Info
  2) Reverse IP Lookup
  3) TCP Port Scan
  4) Whois Lookup
 
 99) Exit the IP-Check
''')

menu()

while True:
	op = input(red+'IP-Check'+cls+':'+blue+'~'+cls+'$ ')
	if op == '1':
		ipInfo.getInfo()
		menu()
	elif op == '2':
		hackertarget.getInfo(op22)
		menu()
	elif op == '3':
		hackertarget.getInfo(op33)
		menu()
	elif op == '4':
		hackertarget.getInfo(op44)
		menu()
	elif op == '99':
		print(99)
		os.system('clear && clear && clear')
		break
	else:
		menu()
os.system('clear && clear && clear')
