from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


options = Options()
ua = UserAgent()
userAgent = ua.random
print(userAgent)

options.add_argument(f'user-agent={userAgent}')
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(executable_path="E:/chromedriver.exe", options=options)

driver.set_window_size(920, 685)

url = "https://train-login.uscourts.gov/csologin/login.jsf?pscCourtId=NVTBK&appurl=https://ecf-train.nvb.uscourts.gov/cgi-bin/login.pl"
driver.get(url)