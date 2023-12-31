 # Python Script to Send Emails Using SMTP and Gmail

This Python script allows you to send emails using the Simple Mail Transfer Protocol (SMTP) and your Gmail account. It provides a user-friendly interface to input the sender's email address, recipient's email address, email subject, and email message. The script then establishes a secure connection with Gmail's SMTP server, authenticates using your Gmail credentials, and sends the email.

## Step-by-Step Explanation of the Code

### 1. Importing the smtplib Module

```python
import smtplib
```

The `smtplib` module provides an easy-to-use interface for sending emails using SMTP. It handles the low-level details of establishing a connection with the SMTP server, authenticating with your credentials, and sending the email.

### 2. Defining Sender and Receiver Email Addresses

```python
sender_email = input('Enter the sender email:-\n')
receiver_email = input('Enter the recipient email:-\n')
```

These lines prompt the user to enter the sender's email address and the recipient's email address. The input is stored in the `sender_email` and `receiver_email` variables, respectively.

### 3. Defining Email Subject and Message

```python
subject = input('Enter your Subject:-\n')
message = input('Enter your message:-\n')
```

These lines prompt the user to enter the email subject and the email message. The input is stored in the `subject` and `message` variables, respectively.

### 4. Establishing a Secure SMTP Connection

```python
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
```

This line establishes a secure connection with Gmail's SMTP server using the `smtplib.SMTP_SSL()` function. The `smtp.gmail.com` argument specifies the hostname of the SMTP server, and the `465` argument specifies the port number. The `with` statement ensures that the connection is automatically closed when the block of code is finished executing.

### 5. Authenticating with Gmail Credentials

```python
server.login("vs299901@gmail.com", "mgjnbeufgnocqgon")
```

This line authenticates with Gmail's SMTP server using the `login()` method. The first argument is your Gmail username (in this case, `vs

