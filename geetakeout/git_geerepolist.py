from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time,os,subprocess,ee,getpass

pathway=os.path.dirname(os.path.realpath(__file__))
def gee_repo():
    options = Options()
    options.add_argument('-headless')
    authorization_url="https://earthengine.googlesource.com/users/"
    uname=str(raw_input("Enter your Username:  "))
    passw=str(getpass.getpass("Enter your Password:  "))
    driver = Firefox(executable_path=os.path.join(pathway,"geckodriver.exe"),firefox_options=options)
    driver.get(authorization_url)
    time.sleep(5)
    username = driver.find_element_by_xpath('//*[@id="identifierId"]')
    username.send_keys(uname)
    driver.find_element_by_id("identifierNext").click()
    time.sleep(5)
    passw=driver.find_element_by_name("password").send_keys(passw)
    driver.find_element_by_id("passwordNext").click()
    time.sleep(5)
    sr=driver.page_source.encode('ascii', 'ignore')
    driver.close()
    with open(os.path.join(pathway,"eed-users.html"), "w") as f:
        f.write(sr)
#geerepo()
