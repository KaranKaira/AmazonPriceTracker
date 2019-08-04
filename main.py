import requests
from bs4 import BeautifulSoup
import smtplib
import time
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('sender email address', 'password of this sender email address')   

    sub = 'Prices are low !! According to your aukat!!'

    body = 'check this amazon link' + urlamazonssd
    msg = f'Subject: {sub}\n\n{body}'

    server.sendmail('sender email address', 'receiver address',msg)
    server.quit()




urlamazonssd = 'https://www.amazon.in/Samsung-250GB-Internal-Solid-MZ-76E250BW/dp/B079DTMNWC/ref=sr_1_6?keywords=ssd&qid=1563442122&s=gateway&sr=8-6'
header = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
}
def check_price():
    page = requests.get(urlamazonssd , headers = header)

    soup = BeautifulSoup(page.content,'html.parser')              #  html.parser- it let retrieve individual component on page

# print(soup.prettify())

    productTitle = soup.find(id='productTitle').get_text()

    price = soup.find(id='priceblock_ourprice').get_text()


    converted_price = price[2:7]

    print(converted_price)

    if converted_price <= '2,800':
                send_mail()
                print("email sent")
    else:
                print('Price out of range')        # though this else statement is not neccessary



while(True):
    check_price()
    time.sleep(86400)       #checing price every 86400 sec or each day


