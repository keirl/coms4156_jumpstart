# coms4156_jumpstart
Jumpstart Project for Columbia University's COMS 4156



## Local Installation
Install Git, Google Cloud SDK, Python 2.7, Pip, Virtualenv (optional)


#### Install virtual machine (Optional)
We recommend installing Linux (Ubuntu 14.04) and using it for local development.  The principal motivation is to ensure library and application compatibility with your continuous integration and deployment (Travis and Google App Engine) chain.  If you have to do something special in your environment, then you will need to do it on deployment.  We especially recommend this if your team has a mixture of Macs and Windows or just Windows machines.  Diligent use of `virtualenv` can overcome library issues on Macs and Linux machines.

There are some side benefits as well, namely, you can destroy and rebuild the VM without affecting the rest of your computer.  One of the authors has still not removed all unnecessary libraries and tools.

1. Download and install VirtualBox.
2. Download Ubuntu 14.04.
3. Install Ubunut 14.04.
4. Setup your VirtualBox (Number of CPUs, memory)
5. Update Ubuntu.
6. Install VirtualBox additions.  (Ubuntu 14.04 has a VirtualBox additions built in; however it is often out of date.)
  - Mount .iso in virtualbox
  - Run VirtualBox additions
  - Shared clipboard


#### Install Local Files (Ubuntu 14.04 Commands)
Install Git, Pip, Virtualenv, [Google Cloud SDK] (https://cloud.google.com/sdk/docs/#deb)

    ```sudo apt-get install git python-pip
    sudo pip install virtualenv
    # The following is to install Google SDK    
    export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"
    echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
    sudo apt-get update && sudo apt-get install google-cloud-sdk

#### Setup GitHub.com Account
Create an [account](https://github.com/)
Create and install [SSH](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/) and GPG keys (https://help.github.com/articles/adding-a-new-gpg-key-to-your-github-account/)

#### Fork coms4156_jumpstart Repository
Go to [coms4156_jumpstart](https://github.com/keirl/coms4156_jumpstart) and click the Fork button in the upper right hand side.

Clone the repository to your local machine.  `git clone git@github.com:keirl/coms4156_jumpstart.git`

#### Creating a virtualenv (optional, but recommended)
Before running or deploying this application, install `virtualenv`.  The step is optional but it helps manage your python dependencies.  If you installed a Virtual Machine dedicated to COMS 4156, so do not need to use virtualenv; however, if you are running natively, then we recommend it and so do [others](https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/).  More information is [here](https://virtualenv.pypa.io/en/stable/installation/)

	```cd ~/coms4156_jumpstart/
    virtualenv env
    source env/bin/activate

If everything worked you will see `(env)` before your command prompt, e.g. `(env) user@vm4156:~/coms4156_jumpstart`.

Everytime you want to work on your Flask application, you will need to run `source env/bin/activate`.  When you done working on the app you run `deactivate`.

#### Python Dependencies
- Before running or deploying this application, install the dependencies using
 [pip](http://pip.readthedocs.io/en/stable/):
 
     `pip install -r requirements.txt`

- Check that Flask is listed
    
    `pip list`

    ```appdirs (1.4.3)
    click (6.7)
    Flask (0.12.1)
    itsdangerous (0.24)
    Jinja2 (2.9.6)
    MarkupSafe (1.0)
    packaging (16.8)
    pip (9.0.1)
    pyparsing (2.2.0)
    setuptools (35.0.2)
    six (1.10.0)
    Werkzeug (0.12.1)
    wheel (0.29.0)

#### Test the local environment
- Run the Flask application 
    ```export FLASK_APP=main.py
    flask run

- Navigate to the local web site at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

- Congratulations! You have a webapp up and running.


## Continuous Deployment

#### Verify GitHub is configured correctly.
Make a change.  Edit `README.md` to include your name and team name.

    ```git add README.md
    git commit -m "Added my name to the README file."
    git push

If you have never run the `git push` on this (virtual) machine to GitHub you will get a prompt to set up your configuration:
  ```git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

Verify that your change to the README shows up on GitHub.com.

#### Travis Account

#### Google Cloud Account
Create a Google Cloud account using your Columbia account.  
> Author's note: Easier to get academic credits, etc. if linked to you columbia.edu account.

Follow the guidelines at https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env

