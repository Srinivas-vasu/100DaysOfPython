student_scores=input("enter the student scores").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
highest_score=0
for i in student_scores:
    if i>highest_score:
        highest_score=i
print(f"The highest score in the class is : {highest_score}")

