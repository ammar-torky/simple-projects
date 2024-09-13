#======================#

email = str(input("Enter Your Email Man : "))
mark = email.index("@")

name = email[0:mark]
domain = email[mark + 1:]

print("your name is ",name," and your domain is ",domain)

#=================#

# here is how to use regular expresssion in our case : 
import re
email2 = str(input("Enter Your Email Man : "))
match1 = re.search(r"[A-Za-z0-9._-]+",email2)
match2 = re.search(r"[A-Za-z0-9]+\.(com|edu|org)",email2)

print(f"name is {match1.group()} domain is {match2.group()}")
