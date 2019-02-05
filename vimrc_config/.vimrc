
" ------------AmirSamimi configs from HERE--------------------------

:set number " Display line numbers on the left side
:set ls=2 " This makes Vim show a status line even when only one window is shown
:filetype plugin on " This line enables loading the plugin files for specific file types
:set tabstop=4 " Set tabstop to tell vim how many columns a tab counts for. Linux kernel code expects each tab to be eight columns wide.
:set expandtab " When expandtab is set, hitting Tab in insert mode will produce the appropriate number of spaces.
:set softtabstop=4 " Set softtabstop to control how many columns vim uses when you hit Tab in insert mode. If softtabstop is less than tabstop and expandtab is not set, vim will use a combination of tabs and spaces to make up the desired spacing. If softtabstop equals tabstop and expandtab is not set, vim will always use tabs. When expandtab is set, vim will always use the appropriate number of spaces.
:set shiftwidth=4 " Set shiftwidth to control how many columns text is indented with the reindent operations (<< and >>) and automatic C-style indentation. 
:setlocal foldmethod=indent " Set folding method
:set t_Co=256 " makes Vim use 256 olors
:set nowrap " Don't Wrap lines!

":colorscheme molokai " Set colorScheme -----NOT SET YET IT {WAS MOLOKAI}------- I added holokai so comment it 
"let g:molokai_original = 1
:set background=dark "holokai has gray and dark background, this choose dark, I Like it (hamid)

:set nocp " This changes the values of a LOT of options, enabling features which are not Vi compatible but really really nice
:set clipboard=unnamed
:set clipboard=unnamedplus
:set autoindent " Automatic indentation
:set cindent " This turns on C style indentation
:set si " Smart indent
:syntax enable " syntax highlighting
:set showmatch " Show matching brackets
:set hlsearch " Highlight in search
:set ignorecase " Ignore case in search
:set noswapfile " Avoid swap files
:set mouse=a " Mouse Integration

" I disable it, these days it bothered me, look for a better way in future
"" auto complete for ( , " , ' , [ , { 
":inoremap        (  ()<Left>
":inoremap        "  ""<Left>
":inoremap        `  ``<Left>
":inoremap        '  ''<Left>
":inoremap        [  []<Left>
":inoremap      {  {}<Left>

"" auto comment and uncooment with F6 and F7 key
:autocmd FileType c,cpp,java,scala let b:comment_leader = '// '
:autocmd FileType sh,ruby,python   let b:comment_leader = '# '

:noremap <silent> #6 :<C-B>silent <C-E>s/^/<C-R>=escape(b:comment_leader,'\/')<CR>/<CR>:nohlsearch<CR> " commenting line with F6
:noremap <silent> #7 :<C-B>silent <C-E>s/^\V<C-R>=escape(b:comment_leader,'\/')<CR>//e<CR>:nohlsearch<CR> " uncommenting line with F7

" :noremap <silent> #5 :!xterm -hold -e './%' <CR> <CR>" execute bash & python script with F5
 
:noremap <silent> #5 :!konsole --hold -e 'python ./%' <CR> <CR>" execute python script with F5

:noremap <silent> #3 :tabprevious<CR> " switch to previous tab with F3
:noremap <silent> #4 :tabnext<CR> " switch to next tab with F2
:map <F8> :setlocal spell! spelllang=en_us<CR> " check spelling with F8
:set pastetoggle =<F2> " Paste mode toggle with F2 Pastemode disable auto-indent and bracket auto-compelation and it helps you to paste code fro elsewhere .



"----------------------------------Plugins settings-------------------------------------
"here are plugins settings

"indentLine 
let g:indentLine_char = '┆'

" autocomplpop setting
:set omnifunc=syntaxcomplete " This is necessary for acp plugin
:let g:acp_behaviorKeywordLength = 1 "  Length of keyword characters before the cursor, which are needed to attempt keyword completion

" airline plugin setting
:let g:airline_theme='wombat' " set airline plugin theme
:let g:airline#extensions#tabline#enabled = 1 " showing tabs 
:let g:airline_powerline_fonts = 1
if !exists('g:airline_symbols')
    let g:airline_symbols = {}
  endif

 " unicode symbols
  let g:airline_left_sep = '»'
  let g:airline_left_sep = '▶'
  let g:airline_right_sep = '«'
  let g:airline_right_sep = '◀'

"vim-airline-clock 
:let g:airline#extensions#clock#format = '%c'

" NERDTree plugin setting

"toggle showing NERDTree with F9
:map <F9> :NERDTreeToggle<CR> 

"open a NERDTree automatically when vim starts up if no files were specified
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif

" close vim if the only window left open is a NERDTree
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

" Open file in new tab with ctrl + t
:let NERDTreeMapOpenInTab='<c-t>'
:set ttymouse=xterm2
"emmet used for html,css,js use [ctrl+y]+,
let g:user_emmet_leader_key='<c-y>'

"make Vim transpareint -->
""https://stackoverflow.com/questions/37712730/set-vim-background-transparent
""hi Normal guibg=NONE ctermbg=NONE

"vim-auto-save
let g:auto_save = 1  " enable AutoSave on Vim startup
let g:auto_save_silent = 1  " do not display the auto-save notification
let g:auto_save_events = ["InsertLeave", "TextChanged"]  "save every change when leave insert mode(normal mode)
"more options in repository: https://github.com/907th/vim-auto-save


"----------------------------Vim-Plug installation plugins--------------------------------
"Plugins will be downloaded under the specified directory.

call plug#begin('~/.vim/plugged')

Plug 'https://github.com/scrooloose/nerdtree.git'
Plug 'itchyny/lightline.vim'
Plug 'mattn/emmet-vim'
"Plug 'https://github.com/changyuheng/color-scheme-holokai-for-vim.git'
Plug 'patstockwell/vim-monokai-tasty'
Plug 'chiel92/vim-autoformat'
"Plug 'alvan/vim-closetag'       "html closeTag, emmet-vim 
Plug 'davidhalter/jedi-vim'     "python autocompletion
Plug 'https://github.com/tc50cal/vim-terminal.git' "type :term
Plug 'https://github.com/907th/vim-auto-save'       "autosave, it has settings above


"List ends here. Plugins become visible to Vim after this call.
call plug#end()

