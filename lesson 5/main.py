'''
import requests as requests
from requests import get
from requests import post

help(requests)

r = get('https://www.python.org')
print(r.status_code)
print(r.content)

payload = dict(key1='value1', key2='value2')
r = post('https://httpbin.org/post', data=payload)
print(r.text)
print(requests.__name__)
'''
import colorama as colorama

'''
from student import Student
student = Student()
print(Student.__name__)
print(Student.__bases__)
print(type(Student))
'''

'''
students = list()
for method in dir(students):
    print(method)

help(list)
'''

from student import Student, Pupil
print(issubclass(Student, Pupil))
'''
getattr()
callable()
issubclass()
isinstance()
'''

help(colorama)


