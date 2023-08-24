from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time

# # Set up the proxy
# proxy = Proxy()
# proxy.proxy_type = ProxyType.MANUAL
# proxy.http_proxy = "IP_ADDRESS:PORT"  # Replace with your proxy details
# proxy.ssl_proxy = "IP_ADDRESS:PORT"   # Replace with your proxy details

# # Set up the browser with the proxy
# capabilities = webdriver.DesiredCapabilities.FIREFOX.copy()
# proxy.add_to_capabilities(capabilities)
# browser = webdriver.Firefox(desired_capabilities=capabilities)
# wait = WebDriverWait(browser, 10)
# Set up the browser
browser = webdriver.Firefox()
wait = WebDriverWait(browser, 10)

# Configuration
frequency = 30
mobile_number = "9445007578"
sms_interval = 35

# Open the website
browser.get('https://www.rummycircle.com/baf.html?11141705&baf_promo_code=FUZZ')

# Find the element to enter the number and send forgot password request
number = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mobile_input"]')))
number.send_keys(mobile_number)

forgot = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="getStarted"]')))
forgot.click()

time.sleep(35)
# Send SMS multiple times
for _ in range(frequency):
    select = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="get_opt_call_btn"]')))
    select.click()
    time.sleep(sms_interval)

# Close the browser
browser.quit()


# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# # Set up the browser
# browser = webdriver.Firefox()
# wait = WebDriverWait(browser, 10)

# # Get input from the user
# mobile_number = input("Enter your mobile number: ")
# frequency = int(input("Enter the number of SMS to send: "))
# sms_interval = 35

# # Open the website
# browser.get('https://www.rummycircle.com/baf.html?11141705&baf_promo_code=FUZZ')

# # Find the element to enter the number and send forgot password request
# number = mber.send_keys(mobile_number)

# forgot = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="getStarted"]')))
# forgot.click()

# time.sleep(35)

# # Send SMS multiple times
# for _ in range(frequency):
#     select = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="get_opt_call_btn"]')))
#     select.click()
#     time.sleep(sms_interval)

# # Close the browser
# browser.quit()
