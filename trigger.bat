@if (@CodeSection == @Batch) @then
timeout /t 10
rundll32.exe cmdext.dll,MessageBeepStub


@echo off
CScript //nologo //E:JScript "%~F0"
goto :EOF
@end
WScript.CreateObject("WScript.Shell").SendKeys("{Enter}}");
	