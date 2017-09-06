source ~/.zplug/repos/zplug/zplug/init.zsh

zplug "zplug/zplug", hook-build:"zplug --self-manage"

zplug "zsh-users/zsh-completions"
# zplug "zsh-users/zsh-syntax-highlighting"
# zplug "zsh-users/zsh-history-substring-search"
# zplug "zsh-users/zsh-autosuggestions"
# zplug "djui/alias-tips"
zplug "plugins/vi-mode", from:oh-my-zsh
zplug "robbyrussell/oh-my-zsh", from:github, use:lib/history.zsh
zplug "grensjo/bullet-train-oh-my-zsh-theme", as:theme

zplug load

# Custom config
[[ -f ~/.zshrc-common ]] && source ~/.zshrc-common
[[ -f ~/.zshrc-local ]] && source ~/.zshrc-local
true
