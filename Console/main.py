## @file main.py
 # @author Anando Zaman
 # @brief Main Program that is used to generate summarized emails
 # @date May 16, 2020
 # @details This is the main file that will be used to control the other files and run the program!
 # @details Uses Text_Summarizer.py & IMAP.py files


# Note: Store your email credentials in a file called credentials.txt
# The first line containing email address, second line containing password
# This is needed for authentication in order to extract email data

from IMAP import IMAP
from Text_Summarizer import summarizer

# Read credentials file
file = open("credentials.txt")
user = file.readline()
pass_ = file.readline()
file.close()

# email object
host = 'imap.gmail.com'
email = IMAP(host,user,pass_)
email.authenticate()

'''Specify number of recent emails to fetch'''
fetch_emails = 5
# Fetch the emails
email.fetch_data(fetch_emails)

'''FileWriter'''
file = open("./Output/EmailSummary.txt", "a")

# Summarize these emails
for i in range(fetch_emails):
    subject_title = email.email_data[i][0]
    sender = email.email_data[i][1]
    # Number of sentences to summarize to
    num_summary_sentences = 7
    # Execute Text_Summarizer
    summarized_email = summarizer(email.email_data[i][2], num_summary_sentences)
    file.write(subject_title+'\n')
    file.write(sender+'\n')
    file.write(summarized_email+'\n')
    file.write('***********************\n')
    print(subject_title)
    print(sender)
    print(summarized_email)
    print()

file.close()
