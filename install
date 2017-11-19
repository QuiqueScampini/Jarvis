#!/bin/bash

cd `dirname $0`

echo "Installing Jarvis"
JARVIS_INSTALL_DIR=`pwd`
export JARVIS_INSTALL_DIR

sed 's|JARVIS_INSTALL_DIR|'`pwd`'|g' ./resources/.bash_aliases_template > ./resources/.bash_aliases

if [ ! -f ~/.bash_aliases ]; then
    echo "Creating ~/.bash_aliases"
    touch ~/.bash_aliases
fi

echo "Adding Environment Variables to .bash_aliases"
cat ./resources/.bash_aliases >> ~/.bash_aliases

echo "Loading Environment Variables from .bash_aliases"
. ~/.bash_aliases