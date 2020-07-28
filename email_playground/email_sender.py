import sys
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path # similar to os.path

receiver = sys.argv[1]
html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = <Senders Name>
email['to'] = <emailAddress>
email['subject'] = 'You won 1,000,000$'
email.set_content(html.substitute(name = receiver), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls() # encryption mechanism to connect
	smtp.login(<emailAddress>, <password>) # login credentials
	smtp.send_message(email)
	print('All good')
