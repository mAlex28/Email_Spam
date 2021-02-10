# download the book data from the website
import requests
# calculate word per message
from math import floor
# delay the mail loop
import time
# connect to the email server
import smtplib as smtp
# create the email
from email.message import EmailMessage 

# Import the book data for war and peace

# Send a request to download the book from the Gutenberg Library
book_url = "https://www.gutenberg.org/files/2600/2600-0.txt"
r = requests.get(book_url)

# Remove ascii characters
book_data = r.text.encode('ascii', 'ignore').decode('ascii')

# Split the words of each book into a list of words
word_list = book_data.split(" ")

# Determine the message data
msg_size = floor(len(word_list) / 1000)
final_msg_size = len(word_list) - (msg_size * 999)
print(f"Words per message: {msg_size}\nFinal message size: {final_msg_size}")

# Setup server authentication variables

# Create the email server connection
# 
# SMTP servers used:
#     smtp.gmail.com (port 587 or 465)
#     smtp.office365.com (port 587)
#     smtp.mail.yahoo.com (port 587 or 465)


user = "abcd1@gmail.com"
password = "pass@abcd"
from_address = "abcd@gmail.com"
to_address = "torecipient@gmail.com"
smtp_host = 'smtp.gmail.com'
smtp_port = 587


# Setup email variables
subject = 'War & Peace - Part '
msg_text = ''
start_pos = 0
msg_count = 0


# Create and send email
#   Open a connectionto the mail server
#   Create and send the email messge



# seperate into chunks of 10 emails in order to avoid sending limits (2000 mails per day)
for b in range(20):
    # open the email server connection
    server = smtp.SMTP(host=smtp_host, port=smtp_port)
    server.starttls()
    server.login(user=user, password=password)
    
    # create and send the message
    for i in range(50):
        # check to see if this is the final message, which has a slightly different range
        if msg_count == 1000:
            start_pos = (len(word_list)-final_msg_size)
            msg_text = ' '.join(word_list[start_pos:])
        else:
            start_pos = msg_count * msg_size
            msg_text = ' '.join(word_list[start_pos:start_pos + msg_size])
        
        # create the email message header and set the payload
        msg = EmailMessage()
        msg['From'] = from_address
        msg['To'] = to_address
        msg['Subject'] = subject + str(msg_count+1)
        msg.set_payload(msg_text)
        
        msg_count += 1
        
        # open the email server and send the message
        server.send_message(msg)
        
        '''delay each email by 0.5 seconds to space out the distribution'''
        
        time.sleep(0.5)
        
    # delay each batch by 60 seconds to avoid sending limits
    time.sleep(60)
    
    # close the server
    server.close()





