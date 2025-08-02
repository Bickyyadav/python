students_name=[23,423,52,62,62,62,325,6236,62352,62325,10]

max_score = students_name[0]

for i in students_name:
    if i < max_score:
        max_score = i

print(max_score)