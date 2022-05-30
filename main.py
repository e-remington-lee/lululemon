from WebDriver.WebBot import WebBot
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


import time
def main():
    browser, wait = WebBot().create_browsers()
    navigation = Navigation()
    browser.get('https://shop.lululemon.com/c/men-pants/_/N-1z140vfZ1z140uoZ7ub')
    navigation.navigate_to_bottom(browser, wait)
    time.sleep(1)
    while not navigation.at_bottom(browser, wait):
        navigation.navigate_to_bottom(browser, wait)
        navigation.click_button(browser, wait, '//*[@id="main-content"]/div/section/div/div[2]/button/div/span')
    time.sleep(5)

class Navigation:
    def __init__(self) -> None:
        self.item_count_xpath = '//*[@id="main-content"]/div/section/div/div[2]/p'
        self.more_items_button_xpath = '//*[@id="main-content"]/div/section/div/div[2]/button/div/span'

    def navigate_to_bottom(self, browser, wait):
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    
    def at_bottom(self, browser, wait):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, self.item_count_xpath)))
        text = element.text
        print(text)
        numbers = re.findall('[0-9]+', text)
        if len(numbers) > 1:
            if numbers[1] == numbers[0]:
                return True
        return False

    def click_button(self, browser, wait, button_xpath):
        element = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
        element.click()




'''
states

1. get to webpage
2. navigate to product offering
3. find sales items
3a. navigate to bottom
4a. 

'''


if __name__=="__main__":
    main()

