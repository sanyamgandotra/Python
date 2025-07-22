# function

# def hello_func():
#     pass

# print(hello_func())

# def hello_func():
#     print('Hello Function')

# hello_func()

# def hello_func():
#     return 'Hello Function'

# print(hello_func())
# print(hello_func().upper())

def hello_func(greeting, name='Stranger'):
    return '{} {} Function.'.format(greeting, name)
# print(hello_func('Hi','Jhon'))
# print(hello_func('Hi'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
# student_info('Maths', 'Arts', name='Jhon', age= 22)

courses = ['Maths', 'Arts']
info= {'name':'Jhon', 'age': 22}

# student_info(courses, info)
# student_info(*courses, **info)

months_days =[0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return year%4 ==0 and (year%100 !=0 or year%400 ==0)

def days_in_month(year,month):
    if not 1<= month <=12:
        return 'Invalid Month'
    if month==2 and is_leap(year):
        return 29
    
    return months_days[month]

print(is_leap(2020))

print(days_in_month(2017,2))