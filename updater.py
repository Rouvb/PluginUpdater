import paramiko
import os
import json


with open('sftp.json', 'r') as f:
    json_data = json.load(f)

# Get plugins from your local folder.
localfiles = os.listdir("./plugins")

try:
    for i in range(len(json_data)):
        # Get SFTP connection profile from sftp.json
        name = json_data[i]['name']
        host = json_data[i]['host']
        port = json_data[i]['port']
        username = json_data[i]['username']
        password = json_data[i]['password']
        
        # Connect to SSH
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(host, port, username, password)
        sftp_client = ssh_client.open_sftp()

        # Upload plugins to SFTP servers.
        for j in range(len(localfiles)):
            localpath = f"./plugins/{localfiles[j]}"
            remotepath = f"./plugins/{localfiles[j]}"
            sftp_client.put(localpath, remotepath)
            print(f"{name}: {localfiles[j]} has been uploaded.")
            
except Exception as e:
    print(e)