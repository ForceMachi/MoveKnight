# Correct Knight's move
#
#    1  2  3  4  5  6  7  8
# 1 |  |  |  |  |  |  |  |  |
# 2 |  |  |xy|  |xy|  |  |  |
# 3 |  |xy|  |  |  |xy|  |  |
# 4 |  |  |  |()|  |  |  |  |
# 5 |  |xy|  |  |  |xy|  |  |
# 6 |  |  |xy|  |xy|  |  |  |
# 7 |  |  |  |  |  |  |  |  |
# 8 |  |  |  |  |  |  |  |  |


x1, y1 = 4, 4   # Start coordinates
x2, y2 = 6, 3   # Try change the coordinates form 1 to 8
dx = abs(x1 - x2)
dy = abs(y1 - y2)

if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('Yes')
else:
    print('No')
