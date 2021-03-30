# coding:utf-8
"""
@file: FindSecMax.py
@time: 2019/3/21 15:36
@contact: dabuwang
@desc: one team with 150 people, call 5*n to pop up until last one. 
"""

all_team = [x+1 for x in range(150)]

cur_index = 0
print all_team, cur_index

while len(all_team) > 1:
    temp_team = []

    for x in all_team:
        cur_index += 1
        if cur_index % 5 == 0:
            continue
        temp_team.append(x)

    all_team = temp_team[:]
    print all_team, cur_index


print "results:", all_team
