# sort dictionary by key or value

# dic = {2: 'jane', 1: 'make', 5: 'clay', 4: 'pain'}
# print("Before sorting keys are :")
# for k in dic.keys():
#     print(f'({k} : {dic[k]})', end=" ")
# print("\nAfter sorting Keys are : ")
# for k in sorted(dic.keys()):
#     print(f'({k} : {dic[k]})', end=" ")

# sorted_dic = sorted(dic.items())
# print('dict before sorting is:')
# print(dic.items(), '\n')
# print('dict after sorting:')
# print(sorted_dic, '\n')
#

# handling missing keys in python
#
# dic = {'dog': 'Sheba', 'cat': 'Ginger', 'snake': 'rattle'}
# n = input('search for the animal ')
# if n in dic.keys():
#     print(f'breed found : {dic.get(n)}')
# else:
#     print('the breed/animal was not found')
#     ani = input('what are you looking for? ')
#     dic[n] = ani
#     print('animal added\n', dic)

# python dictionary with keys having multiple inputs

# lst = {}
# lst1 = {('234', '111'): 'sam', ('211', '111'): 'Tim'}
# phn = input('Enter the phone no.: ')
# id = input('Enter the id: ')
# print('name is ', lst1[phn, id])
#


# Python program to find the sum of all items in a dictionary
# dic = {}
# def findSumDict():
#     sum = 0
#     for val in dic.values():
#         sum += val
#     return sum
# count = 0
# while True:
#     key, value = input('Enter the key and value :').split(' ')
#     dic[key] = int(value)
#     print('Key added :', (key, value))
#     count += 1
#     if count == 3:
#         print(dic)
#         print('sum is: ', findSumDict())
#         break


# Ways to remove a key from dictionaryD
#
# dic = {"Luffy": 30, "Sanji": 19, "Brook": 35, "Zoro": 999}
#
# print("The dictionary before performing remove is : ", dic)
# del dic['Sanji']
# print("The dictionary after remove is : ", dic)


# Ways to sort list of dictionaries by values in Python, using itemgetter and lambda

# from operator import itemgetter
#
# lst = [{"name": "Roronoa Zoro", "age": 20},
# {"name": "Urek Mazino", "age": 33},
# {"name": "Donquixote Doflamingo", "age": 22}]
#
# print("list sorted by name (itemgetter)(ascending order): ")
# print(sorted(lst, key=itemgetter('name')), '\n')
#
# print("list sorted by name (itemgetter)(descending order): ")
# print(sorted(lst, key=itemgetter('name'), reverse=True), '\n')
#
# # sorting using lambda
# print('list sorted by age (lambda)')
# srtd_lst = sorted(lst, key=lambda kv: kv.get('age'))
# print(srtd_lst)

# Merging two Dictionaries
#
# x = {"Roronoa Zoro": 20}
# y = {"Urek Mazino": 33}
# z = {"Donquixote Doflamingo": 22}
# x.update(y)
# x.update(z)
# print(x)


# Program to create grade calculator in Python

# def get_avg(marks):
#     total_sum = sum(marks)
#     total_sum = float(total_sum)
#     return total_sum/len(marks)
#
# def cal_avg(student):
#     assignment = get_avg(student["assignment"])
#     test = get_avg(student["test"])
#     lab = get_avg(student["lab"])
#     return 0.2 * assignment + 0.5 * test + 0.3 * lab
#
# def cal_grade(score):
#     if score >= 90:
#         return "A"
#     elif score >= 80:
#         return "B"
#     elif score >= 70:
#         return "C"
#     elif score >= 60:
#         return "D"
#     else:
#         return "E"
#
# def getInput():
#     name = input('Enter the name of student : ')
#     asst_marks = input('Enter the Assignment marks: ')
#     int_marks = input('Enter the internal marks: ')
#     lab_marks = input('Enter the lab marks: ')
#
#     assignment = []
#     internal = []
#     lab = []
#     for mark in asst_marks.split(' '):
#         assignment.append(int(mark))
#
#     for mark in int_marks.split(' '):
#         internal.append(int(mark))
#
#     for mark in lab_marks.split(' '):
#         lab.append(int(mark))
#     student = {"name": name, 'assignment': assignment, 'test': internal, 'lab': lab}
#
#     avg = cal_avg(student)
#     grade = cal_grade(float(avg))
#     print("Name : ", name, '\n')
#     print(f'Average marks of {name} is : {avg}')
#     print(f'Letter Grade of {name} is : {grade}')
#
#
# getInput()

# Check order of character in string using OrderedDict()

# from collections import OrderedDict
# def checkOrder():
#     patlen = 0
#     for key, val in seq.items():
#         if key == pat[patlen]:
#             patlen = patlen + 1
#
#     if patlen == len(pat):
#         return "true"
#     return "false"
#
#
# strn = input('Enter a String : ')
# pat = input('Enter a Pattern : ')
# seq = OrderedDict.fromkeys(pat)
# # print(seq)
# print(checkOrder())

# dictionary and counter in python to find winner of election

# from collections import Counter
#
# votes = Counter()
# lst = []
# global name_cnt, vote_cnt
# while True:
#     name = input('Enter name of the candidate: ')
#     if name == '':
#         break
#     votes.setdefault(name, 0)
#     if name in votes:
#         votes[name] += 1
#         name_cnt = votes.most_common()[0][0]
#         vote_cnt = max(votes.values())
#
# print('{} won the election with {} votes'.format(name_cnt, vote_cnt))

# find all duplicate characters in a string

# strn = input('Enter a String : ')
# dic = {}
# for char in strn:
#     dic.setdefault(char, 1)
#     if char in dic.keys():
#         dic[char] += 1
# for key,value in dic.items():
#     if value > 1:
#         print(f'{key} is repeated {value-1} times')

# Print anagrams together in Python using List and Dictionary

# def anagram(ip):
#     dic = {}
#     for strVal in ip:
#         key = ''.join(sorted(strVal))
#
#         if key in dic.keys():
#             dic[key].append(strVal)
#         else:
#             dic[key] = []
#             dic[key].append(strVal)
#     output = ""
#     for key, value in dic.items():
#         output = output + ' '.join(value) + ' '
#     return output
#
#
# inp = input().split(' ')    # list
# print(anagram(inp))


# possible words using given characters in python
#
# def char_count(word):
#     dic = {}
#     for i in word:
#         dic[i] = dic.get(i, 0) + 1
#     return dic
#
#
# def all_wds(wds, charst):
#     for word in wds:
#         flag = 1
#         chars = char_count(word)
#         for key in chars:
#             if key not in charst:
#                 flag = 0
#             elif charst.count(key) != chars[key]:
#                 flag = 0
#         if flag == 1:
#             print(word)
#
#
# inp = input('Enter the words: ').split(' ')
# cha = input('Enter the characters: ').split(' ')
# all_wds(inp, cha)


# Create a list of tuples from given list having number and its cube in each tuple

# x = int(input('how many inputs? '))
# lst = []
# for i in range(x):
#     y = int(input('enter a number: '))
#     lst.append((y, y**3))
# print(lst)


# sort a tuple by its second item
#
# lst = [('Roronoa Zoro', 20), ('Bartholmew Kuma', 41),('Urek Mazino', 35), ('25th Baam', 21), ('Hisoka', 24)]
# lst.sort(key=lambda bc: bc[1])
# print(lst)