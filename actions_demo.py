import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('c:/code/tools/chromedriver')

driver.get('https://google.com')

#locate the search box element
search_box = driver.find_element_by_name('q')
time.sleep(3)

#type in our search query into the search box
search_box.send_keys('seleniumhq' + Keys.RETURN)
images = driver.find_element_by_link_text('images')

images.click()

time.sleep(3)
print(driver.title)

driver.quit()
