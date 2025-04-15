import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

class DemoTest:
    def baseCode(self):
        option = webdriver.ChromeOptions()
        option.add_argument("headless")
        driver = webdriver.Chrome(options=option)
        wait = WebDriverWait(driver, 10)
        driver.get("https://v4.practicesoftwaretesting.com/#/")
        driver.maximize_window()
        return driver, wait

    #Selecting value from the filter and clicking on "Hammer" from check box
    def searchSelect(self,driver, wait):
        sel_options = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".form-select")))
        sel_filter = Select(sel_options)
        sel_filter.select_by_value("name,asc")
        hammer_chkbox = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-test='category-3']")))
        hammer_chkbox.click()
        time.sleep(2)
        return driver,wait, hammer_chkbox

    #Click on all hammers, get their name, price, and add them to cart
    def addToCart(self,driver, wait,hammer_chkbox):
        allHammerNames = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h5[class='card-title']")))
        print(len(allHammerNames))
        n = len(allHammerNames)
        try:
            for i in range(n):
                allHammerNames = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h5[class='card-title']")))
                allHammerNames[i].click()
                product_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1[data-test='product-name']"))).text
                product_price = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[aria-label='unit-price']"))).text
                add_to_cart = driver.find_element(By.CSS_SELECTOR, "#btn-add-to-cart")
                add_to_cart.click()
                print(f"{product_name} - {product_price} is added to cart")
                time.sleep(1.5)
                driver.back()
                #Here is a catch, hammer button is cleared on every back button pressed
                #so we need to click hammer check button again
                time.sleep(1.5)
                hammer_chkbox = wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-test='category-3']")))
                hammer_chkbox.click()
                time.sleep(1.5)
        except Exception as e:
            print(f"There is an exception : {e}")
    def quit(self):
        driver.quit()


if __name__ == "__main__":
    dt = DemoTest()
    driver, wait = dt.baseCode()
    hammer_chkbox = dt.searchSelect(driver, wait)
    dt.addToCart(driver, wait, hammer_chkbox)
    dt.quit()





