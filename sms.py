
# import smtplib

# # Sender's email credentials
# sender_email = 'elertsms@gmail.com'
# sender_password = 'frtvmacnyfvtovnn'

# # Recipient's phone number and carrier's email-to-SMS gateway
# recipient_phone_number = '8571994476'
# carrier_gateway = {
#     'AT&T': 'gateway.sms77.io',
#     'Verizon': 'vtext.com',
#     'T-Mobile': 'tmomail.net',
#     # Add more carriers and gateways here
# }

# # Choose the recipient's carrier
# recipient_carrier = 'AT&T'

# # Compose the SMS message
# sms_message = "Hello from Python using email-to-SMS!"

# # Create the email message
# subject = ''
# body = sms_message
# msg = f"Subject: {subject}\n\n{body}"

# # Establish a connection to Gmail's SMTP server
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()

# # Log in to the Gmail account
# server.login(sender_email, sender_password)

# # Send the email-to-SMS
# server.sendmail(sender_email, f"{recipient_phone_number}@{carrier_gateway[recipient_carrier]}", msg)

# # Close the connection
# server.quit()

# print("SMS sent successfully!")


import requests

# Replace with your sms77 API key
api_key = 'your api'

# Set up the API endpoint URL
url = 'https://gateway.sms77.io/api/sms'

# Set the recipient's phone number and message content
recipient = 'sms no'
message = 'This is a test message from the sms77 API.'

# Construct the request payload
payload = {
    'to': recipient,
    'text': message,
    'from': 'gulabsp',  # Replace with your sender name
    'type': 'direct',      # You can also use 'quality' for better delivery
    'key': api_key,
}

# Send the POST request to the API
response = requests.post(url, data=payload)

# Check the response
if response.status_code == 200:
    print('SMS sent successfully!', response)
else:
    print('Failed to send SMS. Response:', response.text)






# import requests
# resp = requests.post('https://textbelt.com/text', {
#   'phone': '',
#   'message': 'Hello world',
#   'key': 'textbelt',
# })
# print(resp.json())











# import requests

# url = "https://www.fast2sms.com/dev/bulkV2"

# querystring = {"authorization":"FPDv4wndutpgU1ImNCycYTaxfl0i9h37OkjZWGeSqXzQ2rHbJMSsQGEwvT8clnPFfIrBJ39g5eC0zRuO","message":"This is test message","language":"english","route":"q","numbers":"8571994476"}

# headers = {
#     'cache-control': "no-cache"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)


