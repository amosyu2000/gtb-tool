#SingleInstance force
#IfWinActive Lunar Client

:*?b0://::
	Input, inputHint, IV, {Enter}{Esc}
	FileAppend, %inputHint%, *
	ExitApp