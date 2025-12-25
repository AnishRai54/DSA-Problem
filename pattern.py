def pattern_7(n):
    for i in range(n):
        for j in range(n):
            if i+j>=n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        for j in range(i-1):
            print("*", end=" ")
        print()
        
rows = 5

for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")

    for j in range(i + 1):
        print("*", end=" ")

    print()

pattern_7(5)
print()
n=5
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    
    for j in range(n - i):
        print("*", end=" ")

    for j in range(n-i-1):
        print("*", end=" ")
    print()


for i in range(n):
    for j in range(n):
        if i+j>=n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    for j in range(i-1):
        print("*", end=" ")
    print()
for i in range(n):
    for j in range(i):
        print(" ", end=" ")
    
    for j in range(n - i):
        print("*", end=" ")

    for j in range(n-i-1):
        print("*", end=" ")
    print()
