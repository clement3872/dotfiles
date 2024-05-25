
alias yeet="yay -Rn"
alias yeeet="yay -Rns"
alias yeet_useless="yay -Rns $(yay -Qtdq)"

# git
alias g="git"
alias gad="git add --all"
alias gcm="git commit -a -m"
alias gcms="git commit -S -m"
alias gph="git push"
alias gpl="git pull"
alias gcl="git clone"
alias gin="git init"

alias gst="git status"
alias glg="git log -n 5"
alias glgr="git reflog"
alias gdf="git diff"

alias gbr="git branch"
alias gsw="git switch"
alias gch="git checkout"
alias gra="git remote add origin git@github.com:"
alias grs="git remote set-url origin git@github.com:"

# other
alias nv="nvim"
alias la="ls -alF"
alias h="history|grep"
alias c="clear" # I know about ctrl l etc.
alias logout="killall -KILL -u $USER"
alias files="nemo"
alias files.="nemo ."
alias help="cat ~/.zshrc | less"

# cd
alias ..="cd .."
alias ....="cd ../.."
alias ......="cd ../../.."
alias ........="cd ../../../.."

# move in terminal
bindkey '^[[1;5C' forward-word
bindkey '^[[1;5D' backward-word

#bindkey '\e\d' backward-kill-word
#bindkey '\e[3;3~' kill-word

# Custom function to delete word before '/'
backward-delete-word-including-slash() {
  local WORDCHARS=${WORDCHARS/\/}
  zle backward-delete-word
}
# Bind Alt+Backspace to the custom function
zle -N backward-delete-word-including-slash
bindkey '^[^?' backward-delete-word-including-slash

#The same but in the other for alt+delete
forward-delete-word-including-slash() {
  local WORDCHARS=${WORDCHARS/\/}
  zle kill-word
}
zle -N forward-delete-word-including-slash
bindkey '\e[3;3~' forward-delete-word-including-slash

# default prompt
#PS1="%n %F{red}%1~ %f%# "

autoload -Uz vcs_info
precmd() { vcs_info }
zstyle ':vcs_info:git:*' formats '%b '
setopt PROMPT_SUBST
PROMPT='%F{green}%*%f %F{blue}%~%f %F{red}${vcs_info_msg_0_}%f$ '
