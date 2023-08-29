from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def send_sms(browser, mobile_number, frequency, sms_interval):
    wait = WebDriverWait(browser, 10)
    browser.get('https://proxyium.com/')

    select = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div/div[2]/div/form/div[1]/div/span[2]')))
    select.click()

    url = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="unique-form-control"]')))
    url.send_keys('https://www.rummycircle.com/baf.html?11141705&baf_promo_code=FUZZ')

    go = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="unique-btn-blue"]')))
    go.click()

    # browser.get('https://www.rummycircle.com/baf.html?11141705&baf_promo_code=FUZZ')

    number = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mobile_input"]')))
    number.send_keys(mobile_number)

    forgot = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="getStarted"]')))
    forgot.click()

    time.sleep(35)

    for _ in range(frequency):
        select = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="get_opt_call_btn"]')))
        select.click()
        time.sleep(sms_interval)

def main():
    mobile_number = input("Enter your mobile number: ")
    frequency = int(input("Enter the number of SMS to send: "))
    sms_interval = 35

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # Set headless mode
    browser = webdriver.Chrome(options=chrome_options)
    
    send_sms(browser, mobile_number, frequency, sms_interval)
    browser.quit()

if __name__ == "__main__":
    main()
