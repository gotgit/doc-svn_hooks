#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
check-mime-type.py: check that every added file has the
svn:mime-type property set and every added file with a mime-type
matching text/* also has svn:eol-style set. If any file fails this
test the user is sent a verbose error message suggesting solutions and
the commit is aborted.

Usage: commit-mime-type-check.pl REPOS TXN-NAME

Rewrite from check-mime-type.pl, by Jiang Xin<WorldHello.net.AT.gmail.com>
"""

__revision__ = '$Id: commit_log_check.py 513 2006-05-06 17:12:03Z jiangxin $'

import sys, os, re, string

if os.name == 'nt':
    SVNLOOK = 'C:/Apps/Subversion/bin/svnlook.exe'
else:
    SVNLOOK = '/usr/bin/svnlook'

os.environ['LANG'] = os.environ['LC_ALL'] = 'zh_CN.UTF8'

MIN_LENGTH = 5

def main(repos, txn):
    """main entry point"""

    files_added = []
    cmd = '%s changed -t "%s" "%s"' % (SVNLOOK, txn, repos)
    padd = re.compile(r'^A.  (.*[^/])$')

    for line in os.popen(cmd, 'r').readlines():
        match = padd.match( line.rstrip("\n") );
        if match:
            groups = match.groups()
            if len(groups) == 1:
                files_added.append( groups[0] );

    pmime = re.compile(r'\s*svn:mime-type : (\S+)')
    peol  = re.compile(r'\s*svn:eol-style : (\S+)')
    ptext = re.compile(r'^text/')
    
    errmsg = []
    for path in files_added:
        cmd = '%s proplist -t "%s" "%s" --verbose "%s"' % (SVNLOOK, txn, repos, path)
        mime_type = ''
        eol_style = ''
        for line in os.popen(cmd, 'r').readlines():
            if pmime.match(line):
                mime_type = pmime.match(line).group(1)
            if peol.match(line):
                eol_style = peol.match(line).group(1)
        if mime_type == "" and eol_style == '':
            errmsg.append( "%s : svn:mime-type or svn:eol-style is not set" % path )
        elif ptext.match(mime_type) and eol_style == '':
            errmsg.append( "%s : svn:mime-type=%s but svn:eol-style is not set" % (path, mime_type) )

    if len( errmsg ) > 0:
        die( errmsg )


def die(msg):
    """
    Write verbose mesage, and exit
    """

    sys.stderr.write( "\n%s\n" % ("="*20) )
    sys.stderr.write( string.join(msg, '\n') )
    sys.stderr.write( "\n%s\n" % ("="*20) )
    
    sys.stderr.write("""\n\n
Every added file must have the svn:mime-type property set. In
addition text files must have the svn:eol-style property set.

For binary files try running
svn propset svn:mime-type application/octet-stream path/of/file

For text files try
svn propset svn:mime-type text/plain path/of/file
svn propset svn:eol-style native path/of/file

You may want to consider uncommenting the auto-props section
in your ~/.subversion/config file. Read the Subversion book
(http://svnbook.red-bean.com/), Chapter 7, Properties section,
Automatic Property Setting subsection for more help.""")
    
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: %s REPOS TXN\n" % (sys.argv[0]))
    else:
        main(sys.argv[1], sys.argv[2])
