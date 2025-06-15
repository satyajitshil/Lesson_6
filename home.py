a = input("Type a symbol: ")
if (ord(a)) >= 65 and ord(a) <= 90 or ord(a) >= 91 and ord(a) <= 122:
    print("This symbol is an alphabet")
else:
    print("This symbol is not an alphabet")