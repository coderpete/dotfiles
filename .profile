## aliases
alias edit='vim -N'
alias ll='ls -laG'
alias murder='kill -9'

## places
alias ndn='cd ~/git/ndn/perl';

## machines
alias yakko='ssh petec@yakko.sd.dreamhost.com'
alias fubar='ssh petec@fubar.dreamhost.com'
alias regor='ssh coderpete@regor.dreamhost.com'

## pycow
alias cowsay='python ~/src/py/cowsay.py';

## Arrow key history autocomplete
bind '"\e[A": history-search-backward'
bind '"\e[B": history-search-forward'

## prompt
PS1='[\u@\h:\w]$ '
#PS1='\[\033[01;31m\]\u\[\033[00m\]\[\033[01;32m\]@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\] \[\033[01;31m\]\$\[\033[00m\] \[\033[01;33m\]\]\]\]\]\]\]\]\]\]'

## mybins
export PATH=/usr/local/bin:${PATH}:/Users/pchudykowski/bin:/usr/local/mysql/bin:/Users/pchudykowski/src/sh

## unfuck pip in osx
if [ $(uname -s) = 'Darwin' ]; then
    export CFLAGS=-Qunused-arguments
    export CPPFLAGS=-Qunused-arguments
fi

## virtualenv stuffs
export WORKON_HOME=~/VENVS
source /usr/local/bin/virtualenvwrapper.sh

cowsay 'oh hi'
