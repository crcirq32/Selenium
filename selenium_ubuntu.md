Steps required to setup Selenium on Ubuntu 24.04
1) install selenium with git - either source or sudo apt install python3-selenium
2) install geckodriver - firefox see link
3) install webdrivermanager - see link
4) remove firefox as snap -
6) Test Webdriver, Firefox, Geckodrivermanager and selenium work:


References:
pypi.org/project/selenium/#files
https://www.zenrows.com/blog/selenium-python-web-scraping#getting-started

```
git clone https://www.github.com/selenium/SeleniumHQ/selenium.git
```

```
https://www.zenrows.com/blog/selenium-python-web-scraping#getting-started
```
Install geckodriver on mozilla
```
https://dev.to/eugenedorfling/installing-the-firefox-web-driver-on-linux-for-selenium-d45
```
---

Install GeckoDriver on Mozilla
```
mv ~/Downloads/geckodriver-v0.35.0-linux64.tar.gz .
gzip -d  ./geckodriver-v0.35.0-linux64.tar.gz
tar -C /usr/local/bin -xvf  geckodriver-v0.35.0-linux64.tar.gz
#This may be necessary Make sure to append to current PATH
export PATH=$PATH:<path of geckodriver>
```

3) Download webdriver_manager https://github.com/SergeyPirogov/webdriver_manager
Unable to locate driver error:
selenium.dev/documentation/webdrivermanager/troubleshooting/errors/driver_location

Install Webdriver-manager:	 
```
wget https://github.com/SergeyPirogov/webdriver_manager
gzip -d 
tar -xvf webdriver_manger-4.0.2
cd web webdriver_manger
python3 setup.py build
python3 setup.py install
```
Disclaimer: Firefox can not be a snap:
```
https://www.omgubuntu.co.uk/2022/04/how-to-install-firefox-deb-apt-ubuntu-22-04#:%7E:text=Installing%20Firefox%20via%20Apt%20(Not%20Snap)&text=You%20add%20the%20Mozilla%20Team,%2C%20bookmarks%2C%20and%20other%20data.
```
Fix firefox:
```
Step 1: Uninstall the Firefox Snap:
sudo snap remove firefox
Step 2: Create an APT keyring (if one doesn’t already exist):
sudo install -d -m 0755 /etc/apt/keyrings
Step 3: Import the Mozilla APT repo signing key (if wget is missing, install it first):
wget -q https://packages.mozilla.org/apt/repo-signing-key.gpg -O- | sudo tee /etc/apt/keyrings/packages.mozilla.org.asc > /dev/null
Step 4: Add the Mozilla signing key to your sources.list:
echo "deb [signed-by=/etc/apt/keyrings/packages.mozilla.org.asc] https://packages.mozilla.org/apt mozilla main" | sudo tee -a /etc/apt/sources.list.d/mozilla.list > /dev/null
Step 5: Set the Firefox package priority to ensure Mozilla’s DEB is always preferred. If you don’t do this the Ubuntu transition package will be reinstalled, and you’ll have the Firefox snap:

echo '
Package: *
Pin: origin packages.mozilla.org
Pin-Priority: 1000

Package: firefox*
Pin: release o=Ubuntu
Pin-Priority: -1' | sudo tee /etc/apt/preferences.d/mozilla
```
Step 6: Finally, use APT to remove Ubuntu’s pretend Firefox DEB (if still present) and install from Mozilla’s repository:

```
sudo apt update && sudo apt remove firefox
sudo apt install firefox
```

Tests:
```
from selenium import webdriver
#Creates webdriver instance for firefox
from selenium.webdriver.firefox.service import Service as FirefoxService
#imports Geckodriver
from webdriver_manager.firefox import GeckoDriverManager

#test to see if instance is created: Pop-up will show it's working.
driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
```
