from ahk import AHK
from os import system, name
import re

ahk = AHK()
matching_words = []

def clear_console():
	# windows
	if name == 'nt':
		system('cls')
	# others
	else:
		system('clear')

def sanitize_input(argument):
	argument = str(argument).strip()
	if (argument.startswith('/')):
		argument = argument[1:]
	return argument

def type_word_at_position(argument):
	index = int(argument) - 1
	if (index < len(matching_words)):
		word = matching_words[index]
		ahk.key_press('t')
		ahk.type(word.lower())
		ahk.key_press('Enter')

def search_word_list(argument):
	# convert input to regex
	hint = '^' + argument.replace('_', '\\S').replace(' ', '\\s') + '$'
	global matching_words
	matching_words = []

	clear_console()

	try:
		# Verify that the regex is valid
		re.compile(hint)

		# find words that match the hint
		matching_words = [word for word in word_list if re.match(hint, word, flags=re.IGNORECASE)]
		
		if len(matching_words) == 0:
			print('<no matches>')
		else:
			num_width = len(str(len(matching_words)))
			for i in range(len(matching_words)):
				print(f"({i+1:0>{num_width}}) {matching_words[i]}")
	
	except re.error:
		print('<invalid regex>')

# script for receiving user inputs
with open('input.ahk') as file:
	input_script = file.read()

# text file that contains all possible words
with open('word_list.txt') as file:
	word_list = file.read().splitlines()

# text file that contains the welcome message
with open('welcome.txt') as file:
	welcome_msg = file.read()

# print welcome message on startup
clear_console()
print(welcome_msg)

while True:
	# wait for user to input (either a hint or request exit)
	argument = sanitize_input(ahk.run_script(input_script))

	# wait for user to release Enter key
	ahk.key_wait('Enter', released=True)

	if argument == 'e':
		exit()
		quit()
	elif argument.isdigit():
		type_word_at_position(argument)
	else:
		search_word_list(argument)
