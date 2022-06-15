import re
NAME_USER = re.compile(r'[A-Za-z\d_\.]+')
DOMAIN = re.compile(r'[a-z\d]+\.[a-z]+')
def email_parse(email):
    result = re.split('@', email)
    if NAME_USER.match(result[0]) and DOMAIN.match(result[1]):
        out = dict(
            username=result[0],
            domain=result[1]
        )
        print(out)
    else:
        raise ValueError(f'wrong email: {email}')

email_parse('someone@gmail.com')
email_parse('someone@gmailcom')


