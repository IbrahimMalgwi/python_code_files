score = int(input("Enter score: "))

if score >= 70:
    print("A")
elif 60 <= score <= 69:
    print("B")
elif 50 <= score <= 59:
    print("C")
elif 45 <= score <= 49:
    print("D")
elif 40 <= score <= 44:
    print("E")
else:
    print("F")