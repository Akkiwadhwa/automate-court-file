import os
import time

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

dir = f'{str(os.getcwd())}\\'
client_code = input("Enter Client Code: ")
print("Please wait while loging in")
url = "https://ecf-train.nvb.uscourts.gov/cgi-bin/Dispatch.pl?caseupld"

options = Options()
ua = UserAgent()
userAgent = ua.random
# options.add_argument("--headless")
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
    c = input("Enter Y to upload files\A to misc. menu: ").upper()
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
            driver.get_screenshot_as_file(filename=f"{str(round(time.time()))}.png")
        except Exception as e:
            print(e)
        else:
            driver.implicitly_wait(2)
            print("Files uploaded successfully")
    elif c == "A":
        url1 = "https://ecf-train.nvb.uscourts.gov/cgi-bin/Dispatch.pl?misc"
        driver.get(url1)
        driver.find_element(By.ID, "case_number_text_area_0").send_keys("22-70031")
        driver.find_element(By.ID, "case_number_find_button_0").click()
        time.sleep(4)
        driver.find_element(By.NAME, "button1").click()
        l = driver.find_elements(By.CLASS_NAME, "fakeOption")
        for i in l:
            text = i.text
            if text == "Statement of Social Security Number(s) (Must be Docketed Separately)":
                i.click()
        driver.find_element(By.ID, "button1").click()
        select = Select(driver.find_element(By.NAME, "yn"))
        select.select_by_visible_text("No")
        driver.find_element(By.NAME, "button1").click()
        l = driver.find_element(By.NAME, "party_person").find_elements(By.TAG_NAME, "option")
        for i in l:
            text = i.text
            if "[Debtor]" in text:
                i.click()
        driver.find_element(By.NAME, "button1").click()
        driver.find_element(By.NAME, "file_1").send_keys(dir + "a.pdf")
        driver.find_element(By.NAME, "button1").click()
        time.sleep(2)
        driver.find_element(By.NAME, "button1").click()
        time.sleep(2)
        driver.find_element(By.NAME, "button1").click()
        time.sleep(2)
        driver.find_element(By.NAME, "button1").click()
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, "container-close")
        driver.get_screenshot_as_file(filename=f"{str(round(time.time()))}.png")

    else:
        driver.close()
        driver.quit()
        print("Program Exit")
        break
