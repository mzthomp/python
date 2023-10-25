width = int(input())
height = int(input())
triangle_height = int(input())

while triangle_height <= height:
    triangle_height = int(input())

i = 0
while i < width:
    i = i + 1
    i2 = 0
    while i2 < height:
        print('*',end = '')
        i2=i2+1
    print()

for i in reversed(range(triangle_height)):
    print(('*') * (i + 1))
