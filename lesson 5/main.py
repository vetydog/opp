'''
import requests
from requests import get
from requests import post
#help(requests)

r = get('https://www.python.org')
print(r.status_code)
print(r.text)

payload = dict(key1='value1', key2='value2')
r = post('https://httpbin.org/post', data=payload)
print(r.text)

from student import Student
student = Student()
print(Student.__name__)
print(Student.__bases__)
print(type(Student))
'''
import colorama

'''
students = list()
for method in dir(students) :
    print(method)
help(list)
'''


from student import Student
print(issubclass(Student, Pupil))

'''
getattr()
callable()
issubclass()
issubctance
'''
help(colorama)



