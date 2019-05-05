from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
options = Options()
options.add_argument("--disable-notifications")

driver = webdriver.Chrome(r"path to \chromedriver_win32\chromedriver.exe",chrome_options=options)
f=open("javascript.txt","r")
array=f.readlines()
f.close()
for x in array:
    driver.get(x+'/archive/master.zip')
    sleep(30)

driver.quit()
