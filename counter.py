# program to count the number of words in a user given text

# Step-1: introduction for the program in heading 

print("\n\n**************** WELCOME TO WORD COUNT PROGRAM***************")
print("---------------------------------------------------------------\n")

# Step-2: Take the input from the user either its a sentence or a paragraph

sentence=input("Enter your text to check for count of words :\n \n")
print("\n your entered text is :\n\n\t",sentence)

 # this will check weather user has given any text or not vy using strip function
if sentence.strip() == "":
    print("You didn't enter any text.\n Please enter the text......")
else:
    # Step-3: Convert your text into list using split() function

    list=sentence.split()

    # Step-4: find the length of the list using len() function

    length=len(list)

    # Step-5: This is the final step print the length of the list

    print(f"\n The total number of words in the given text is: { length}") 
print()
print()
