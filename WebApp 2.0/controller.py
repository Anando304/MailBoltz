## @file main.py
 # @author Anando Zaman
 # @brief Main Program that is used to generate summarized emails
 # @date May 16, 2020
 # @details This is the main file that will be used to control the other files and run the program!
 # @details Uses Text_Summarizer.py & IMAP.py files

from IMAP import IMAP
from Text_Summarizer import summarizer
import os

def controller(user,pass_,N,folder):
    # email object
    host = 'imap.gmail.com'
    email = IMAP(host,user,pass_)
    try:
        email.authenticate()
    except:
        print("Failed to authenticate credentials")
        return ["failed","failed"]

    '''Specify number of recent emails to fetch'''
    try:
        fetch_emails = N
        # Fetch the emails
        email.fetch_data(fetch_emails, folder)
    except:
        print("Failed to fetch emails")
        return ["failed","failed"]


    # Summarize these emails
    #summary = ""
    summary_list = []
    for i in range(fetch_emails):
        subject_title = email.email_data[i][0]
        sender = email.email_data[i][1]
        # Number of sentences to summarize to
        num_summary_sentences = 7
        # Execute Text_Summarizer
        summarized_email = summarizer(email.email_data[i][2], num_summary_sentences)
        #dictionary containing the data
        summary = {
            "title"   : subject_title,
            "sender"  : sender,
            "summary" : summarized_email
        }
        # append summary to list of email_summaries
        summary_list.append(summary)
        '''summarized_email = summarizer(email.email_data[i][2], num_summary_sentences)
        summary = summary + (" " + subject_title + "\n")
        summary = summary + (" " + sender + "\n")
        summary = summary + (" " + summarized_email + "\n")
        summary = summary + (" " + '***********************' + "\n")'''
        '''summary = summary + ("<pre>" + subject_title+ "</pre> <br>\n")
        summary = summary +("<pre>" + sender + "</pre> <br>\n")
        summary = summary +("<pre>" + summarized_email + "</pre> <br>\n")
        summary = summary +("<pre>" + '***********************' + "</pre> <br>\n")'''
        print(subject_title)
        print(sender)
        print(summarized_email)
        print()

    #.encode('utf-8').strip()
    return ["Success",summary_list]
