# coms4156_jumpstart
Jumpstart Project for Columbia University's COMS 4156

## Getting Started
One person will need to be "Devops" for the duration of the project (pick someone who won't drop the class.)  This person will need to own the GitHub repo and all the other tools.  

TODO on README
- Getting OAuth key
- Setting up permissions for group members
- Setting up Datastore emulator
- pip install --upgrade google-cloud-datastore
- https://cloud.google.com/datastore/docs/reference/libraries#client-libraries-install-python

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
Install Git, Pip, Virtualenv, Ruby, [Google Cloud SDK](https://cloud.google.com/sdk/docs/#deb)

    sudo apt-get install git python-pip ruby ruby-dev
    sudo pip install virtualenv
    # The following is to install Google SDK    
    export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"
    echo "deb https://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
    sudo apt-get update && sudo apt-get install google-cloud-sdk

#### Setup GitHub.com Account
Create a GitHub [account](https://github.com/).

Create and install [SSH](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/) keys.

Create and install [GPG keys](https://help.github.com/articles/adding-a-new-gpg-key-to-your-github-account/).

#### Fork coms4156_jumpstart Repository
Go to [coms4156_jumpstart](https://github.com/keirl/coms4156_jumpstart) and click the Fork button in the upper right hand side.

Clone the repository to your local machine.  `git clone git@github.com:keirl/coms4156_jumpstart.git`

#### Creating a virtualenv (optional, but recommended)
Before running or deploying this application, install `virtualenv`.  The step is optional but it helps manage your python dependencies.  If you installed a Virtual Machine dedicated to COMS 4156, so do not need to use virtualenv; however, if you are running natively, then we recommend it and so do [others](https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/).  More information is [here](https://virtualenv.pypa.io/en/stable/installation/)

	cd ~/coms4156_jumpstart/
    virtualenv env
    source env/bin/activate

> You might be thinking why should I use virtualenv?  Then you did not read the links above.  In short, virtualenv isolates the libraries used in this project from other projects.  This ensures that external package changes do not impact your development or project because you are only using a specific version (defined in `requirements.txt`).  If you have more than one project ongoing, it makes it so that changes to one do not break others.  Why should you do it for this project on a fresh VM dedicated to one project?  That is less compelling, but it is something that everyone working in Python, so we'll just say professional development.

If everything worked you will see `(env)` before your command prompt, e.g. `(env) user@vm4156:~/coms4156_jumpstart`.

Everytime you want to work on your Flask application, you will need to run `source env/bin/activate`.  When you done working on the app you run `deactivate`.

#### Python Dependencies
Before running or deploying this application, install the dependencies using [pip](http://pip.readthedocs.io/en/stable/):
 
    pip install -r requirements.txt

Check that Flask is listed
    
    pip list

    appdirs (1.4.3)
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

You should also update the requirements.txt file, `pip freeze > requirements.txt`.  One of the key benefits of using virtualenv is that only the libraries being used in the project 

#### Test the local environment
Run the Flask application 
    
    export FLASK_APP=main.py
    flask run

Navigate to the local web site at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

Congratulations! You have a webapp up and running.


## Continuous Deployment

#### Verify GitHub is configured correctly.
Make a change.  Edit `README.md` to include your name and team name.

    git add README.md
    git commit -m "Added my name to the README file."
    git push

If you have never run the `git push` on this (virtual) machine to GitHub you will get a prompt to set up your configuration:

    git config --global user.email "you@example.com"
    git config --global user.name "Your Name"
    git config --global push.default matching

Verify that your change to the README shows up on GitHub.com.

#### Travis Account
Go to [Travis CI](https://travis-ci.com/) and sign in with your GitHub.  Only one person on the team needs to do this.  This person must be the owner of the repository.

Follow their prompts to turn on Travis for this repo (short for repository).  

Test that Travis is working as expected.  Make another change and see whether the build passes.  It normally takes about 5 minutes, so go get a cup of coffee from Blue Java.

Additional guidance on setting up Travis CI for Python is available at [Travis CI](https://docs.travis-ci.com/user/languages/python/).

#### Setup Google Cloud Account
Create a Google Cloud account using your Columbia account at [https://cloud.google.com/](https://cloud.google.com/)
> Author's note: Easier to get academic credits, etc. if linked to you columbia.edu account.

Create a new project, say COMS4156.  The name does not really matter.  They will give you a cute name from your project name, e.g. "astute-anagram-165723".

#### Setup Google Cloud App Engine
Navigate to [https://cloud.google.com/appengine/](https://cloud.google.com/appengine/) and then select "View my console."

You may want to follow their "My First App Tutorial."  It will help you understand how app engine works.

Follow the guidelines from [Google](https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env) and [QuickStart](https://cloud.google.com/appengine/docs/standard/python/quickstart).

    gcloud init

Google will have you sign into your Google account.  Use the one that you signed up for Google Cloud with.

We've setup the configuration files: `app.yaml` and `appengine_config.py`.  If you do more advanced functionality, you may need to change `app.yaml` and Google's docs are good at describing the various settings.  `appengine_config.py` just tells App Engine where to look for libraries.  Speaking of which...

#### Deploy the Application
You'll need to install the libraries again to put them in the right place for App Engine (`lib/`).  `env/lib` has these files plus many more.  This will only need to be run initially and then whenever a new module is added.

    pip install -t lib -r requirements.txt

Now deploy the application to App Engine.

    gcloud app deploy

Verify that it is deployed by 

    gcloud app browse

We strongly recommend that you browse the App Engine docs to get a feel for what is happening under the hood.

#### Connect Travis to App Engine for Continuous Deployment
You are going to follow the guides from [Travis CI](https://docs.travis-ci.com/user/deployment/google-app-engine/) and [Google Cloud](https://cloud.google.com/solutions/continuous-delivery-with-travis-ci).  Information on the Travis CI tool is available [here](https://blog.travis-ci.com/2013-01-14-new-client/). *Note: The approach of 

There are two items that are needed to get Travis to work with Google Cloud, an API key and a secret key.  Neither should go into your repo unencrypted.  

Assuming you installed Ruby earlier, simply call `sudo gem install travis`

Turn on [“Google App Engine Admin API”](https://console.developers.google.com/apis/).  Click on `Enable API` then search for `Google App Engine Admin API`.

Go to “Credentials”, click “Add Credential” and “API key” and copy to your clipboard.  Restrict the API key to an HTTP referrer `www.travis-ci.org`. (This keeps people from hijacking your website.) Rename `api_key.py.sample` to `api_key.py`.  Within `api_key.py`, change `'YOU-API-KEY'` to the API key from Google Cloud.  *Be sure to keep the quotes around the key*.  **Save to your local Git directory, but do not add to the repo.  This file is part of the default .gitignore, so just don't override the .gitignore.**  
Go to “Credentials”, click “Add Credential” and “Service account key”, finally click “JSON” to download the your Service Account JSON file.  Rename to `client-secret.json`. **Save to your local Git directory, but do not add to the repo.  This file is part of the default .gitignore, so just don't override the .gitignore.**

Login to Travis with your GitHub account.
    
	travis login --org

Tar your credentials into a single file:

	tar -czf credentials.tar.gz client-secret.json api_key.py

Encrypt your credentials in your Git directory.  

	travis encrypt-file credentials.tar.gz

Switch to the continuous deployment `.travis.yml`

	mv .travis.yml .travis.yml.ci
	mv .travis.yml.cd .travis.yml
    
Edit `.travis.yml` to set up continuous deployment.  Change `project: google_cloud_project_id` to the proper name.

Commit changes to you Git repo.

	git add credentials.tar.gz.enc .travis.yml
	git commit -m "Added keys for Google App deployment"
	git push

Verify that everything is working as expected.  Look at the Travis CI log, make a small change to the application and make sure it ended up there.

#### Advanced things to look into...
You can integrate GitHub into Slack so that you see all commits.  You can do the same with [Travis builds](https://docs.travis-ci.com/user/notifications/#Configuring-slack-notifications).  

The Google Cloud app is pretty good and allows you to see the console from your phone.  Can be helpful if you are helping someone debug. 

Use tail to look at App Engine logs: `gcloud app logs tail -s default`.

### Have fun! and Don't Break the Build!
