# What is Plugin Updater?
Transfer your plugins to multiple SFTP servers and remove the old version plugins.
# Installation
## Create a Virtual Environment
### Unix/macOS
```
python3 -m venv venv_name
source venv_name/bin/activate
```
### Windows
```
py -m venv venv_name
call venv_name/Scripts/activate
```
## Install Packages
```
pip install -r requirements.txt
```
## Usage
- Rename sftp-example.json to sftp.json
- Make a folder named "plugins".
```json
[
    {
        "name": "SFTP Instance Name",
        "host": "sftp_host",
        "port": 22,
        "username": "sftp_username",
        "password": "sftp_password"
    },
    {
        "name": "SFTP Instance Name 2",
        "host": "sftp_host 2",
        "port": 22,
        "username": "sftp_username 2",
        "password": "sftp_password 2"
    }
]
```
