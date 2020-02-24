# Outline:
# 1. Need to know if the ports are in a LAG
# 2. Build two different functions depending on the answer
# 3. Be able to handle many different Sections of renaming...
# 3a. This includes being able to repeat until all port names on box are complete
# 3b. All printed onto one copyable output


section = int(input("How many different name schemes to be input: "))


# This is important, say that there are ports that are being renamed to: P_LOOP_5G_GTP_OUTER
# This could be anything, like we are just adding the P_LOOP for example recently.
# This particular group of ports that are having P_Loop added are considered 1 'section' of ports
# This will also be the Dictionary Key later in the script.

#Laged Port Section
# Returns a list of strings
def LaggedPorts():
    lag_name = input("Please Enter LAG Name: ")
    rename = input("Please enter the new name for these ports: ")
    card_number = input("Card Number: ")
    print("enter 'x' to quit, Please Enter Ports")
    output = []
    UserInput = ''
    output.append("lag " + lag_name)
    while UserInput != 'x':
        UserInput = input("Port Number: ")
        if UserInput != 'x':
            output.append("port-name " + rename + ' e ' + card_number + '/' + UserInput)
        else:
            return output
        return output
# Non Lagged Section
def NonLagged():
    rename = input("Please enter the new name for these ports: ")
    card_number = input("Card Number: ")
    print("enter 'x' to quit, Please Enter Ports")
    output = []
    UserInput = ''
    while UserInput != 'x':
        UserInput = input("Port Number: ")
        if UserInput != 'x':
            output.append("interface ethernet " + card_number + '/' + UserInput)
            output.append("port-name " + rename)
        else:
            return output
        return output


# Script Structure
# Our lists of strings from LaggedPorts() and NonLagged() will be stored in a dictionary, with a key based on
# Section Number

master_dictionary = {}
master_list = [] # just trying different methods.
i = 1 # Section Counter
while i <= section:
    print("Section " + str(i))
    is_lag = input("Is this section of ports inside of a LAG? y/n: ")
    if is_lag == 'y':
        command_list = LaggedPorts()
        master_list.append(command_list)
        print("This section is now complete")
        i = i + 1
    elif is_lag == 'n':
        command_list = NonLagged()
        master_list.append(command_list)
        i = i + 1
        print("This section is now complete")
    else:
        print("Error, Try Again")

for thing in master_list:
    print(thing)



