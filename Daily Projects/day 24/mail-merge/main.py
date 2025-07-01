#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
with open("/Users/Dell/Documents/python-stuff/day 24/mail-merge/Input/Letters/starting_letter.txt", mode="r") as letter_file:
    lines = letter_file.readlines(-1)
    letter_file.close()
with open("/Users/Dell/Documents/python-stuff/day 24/mail-merge/Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines(-1)
    previous_name = "[name]"
    for name in names:
        strip_name = name.strip()
        lines[0] = lines[0].replace(previous_name, strip_name)
        previous_name = strip_name
        with open(f"/Users/Dell/Documents/python-stuff/day 24/mail-merge/Output/ReadyToSend/{strip_name}.docx", mode="w") as new_letter:
            for line in lines:
                new_letter.write(line)
            new_letter.close()
    names_file.close()
    