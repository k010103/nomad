#!/bin/bash

VENE_DIR=".venv"
PYTHON_PATH="/usr/bin/python3"

# setup venv
$PYTHON_PATH -m virtualenv $VENE_DIR
source $VENE_DIR/bin/activate

# pip version
pip3 install --upgrade pip #> /dev/null 2>&1
pip3 --version

# pip install
pip3 install flask #> /dev/null 2>&1
pip3 install requests #> /dev/null 2>&1
pip3 install bs4 #> /dev/null 2>&1
pip3 list
echo -e "
      =====================================================
      --------------------  make venv  --------------------
      =====================================================\n"