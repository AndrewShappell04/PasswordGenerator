import random


# Checks to make sure no value is repeated
def checker(prompt, existing_values):
    while True:
        value = input(prompt)
        if value in existing_values:
            return f"Duplicate! Please re-enter new value for {value}"
        
# Gets random info from user
hobby = checker("What is your favorite hobby?\n")
existing = [hobby]

birth_year = checker("What is your birth year?\n", existing)
existing.append(birth_year)

pet_name = checker("What is your pet's name?\n", existing)
existing.append(pet_name)

sports_team = checker("What is your favorite sports team?\n", existing)
existing.append(sports_team)

# Puts space between the output and the password
print("\n")

# List of info stored from the inputs
info_list = [hobby, birth_year, pet_name, sports_team]

# Empty list to store the randomized order of info 
printed_values = []


# List of filler characters that go between 2 pieces of info for the password
filler = ['-', '_', '.', '=', '!']

# Function to get the random info from the info_list
def in_infolist(info_list):
        info_choice = random.choice(info_list)
        if info_choice not in printed_values:
            printed_values.append(info_choice)


# Function to grab a random filler and put it in a position that is fitting
def in_fillerlist(filler):
    filler_choice = random.choice(filler)        
    if filler_choice not in printed_values:
        if filler_choice in ['-', '_', '=']:
            if len(printed_values) == 1:
                printed_values.append(filler_choice)
        elif filler_choice in ['!']:
            if len(printed_values) == 3:
                printed_values.append(filler_choice)
        else:
            printed_values.append(filler_choice)


# Repeats the function until 4 things have been added to the empty list
while len(printed_values) < 4:
    in_infolist(info_list)
    in_fillerlist(filler)


print(f"{printed_values[0]}{printed_values[1]}{printed_values[2]}{printed_values[3]}")