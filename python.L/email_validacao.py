import re 
regex = r'^[\w\,-]+@[\w\,-]+\,\w+$'

email = input("digite seu email")
if re.match(regex, email):
     print("u+ 274 email valido")
     
else:
