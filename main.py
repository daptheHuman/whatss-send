# noinspection
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

# open the browser (chrome)
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 10)

# QR SCAN
print("SCAN BARCODE, Click Enter When You Done.")
time.sleep(7)
driver.minimize_window()
input()

# DATA INPUT
names = input('enter the name of user ')
msg = input('enter your message ')
amount = int(input("enter the amount "))
time.sleep(3)

# LOOP DATA
repeat = True
while repeat:

    cntct_box_search = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]')))
    cntct_box_search.click()
    cntct_box_search.send_keys(names)
    time.sleep(5)
    print("contact found!")  # contact finder
    time.sleep(2)

    selected_contact = driver.find_element_by_xpath('//span[@title = "{}"]'.format(names.title()))
    print('contact selected')  # contact selector
    selected_contact.click()
    time.sleep(2)
    msgbox = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    msgbox.click()  # msgbox click

    # sent the messages for loop (amount)
    for i in range(amount):
        msgbox.send_keys(msg + Keys.ENTER)
        print('Total ' + str(amount) + ' messages has sent!')

    # loop back
    resend = input('send another messages?' 'Y/N?')
    if resend.lower() == "y":
        repeat = True
    elif resend.lower() == 'n':
        repeat = False
    else:
        resend

