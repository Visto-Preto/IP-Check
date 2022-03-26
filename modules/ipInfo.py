#!/usr/bin/python3
from requests import get
import os

red = '\033[1;31m'
green = '\033[1;32m'
yellow = '\033[1;33m'
blue = '\033[1;34m'
cls = '\033[m'

def getInfo():
	os.system('clear && clear && clear')
	print(blue, 6*' ','}---------', green, 'IP-Check', blue, '---------{', cls)
	print()

	os.system('''echo '\033[1;31mIP Info\033[m' | cowsay''')
	print()
	print(blue, 4*' ','}-- Created by:', red, 'Leonardo Sousa', blue,'--{')
	print(8*' ','}--- Codename:', red, 's0u54l30', blue, '--{')
	print(15*' ', 'Version: ', red, '1.0', blue)
	print()
	print(2*'', 'Visit', red, ' https://github.com/s0u54l30/IP-Check', cls)
	print()
	print(''' Enter IP Address:

 99) Back''')
	print()
	ip = input(red+'IP-Check'+cls+':'+blue+'~'+cls+'$ ')
	if ip == '99':
		pass
	else:
		myip = get('https://ipinfo.io/ip').text
		mp = ''
		for mip in myip:
			if mip == '\n':
				continue
			mp += mip
		check = get('https://ipinfo.io/' + ip).text
		info = ''
		for i in check:
			if i == '\n':
				info += '\033[1;32m' + i
			elif ip == '':
				info += '\n\033[1;31mYour ip information\033[m\n'
				ip = 0
			elif ip == mp:
				info += '\n\033[1;31mYour ip information\033[m\n'
				mp = 0
			elif i == '{':
				continue
			elif i == '"':
				continue
			elif i == ':':
				info += '\033[m' + i
			elif i == ',':
				info += ' '
				continue
			elif i == '}':
				info += '\033[m'
				continue
			else:
				info += i
		print(info)
		print('''  1) Check again
 
 99) Back''')
		print()
		op1 = input(red+'IP-Check'+cls+':'+blue+'~'+cls+'$ ')
		if op1 == '1':
			getInfo()
		elif op1 == '99':
			pass
		else: 
			getInfo()