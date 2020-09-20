x = int(input("введите год: "))
if x % 4 != 0 or (x % 100 == 0 and x % 400 != 0):
    print("NO")
else:
    print("YES")
