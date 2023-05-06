from selenium import webdriver
from selenium.webdriver.common.by import By
#import action to hover mouse
from selenium.webdriver.common.action_chains import ActionChains
import time
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://all-free-download.com/free-photos/test-image.html")
time.sleep(5)
apple = driver.find_element(by=By.XPATH, value='//*[@id="g-517290"]/div[1]/a/img')
assert apple.is_displayed,"Apple is not visible"
action = ActionChains(driver)
action.move_to_element(apple)
time.sleep(5)
download = driver.find_element(by=By.XPATH, value='//*[@id="g-517290"]/div[3]/a/img')
assert download.is_displayed,"download is not- visible"
download.click()
time.sleep(20)
driver.quit()
print ("Succesfully downloaded")
