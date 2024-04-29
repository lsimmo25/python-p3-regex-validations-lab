import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"^[A-Z][a-zA-Z]*(?:[' -][A-Z][a-zA-Z]*)*$"
name_regex = re.compile(name)

phone_number = r"^(\+?\d{0,2})?[\D]?\(?(\d{3})\)?[\D]?(\d{3})[\D]?(\d{4})$"
phone_regex = re.compile(phone_number)

email_address = r"^([^\W\d_][\w.-]*@[a-zA-Z\d.-]+\.[a-zA-Z]{2,})$"
email_regex = re.compile(email_address)
