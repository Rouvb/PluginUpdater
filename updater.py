import re
import paramiko
import os
import json

def extract_version(filename):
    match = re.search(r"[-\s]*v?\s*(\d+(?:\.\d+)*)\.jar$", filename, re.IGNORECASE)
    return match.group(1) if match else None

def extract_base_name_and_version(filename):
    version = extract_version(filename)
    if version:
        base_name = re.sub(r"[-\s]*v?\s*\d+(?:\.\d+)*\.jar$", "", filename, flags=re.IGNORECASE)
        return base_name.lower(), version
    else:
        return filename.lower(), None

with open("sftp.json", "r") as f:
    json_data = json.load(f)

localfiles = os.listdir("./plugins")

try:
    for config in json_data:
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(config["host"], config["port"], config["username"], config["password"])
        sftp_client = ssh_client.open_sftp()

        remote_files = sftp_client.listdir("./plugins")

        # Remove old version plugins
        for localfile in localfiles:
            base_name, local_version = extract_base_name_and_version(localfile)
            
            if local_version:
                for remote_file in remote_files:
                    remote_base_name, remote_version = extract_base_name_and_version(remote_file)
                    # Remove old version plugin if local version and remote version is not matched
                    if base_name == remote_base_name and local_version != remote_version:
                        sftp_client.remove(f"./plugins/{remote_file}")
                        print(f"{config['name']}: {remote_file} has been removed.")
                        remote_files.remove(remote_file) 

        # Upload file
        for localfile in localfiles:
            localpath = f"./plugins/{localfile}"
            remotepath = f"./plugins/{localfile}"
            sftp_client.put(localpath, remotepath)
            print(f"{config['name']}: {localfile} has been uploaded.")

except Exception as e:
    print(e)

finally:
    if sftp_client:
        sftp_client.close()
    if ssh_client:
        ssh_client.close()