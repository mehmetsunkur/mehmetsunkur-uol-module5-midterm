
set-brace:
  export BRAVE_API_KEY=BSA6acA_VQpnAly0K93uqL4q1sHGLuc

set-git:
  git config --global user.email "mehmetsunkur@gmail.com"
  git config --global user.name "Mehmet Sunkur"

mcp:
  pip install mcp-server-time
  pip install mcp-server-git

node:
  curl -fsSL https://deb.nodesource.com/setup_lts.x | bash - && apt-get install -y nodejs

node-not-wotking:
  curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
  nvm install 22


nvm-post:
  export NVM_DIR="$HOME/.nvm"
  [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  
  [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"


post-start-prompt:
  run 'pip install mcp-server-time' .
  run 'pip install mcp-server-git'
  run 'pip install uv'
  run 'pip install mcp-server-fetch'
  run 'npm install -g npm@latest'
  run 'npm install -g node@22'
  install nvm.
  install nodejs 22 nvm
  install npx

  