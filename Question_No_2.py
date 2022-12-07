
"""
Question 2:
WAP to get the Social Links, Email & Contacts details of a website on user input.
"""


import urllib.request
from re import findall


url = input("Enter url : ")
response = urllib.request.urlopen(url)

html = response.read()

htmlstr = html.decode()

email = findall(r"[\w._+-]{1,20}@[\w]{2,20}.[a-z{2,3}]", htmlstr)

contacts = findall(r"[+1]{0,2}[-\s]{0,1}[0-9]{3}[-.\s]{0,1}[0-9]{3}[-.\s]{0,1}[0-9]{4}", htmlstr)

social_links = findall(r"[https]{5}://[w]{3}.[\w]{2,20}.[\w]{2,3}/[a-zA-Z0-9|-]{0,10}/[a-zA-Z0-9|-]{0,100}", htmlstr)

print()
print("Email/s :")
for item in email:
    print(item)

print()
print("contact :")
for item in contacts:
    print(item)

print()
print("Social Links :")
for item in social_links:
    print(item)
