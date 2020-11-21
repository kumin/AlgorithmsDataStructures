#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'waitingTime' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY tickets
#  2. INTEGER p
#

def waitingTime(tickets, p):
    t = 0
    alex_posit = p
    while tickets[alex_posit] > 0:
        tickets[0] -= 1
        t += 1

        if tickets[0] == 0 and alex_posit == 0:
            return t

        temp = tickets[0]
        tickets.remove(tickets[0])

        if temp != 0:
            tickets.append(temp)

        print(tickets)

        alex_posit -= 1
        if alex_posit < 0:
            alex_posit = len(tickets) - 1

    return t


if __name__ == '__main__':
    tickets = [1, 2, 5]

    p = 0

    print(waitingTime(tickets, p))
