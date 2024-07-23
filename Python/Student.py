class Student:
    def __init__(self):
        pass

    def avg(self, name, list):
        sum =0
        average = 0
        for value in list:
            sum += value
        average = sum/len(list)
        return average

obj = Student()

print("averge of list is :" , obj.avg("naman", [1,2,3,4, 5]))
