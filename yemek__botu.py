from hashlib import new
from types import NoneType
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver import ChromeOptions
from selenium.webdriver import Chrome

calender_page = requests.get("https://www.turktakvim.com")
calender_soup = BeautifulSoup(calender_page.content, "html.parser")
date_division = calender_soup.find(class_ = "tarihay")
date_division.find("br").decompose()
date_division.find("br").decompose()
days = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cuma", "Cumartesi", "Pazar"]
today = ""
for date_element in date_division:
    for day in days:
        if date_element.text.strip() == day:
            today = day

food_today = ""
food_page = requests.get("http://www.sksdb.hacettepe.edu.tr/bidbnew/grid.php?parameters=qbapuL6kmaScnHaup8DEm1B8maqturW8haidnI%2Bsq8F%2FgY1fiZWdnKShq8bTlaOZXq%2BmwWjLzJyPlpmcpbm1kNORopmYXI22tLzHXKmVnZykwafFhImVnZWipbq0f8qRnJ%2BioF6go7%2FOoplWqKSltLa805yVj5agnsGmkNORopmYXam2qbi%2Bo5mqlXRrinJdf1BQUFBXWXVMc39QUA%3D%3D")
food_soup = BeautifulSoup(food_page.content, "html.parser")
food_divisions = food_soup.find_all(class_ = "panel-grid-cell col-md-6")
for food_division in food_divisions:
    food_date_division = food_division.find(class_ = "popular")
    food_date = food_date_division.find(text = True, recursive = False)
    if today in food_date.text.strip():
        food_today = food_division
        break
food_today = food_today.text.strip()

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\HP\\AppData\\Local\\Google\\Chrome\\User Data\\whatsappbot")
driver = webdriver.Chrome("executable_path=C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe", options=options)

contact = "food bot test group"
driver.get("https://web.whatsapp.com")
time.sleep(20)
inp_xpath_search = '//*[@id="side"]//div[1]//div//div//div[2]//div//div[2]'
input_box_search = WebDriverWait(driver,50).until(lambda driver: driver.find_element(By.XPATH, inp_xpath_search))
input_box_search.click()
time.sleep(1)
input_box_search.send_keys(contact)
time.sleep(1)    
selected_contact = driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[2]')
selected_contact.click()
time.sleep(1)

keywords = ["yemekhane", "yemek"]
while True:
    last_message = driver.find_element(By.CLASS_NAME, '_1qB8f')
    for keyword in keywords:
        if keyword in last_message.text.strip().lower():
            inp_xpath = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
            input_box = driver.find_element(By.XPATH, inp_xpath)
            time.sleep(1)
            input_box.send_keys(food_today + Keys.ENTER)
            print("List has been sent.")
            time.sleep(3)
            break
        else:
            print(f"Keyword {keyword} is not included in the last message")
            time.sleep(1)
 



