from selenium import webdriver
import time
from selenium.webdriver import ActionChains
driver=webdriver.Chrome(executable_path="C:\\Users\\Anitha_C_k\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
driver.get("https://www.amazon.in/")
# cookies=driver.get_cookies()
# print(len(cookies))
# print(cookies)
#Adding cookies object
cookie={"name":"mycookies","value":"12345"}
driver.add_cookie(cookie)

# cookies=driver.get_cookies()
# print(len(cookies))
# print(cookies)

#Deleting cookies
driver.delete_cookie("mycookies")
time.sleep(2)
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)

#Deleting all the cookies
driver.delete_all_cookies()
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)
