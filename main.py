from datetime import date
from settings import get_password
from get_gold_rate import get_gold_rate
from send_mail import send_mail

uname = 'i51vignesh@gmail.com'
pwd = get_password() # the 16 digit character which we got from myaccounts.google.com

this_day = date.today()
today = this_day.strftime("%d/%m/%Y")

get_gold_rate()
send_mail(uname,pwd,text="Gold rate today man !!", subject="Gold rate "+today,from_email= "i51vignesh@gmail.com",to_emails=["vigneshkathirkamar@gmail.com","ilamathi1996@gmail.com"])
