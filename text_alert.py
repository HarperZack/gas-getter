import smtplib
import email
from datetime import datetime
import restricted


# Change from and to based on email address and receiving phone.
# Carrier specific suffix must be attached to end of phone number.
def send_alert(store, price):
    subject = f'The cheapest gas is {price}. '
    message = f'{store} has gas for {price}'
    send_text(subject=subject, body=message)


def send_text(subject, body):
    msg = email.message.EmailMessage()

    msg["Subject"] = subject
    msg["From"] = restricted.MY_EMAIL
    msg["To"] = restricted.MY_PHONE
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(restricted.MY_EMAIL, restricted.APP_PASS)
        now = datetime.now().strftime('%I:%M:%S %p')

        print(f'Sending alert at {now}.')
        smtp.send_message(msg)
        print('Alert sent')