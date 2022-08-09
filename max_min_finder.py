largest = 0
smallest = 0
while True:

    numm = input("Enter a number: ")
    if numm == "done":
        break

    try:
        num=int(numm)
    except:
        print('Invalid input')
        continue

    if num > largest:
        largest=num

    if smallest==0:
        smallest=num
    else:
        if num<smallest:
            smallest=num

print("Maximum is", largest)
print("Minimum is", smallest)
