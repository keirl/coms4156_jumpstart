# coms4156_jumpstart
Jumpstart Project for Columbia University's COMS 4156

** All of this will be re-written into complete English sentences. **

# Local Installation
Local installation will be on a virtual machine (Ubuntu 14.04).  Motivation: Ensure maximum compatibility with testing (Travis CI) and deployment environment.  If you have to do something special in your environment, then you will need to do it on deployment.

Side benefits:
- Eliminate unique installation hassles of Mac vs. Windows.  Replaces them with common Linux installation headaches.
- You can destroy and rebuild the VM without affecting the rest of your computer.
- It is a common thing you will be asked to do in other classes.

## Install virtual machine
1. Download and install VirtualBox.
2. Download Ubuntu 14.04.
3. Install Ubunut 14.04.
4. Setup your VirtualBox
  - # CPUs, memory.
  - Shared clipboard.
5. Update Ubuntu.
6. Install VirtualBox additions.
  Ubuntu 14.04 has a VirtualBox additions built in; however it is often out of date.
  - Mount .iso in virtualbox
  - Run additions


## Install Local Files
- Install Git
  sudo apt-get install git
- Install Google Cloud https://cloud.google.com/sdk/docs/#deb
  sudo apt-get install google-cloud-sdk
- Before running or deploying this application, install the dependencies using
[pip](http://pip.readthedocs.io/en/stable/):

    pip install -t lib -r requirements.txt


Setup using virtualenv 

## Setup Git Account
- Create an account
- Create and install SSH and GPG keys



# Continuous Deployment



## Travis Account

## Google Cloud Account
Create a Google Cloud account using your Columbia account.  
> Author's note: Easier to get academic credits, etc. if linked to you columbia.edu account.

Follow the guidelines at https://cloud.google.com/appengine/docs/standard/python/getting-started/python-standard-env


