n = 15

starlist = []
dashlist = []
first, second = (0, 0)
for i in range(n):
    starlist.append((first, second))
    if len(starlist) == n:
        break
    j = 0
    if i%2==0:
        inja = i+1
    else:
        inja = i
    while j < inja:
        if i%4 == 0:
            first += 1
        elif i%4 == 1:
            second += 1
        elif i%4 == 2:
            first -= 1
        else:
            second -= 1
        dashlist.append((first, second))
        j+=1
    if i%4 == 0:
        first += 1
    elif i%4 == 1:
        second += 1
    elif i%4 == 2:
        first -= 1
    else:
        second -= 1

x, y = starlist[-1]
print(x//2, y//2)
print(starlist)
print(dashlist)
# for i in range(-n, n+1):
#     for j in range(-n, n+1):
#         if (i, j) in starlist:
#             print("* ", end='')
#         elif (i, j) in dashlist:
#             print("- ", end='')
#         else:
#             print("  ", end='')
#     print()
for j in range(n, -n-1, -1):
    for i in range(-n, n+1):
        if (i, j) in starlist:
            print("* ", end='')
        elif (i, j) in dashlist:
            print("- ", end='')
        else:
            print("  ", end='')
    print()
        
