from scraper import scraper
from send_email import send_email

if __name__ == '__main__':
    x = scraper()
    if x == None:
        print("do nothing")
    else:
        print("sending email")
        send_email(x)
