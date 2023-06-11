students = ["Ceyhun Onaç","Mahmut Abuzeroğlu","Pakize Coşkun"]



def studentAppend():
    students.append("Ediz Coşkun")
    print(students)

def studentRemove():
    students.remove("Pakize Coşkun")
    print(students)


def studentExtend():
    students.extend(["Pakize Coşkun","Mustafa Coşkun","Ahmet Tellioğlu"])
    print(students)


def studentSeparateList():
    for student in students:
        print(student)



def studentIndexList():
    i=0
    while i<len(students): 
        print(i)
        print(students[i])
        i+=1



def studentMultipleAdd():  
    i=0
    while True:
        x = int(input("Silinecek öğrenci sayısı:"))
        for i in range(x):
            removeStudent=input("Lütfen silmek istediğiniz öğrencinin adını ve soyadını yazınız:")
            students.remove(removeStudent)
        print(students)
        break      
        


print("---------------1---------------")
studentAppend()

print("---------------2---------------")
studentRemove()

print("---------------3---------------")
studentExtend()

print("---------------4---------------")
studentSeparateList()

print("---------------5---------------")
studentIndexList()

print("---------------6---------------")
studentMultipleAdd()
