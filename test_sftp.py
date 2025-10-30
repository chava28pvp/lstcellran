import paramiko, fnmatch

host, user, pwd = "10.32.223.253", "u_noc", "LR2pioNJ"
remote_path = "/"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

client.connect(hostname=host, username=user, password=pwd, port=22, timeout=10)
sftp = client.open_sftp()

sftp.chdir(remote_path)
matches = [e for e in sftp.listdir_attr(".") if e.filename.endswith("TOPOFF.zip")]
for e in matches:
    print(f"{e.filename}\t{e.st_size} bytes")

sftp.close()
client.close()
