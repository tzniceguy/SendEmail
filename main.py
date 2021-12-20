from getpass import getpass
import smtplib, ssl


try:
  with smtplib.SMTP('smtp.gmail.com', 587)  as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    email =input('Enter Email: ')
    password= getpass()
    smtp.login(email,password)

    reciever =input('Enter a recepient mail: ')

    SUBJECT = input('Enter the mail Subject: ')

    BODY = input('Enter the email body: ')

    message = f'Subject: {SUBJECT} \n\n body: {BODY}'

    smtp.sendmail(email, reciever, message)
    print('email sent sucessfully')
    smtp.quit()
except Exception as e:
    print(e)



