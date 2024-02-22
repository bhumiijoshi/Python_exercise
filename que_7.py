import re
emails = ["abc@gmail.com", "123$tt*@xyz.com", "good@bad@uk.in", "nasa@usa12.space", "no-reply@domain.in", "ramhanuman@saketa.lok", "ruhi.mohan@exter123.123", "fake@fake123.fakercom"]

pattern = r'\b[A-Za-z0-9|_|-]+@[A-Za-z0-9]+\.[A-Za-z]{2,5}\b'
valid_emails = []
for email in emails:
    
    if re.match(pattern,email):
        valid_emails.append(email)
        
print(valid_emails)   
