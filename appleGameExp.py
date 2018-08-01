# --*-- encoding:utf-8 --*--
#! usr/bin/env python3

students = ['小明', '小红', '小兰']

for student in students:
    print('%s%s' %(student, '吃了一个苹果！'))


students = ['小明', '小红', '小兰']

for student in students:
    if student == '小红':
        continue
    print('%s%s' %(student, '吃了一个苹果！'))
