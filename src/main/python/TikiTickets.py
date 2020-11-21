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

    for i in range(len(tickets)):
        if tickets[i] < tickets[p]:
            t += tickets[i]
        else:
            if i <= p:
                t += tickets[p]
            else:
                t += tickets[p] - 1

    return t


if __name__ == '__main__':
    tickets = [1, 2, 1, 2, 1, 1]

    p = 0

    print(waitingTime(tickets, p))
