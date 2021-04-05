#SingleInstance force
#IfWinActive Lunar Client

:b0*:/h::
	Input, inputHint, IV, {Enter}{Esc}
	FileAppend, %inputHint%, *
	ExitApp

:b0:/exit::
	FileAppend, b69f6143-fbf5-4c6c-bd5a-1293276202be, *
	ExitApp