import re

class EmailAddressParser:
    def __init__(self, email_string):
        self.email = email_string
        
    def parse(self):
        email_regex = re.compile(r"[\w\.]+@[\w]+\.com")
        emails = email_regex.findall(self.email)
        emails.sort()
        print(emails)
        return emails

