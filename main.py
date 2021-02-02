"""
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Dafa"
__github__ = "https://github.com/daptheHuman"
__copyright__ = "Copyright 2021, daptheHuman"
__credits__ = ["daptheHuman"]
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "1.0.0"

# Created by Dafa-PC at 14/01/2021
# !/usr/bin/env python

# code{}
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from profiles import CHROME_USER_PROFILES
from profiles import username  # import profiles
import time


# open the browser (chrome)
options = webdriver.ChromeOptions()
options.add_argument(CHROME_USER_PROFILES)

driver = webdriver.Chrome(executable_path=r'C:/Users/{}/Downloads/chromedriver/chromedriver.exe'.format(username),
                          options=options)
driver.maximize_window()
driver.get("https://web.whatsapp.com/")
wait = WebDriverWait(driver, 20)


# QR SCAN
print("SCAN BARCODE, Click Enter When You Done.")
time.sleep(10)
driver.minimize_window()
input()

# LOOP DATA
repeat = True
while repeat:
    names = input('enter the name of user ')
    msg = input('enter your message ')
    amount = int(input("enter the amount "))
    time.sleep(3)

    cntct_box_search = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="side"]/div[1]/div/label/div/div[2]')))
    cntct_box_search.click()
    cntct_box_search.send_keys(names)
    time.sleep(5)
    print("contact found!")  # contact finder
    time.sleep(2)

    selected_contact = wait.until(
        EC.visibility_of_element_located((By.XPATH, '//span[@title = "{}"]'.format(names.title()))))
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
    resend = input('send another messages?  ' '(Y/N)').lower()
    while resend not in ["y", "n"]:
        print("ONLY Y/N")
        resend = input('send another messages?  (Y/N)').lower()
    if resend.lower() == "y":
        repeat = True
    else:
        repeat = False
