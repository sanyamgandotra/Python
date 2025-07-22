courses_1= ['History', 'Physics', 'Chemistry', 'Maths', 'English']
courses_2= ['Art', 'Politics','Comp Science']

# print(courses_1)
# print(courses_2)

# for item in courses_1:
#     print(item)

# for item in courses_2:
#     print(item)

# for index, item in enumerate(courses_1):
#     print(item, index)

courses_1_str= '-'.join(courses_1)
# print(courses_1_str)

new_list= courses_1_str.split('-')
# print(new_list)

list_1 = ['H', 'M', 'S', 'P', 'Q']
list_2= list_1
# print(list_2)

list_1[0]= 'A'
# print(list_1)
# print(list_2)

tuple_1 = ('H', 'M', 'S', 'P', 'Q')
tuple_2= tuple_1
# print(tuple_1)
# print(tuple_2)

# tuple_1[0]= 'A'
# print(tuple_1)
# print(tuple_2)

cs_course = {'H', 'M', 'S', 'P', 'Q'}
# print(cs_course)

art_courses = {'A', 'B', 'S', 'M'}

# print(cs_course.intersection(art_courses))
# print(cs_course.difference(art_courses))
# print(cs_course.union(art_courses))

student= {'name':'Jenny', 'age':25, 'subjects':['M', 'C']}
# print(student)
# print(student['name'])
# print(student['age'])
# print(student['subjects'])

# print(student['Phone'])
# print(student.get('Phone'))
# print(student.get('Phone','Not Found'))

# student['phone']= '555-555'
# student['name']= 'Penny'
# print(student)

# student.update({'name':'Penny', 'age':35, 'subjects':['A', 'C'], 'phone': '555-555'})
# print(student)

# del student['age']
# print(student)

# age = student.pop('age')
# print(student)
# print(age)

# print(student.keys())
# print(student.values())
# print(student.items())
# 
# for key in student:
    # print(key)
# 
# for key, value in student.items():
    # print(key,value)

# if True:
#     print(True)

# if False:
    # print(False)

l='python'

if l=='Python':
    print('Sexy')
else:
    print('Fuck')

x = 'panda'

if x=='python':
    print(sexy)
elif x=='panda':
    print('sexxxxxy')
else:
    print('Fucccckkkk')