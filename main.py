import time

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
ua = UserAgent()
userAgent = ua.random
print(userAgent)

options.add_argument(f'user-agent={userAgent}')
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path="F:/chromedriver.exe", options=options)

driver.set_window_size(920, 685)

url = "https://ecf-train.nvb.uscourts.gov/cgi-bin/Dispatch.pl?caseupld"
driver.get(url)
driver.find_element(By.ID, "loginForm:loginName").send_keys("davkrieg")
driver.find_element(By.ID, "loginForm:password").send_keys("Whited0g#")
driver.find_element(By.ID, "loginForm:clientCode").send_keys("anycode")
driver.find_element(By.ID, "loginForm:fbtnLogin").click()
time.sleep(2)
driver.find_element(By.ID,"regmsgPopup:bpmContinue").click()
driver.find_element(By.CLASS_NAME,"ui-chkbox-box").click()
driver.find_element(By.ID,"regmsg:bpmConfirm").click()
driver.implicitly_wait(10)
driver.find_element(By.NAME,"case_1").send_keys("F:/chromedriver.exe")
driver.find_element(By.NAME,"file_1").send_keys("F:/chromedriver.exe")
driver.find_element(By.NAME,"file_1_MTX").send_keys("F:/chromedriver.exe")
driver.find_element(By.NAME,"configured_file_0").send_keys("F:/chromedriver.exe")
driver.find_element(By.NAME,"configured_file_1").send_keys("F:/chromedriver.exe")
driver.find_element(By.NAME,"button1").click()