## @file IMAP.py
 # @author Anando Zaman
 # @brief Extracts email data
 # @date May 16, 2020
 # @details Extract and text-processing of email data

'''IMAP allows the client program to manipulate the e-mail
   message on the server without downloading them on the
   local computer.

   We could also extract emails using the GMail API shown in the Gmail_test.py file
   '''

import imaplib
import email as EMAIL
from email.header import decode_header

''' @brief class used for creating IMAP objects
 *  @details Extracts email data from the Inbox folder of an email client(ie; GMail)
 '''
class IMAP:

    def __init__(self,Host,User,Pass):
        self.Host = Host
        self.User = User
        self.Pass = Pass
        self.imap = ''
        self.email_data = []

    def get_imap(self):
        return self.imap

    def get_email_data(self):
        return self.email_data

    def set_imap(self, x):
        self.imap = x

    def append_email_data(self, x):
        self.email_data.append(x)

    # Authentication flow
    def authenticate(self):
        imap_host = self.Host
        imap_user = self.User
        imap_pass = self.Pass

        # connect to host using SSL
        imap = imaplib.IMAP4_SSL(imap_host)

        # Authenticate
        imap.login(imap_user, imap_pass)
        self.set_imap(imap)

    # Fetches the N-top emails
    def fetch_data(self, N):
        imap = self.get_imap()
        # Change to 'SPAM' if you want to get emails from SPAM folder
        status, messages = imap.select("INBOX")
        # response status check
        if (status != 'OK'):
            print("Could not retrieve data")
            return

        # total number of emails
        messages = int(messages[0])

        # Extract top N-emails
        for i in range(messages, messages - N, -1):

            # Used to temporarily store each email data in preperation for insertion
            data_list = []

            # fetch the email message by ID
            res, msg = imap.fetch(str(i), "(RFC822)")

            # response status check
            if res != 'OK':
                print("Could not retrieve email number: ", i)
                return

            # Parse email-response bytes data
            for response in msg:
                if isinstance(response, tuple):
                    # Parse: bytes email --> message object
                    msg = EMAIL.message_from_bytes(response[1])
                    # Decode email subject
                    subject = decode_header(msg["Subject"])[0][0]
                    if isinstance(subject, bytes):
                        # if in bytes, decode bytes --> string
                        subject = subject.decode()
                    # Extract sender info
                    from_ = msg.get("From")
                    # Append to data list
                    data_list.append(subject)
                    data_list.append(from_)
                    #print("Subject:", subject)
                    #print("From:", from_)

                    # if the email message is multipart(composed of sections for each Content-Type)
                    if msg.is_multipart():
                        # Iterate over email parts
                        for part in msg.walk():
                            # extract content type of email
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            try:
                                # get the email body
                                body = part.get_payload(decode=True).decode()
                            except:
                                pass
                            if content_type == "text/plain" and ("attachment" not in content_disposition):
                                # append text/plain emails and skip attachments
                                data_list.append(body)
                                #print(body)


                    # if NOT multipart
                    else:
                        # extract content type of email
                        content_type = msg.get_content_type()
                        # get the email body
                        body = msg.get_payload(decode=True).decode()
                        if content_type == "text/plain":
                            # save only text email parts
                            data_list.append(body)
                            #print(body)

            # Insert data_list containing data for an email, into the list of all email_data
            self.append_email_data(data_list)

        imap.close()
        imap.logout()