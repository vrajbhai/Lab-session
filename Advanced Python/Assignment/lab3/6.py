class Test:

    count = 0

    def __init__(self):
        Test.count += 1
        print("Constructor Called")

    def __del__(self):
        print("Destructor Called")


t1 = Test()
t2 = Test()
t3 = Test()
t4 = Test()

print("Number of reference variables =", 4)

print("\nDeleting t1 and t3")
del t1
del t3

print("Destructor called for deleted objects.")

print("\nDeleting t2 and t4")
del t2
del t4

print("Program End")