#The variable called word is iqual to the string is going to be modified,
#the consecutive varible called new_word is empty and is going to storage the new modified string.

word = "Sebastian Martinez"
new_word = ""

#An if,else code block is created within a for loop, the condition is to iterate over heach
#charachter of the string and apply the methods .upper() and .lower() depending of an even or odd 
#index position and storage it on the new_word variable.

for i in range(len(word)):
    if i % 2 == 0:
        new_word += word[i].upper()
    else:
        new_word += word[i].lower()

#the variable new_word is displayed.        

print(new_word)

#the second part use the method .split(), the strings obtained are going to be
#stored as a list in to the variable split_word.
#A new variable called new_split_word is created with an empty list as a value.
#An if,else condition within a for loop is used to iterate truogh ehach element of the list,
# making it upper or lower case depending of it position.

split_word = word.split()
new_split_word = []

for i in range(len(split_word)):
    if i % 2 == 0:
        new_split_word.append(split_word[i].upper())
    else:
        new_split_word.append(split_word[i].lower())

#Lastlly .join() method is called to join with whitespaces
#  the strings elements in the variable new_split_word to proceed to displayed it.

print(" ".join(new_split_word))        