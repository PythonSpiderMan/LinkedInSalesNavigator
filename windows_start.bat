@echo off
md temp
cd temp
md step_1 step_2 step_3 step_4 step_5 step_6 step_7
cd ..
md output

python step_1.py
python step_6.py
python step_7.py

echo Removing last scrapped archives
rd scrapped_webpages_archives

rename temp scrapped_webpages_archives
echo All done! (LinkedIn Spider)