import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

sender_email_v = 'elertsms@gmail.com'
sender_password_v = 'quuv rnds adlb pcwv'

def send_mail(mailsList, body, subject, image_path):
    # Sender's email credentials
    sender_email = sender_email_v
    sender_password = sender_password_v

    # List of recipient email addresses
    recipient_emails = mailsList

    # Create a MIMEMultipart object to represent the email content
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = ', '.join(recipient_emails)  # Join the email addresses with a comma and space
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Open the image file in binary mode
    with open(image_path, 'rb') as image_file:
        # Create a MIMEImage object
        img = MIMEImage(image_file.read())
        # Add the header to specify the content disposition
        img.add_header('Content-Disposition', f'attachment; filename="{image_path.split("/")[-1]}"')
        # Attach the image to the message
        message.attach(img)

    # Establish a connection to the SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Log in to the email account
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, recipient_emails, message.as_string())

    # Close the connection
    server.quit()

    print("Email sent successfully with image attachment!")

# Example usage:
mailsList = ["gulabpreets01@gmail.com", "gulabpreets.cse@gmail.com"]
body = "This is the email body."
subject = "Email Subject"
image_path = "Unknown/unknown_2024-05-20_01-18-15_0.jpg"
send_mail(mailsList, body, subject, image_path)
