#Script que testa o teclado instalado no RaspBerry Pi e printa na tela

import md5
import curses
import signal
import sys
def signal_handler(signal, frame):
		print('You pressed Ctrl+C!')
		curses.nocbreak()
		sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


def criptografate(passaword):
	
	m = md5.new()

	m.update(password)

	return m.digest()


def autenticate(password):

	if password == "1234":
		return True

window = curses.initscr()
#curses.cbreak()

while True:

	password = str(window.getch())

	print password

	
	

	#print criptografate(password)

	if autenticate(password):
		print "Certo!"
	else:
		print "Errado!"


	