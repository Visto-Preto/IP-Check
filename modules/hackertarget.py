#!/usr/bin/python3
from requests import get
import os

red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
cls = '\033[m'


def getInfo(x):
	os.system('clear && clear && clear')
	print(blue, 6*' ','}---------', green, 'IP-Check', blue, '---------{', cls)
	print()
	if 'reverseiplookup' in x:
		os.system('''echo '\033[1;31mReverse IP Lookup\033[m' | cowsay''')
		mn = (''' Enter IP Address:
 
 99) Back''')
	elif 'nmap' in x:
		os.system('''echo '\033[1;31mTCP Port Scan\033[m' | cowsay''')
		mn = (''' Enter IP Address:
 
 99) Back''')
	elif 'whois' in x:
		os.system('''echo '\033[1;31mWhois Lookup\033[m' | cowsay''')
		mn = (''' Enter IP or Domine fo lookup:
 
 99) Back''')

	print()
	print(blue, 4*' ','}-- Created by:', red, 'Leonardo Sousa', blue,'--{')
	print(8*' ','}--- Codename:', red, 's0u54l30', blue, '--{')
	print(15*' ', 'Version: ', red, '1.0', blue)
	print()
	print(2*'', 'Visit', red, ' https://github.com/s0u54l30/IP-Check', blue)
	print(cls)
	print(mn)
	print()
	ip = input(red+'IP-Check'+cls+':'+blue+'~'+cls+'$ ')
	if ip == '99':
		pass
	else:
		if ip == '':
			ip = get('https://ipinfo.io/ip').text
		rvrs = get(x + ip).text
		print()
		print(rvrs)
		print()
		print('''  1) Check again
 
 99) Back''')
		print()
		op1 = input(red+'IP-Check'+cls+':'+blue+'~'+cls+'$ ')
		if op1 == '1':
			getInfo(x)
		elif op1 == '99':
			pass
		else: 
			getInfo(x)