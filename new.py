import random


class ListAppend(list):
    def append(self, object):
        print("Appended Succesfully To Your List")
        # super() ==> to call the append function from the Base/Parent class which is ==> list
        super().append(object)


list1 = ListAppend()
list1.append("My")
list1.append("Name")
list1.append("is")
list1.append("Zaher")
list1.append("Abuamro")
print(list1)
