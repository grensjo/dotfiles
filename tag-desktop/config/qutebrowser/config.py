config.source('colors.py')
config.source('keys.py')
config.source('ui.py')

# Various settings
c.editor.command = ['blocking-gnome-terminal', 'vim {}']

# Search engines
c.url.searchengines['DEFAULT'] = 'https://www.google.com/search?hl=en&q={}'
c.url.searchengines['ddg'] = 'https://duckduckgo.com/?q={}'
c.url.searchengines['w'] = 'https://en.wikipedia.org/w/index.php?search={}'
c.url.searchengines['ws'] = 'https://sv.wikipedia.org/w/index.php?search={}'
c.url.searchengines['aur'] = 'https://aur.archlinux.org/packages/?O=0&K={}'
c.url.searchengines['pkg'] = 'https://www.archlinux.org/packages/?sort=&q={}'
c.url.searchengines['aw'] = 'https://wiki.archlinux.org/index.php?title=Special%3ASearch&search={}'
c.url.searchengines['yt'] = 'https://www.youtube.com/results?search_query={}'


# Aliases
c.aliases['transl'] = 'open -t -r https://translate.google.com/translate?sl=auto&tl=en&u={url}'
c.aliases['archive.is'] = 'open -t -r https://archive.is/{url}'
c.aliases['webarchive'] = 'open -t -r https://web.archive.org/web/*/{url}'
c.aliases['x'] = 'quit --save'
c.aliases['cal'] = 'spawn --userscript calendar'
c.aliases['lyrics'] = 'spawn --userscript lyrics'

# c.spellcheck.languages = ['en-US', 'sv-SE']

c.session.lazy_restore = True
