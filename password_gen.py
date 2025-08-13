import random


# Gets random info from user
hobby = input("What is your favorite hobby?\n")
birth_year = input("What is your birth year?\n")
pet_name = input("What is your pet's name?\n")
sports_team = input("What is your favorite sports team?\n")


# List of info stored from the inputs
info_list = [hobby, birth_year, pet_name, sports_team]
values_set = {hobby, birth_year, pet_name, sports_team}

# Checks to make sure no value is repeated
while len(values_set) < len(info_list):
    print("\nThere is a duplicate value! Re-enter the info.")
    hobby = input("What is your favorite hobby?\n")
    birth_year = input("What is your birth year?\n")
    pet_name = input("What is your pet's name?\n")
    sports_team = input("What is your favorite sports team?\n")
    values_set = {hobby, birth_year, pet_name, sports_team}
    info_list = [hobby, birth_year, pet_name, sports_team]


# Puts space between the output and the password
print("\n")

# Empty list to store the randomized order of info 
printed_values = []

# List of filler characters that go between 2 pieces of info for the password
filler = ['-', '_', '.', '=', '!']

# Function to get the random info from the info_list
def in_infolist(info_list):
        info_choice = random.choice(info_list)
        info_choice = str(info_choice)
        if info_choice not in printed_values:
            info_choice = info_choice.replace("S", "$").replace("a", "@")
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