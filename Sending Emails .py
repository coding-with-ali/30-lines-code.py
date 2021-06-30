import os
import smtplib
import time
import concurrent.futures

t1=time.perf_counter()

# set the email and passowrd either in the path
# email=os.environ.get('USER_EMAIL')
# password=os.environ.get('USER_PASSWORD')


# to make it happen allow the less secure app to access your account
# https://myaccount.google.com/lesssecureapps

i=0
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(email, password)

    while True:
        print(i)
        i=i+1

        subject='Hello'
        body=f'hi how are you{i}'

        message=f'Subject: {subject}\n\n {body}'

        smtp.sendmail(email,'Saifurrehmanparwak123@gmail.com',message)
t2=time.perf_counter()
print(t2-t1)

