import re
pr=re.compile(r'\+\d{12}')
er=re.compile(r'[A-Za-z0-9._]+@[A-Za-z0-9]+.[A-Z|a-z]{2,}')

with open('ex.txt','r')as n:
    for line in n:
        matches=pr.findall(line)
        for match in matches:
            print(match)
        matches=er.findall(line)
        for match in matches:
            print(match)
            
