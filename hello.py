print("hello world")
import socket as s

hostname_get=s.gethostname()
print(f"host name of the device : {hostname_get}")

ip_hostname=s.gethostbyname(hostname_get)
print(f"the host of the device{hostname_get} and the ip adress of the hostname {ip_hostname}")

host_name='python.org'
print(f"namee of the host of the website {host_name}")

ip_user=s.gethostbyname(host_name)
print(f"name of the host is {host_name} ip of {ip_user} ")