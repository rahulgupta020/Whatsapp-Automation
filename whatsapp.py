from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver=webdriver.Chrome(ChromeDriverManager("81.0.4044.138").install())
# driver=webdriver.Chrome(ChromeDriverManager().install())
# driver=webdriver.Chrome(executable_path='C:/Users\rahul/.wdm/drivers/chromedriver/81.0.4044.138/win32/chromedriver.exe')

import time

driver.get("https://web.whatsapp.com/")
name = input('Enter the name of user or group : ')
msg = input('Enter your message : ')
count = int(input('Enter the count : '))

input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_39LWd')
# _39LWd
# _2S1VP 
# _3F6QL _2WovP
# _1Plpp

# msg_box.send_keys(msg)
# button = driver.find_element_by_class_name('_35EW6')
# button.click()

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_2S1VP')
    button.click()

# weEq5
# _35EW6












# time.sleep(100)
# driver.close()
# driver.quit()
