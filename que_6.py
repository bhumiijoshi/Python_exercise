import re

string = "PQRQRQRQ" 
res= len(re.findall('(?=(QRQ))', string))

print(res)