# ==========================================
# Program : Simple Gmail Mail Sender
# Author  : Raviraj Aade 
# Purpose : Send mail using Python SMTP
# ==========================================

import smtplib
from email.message import EmailMessage
import schedule
import time


# ------------------------------------------------
# Function : send_mail
# Description : Sends email using Gmail SMTP server
# ------------------------------------------------
def send_mail(sender, app_password, receiver, subject, body) :
    # create Email Object 
    msg = EmailMessage()
    
    # Set mail header
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    
    # Add mail body
    msg.set_content(body)
    
    # Create SMTP SSL Connection Manually
    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)
    
    # Login using Gmail + App Password
    smtp.login(sender,app_password)
    
    # Send the email
    smtp.send_message(msg)
    
    print("Mail send successfully")
    # Close Connection Manually
    smtp.quit()

# ------------------------------------------------
# Function : main
# Description : Driver code
# ------------------------------------------------

def main():
    sender_email = "ravirajade2@gmail.com"
    
    app_passward = "waiy ebld ffyb lqxv"
    
    receive_email = "ravirajaade15@gmail.com" 
    
    subject = "Test mail from python script"
    
    body = """Jay Ganesh,
    
        This is a test email sent using  Python.
        Regards,
        Raviraj Aade
    """
    
    # send_mail(sender_email,app_passward, receive_email,subject, body)
    
    schedule.every(1).minute.do(send_mail,sender_email,app_passward,receive_email,subject,body)
    # print("Mail send successfully")

    while True:
        schedule.run_pending()
        time.sleep(1)
        
        

if __name__ == "__main__":
    main()
    