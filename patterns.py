#printing a square
n = 5
for i in range(n):
    for k in range(n):
        print("*", end=" ")
    print()

print("- " * n)

#printing an increasing triangle
for i in range(n):
    for k in range(i + 1):
        print("*", end=" ")
    print()

print("- " * n)

#printing a decreasing triangle
for i in range(n):
    for k in range(i, n):
        print("*", end=" ")
    print()

print("- " * n)

#right sided triangle
for i in range(n):
    for k in range(i, n):
        print(" ", end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()

print("- " * n)

#right sided triangle 2
for i in range(n):
    for k in range(i + 1):
        print(" ", end=" ")
    for j in range(i, n):
        print("*", end=" ")
    print()

print("- " * n)

#hill/pyramid pattern
for i in range(n):
    for k in range(i, n):
        print(" ", end=" ")
    for l in range(i + 1):
        print("*", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()

print("- " * n)

#reverse hill/pyramid pattern
for i in range(n):
    for k in range(i + 1):
        print(" ", end=" ")
    for l in range(i, n):
        print("*", end=" ")
    for k in range(i, n - 1):
        print("*", end=" ")
    print()

print("- " * n)

#diamond pattern
for i in range(n - 1):
    for k in range(i, n):
        print(" ", end=" ")
    for k in range(i + 1):
        print("*", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()
for i in range(n):
    for k in range(i + 1):
        print(" ", end=" ")
    for k in range(i, n):
        print("*", end=" ")
    for k in range(i, n - 1):
        print("*", end=" ")
    print()
