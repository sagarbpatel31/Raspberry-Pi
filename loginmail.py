from urllib.request import urlopen
import re
import smtplib
fromaddr = "sagarp3199@gmail.com"
toaddr="sagarp3199@gmail.com"
subject= "Play Raspberry PI"
username = "sagarp3199"
password = "399ansimla2603"

url = "http://checkip.dyndns.org"
print("IP address service is ",url)

request = urlopen(url).read().decode('utf-8')

ourIP = re.findall("\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",request)
ourIP = str(ourIP)
print("Our IP Address is ",ourIP)

def send_email(ourIP):
    body_text = ourIP + " is our Rasperry PI Playing IP Address"
    msg = "Hello IP is "+ourIP

    server= smtplib.SMTP("smtp.gmail.com:587")
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr,toaddr,msg)
    server.quit()
    print("Our email has been sent....")

with open('/home/pi/Documents/ipemail/lastip.txt','rt') as last_ip:
    last_ip=last_ip.read()

print("IP = ",last_ip)
if last_ip == ourIP:
    print("Same")
    print("Our IP address is not changed..")
else:
    print("We have a new IP Address..")
    with open('/home/pi/Documents/ipemail/lastip.txt','wt') as last_ip:
        last_ip.write(ourIP)
    print("We have a new IP Address to new file")
    send_email(ourIP)

