student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

sum_heights=0

for i in student_heights:
    sum_heights+=i

total_students=0
for i in student_heights:
    total_students+=1


avg_height=sum_heights/total_students
print(round(avg_height ))
