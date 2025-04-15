
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select

class TestShop:
    def work_func(self):
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 10)
        driver.get("https://react-shopping-cart-67954.firebaseapp.com/")
        driver.maximize_window()

        #Get product names
        product_names = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "p[class='sc-124al1g-4 eeXMBo']")))
        for name in product_names:
            print(name.text)
        

