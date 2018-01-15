# Tabs
c.tabs.background = True
c.tabs.last_close = 'close'
c.tabs.show = 'multiple'
c.tabs.position = 'left'
c.tabs.select_on_remove = 'prev'
c.tabs.width = "15%"


# Statusbar
c.downloads.position = 'bottom'
c.statusbar.position = 'top'
c.scrolling.smooth = True


# Change font size from 10pt to 8pt EVERYWHERE.
fontsize_settings = map(lambda x: "fonts." + x, [
        'completion.category',
        'completion.entry',
        'debug_console',
        'downloads',
        'hints',
        'keyhint',
        'messages.error',
        'messages.info',
        'messages.warning',
        'prompts',
        'statusbar',
        'tabs'
    ])
for setting in fontsize_settings:
    config.set(setting, config.get(setting).replace('10pt', '8pt'))
