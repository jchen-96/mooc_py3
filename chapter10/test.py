import re
language = 'pythonC#javaphpc#'


def convert(value):
    matched = value.group()
    return '!!' + matched + '!!'


r = re.sub('c#', convert, language, 1, re.I)
print(r)

re.match
