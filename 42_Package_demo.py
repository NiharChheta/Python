#how to import module from package
# from package import module 
from Python import asia 
from Python import north_america as na 
from Python import europe as e 
# OR
# import earth.asia 
# import earth.europe as e 
# import earth.north_america as na 

print(asia.getCountries())
print(e.getCountries())
print(na.getCountries())