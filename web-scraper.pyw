from bs4 import BeautifulSoup as bs
import requests
import time
import winsound as sound
import smtplib, ssl
from webbrowser import open
from win10toast import ToastNotifier

toaster = ToastNotifier()
toaster.show_toast("Creality sale bot is starting", " ")

sold = 5
#### Checking if it sold ####
url_5_pro = 'https://www.creality3dofficial.com/products/ender-5-pro-3d-printer?variant=31177472409673'
url_3_pro = 'https://www.creality3dofficial.com/products/creality-ender-3-pro-3d-printer?variant=31314964578377'
while True:
    headers = {"User-Agent": "Mozilla/5.0"} 
    pro_5 = requests.get(url_5_pro, headers=headers)
    pro_3 = requests.get(url_3_pro, headers=headers)
    txt_5 = pro_5.text
    txt_3 = pro_3.text
    soup_5 = bs(txt_5, 'lxml')
    soup_3 = bs(txt_3, 'lxml')
    div_5 = soup_5.find_all('div', class_="product-form__item product-form__item--submit")
    div_3 = soup_3.find_all('div', class_="product-form__item product-form__item--submit")

    if 'Sold' in div_5[0].text:
        print("The Ender 5 Pro is still out of stock.")
    else:
        toaster.show_toast("The Ender 5 Pro is on sale!", " ")
        print("The ender 5 pro is on sale")
        open(url_5_pro, new = 1, autoraise = True)
        break

    if 'Sold' in div_3[0].text:
        print("The Ender 3 Pro is also out of stock. \n")
        print(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime()))
        print("Waiting... \n")
        time.sleep(600)
    else:
        sold = 3
        toaster.show_toast("The Ender 3 Pro is on sale!", " ")
        print("The ender 3 pro is on sale!")
        open(url_3_pro, new = 1, autoraise = True)
        break

#### Emailing myself ####

# If using Gmail, enable 2FA and generate an App Password here:
# https://myaccount.google.com/apppasswords

port = 465
password = ""
sender_email = ""
receiver_email = ""

# Creating the message
SUBJECT_3 = "The Ender 3 Pro is in stock!!"
TEXT_3 = """    Go check it out:
    https://www.creality3dofficial.com/products/creality-ender-3-pro-3d-printer?variant=31314964578377
    """

SUBJECT_5 = "The Ender 5 Pro is in stock!!"
TEXT_5 = """    Go check it out:
    https://www.creality3dofficial.com/products/ender-5-pro-3d-printer?variant=31177472409673
    """

if sold == 5:
    message = 'Subject: {}\n\n{}'.format(SUBJECT_5, TEXT_5)
else:
    message = 'Subject: {}\n\n{}'.format(SUBJECT_3, TEXT_3)
# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
print("The email has been sent")
#### Playing a sound out of the speakers ####
print("Ringing the bells... \n")
dur = 1150
for _ in range(0, 3):
    for i in range(1, 11):
        if i % 2 ==0:
            sound.Beep(500, dur)
        else:
            sound.Beep(950, dur)

print("GO BUY THAT PRINTER!!")



