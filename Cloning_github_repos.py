from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from time import sleep
options = Options()
options.add_argument("--disable-notifications")
#options.add_argument("download.default_directory=C:\\Users\\minni\\Desktop\\javascript_games")
driver = webdriver.Chrome(r"C:\Users\minni\Downloads\chromedriver_win32\chromedriver.exe",chrome_options=options)
f=open("javascript.txt","r")
array=f.readlines()
f.close()
for x in array:
    driver.get(x+'/archive/master.zip')
    sleep(30)

driver.quit()
