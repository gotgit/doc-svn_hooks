REM  POST-COMMIT HOOK for Windows

setlocal
set REPOS_FULL=%1
set REPOS_NAME=%~n1
set REV=%2

TOOLS_DIR=%REPOS_FULL%/hooks/scripts
set PYTHONCMD=C:\Apps\Python\python
set PERLCMD=C:\Apps\Perl\bin\perl

REM %PERLCMD%   %TOOLS_DIR%/commit-email.pl "%REPOS_FULL%" "%REV%" -m "." --from noreply@worldhello.net -r noreply@worldhello.net -s "[test]" email@address

endlocal
exit 0
