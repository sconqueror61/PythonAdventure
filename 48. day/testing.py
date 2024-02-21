from selenium import webdriver
from selenium.webdriver.common.by import By
#Keep Chrome browser open
chrome_options= webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver= webdriver.Chrome() 
driver.get("https://www.python.org")

price_dollar= driver.find_element(By.CLASS_NAME,value="a-price-whole")
price_cents= driver.find_element(By.CLASS_NAME, value="a-price-fraction")
print(f"The price is {price_dollar.text}.{price_cents.text}")

search_bar=driver.find_element(By.NAME,value="q")
button= driver.find_element(By.ID,value="submit")
print(button.size)
# driver.close()
driver.quit()
