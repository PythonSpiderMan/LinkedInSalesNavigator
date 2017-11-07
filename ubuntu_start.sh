#!/usr/bin/env bash
mkdir temp && cd temp
mkdir step_1 step_2 step_3 step_4 step_5 step_6 step_7
cd ..
mkdir output

python step_1_linux.py
python step_6.py
python step_7.py



