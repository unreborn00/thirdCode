import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

#option = webdriver.ChromeOptions()
#option.add_argument()
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("https://react-shopping-cart-67954.firebaseapp.com/")
driver.maximize_window()

#Get all product names
names = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "p[class='sc-124al1g-4 eeXMBo']")))
add_to_cart = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[normalize-space()='Add to cart']")))
close_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[class='sc-1h98xa9-0 gFkyvN']")))
for name,button in zip(names,add_to_cart):
    button.click()
    close_button.click()
    time.sleep(2)
    print(f"{name.text.strip()} is added to cart")
