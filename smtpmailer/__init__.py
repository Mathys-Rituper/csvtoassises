import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv


class Mailer:
    """
    A SMTP mailer that enables you to send emails and attachements.
    """

    def __init__(self, server, port, email_address, password):
        """
        Initialize the mailer.
        :param server: The SMTP server.
        :param port: The SMTP port.
        :param email_address: The email address of the sender.
        :param token: The SMTP token.
        """

        self.server = server
        self.port = port
        self.email_address = email_address
        self.password = password

        print("Initializing SMTP client...")
        self.smtp = smtplib.SMTP(self.server, self.port)
        print("SMTP client initialized.")
        print("starting ehlo")
        self.smtp.ehlo()
        print("ehlo done")
        if self.server != 'localhost':
            print("starting starttls")
            self.smtp.starttls()
            print("starttls done")
            print("starting ehlo")
            self.smtp.ehlo()
            print("ehlo done")
            print("starting login")
            self.smtp.login(self.email_address, self.password)
            print("login done")
        print("SMTP client initiated.")

    def close(self):
        """
        Close and delete the mailer.
        """

        self.smtp.close()

    def send_email(self, recipient, subject, body, attachments=None):
        """
        Send an email.
        :param recipient: The email address of the recipient.
        :param subject: The subject of the email.
        :param body: The body of the email.
        :param attachments: A list of attachments.
        """
        print(f"Sending email {subject  } to {recipient}...")
        msg = MIMEMultipart()

        msg['From'] = self.email_address
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain', 'utf-8'))

        if attachments is not None:
            for attachment in attachments:
                with open(attachment, 'rb') as f:
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload(f.read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition', 'attachment; filename="{}"'.format(attachment))
                    msg.attach(part)

        self.smtp.send_message(msg)
        print("Email sent.")


if __name__ == '__main__':
    load_dotenv()
    mail_server = os.getenv('EMAIL_HOST')
    mail_port = os.getenv('EMAIL_PORT')
    mail_address = os.getenv('EMAIL_ADDRESS')
    password = os.getenv('EMAIL_PASSWORD')

    print("initiating email client...")
    mailer = Mailer(mail_server, mail_port, mail_address, password)
    print("email client initiated.")

    print("Sending test email...")
    mailer.send_email("fffgrenoble@riseup.net", "Test email", "test message")
    print("Test email sent.")

    mailer.close()
