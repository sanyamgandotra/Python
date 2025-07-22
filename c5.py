# import my_module as mm

# courses = ['History', 'Maths', 'Physics', 'CompSci']

# index= mm.find_index(courses, 'Maths')
# print(index)

import sys
sys.path.append('/Users/sanyamgandotra/Desktop/Module Py')

from my_module_alt import find_index, test

courses = ['History', 'Maths', 'Physics', 'CompSci']

index= find_index(courses, 'Maths')
# print(index)
# print(test)
# print(find_index(test,'t'))

print(sys.path)

# from my_module import *
# courses = ['History', 'Maths', 'Physics', 'CompSci']

# index= find_index(courses, 'Maths')
# print(index)
# print(test)

"""Changing pythonpath environment variable to acces any module in any directory withouth appending sys.path"""
"""in termial run
nano ~/.bash_profile

go to the end and write 

export PYTHONPATH="Path of the file" 
and save"""

