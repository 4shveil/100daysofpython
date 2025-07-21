# numbers = [1 , 2, 3]

# new_numbers = [num + 1 for num in numbers]

# print(new_numbers)

# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

# new_list = [x * 2 for x in range(1,6)]
# print(new_list)

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# short_names = [name.upper() for name in names if len(name) > 4]
# print(short_names)

student_scores = {
    "Alex": 51,
    "Beth": 72,
    "Caroline": 62,
    "Dave": 81,
    "Eleanor": 38,
    "Freddie": 89,
}

passed_students = {key:value for (key, value) in student_scores.items() if value >= 60}

print(passed_students)
