#TODO: Create a letter using starting_letter.txt
with open("Input/Letters/starting_letter.txt", "r") as letter_file:
    letter_content = letter_file.read()

#for each name in invited_names.txt
with open("Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()
#Replace the [name] placeholder with the actual name.
for name in names:
    stripped_name = name.strip()
    personalized_letter = letter_content.replace("[name]", stripped_name)
    #Save the letters in the folder "ReadyToSend".
    output_file = f"Output/ReadyToSend/{stripped_name}.txt"

    with open(output_file, "w") as output_file:
        output_file.write(personalized_letter)

    print(f"Letter created successfully for {stripped_name} in {output_file}")
    
