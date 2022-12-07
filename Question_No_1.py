
"""
Question 1: 
WAP to check if the given contact number is valid or invalid using regular expressions
"""


import re

phone_numbers = r"2124567890 212-456-7890 (212)456-7890 (212)-456-7890 212.456.7890 212 456 7890 +12124567890 +1 212.456.7890 +212-456-7890 1-212-456-7890"

print()
print("Valid Phone Numbers : ")
print()
x=1
for i in re.findall("[\d()+]{3,5}[-.\s]{0,1}[0-9]{3}[-.\s]{0,1}[0-9]{4}", phone_numbers):
	print(x,") ",i)
	x+=1

print()
print("Total Valid Numbers :", len(re.findall("[\d()+]{3,5}[-.\s]{0,1}[0-9]{3}[-.\s]{0,1}[0-9]{4}", phone_numbers)))
print()