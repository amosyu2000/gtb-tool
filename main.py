from ahk import AHK
from os import system, name
import re

ahk = AHK()
exit_key = 'b69f6143-fbf5-4c6c-bd5a-1293276202be'

def clear():
	# windows
	if name == 'nt':
		system('cls')
	# others
	else:
		system('clear')

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
clear()
print(welcome_msg)

while True:
	# wait for user to input (either a hint or request exit)
	argument = str(ahk.run_script(input_script)).strip()

	# wait for user to release Enter key
	ahk.key_wait('Enter', released=True)

	if argument == exit_key:
		exit()
		quit()

	# convert input to regex
	hint = '^' + argument.replace('_', '\\S').replace(' ', '\\s') + '$'

	clear()

	# find words that match the hint
	matching_words = []
	for word in word_list:
		if re.match(hint, word, flags=re.IGNORECASE):
			matching_words.append(word.upper())
	
	if len(matching_words) == 0:
		print('<no matches>')
	elif len(matching_words) == 1:
		matching_word = matching_words[0]
		prompt = '<press Enter to type>'
		print(matching_word, prompt, sep='\n')
		try:
			ahk.key_wait('Enter', timeout=5)
			# Type the matching word in the window
			ahk.key_press('t')
			ahk.type(matching_word.lower())
			ahk.key_press('Enter')
		except TimeoutError:
			pass
		# Clear the previous line from console
		# https://stackoverflow.com/a/51388326/12191708
		print ('\033[A', ' '*len(prompt), '\033[A')
	else:
		print('\n'.join(matching_words))
