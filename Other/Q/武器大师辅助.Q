[General]
SyntaxVersion=2
BeginHotkey=121
BeginHotkeyMod=0
PauseHotkey=0
PauseHotkeyMod=0
StopHotkey=123
StopHotkeyMod=0
RunOnce=1
EnableWindow=
MacroID=0a1bdef0-cfc4-4aed-a6e3-5ee2d6edbab7
Description=武器大师辅助
Enable=1
AutoRun=0
[Repeat]
Type=0
Number=1
[SetupUI]
Type=2
QUI=
[Relative]
SetupOCXFile=
[Comment]

[Script]
While True
    userKey = WaitKey()
    
//  点击按键1  
    If userKey = 49  Then
        Delay 100
        KeyPress "Q", 1

    ElseIf userKey = 32 Then
        MoveTo 242,862
        LeftClick 1
    ElseIf userKey = 27 Then
        MsgBox "结束"
        ExitScript
    End If
Wend