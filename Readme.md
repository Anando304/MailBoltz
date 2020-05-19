# MailBoltz - Overview
- A program designed to summarize your daily emails(Inbox) in one place!
- Saves time from checking/reading every email manually.
- Get all the important details summarized in a few sentences.
- Uses Extraction based summarization along with IMAP to extract emails
- An SMTP client can also be established if the user wants the summarized
 emails to be emailed to them instead of having it saved locally in the `Output` folder.
- Additionally, pairing this with Heroku can allow for scheduled email summaries to be sent
  without having to run the scripts locally.

# Installation Instructions
```installation:
git clone https://github.com/Anando304/MailBoltz.git
cd MailBoltz
conda create -n MailBoltz python=3.7
conda activate MailBoltz
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
pip install lxml
pip install beautifulsoup4
pip install nltk
```

***PyCharm***
If you're using PyCharm, then open File-> Settings -> Project Interpreter -> and set VirtualEnv directory
If you used conda instead of virtual env, navigate to Conda Environment --> existing environment, and locate
the conda folder created C:Users/name/Anaconda3/envs/envName

# Authentication
- Replace the lines in the credentials.txt file with that of yours.
- This is necessary in order for the script to extract the emails

# Running `main.py`
- This file controls the rest of the other scripts
- If you are using an email service other than Gmail, then change the `host` address
- Specify the number of recent emails to fetch using `fetch_emails` variable
- Specify the number of sentences to summarize to using the `num_summary_sentences` variable
- Run the program.


