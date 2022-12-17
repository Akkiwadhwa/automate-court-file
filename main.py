import datetime
import os
import time
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

time1 = f"{str(round(time.time()))}.png"
print(time1)
dir = f'{str(os.getcwd())}\\'
client_code = input("Enter Client Code: ")
print("Please wait while loging in")
url = "https://ecf-train.nvb.uscourts.gov/cgi-bin/Dispatch.pl?caseupld"

options = Options()
ua = UserAgent()
userAgent = ua.random
options.add_argument("--headless")
options.add_argument(f'user-agent={userAgent}')
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
try:
    driver.get(url)
    driver.find_element(By.ID, "loginForm:loginName").send_keys("davkrieg")
    driver.find_element(By.ID, "loginForm:password").send_keys("Whited0g#")
    driver.find_element(By.ID, "loginForm:clientCode").send_keys(client_code)
    driver.find_element(By.ID, "loginForm:fbtnLogin").click()
    time.sleep(2)
    driver.find_element(By.ID, "regmsgPopup:bpmContinue").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME, "ui-chkbox-box").click()
    time.sleep(2)
    driver.find_element(By.ID, "regmsg:bpmConfirm").click()
except Exception as e:
    print(e)
else:
    print("Logged-in successfully")

while True:
    c = input("Enter Y to upload files: ").upper()
    if c == "Y":
        case_info = input("Case information (.txt): ")
        petition = input("Case petition (.pdf): ")
        list_creditors = input("List_creditors (.txt): ")
        chapter_13 = input("Chapter_13 (.pdf): ")
        cert_for_credit_counsel = input("Cert_for_credit_counsel (.pdf): ")
        print("Please wait while uploading files")
        try:
            driver.get(url)
            time.sleep(2)
            driver.find_element(By.NAME, "case_1").send_keys(dir + case_info)
            driver.find_element(By.NAME, "file_1").send_keys(dir + petition)
            driver.find_element(By.NAME, "file_1_MTX").send_keys(dir + list_creditors)
            driver.find_element(By.NAME, "configured_file_0").send_keys(dir + chapter_13)
            driver.find_element(By.NAME, "configured_file_1").send_keys(dir + cert_for_credit_counsel)
            driver.find_element(By.NAME, "button1").click()
            driver.get_screenshot_as_file(filename=time1)
        except Exception as e:
            print(e)
        else:
            driver.implicitly_wait(2)
            print("Files uploaded successfully")
    else:
        driver.close()
        driver.quit()
        print("Program Exit")
        break
