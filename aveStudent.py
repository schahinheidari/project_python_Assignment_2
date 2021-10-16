#Assignment 2

n = int(input("number of student in the class: "))
a = []

while len(a) < n:
        i = float(input("please input the marks: "))
        a.append(i)
        for i in range(n):    
            average = sum(a) / float(len(a))
        print("list of marks: ",a)

print("average in the class: ",average)
