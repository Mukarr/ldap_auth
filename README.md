# LDAP_auth (development branch)
**A unix-executable to automate the LDAP authentication for IIT Mandi students and faculty.**

## Requirements
- chromedriver : [How to download and install chromedriver](https://sites.google.com/a/chromium.org/chromedriver/getting-started)

## How to run
#### Download
 **Clone the repository**
```
git clone https://github.com/Mukarr/ldap_auth.git
cd ldap_auth
```
#### Edit Credentials
Edit [credentials.txt](https://github.com/Mukarr/ldap_auth/blob/develop/dist/ldap_auth/credentials.txt) in dist/ldap_auth folder to add your username and password

#### Double-click [ldap_auth](https://github.com/Mukarr/ldap_auth/blob/develop/dist/ldap_auth/ldap_auth) in dist/ldap_auth to see it in action

## How it works
- The unix-executable **ldap_auth** can be found in [dist/ldap_auth](https://github.com/Mukarr/ldap_auth/tree/develop/dist/ldap_auth) folder
- The parent python script is **[ldap_auth.py](https://github.com/Mukarr/ldap_auth/blob/develop/ldap_auth.py)**
- [pyinstaller](http://www.pyinstaller.org/) is used to generate the executable from the python script
  `pyinstaller ldap_auth.py`

##How to Contribute
Feel free to contribute by submitting an issue at https://github.com/Mukarr/ldap_auth/issues or a [pull request](https://help.github.com/articles/about-pull-requests/) 
