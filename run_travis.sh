#!/usr/bin/env bash
python runtest.py
python run.py > /dev/null &
nosetests --with-coverage