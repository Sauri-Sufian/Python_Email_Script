import smtplib
import  sys
from email.message import EmailMessage
from string import  Template
from pathlib import  Path
html = Template(Path('index.html').read_text())
email = EmailMessage()

email['from']='House of Dollars '
email['to']=sys.argv[1]
email['subject']='You won 1,000,000 dollars!'
name1= sys.argv[2]
email.set_content(html.substitute(name=name1),'html')


with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('5trawhat5.u5a@gmail.com','Siam1998')
    smtp.send_message(email)
    print("Successfully done !")
