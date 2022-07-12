import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
@pytest.fixture()
def test_setup():
 global driver
 driver = webdriver.Chrome('chromedriver.exe')
 driver.implicitly_wait(20)
 driver.maximize_window()
 yield
 driver.close()
 driver.quit()

def test_sample(test_setup):
    driver.get('https://www.kayak.com')
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[1]/div[1]/div/div[1]/div/div/section[2]/div[2]/div/div/div/div/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[1]/div[1]/div/div[1]/div/div/section[2]/div[2]/div/div/div/div/div[1]/div[2]/div/div[1]/div/div/input').click()
    time.sleep(2)
    #diparture airport place
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[1]/div[1]/div/div[1]/div/div/section[2]/div[2]/div/div/div/div/div[1]/div[2]/div/div[1]/div/div/input').send_keys("New York")
    time.sleep(2)
    #Arrival airport
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[1]/div[1]/div/div[1]/div/div/section[2]/div[2]/div/div/div/div/div[1]/div[2]/div/div[3]/div/div/input').click()
    #Arrival airport place
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[1]/div[1]/div/div[1]/div/div/section[2]/div[2]/div/div/div/div/div[1]/div[2]/div/div[3]/div/div/input').send_keys("Alaska")
    time.sleep(2)
    #Departure date
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[1]/div[1]/div/div[1]/div/div/section[2]/div[2]/div/div/div/div/div[1]/div[2]/div/div[4]/div/div/div/div[1]/span/span[2]').click()
    time.sleep(2)
    # Arrival date
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[1]/div[1]/div/div[1]/div/div/section[2]/div[2]/div/div/div/div/div[1]/div[2]/div/div[4]/div/div/div/div[3]/span').click()
   # search
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[1]/div[1]/div/div[1]/div/div/section[2]/div[2]/div/div/div/div/div[1]/div[2]/div/div[5]').click()
    time.sleep(5)
    #display departure and arrival page
    elem = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/div[2]/div[2]/div[1]/div/div/div[2]/canvas')
    elem.is_displayed()
    time.sleep(5)