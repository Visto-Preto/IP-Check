#!/data/data/com.termux/files/usr/bin/env python3

import sys, os



# ________________________________

__author__ = 'VistoPreto'
__version__ = '1.1'

# ________________________________


if len(sys.argv) == 1:
	arg = ''
elif len(sys.argv) == 2:
	arg = sys.argv[1]
else:
	arg = 'err'

descricao = '''

ipcheck [-about] [-start] [-uninstall] [-upgrade]

-about		Sobre o script
-start		Inciar funçoes do script
-unistall	Remover a instalação do script
-upgrade	Atualizar para versão mais recente

'''

def arg_analise(x):
	if x == '-about':
		print()
		print('Desenvolvido por ', __author__)
		print('Version ', __version__)
		print()
	elif x == '-start':
		os.system('python /data/data/com.termux/files/usr/share/ipcheck/main.py')
	elif x == '-uninstall':
		os.system('bash /data/data/com.termux/files/usr/share/ipcheck/uninstall.sh')
	elif x == '-upgrade':
		os.system('bash /data/data/com.termux/files/usr/share/ipcheck/upgrade.sh')
	elif x == '' or x == 'err':
		print(descricao)
	else:
		print(descricao)

arg_analise(arg)
