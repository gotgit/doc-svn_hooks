REM SVN pre-commit hook for Windows
REM by Jiang Xin <worldhello.net@gmail.com>

setlocal

set REPOS=%1
set TXN=%2
set TOOLS_DIR=%REPOS%/hooks/scripts
set PYTHONCMD=C:\Apps\Python\python
set PERLCMD=C:\Apps\Perl\bin\perl

echo %REPOS%  1>&2
echo %TOOLS_DIR% 1>&2

REM # Check commit log, by <WorldHello.net.AT.gmail.com>
%PYTHONCMD% %TOOLS_DIR%/commit_log_check.py "%REPOS%" "%TXN%" || exit 1

REM # New file must set svn:mime-type and svn:eol-style
%PYTHONCMD% %TOOLS_DIR%/check-mime-type.py "%REPOS%" "%TXN%" || exit 1

REM # Check for case conflicts
REM %PYTHONCMD% %TOOLS_DIR%/check-case-insensitive.py "%REPOS%" "%TXN%" || exit 1

REM # Check that the author of this commit has the rights to perform
REM # the commit on the files and directories being modified.
REM %PYTHONCMD% %TOOLS_DIR%/svnperms.py -r "%REPOS%" -t "%TXN%" -f %TOOLS_DIR%/svnperms.conf || exit 1

REM # All checks passed, so allow the commit.
endlocal
exit 0
