import smtplib

from email.message import EmailMessage
def forgotemail(TEXT,tomail):
    msg = EmailMessage()
    msg['Subject'] = 'Forgot your Password'
    msg['From'] = 'yashaswinicv8804@gmail.com'
    msg['To'] = tomail
    msg.set_content('')
    msg.add_alternative(TEXT,subtype='html')


    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login('yashaswinicv8804@gmail.com','dlueuvfazzfonzot')
        smtp.send_message(msg)


def sendgrid(TEXT,email):
    msg = EmailMessage()
    msg['Subject'] = 'Alert!! Monthly Limit Exceeded'
    msg['From'] = 'yashaswinicv8804@gmail.com.com'
    msg['To'] = email
    msg.set_content('')
    msg.add_alternative(TEXT,subtype='html')


    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login('yashaswinicv8804@gmail.com','dlueuvfazzfonzot')
        smtp.send_message(msg)

   
