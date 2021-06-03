#SingleInstance force
#IfWinActive Lunar Client

WinSet, AlwaysOnTop, On, ahk_class ConsoleWindowClass

:*?b0://::
	Input, inputHint, IV, {Enter}{Esc}
	FileAppend, %inputHint%, *
	ExitApp