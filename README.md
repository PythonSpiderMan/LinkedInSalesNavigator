# (Spider) LinkedIn Sales Navigator URL
> You'll need to have an account that can access the LikedIn Sales Navigator

[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)

## Install Dependencies on x86_64 Windows®
> IMPORTANT: If the software asks you whether to install to `PATH`, choose `YES`


- Install Anaconda from Official Website \
`https://repo.continuum.io/archive/Anaconda3-5.0.1-Windows-x86_64.exe`

- Install Firefox® from Mozilla's official website \
`https://www.mozilla.org/en-US/firefox/new/`

- Install Git for windows \
`https://git-scm.com/download/win`


## Run program on x86_64 Windows®
* Open a command line \
by pressing `CMD + R` then enter `cmd` 

* Clone the Git Repository \
`git clone https://gitlab.com/XetRAFHan/linkedinspider.git`
* Change directory to program folder \
`cd linkedinproject`
* Create a new Anaconda® environment \
`conda create --name linkedin python=3.6`
* Activate Anaconda® environment \
`activate linkedin`
* Install Python dependencies from pypi \
`pip install -r requirement_windows.txt`
* Install Scrapy from Anaconda \
`conda install -c conda-forge scrapy`
* Open a Firefox Browser
* Run the program \
`windows_start.bat`
* Enter your LinkedIn Sales Navigator Account
* You may need to pass the reCAPCHA
* Enter your LinkedIn Sale Navigator URL
> If your don't know what is a LinkedIn Sales Navigator, Please check this Youtube Video Introduction (->)
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/4DwuiurKTh0/0.jpg)](https://www.youtube.com/watch?v=4DwuiurKTh0)

> When the URL is opened, you should see something like this
![LSNS](https://raw.githubusercontent.com/XetRAHF/Spider_LinkedInSalesNavigatorURL/7758fd001ee1debcf44ada0d7f8c2fcd0c801f0d/imgs/sales_navigator_eg.png)

> Here is an example LinkedIn Sales Navigator URL \
`https://www.linkedin.com/sales/search?keywords=CEO&facet=G&facet=I&facet=CS&facet.G=us%3A70&facet.I=43&facet.CS=D&facet.CS=G&count=25&start=0&updateHistory=true&searchHistoryId=2107126404&trackingInfoJson.contextId=1809E16E40A8F114008596FB612B0000`
* Patiently wait for your result in `output` folder
* Remember to delete `temp` folder when scraping had finished

## Install Dependencies on x86_64 Ubuntu
> It's highly recommended to run any spider on a cloud instance. (The Internet connection speed will be much better)

* Install Git for Ubuntu
`sudo apt-get install -y git`
* If your Ubuntu Doesn't have a desktop environment, you should install a GNOME.
```
sudo apt-get install -y lubuntu
sudo reboot
```
* Clone the Git Repository \
`git clone https://gitlab.com/XetRAFHan/linkedinspider.git`
* Change directory to program folder \
`cd linkedinproject`
* Install dependencies
`bash ubuntu_dependencies.sh`
* Install pip dependencies
`sudo pip3.6 install -r requirement.txt`

## Run program on x86_64 Ubuntu
* Open a Firefox Browser
* Run the program 

`bash ubuntu_start.sh`
* Enter your LinkedIn Sales Navigator Account
* You may need to pass the reCAPCHA
* Enter your LinkedIn Sale Navigator URL
* Patiently wait for your result in `output` folder
* Remember to delete `temp` folder when scraping had finished

## Target Data
		
| Title | Name | First Name | Last Name | Time in role | Twitter | Contact Linkedin Profile URL | Contact Location | Company | Company Size (Employees) | Industry | Company Profile Linkedin URL | Company Website | ID |
|-------|------|------------|-----------|--------------|---------|------------------------------|------------------|---------|--------------------------|----------|------------------------------|-----------------|----|
| CEO & president | ZhiXing Zhe | ZhiXing | Zhe | 10 years and 3 months in role xxxx | https://www.twitter.com/xxxx | https://www.linkedin.com/sal/zhixingzhe | Great China | ZhongGuo DianXin | 50 - 100 | telecommunications | https://www.linkedin.com/sal/xxxx | https://www.somecompany.com/ | 0 based |

