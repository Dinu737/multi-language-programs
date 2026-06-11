import paramiko

host = "EC2-PUBLIC-IP"
username = "ec2-user"
key = "python-key.pem"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(
    host,
    username=username,
    key_filename=key
)

stdin, stdout, stderr = ssh.exec_command(
    "python3 /home/ec2-user/python-app/app.py"
)

print(stdout.read().decode())

ssh.close()
