import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://shop.lululemon.com/")
driver.maximize_window()
time.sleep(1)
#Closing pop
popup_close = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".closeButton__onjV4S")))
popup_close.click()
#Clicking on Shop What's New
whats_new_button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@class='link button_button__Sn_Jv button_buttonOutline__ftaET']")))
whats_new_button.click()
#Click on Men's Checkbox
checkbox = driver.find_element(By.ID, "Men")
driver.execute_script("arguments[0].click();", checkbox)
time.sleep(2)
accessories = driver.find_element(By.ID,"Accessories")
driver.execute_script("arguments[0].click();", accessories)
time.sleep(1.5)
every_day_bag_2L = wait.until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Everywhere Belt Bag Large 2L']")))
every_day_bag_2L.click()
select_color = wait.until(EC.presence_of_element_located((By.XPATH, "(//img[@title='Lava Cake'])[1]")))
select_color.click()
add_to_bag = wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Add to Bag']")))
add_to_bag.click()
view_bag = wait.until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='View Bag & Checkout']")))
view_bag.click()
remove_item = wait.until(EC.presence_of_element_located((By.XPATH, "(//div[normalize-space()='Remove'])[1]")))
remove_item.click()
remove_confirmation = wait.until(EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='YES, REMOVE THIS ITEM']")))
remove_confirmation.click()
shop_new = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-lulu-track ='cart-continue-shopping-cta']")))
shop_new.click()
time.sleep(1.5)
driver.save_screenshot("women_checkbox_auto_selected.jpg")






time.sleep(5)
driver.quit()

