# Step 1 receive input as integer n, which equals amount statues needed.

import math

statueNeeded = int(input())
day = 5
statueMax = 16
if statueNeeded < 5:
    day = statueNeeded
if statueNeeded == 4:
    day = 3
if 5 <= statueNeeded <= 7:
    day = 4
if statueNeeded >= 8:
    while math.log2(statueNeeded) > math.log2(statueMax):
        previousMax = statueMax
        statueMax = previousMax * 2
        day += 1

print(day)
