" IMPORTANT! don't be backward-compatible with unix vi
set nocompatible

"easy plugin management with pathogen
call pathogen#infect()

" Make sure we use a better leader key
let mapleader = ","
let g:mapleader = ","

"filetype plugin indent on
syntax enable
set background=dark
let g:solarized_termcolors=16
colorscheme solarized

" syntastic settings
let g:syntastic_enable_signs=1
let g:syntastic_auto_jump=0
let g:syntastic_auto_loc_list=2
let g:syntastic_quiet_warnings=0
let g:syntastic_disabled_filetypes = ['html']

" syntastic autocompletion settings
inoremap <expr> <down> ((pumvisible())?("\<C-n>"):("<down>"))
inoremap <expr> <up> ((pumvisible())?("\<C-p>"):("<up>"))
inoremap <expr> <CR> ((pumvisible())?("\<C-y>"):("<CR>"))
let g:acp_behaviorPythonOmniLength = 5

set number         " line numbers
set ruler          " column/line/% status info

" formatting options
set autoindent
set tabstop=4      " 4 column indent
set shiftround     " indent to the nearest tabstop
set backspace=indent,eol,start

" the following settings are controversial!
set expandtab      " expand tabs into spaces 'set noet' to disable
set softtabstop=4  " 'set sts=' to disable
set shiftwidth=4   " 'set sw=' to disable 

set history=100    " command/search/input history size
set viminfo+=%     " restore buffer list if zvim is launched without a file arg
set viminfo+=r/tmp " don't save info for temp files
"set wildmenu       " interactive auto-complete menu

set laststatus=2   " always show status line
set hlsearch       " highlight searches

" Make sure we use a better leader key
let mapleader = ","
let g:mapleader = ","

" Pytest leader mappings
nmap <silent><Leader>f <Esc>:Pytest file<CR>
nmap <silent><Leader>m <Esc>:Pytest method<CR>
"nmap <silent><Leader>c <Esc>:Pytest class<CR>
map <F3> :Pytest session<CR>

" replace tabs with 4 spaces in python source files only
au FileType python setl sw=4 sts=4 et

" syntax highlight mako files with html highlighting
filetype on
au BufNewFile,BufRead *.mak set filetype=html

"for taglist: http://vim-taglist.sourceforge.net/installation.html
let Tlist_Inc_Winwidth = 0
let Tlist_Ctags_Cmd='/home/pchudykowski/ctags/bin/ctags'

" use shift-T to toggle tags pane
nnoremap <silent> T :TlistToggle<CR>

" SVNCommand settings
let SVNCommandEnableBufferSetup=1
let SVNCommandEdit='split'
let SVNCommandNameResultBuffers=1

:map \pt :%!perltidy -q<CR>
autocmd BufRead *.java set efm=%A\ %#[javac]\ %f:%l:\ %m,%-Z\ %#[javac]\ %p^,%-C%.%#
autocmd BufRead *.java set include=^#\s*import

