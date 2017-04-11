""" Disable VI compatibility
set nocompatible

""" Colors
set bg=dark     " use colors reasonable for a dark terminal background
syntax on       " enable syntax highlighting

""" Indentation
filetype plugin indent on   " load filetype-specific indent files and plugins
set tabstop=4           " Number of visual spaces per tab   
set softtabstop=4       " Number of spaces in tab when editing
set shiftwidth=4        " Number of spaces text is shifted with << and >>
set expandtab           " Tabs are spaces

""" Project-specific settings
au BufRead,BufNewFile */git/aiprojekt/*.cpp setlocal noexpandtab
au BufRead,BufNewFile */git/aiprojekt/*.h setlocal noexpandtab
au BufRead,BufNewFile *.yml setlocal softtabstop=2 tabstop=2 shiftwidth=2


""" UI 
set showcmd             " show latest command in bottom bar
set wildmenu			" show graphical menu of tab completations in bottom bar
" set cursorline        " highlight current line (TODO make it look good)
" set number            " show line numbers to the left (TODO make it look good)
" set relativenumber

""" Searching
set smartcase
set ignorecase
set incsearch
set hlsearch
noremap <c-l> :nohlsearch<cr><c-l>

" Swedish layout things
noremap Ö :
noremap ö :
"noremap ; <
"noremap : >

noremap ; :

noremap <tab> gt
noremap <s-tab> gT
noremap <c-p> <c-i>
noremap - /

imap <f1> <esc>

set scrolloff=3

nnoremap <silent> [b :bprevious<CR>
nnoremap <silent> ]b :bnext<CR>
nnoremap <silent> [B :bfirst<CR>
nnoremap <silent> ]B :blast<CR>


"LaTeX things
imap <f2> <esc><f2>
map <f2> öw<enter>ö!pdflatex %;<enter>
map <f3> ö!xdg-open %:r.pdf &> /dev/null<enter>

" Local config
if filereadable($HOME . "/.vimrc.local")
  source ~/.vimrc.local
endif


" Plugin management
let g:plug_shallow = 0

call plug#begin('~/.vim/plugged')

if filereadable($HOME . "/.vim/plugins")
  source ~/.vim/plugins
endif

if filereadable($HOME . "/.vim/plugins.local")
  source ~/.vim/plugins.local
endif

call plug#end()
delc PlugUpgrade

let g:airline_theme='papercolor'

let g:airline#extensions#tabline#enabled = 1
let g:airline_powerline_fonts = 1

if has('nvim')
    :tnoremap <Esc> <C-\><C-n>
endif
