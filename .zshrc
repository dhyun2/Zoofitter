
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm

export NVM_DIR=~/.nvm
source $(brew --prefix nvm)/nvm.sh

# bun completions
[ -s "/Users/donghyunpark/.bun/_bun" ] && source "/Users/donghyunpark/.bun/_bun"

# bun
export BUN_INSTALL="$HOME/.bun"
export PATH="$BUN_INSTALL/bin:$PATH"
