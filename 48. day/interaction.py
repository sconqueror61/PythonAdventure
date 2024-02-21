from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver= webdriver.Chrome(options=chrome_options) 

#Navigate our webpage
driver.get("https://en.wikipedia.org/wiki/Main_Page")
articlecount=driver.find_element(By.CSS_SELECTOR, value="#articlecount a")

all_portals= driver.find_element(By.LINK_TEXT,value="Content Portals")

search= driver.find_element(By.NAME,value="search")
search.send_keys("Python",Keys.ENTER)
