from datetime import datetime
now = datetime.now();
print(now)

#indian format 
indian_format = now.strftime("%a - %d/%m/%y %H:%M:%S")
print(indian_format)

#us format
us_format = now.strftime("%A, %B %d, %Y %I:%M:%S %p")
print(us_format)