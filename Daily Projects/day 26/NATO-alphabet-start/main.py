student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data = pd.read_csv("/Users/Dell/Documents/python-stuff/day 26/NATO-alphabet-start/nato_phonetic_alphabet.csv")
dict = {row.letter:row.code for (_, row) in data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
desired_input = input("Write anything: ").upper()

output = [dict[letter] for letter in desired_input]
print(output)
