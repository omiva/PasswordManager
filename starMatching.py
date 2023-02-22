import re
# bat = re.compile(r"(ha){3,6}")  op hahahaha
# m1 = bat.search("hahahaha")
# print(m1.group())

# bat = re.compile(r"(ha){3,6}?")   # op hahaha
# m1 = bat.search("hahahaha")
# print(m1.group())
#
# bat = re.compile(r"(\d\d\d)-(\d\d\d)-(\d\d\d)")
# m1 = bat.findall("my num is 411-422-899 and alter num is 411-560-897")
# print(m1)
#
#
# bat = re.compile(r"(ha)+")
# m1 = bat.search("hahahaha")
# print(m1.group())

# bat = re.compile(r"bad(land|sand|boy|dy)")
# m1 = bat.search("badland")
# print(m1.group())

# bat = re.compile(r"\d+\s\w+")
# m1 = bat.search("123 skhfdal")    # op 12 days
# print(m1.group())

# bat = re.compile(r"[a-z]", re.I)
# m1 = bat.findall("marRY had a little lamp")
# print(m1)

# bat = re.compile(r"\d+$")
# m1 = bat.search("13 days, days 12")
# print(m1.group())
#
# bat = re.compile(r"^\d+\w+$")
# bat1 = re.compile(r"\d+\w+")
# m1 = bat.search("12s")
# m2 = bat1.search("12z")
# print(m1.group(),"\n", m2.group())
#
# spam = ["name", "age", 1, 199]
# print(spam)
#
# s = "        hey man wassup       "
# print(s)
# print(s.lstrip())

# digitRegex = re.compile(r'(\d){3,5}')
# x = digitRegex.search('123456')
# print(x.group())

#
# import shutil, os
# from pathlib import Path
# p = Path.home()
# shutil.copytree(p / 'spam.txt', p / 'spam_backup.txt')
#
# find = re.compile(r'\S+@\S+')
# check = find.findall('heyyo @ me at blablabla21@gmail.com or kekw12@yahoo.com')
# print(check)

# person = {'name': 'Phill'}
#
# # key is not in the dictionary
# salary = person.setdefault('salary','12000')
# print('person = ',person)
# print('salary = ',salary)
#
# # key is not in the dictionary
# # default_value is provided
# age = person.setdefault('age', '22')
# print('person = ',person)
# print('age = ',age)
#
# string = re.compile(r'^a[a-z]{8}z$')
# check = string.search('aaaddfszzz')
# print(check.group())

x = list(input().split())
print(' '.join(x[::-1]))