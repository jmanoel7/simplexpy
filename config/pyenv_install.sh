#!/bin/bash
set -e
source "${SIMPLEXPY_CONFIG:-.}/bashrc"
rm -rf "${PYENV_ROOT}"
git clone https://github.com/pyenv/pyenv.git "${PYENV_ROOT}"
export PATH="${PYENV_ROOT}/bin:${PATH}"
eval "$(pyenv init -)"
pyenv install 2.7.14
exit 0
