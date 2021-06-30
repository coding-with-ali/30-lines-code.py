from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup



#####################################Requierd Data From the User #################
filename="emails.txt"
subjecttext="sub"
messagefile='test.html'


# filename = input("File Name in the Current Directory that contain Emails:")
# subjecttext=input("Enter the Subject of Your Message:")
# messagefile=input("Please enter the Html file name that contain the message :")



######################################### Reading the HtTML########################
with open(messagefile,"r") as file:
    filedata=file.read()
    soup = BeautifulSoup(filedata,features="html.parser")
    html=soup


######################################## READING THE EMAILS ##########################
with open(filename,"r") as file:
    allemails=file.readlines();


##########################################SETTNG UP BOT ###############################
PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://ferozo.email/?_task=mail&_mbox=INBOX")


############################################LOCATING ELEMENTS ON THE PAGE##############


##################USERNAME#########################
try:
    email = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "rcmloginuser"))
    )
    email.send_keys("myclient.ferozo.com")
    email.send_keys(Keys.RETURN)

finally:
    pass


#################PASSWORD#########################
try:
    password = ment = WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.ID, "rcmloginpwd"))
    )
    password.send_keys("1Mpa*w20oF")
    password.send_keys(Keys.RETURN)
finally:
    pass



def repeatt(email):
    try:
        compose = ment = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.ID, "rcmbtn110"))
        )
        compose.click()

    finally:
        pass
    try:
        to_email_list = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.ID, "_to"))
        )
        to_email_list.send_keys(email)
        subject = driver.find_element_by_id("compose-subject")
        subject.send_keys(subjecttext)
        import time
        time.sleep(1)

        testhtml = f"""{html}"""
        testhtml = testhtml.replace("\n", " ")

        composeframe = driver.find_element_by_id("composebody_ifr")
        driver.switch_to.frame(composeframe)
        print("i am in frame")

        nowhtml = driver.find_element_by_tag_name("html")
        nowhtml.click()
        driver.execute_script(f"arguments[0].innerHTML = '{testhtml}'", nowhtml)

        driver.switch_to_default_content()

        send_btn = driver.find_element_by_id("rcmbtn111")
        send_btn.click()


    finally:
        pass

import time
with open(filename,"r") as file:
    for email in file.readlines():
        repeatt(email)
        time.sleep(7)
