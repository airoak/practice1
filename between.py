first = raw_input("First digit: ")
last = raw_input("Last digit: ")

for i in range(int(first)+1,int(last)):
    if i % 2 == 1:
        print i
