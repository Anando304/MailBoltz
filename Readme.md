<img src="./WebApp 2.0/static/imgs/logo.png" width="232" height="200">

# MailBoltz - Overview
- An application designed to summarize your daily emails in one place!
- Saves time from having to read entire sets of emails.
- Get all the important details summarized in a few sentences.
- Uses Extraction based summarization along with IMAP to extract emails
- An SMTP client on a scheduled server can also be established if the user wants the summarized
 emails to be emailed to them at a set period of time.

# Ways to use:
- ***2 options available***
- Use the **webapp** available <a href="https://mailboltz.herokuapp.com/home"> here </a>
- Use directly via Python **console/terminal**

# Console - Installation Instructions
```installation:
git clone https://github.com/Anando304/MailBoltz.git
cd MailBoltz
cd Console
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

# Console - Authentication
- Replace the lines in the credentials.txt file with that of yours.
- This is necessary in order for the script to extract the emails

# Console - Running `main.py`
- This file controls the rest of the other scripts
- If you are using an email service other than Gmail, then change the `host` address
- Specify the number of recent emails to fetch using `fetch_emails` variable
- Specify the number of sentences to summarize to using the `num_summary_sentences` variable
- Run the program.

# WebApp 2.0 - Installation Instructions
- The deployed webapp is available <a href="https://mailboltz.herokuapp.com/home"> here </a>
- You can also run the webapp locally using the instructions below!
```installation:
git clone https://github.com/Anando304/MailBoltz.git
cd MailBoltz
cd 'WebApp 2.0'
conda create -n MailBoltz python=3.7
conda activate MailBoltz
pip install lxml
pip install beautifulsoup4
pip install nltk
pip install flask
pip install gunicorn
```

# WebApp 2.0 - Running `app.py`
- Run this script
- Navigate to <a href="127.0.0.1:5000/home">127.0.0.1:5000/home</a>

