#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Validate commit log:
* Check the length of commit log;
* Check certain contents against Regular Expression;

by Jiang Xin<WorldHello.net.AT.gmail.com>
"""

__revision__ = '$Id: commit_log_check.py 521 2006-05-08 15:06:48Z jiangxin $'

import sys, os, re

if os.name == 'nt':
    SVNLOOK = 'C:/Apps/Subversion/bin/svnlook.exe'
else:
    SVNLOOK = '/usr/bin/svnlook'

MIN_LENGTH = 5

def main(repos, txn):
    """main entry point"""
    log_cmd = '%s log -t "%s" "%s"' % (SVNLOOK, txn, repos)
    log_msg = os.popen(log_cmd, 'r').read().rstrip('\n')
    
    # Check the length of commit log
    check_strlen(log_msg, MIN_LENGTH)
    
    # Check certain contents against Regular Expression
    check_pattern(log_msg)


def check_strlen(log_msg, min_strlen):
    """
    Check length of log_msg, not less then min_strlen
    """
    log_length = len(log_msg)

    if log_length > 0:
        char  = log_msg[0]
        char2 = log_msg[-1]        
        idx = 1
        while idx < len(log_msg):
            if char == -1 and char2 == -1 and log_length <= 0:
                break

            if (char == log_msg[idx]) and (char != -1):
                log_length = log_length - 1
                char = log_msg[idx]
            else:
                char = -1

            if (char2 == log_msg[-idx]) and (char2 != -1):
                log_length = log_length - 1
                char2 = log_msg[-idx]
            else:
                char2 = -1

            idx = idx + 1
    
    if log_length < min_strlen:
        sys.stderr.write ("Commit log must greater than %d characters, "
            "or too simple.\n" % min_strlen)
        sys.exit(1)


def check_pattern(log_msg):
    """
    Check log_msg against patterns
    """
    patterns = [
               #r'(issue\s*[#]?[0-9]+)|(new.*:)|(bugfix:)',
               ]
    for pat in patterns:
        if re.compile(pat, re.I).search(log_msg, 1):
            continue
        else:
            sys.stderr.write ("Cannot find pattern: "
                "'%s' in commit log.\n" % pat)
            sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: %s REPOS TXN\n" % (sys.argv[0]))
        if len(sys.argv) == 2:
            check_strlen(sys.argv[1], MIN_LENGTH)
            check_pattern(sys.argv[1])
    else:
        main(sys.argv[1], sys.argv[2])
