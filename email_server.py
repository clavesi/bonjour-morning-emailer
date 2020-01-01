import smtplib, ssl, settings
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import date

# Email body text
email_html = open('email.html') # Open html file
email_body = email_html.read() # Read html
filename = 'pfst.jpg' # Files to attach to email

# Configurating user's info
msg = MIMEMultipart()
msg['To'] = formataddr((settings.RECEIVER_NAME, settings.RECEIVER_EMAIL))
msg['From'] = formataddr((settings.SENDER_NAME, settings.SENDER_EMAIL))
msg['Subject'] = f'Today is {date.today().strftime("%A, %B %d, %Y")}'
msg.attach(MIMEText(email_body, 'html')) # Body is the html file

# Attaches file to email
try:
    #Open PDF file in binary mode
    with open(filename, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        'Content-Disposition',
        f'attachment; filename= {filename}',
    )

    msg.attach(part)

except Exception as e:
    print(f'Oh no! We didn\'t find the attachment!\n{e}')

# Sends email
try:
    # Creating a SMTP session | use 587 with TLS, 465 SSL and 25
    server = smtplib.SMTP('smtp.gmail.com', 587)
    # Encrypts the email
    context = ssl.create_default_context()
    server.starttls(context=context)
    # We log in into our Google account
    server.login(settings.SENDER_EMAIL, settings.PASSWORD)
    # Sending email from sender, to receiver with the email body
    server.sendmail(settings.SENDER_EMAIL, settings.RECEIVER_EMAIL, msg.as_string())
    print('Email sent!')
except Exception as e:
    print(f'Oh no! Something bad happened!\n{e}')
finally:
    print('Closing the server...')
    server.quit()