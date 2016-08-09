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
        print("{num: >2}. \x1b[38;5;196m{my}\x1b[0m" \
                " -> \x1b[38;5;46m{right}\x1b[0m".format( \
                num=i + 1, right=right[i], my=my[i]))
        count += 1

if count > 0: print("Total/Wrong/Right/Rate: {}/{}/{}/{:.2%}".format( \
            prob_num, count, prob_num - count, 1 - count / prob_num))
