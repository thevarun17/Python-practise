import re
var = """
India ip address is 192.3.4.67
Australia ip address is 23.123.5.4
Canada ip address is 165.211.90.43 and 1.45.78.65
"""


patc = '[A-Z][a-z]{1,}'
patip = '[0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}[.][0-9]{1,3}'


countries = re.findall(patc, var)
ips = re.findall(patip,var)

print(countries)
print(ips)