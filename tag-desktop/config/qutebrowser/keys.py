config.bind('F', 'hint all tab-fg')         # Switch to open in foreground
config.bind('M', 'bookmark-add --toggle')   # Add --toggle

config.unbind('<ctrl-q>') # do not want to close windows by mistake, the
                          # command :q or i3's <Ctrl-Shift-Q> are good enough

# Vim-style jumps to top and bottom (well, in
# Vim its Shift-H and Shift-L, but close enough)
config.bind('<ctrl-h>', 'tab-focus 1') # overriding shortcut to home, but who cares?
config.bind('<ctrl-l>', 'tab-focus -1')

# Jump quickly between tabs
config.bind('<ctrl-j>', 'run-with-count 5 tab-next')
config.bind('<ctrl-k>', 'run-with-count 5 tab-prev')
config.bind('<ctrl-shift-j>', 'run-with-count 10 tab-next')
config.bind('<ctrl-shift-k>', 'run-with-count 10 tab-prev')

# Easily accessible UI tweaks!
config.bind('tt', 'config-cycle --temp tabs.show multiple switching')
config.bind('sh', 'config-cycle --temp statusbar.hide')

# Userscripts, ftw!
config.bind('pa', 'spawn --userscript password_fill')
config.bind(r'\a', 'spawn --userscript rlist add')
config.bind(r'\c', 'spawn --userscript rlist add -c')
config.bind(r'\d', 'spawn --userscript rlist done')
config.bind(';a', 'hint links userscript rlist-add')
config.bind(';A', 'hint --rapid links userscript rlist-add')
config.bind(';c', 'hint links userscript rlist-add-comments')
config.bind(';C', 'hint --rapid links userscript rlist-add-comments')
config.bind('gk', 'spawn --userscript kattisid')
config.bind('gv', 'spawn --userscript view_in_mpv')

# Passthrough
config.bind('<ctrl-[>', 'leave-mode', mode='passthrough')
config.bind('<ctrl-v>', 'fake-key <ctrl-v>', mode='passthrough')

# CSS tweaks
css = '~/.config/qutebrowser/custom-stylesheets/solarized-all-sites-dark.css'
config.bind(',n', f'config-cycle content.user_stylesheets {css} "" ;; reload')
