#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# readlines returns a list containing each line in the file as a list item
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
    #  string.replace() replaces a specified phrase with another specified phrase 
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        # string.strip() removes any beginning or ending spaces

PLACEHOLDER = "[name]"
with open("C:/Users/USER/PycharmProjects/DAY 24/Mail Merge Project Start/Input/Names/invited_names.txt", mode="r") as file:
    names = file.readlines()
with open("C:/Users/USER/PycharmProjects/DAY 24/Mail Merge Project Start/Input/Letters/starting_letter.txt", mode="r") as letter_cont:
    letters = letter_cont.read()
    for i in names:
        str_i = i.strip()
        new = letters.replace(PLACEHOLDER,str_i)
        with open(f"C:/Users/USER/PycharmProjects/DAY 24/Mail Merge Project Start/Output/ReadyToSend/letter_for_{str_i}", mode="w") as to_be_sent:
            to_be_sent.write(new)




# with open("c:/Users/USER/PycharmProjects/DAY 24/Mail Merge Project Start/invited_names.txt" mode="r") as file:
#     file.write(f"{self.high_score}")

# c:/Users/USER/PycharmProjects/DAY 24/Mail Merge Project Start/Input/Names/invited_names.txt

