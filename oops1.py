class employee:
    def __init__(self):
        print("Constructor called")
        self.id = 101
        self.salary = 10000
        self.designation = "Manager"
        print("Employee created")

    def travel(self,destination):
        print("Travelling to")
        print("Travelling to",destination)


sam = employee()
#print(sam.salary)
sam.travel("New York")

print(type(sam))