## aliases
alias edit='vim -N'
alias ll='ls -laG'

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

## mybins
export PATH=${PATH}:/Users/pchudykowski/bin:/usr/local/mysql/bin:/Users/pchudykowski/src/sh

## virtualenv stuffs
export WORKON_HOME=~/VENVS
source /usr/local/bin/virtualenvwrapper.sh

cowsay 'oh hi'
