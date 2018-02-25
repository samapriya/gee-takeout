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
def gitcreate(reponame,uname,passw):
    options = Options()
    options.add_argument('-headless')
    authorization_url="https://code.earthengine.google.com/"
##    uname=str(raw_input("Enter your Username:  "))
##    passw=str(getpass.getpass("Enter your Password:  "))
    try:
        driver = Firefox(executable_path=os.path.join(pathway,"geckodriver.exe"),firefox_options=options)
        driver.get(authorization_url)
        time.sleep(2)
        username = driver.find_element_by_xpath('//*[@id="identifierId"]')
        username.send_keys(uname)
        driver.find_element_by_id("identifierNext").click()
        time.sleep(3)
        passw=driver.find_element_by_name("password").send_keys(passw)
        driver.find_element_by_id("passwordNext").click()
        time.sleep(10)
        try:
            driver.find_element_by_xpath("//div[@id='submit_approve_access']/content/span").click()
            time.sleep(2)
        except Exception:
            pass
        driver.find_element_by_xpath("//div[@id='main']/div/div/div/div/div/div/div/div[2]/div/div/div/div/div").click()
        time.sleep(3)
        driver.find_element_by_xpath("//div[@id=':l']/div").click()
        driver.find_element_by_xpath("(//input[@type='text'])[4]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[4]").send_keys(reponame)
        driver.find_element_by_name("Create").click()
        driver.close()
    except Exception as e:
        print(e)

def gitcreate_rec(folder):
    uname=str(raw_input("Enter your Username:  "))
    passw=str(getpass.getpass("Enter your Password:  "))
    for folderpath in os.listdir(folder):
        print("Now Creating " +str(folderpath))
        gitcreate(folderpath,uname,passw)
#gitcreate_recursive(folder=r"C:\Users\samapriya\Box Sync\IUB\Pycodes\Applications and Tools\Earth Engine Codes\EE_Replicate\Code Replication\Code-Downloader\gitee-cli\samapriya")
