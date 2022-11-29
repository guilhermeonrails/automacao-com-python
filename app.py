from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.selenium.dev/selenium/web/web-form.html')
campo_de_texto = driver.find_element(By.ID, 'my-text-id')
sleep(0.5)
campo_de_texto.send_keys('Caroline Martins')
sleep(0.5)
campo_text_area = driver.find_element(By.XPATH, '/html/body/main/div/form/div/div[1]/label[3]/textarea')
campo_text_area.send_keys('Palestra de automação com Python')
botao = driver.find_element(By.XPATH, '/html/body/main/div/form/div/div[2]/button')
sleep(2)
botao.click()
sleep(2)

driver.quit()