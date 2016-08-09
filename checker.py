#!/usr/bin/python3
import sys

raw_my = input("Your Answer: ")
raw_right = input("Correct Answer: ")

my = ''.join(list(filter(lambda a: a in "ABCDEFGHJ?", raw_my)))
right = ''.join(list(filter(lambda a: a in "ABCDEFGHJ?", raw_right)))

if len(my) != len(right):
    print("Length not equal.", file=sys.stderr)
    sys.exit()

count = 0
prob_num = len(my)

for i in range(prob_num):
    if right[i] != my[i]:
        print("{num: >2}. {right} ({my})".format( \
                num=i + 1, right=right[i], my=my[i]))
        count += 1

if count > 0: print("Total/Wrong/Right/Rate: {}/{}/{}/{:.2%}".format( \
            prob_num, count, prob_num - count, 1 - count / prob_num))
