import smtplib

# Define sender and receiver email addresses
sender_email = input('Enter the sender email:-\n')
receiver_email = input('Enter the recipient email:-\n')

print("-----------------Email body----------------------")
# Define email subject and message
subject = input('Enter your Subject:-\n')
message = input('Enter your message:-\n')
print('----------------Sending---------------------------')
# Create a secure SMTP connection with your Gmail server
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    # Login with your Gmail credentials
    server.login("vs299901@gmail.com", "mgjnbeufgnocqgon")
    # Send the email
    server.sendmail(sender_email, receiver_email, f"Subject: {subject}\n\n{message}")

print("Email sent successfully!")
