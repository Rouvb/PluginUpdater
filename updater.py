import paramiko
import os


# FTP Connection Information
sftp_host = ""
sftp_port = ""
sftp_user = ""
sftp_password = ""

# Connect to SSH
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(sftp_host, sftp_port, sftp_user, sftp_password)
sftp_client = ssh_client.open_sftp()
print("SSH has been connected.")

# Get plugins from your local folder.
localfiles = os.listdir("./plugins")

# Upload plugins to SFTP servers.
for i in range(len(localfiles)):
    localpath = f"./plugins/{localfiles[i]}"
    remotepath = f"./plugins/{localfiles[i]}"
    sftp_client.put(localpath, remotepath)
    print(f"{localfiles[i]} has been uploaded.")