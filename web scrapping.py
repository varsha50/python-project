import requests  # this is used to make the perfect that connections between the URls that to call in the function
import re  # this is used to get remove the commas
from bs4 import BeautifulSoup  # used for the web extraction
import smtplib  # this is the library used to make the connection

URL = 'https://www.amazon.in/ZenBook-UX334FL-A7622TS-13-3-inch-MS-Office-Graphics/dp/B07YSJ3676/ref=sr_1_11?keywords=asus+zenbook+ultra+slim+laptop&qid=1580234403&sr=8-11'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    # this price is in the string that should we want to change
    # in the intger or the float value of the given function
    converted_price = int(re.sub("[ ,]", "", price[1:10]))
    if (converted_price < 110000):
        send_mail()

    print(title.strip())

    print(converted_price)


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()  # this is used to make the connection to server from our progrm to gmail server that is needed in the function of the given program
    server.starttls()  # this is used to start the connection in the list
    server.login("kingarya1020304050@gmail.com", 'King@123')
    subject = 'price has been fall down please purchase fastly '
    body = 'check the amazon link https://www.amazon.in/ZenBook-UX334FL-A7622TS-13-3-inch-MS-Office-Graphics/dp/B07YSJ3676/ref=sr_1_11?keywords=asus+zenbook+ultra+slim+laptop&qid=1580234403&sr=8-11'
    msg = f"Subject:{subject}\n\n{body}"
    server.sendmail('kingarya1020304050@gmail.com',
                    'hksin70@gmail.com',
                    msg)
    print("YOUR EMAIL HAS BEEN SENT IN YOUR LOCATION")
    server.quit()


check_price()