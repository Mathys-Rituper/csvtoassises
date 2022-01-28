# from pyvirtualdisplay import Display
from math import floor

from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ProtonMail does not provide a free API... Therefore, scrapping time, this is the whole purpose of the module :/

def connect_driver(email, password):
    try:
        # display = Display(visible=0, size=(1920, 1080))   # Used to create a virtual display to be able to run selenium in a terminal without GUI
        # display.start()
        print("Initiating webdriver...")
        driver = webdriver.Firefox()
        print("Connecting to ProtonMail client...")
        driver.get('https://mail.protonmail.com/login')
        sleep(5)
        driver.find_element_by_id('username').send_keys(email)
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_class_name("button-henlo").click()
        print("clicked on login")
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.CLASS_NAME, "button-large")))
        print(f"Successful connexion to {email}.")
        # return (driver,display)
        return (driver)
    except Exception as err:
        driver.quit()
        # display.stop()
        print('\nError while initiating protonmail connexion!')
        status = (str(err), 'Error Origin: Proton Mail Script')
        print(status)
        del err
        del status
        del driver
        # del display
        raise err


# def send_email(email_to, email_subject, email_message,driver,display):
def send_email(email_to, email_subject, email_message, driver):
    try:
        print(f"Sending email to {email_to}...")
        driver.find_element_by_class_name("button-large").click()
        sleep(3)
        driver.switch_to_active_element().send_keys(email_to.strip() + Keys.ENTER + Keys.TAB + Keys.TAB)
        sleep(2)
        driver.switch_to_active_element().send_keys(email_subject + Keys.TAB + Keys.TAB)
        sleep(2)
        length = len(email_message)
        driver.switch_to_active_element().send_keys(email_message[0:floor(length / 2)])
        sleep(2)
        driver.switch_to_active_element().send_keys(email_message[floor((length / 2)):length - 1])
        sleep(1)
        driver.find_element_by_class_name("composer-send-button").click()
        print('E-mail sent.')
        sleep(3)
        del email_subject
        del email_message
    except Exception as err:
        driver.quit()
        # display.stop()
        print('\nError Occurred while sending e-mail!!')
        print(f"\nDid not send email {email_subject} to {email_to}.")
        status = (str(err), 'Error Origin: Proton Mail Script')
        print(status)
        del err
        del status
        del driver
        raise err
        # del display


# def kill_driver(driver ,display):
def kill_driver(driver):
    driver.quit()
    # display.stop()
    del driver
    # del display
