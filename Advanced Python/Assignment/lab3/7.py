class Test:

    def __init__(self):
        print("Constructor Called")

    def __del__(self):
        print("Destructor Called")


object_list = [Test(), Test(), Test(), Test()]

print("Deleting List...")

del object_list

print("Program End")