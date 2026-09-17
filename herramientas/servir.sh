#!/bin/sh
# Compila y sirve la web en http://localhost:4000 con recarga automática.
# Uso: sh herramientas/servir.sh        (o: sh herramientas/servir.sh build  para solo compilar)
cd "$(dirname "$0")/.." || exit 1
export LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8
export PATH="/opt/homebrew/opt/ruby/bin:$PATH"
export RUBYOPT="-r$(pwd)/herramientas/ruby-compat.rb -W0"
if [ "$1" = "build" ]; then
  exec bundle exec jekyll build
else
  PORT="${PORT:-4000}"
  # Puerto de recarga distinto para cada servidor, así pueden convivir varios (4000 → 34000)
  exec bundle exec jekyll serve --livereload --port "$PORT" --livereload-port "$((PORT + 30000))"
fi
