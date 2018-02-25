from os.path import expanduser
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
githome=expanduser("~/geetakeout/gitkey")
if not os.path.exists(os.path.join(expanduser("~"),"geetakeout","gitkey")):
    os.makedirs(os.path.join(expanduser("~"),"geetakeout","gitkey"))
def gitwinauth():
    options = Options()
    options.add_argument('-headless')
    authorization_url="https://earthengine.googlesource.com/"
    try:
        uname=str(raw_input("Enter your Username:  "))
        passw=str(getpass.getpass("Enter your Password:  "))
        driver = Firefox(executable_path=os.path.join(pathway,"geckodriver.exe"),firefox_options=options)
        driver.get(authorization_url)
        time.sleep(2)
        username = driver.find_element_by_xpath('//*[@id="identifierId"]')
        username.send_keys(uname)
        driver.find_element_by_id("identifierNext").click()
        time.sleep(3)
        passw=driver.find_element_by_name("password").send_keys(passw)
        driver.find_element_by_id("passwordNext").click()
        time.sleep(2)
        try:
            driver.find_element_by_xpath("//div[@id='submit_approve_access']/content/span").click()
            time.sleep(2)
        except Exception:
            pass
        driver.find_element_by_link_text("Generate Password").click()
        pin_element=driver.find_element_by_id("install-windows").get_attribute("value")
        driver.close()
        with open(os.path.join(githome,"git-"+str(uname).split("@")[0]), "w") as f:
            f.write(pin_element)
        print("Git key saved at "+str(githome))
    except Exception as e:
        print(e)
#gitwinauth()
