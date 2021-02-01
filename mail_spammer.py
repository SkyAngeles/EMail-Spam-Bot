import sys
import time
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = "address" # enter email address
EMAIL_PASSWORD = "password" # enter email password
RECEIVER = ["recepient_adress"] # enter recepient address
limit = 10
sentmails = 0
# num = 0
# txt = open(r"path to spam script txt file", "r") # optional feature
# file = txt.readlines()

def update_email_info():
    global msg
    # glonal file
    
    msg = EmailMessage()
    msg['Subject'] = "subject" # enter email subject
    # msg['Subject'] = f"Line {num}"
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ', '.join(RECEIVER)
    msg.set_content("content") # enter email content
    # msg.set_content(file[num])

update_email_info()

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    while True:
        try:
            for a in range(2):
                for i in range(5):
                    smtp.send_message(msg)
                    print("email sent")
                    # num +=1
                    update_email_info()
                    sentmails += 1
                    if sentmails >= limit:
                        # txt.close
                        sys.exit()
                    time.sleep(0.5)
            time.sleep(60)
        except:
            pass
