#!/usr/bin/env bash

#This will install firefox and other tools needed to compile python3.6
sudo apt-get update
sudo apt-get install -y build-essential checkinstall wget tar
sudo apt-get install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
sudo apt-get install -y firefox

#This will install Gecko Driver(Required by Selenium Driver)
wget https://github.com/mozilla/geckodriver/releases/download/v0.11.1/geckodriver-v0.11.1-linux64.tar.gz
tar -xvzf geckodriver-v0.11.1-linux64.tar.gz
rm geckodriver-v0.11.1-linux64.tar.gz
chmod +x geckodriver
cp geckodriver /usr/local/bin/

#This will install a brand new python3.6 and pip3.6 into your ubuntu
wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tgz
tar xzf Python-3.6.2.tgz
cd Python-3.6.2
./configure
sudo make altinstall