student_heights= input("input a list of student height ").split()
for n in range(0, len(student_heights)):
    student_heights[n]=int(student_heights[n])
print(student_heights)
total_height =0
for height in student_heights:
    total_height+=height

avarage_height = total_height/len(student_heights)
print(f"Avarage height: {round(avarage_height)}")