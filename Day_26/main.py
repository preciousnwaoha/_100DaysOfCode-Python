student_dict = {
  "student": ["Angela", "James", "Lily"],
  "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
  print(value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Precious":
        print(row.score)
