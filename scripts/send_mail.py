# mime stands for multipurpose internet mail extension
# ==> pass
from email.mime import multipart 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage # to accomodate image attachment
from email import encoders


# defining a function to send a mail with attachment (picture)

def send_mail(uname,pwd,text="Gold rate today!!", subject="Gold rate today",from_email= None,to_emails=None, html=None,attachment=None,):
    assert isinstance(to_emails, list)
    msg = MIMEMultipart()
    msg['From'] = str(from_email)
    msg['To'] = ", ".join(str(to_emails))
    msg['Subject'] = subject

    text = "Grettings!! Find Today's gold rate in the attachment"

    msg.attach(MIMEText(text, 'plain'))

    with open("gold.csv",'rb') as file:

        msg.attach(MIMEApplication(file.read(), Name="goldrate.csv"))


    server = smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.ehlo()
    server.starttls()
    server.login(uname, pwd)
    server.sendmail(from_email,list(to_emails),msg.as_string())
    server.quit() # quits the server

