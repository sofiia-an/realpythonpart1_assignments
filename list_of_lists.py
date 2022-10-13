#Assignment: List of lists p100

universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

def enrollment_stats(lists):
    students = []
    tuition = []
    for data in lists:
        students.append(data[1])
        tuition.append(data[2])
    return students, tuition

lists = list(enrollment_stats(universities))


def mean(list):
    total = 0
    for num in list:
        total += num
    return int(total / len(list))

def median(list):
    list.sort()
    num = int(len(list) / 2)
    return list[num]

total_students = 0
for i in lists[0]:
    total_students += i
total_tuition = 0
for i in lists[1]:
    total_tuition += i

print("Total students:", total_students)
print("Total tuition: $", total_tuition)
print("Student mean: ", mean(lists[0]))
print("Student median:", median(lists[0]))
print("Tuition mean: $", mean(lists[1]))
print("Tuition median: $", median(lists[1]))
