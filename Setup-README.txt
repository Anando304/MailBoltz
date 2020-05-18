Install packages to a specific project: So create a virtual env via venv or conda
1.create a new conda -> 'conda create -n MailBoltz python=3.7'
To activate: To activate this environment, type 'conda activate MailBoltz'
To deactivate: 'conda deactivate'
OR 
2.USING Virtual env
pip install virtualenv
***Create Virtual env***
python3 -m venv env
THen activate it -> 'env\Scripts\activate.bat'
To deactivate, type 'deactivate'
'pip freeze' reads the versions of the modules in a local virtual env
and produces a text file with package version for each python package specified.
We will paste the 'versions' info in requirements.txt.
For specific module info to be displayed to screen, type 'pip show <package name>
pip install -r requirements.txt

******************PyCharm*******************
If you're using PyCharm, then open File-> Settings -> Project Interpreter -> and set VirtualEnv directory
If you used conda instead of virtual env, go to Conda Environment, existing environment, and locate
the conda folder created C:Users/name/Anaconda3/envs/envName


******************Python Libraries*************
activate the environment: (using conda: activate test-scikit)

# Installation
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib


GMAIL:
Gmail Settings -> Forwarding and POP / IMAP -> IMAP Acess to Enable IMAP
https://myaccount.google.com/lesssecureapps <---enable
