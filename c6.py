import random
import math
import datetime
import calendar
import os

courses = ['History', 'Maths', 'Physics', 'CompSci'] 

random_course = random.choice(courses)

print(random_course)

rads = math.radians(90)

print(rads)
print(math.sin(rads))

date = datetime.date.today()

print(date)

print(calendar.isleap(2017))

print(os.getcwd())
print(os.__file__)