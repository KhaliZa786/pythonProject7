from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://www.ozon.ru/')
browser.find_element(By.XPATH, '//*[@id="layoutPage"]/div[1]/header/div[2]/div/div/ul/li[2]/a').click()


browser.get('https://www.ozon.ru/')
browser.find_element(By.XPATH, '//*[@id="stickyHeader"]/div[3]/div/div[2]/form/div[1]/div[2]/input[1]').click()
browser.find_element(By.XPATH,'//*[@id="stickyHeader"]/div[3]/div/div[2]/form/div[1]/div[2]/input[1]').send_keys('диван')
browser.find_element(By.XPATH, '//*[@id="stickyHeader"]/div[3]/div/div/form/div[2]/button/span/svg').click()

browser.get('https://www.ozon.ru/')
browser.find_element(By.XPATH,'//*[@id="stickyHeader"]/div[2]/div/div/button/span/span').click()
browser.find_element(By.XPATH, '//*[@id="7500"]/span)    //*[@id="7500"]/span').click()

