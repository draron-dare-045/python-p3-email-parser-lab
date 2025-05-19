import re

class EmailAddressParser:
    def __init__(self, email_string):
        self.email_string = email_string

    def parse(self):
        normalized = self.email_string.replace(",", " ")
        parts = normalized.split()
        email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
        valid_emails = [email for email in parts if email_pattern.fullmatch(email)]
        return sorted(set(valid_emails))
