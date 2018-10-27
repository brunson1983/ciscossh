
import paramiko
import time

ip_address = "192.168.10.9"
username = "brunson"
password = "12345"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print ("Successful connection!", ip_address)

remote_connection = ssh_client.invoke_shell()

remote_connection.send("config t\n")
remote_connection.send("int fa0/1\n")
remote_connection.send("ip address 192.168.10.220 255.255.255.0\n")
remote_connection.send("no shut\n")
remote_connection.send("exit\n")
remote_connection.send("int fa0/2\n")
remote_connection.send("ip address 10.0.0.2 255.255.255.0\n")
remote_connection.send("no shut\n")
remote_connection.send("exit\n")


for n in range (2,21):
    print ("Creating VLAN" +str(n))
    remote_connection.send("vlan " + str(n) + "\n")
    remote_connection.send("name VLAN_TWO" + str(n) + "\n")
    time.sleep(0.5)

remote_connection.send("end\n")

time.sleep(1)
output = remote_connection.recv(65535)
print (output)

ssh_client.close


