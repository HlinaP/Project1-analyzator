"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Petr Hlisnikovský
email: hlisnikovskyp@gmail.com
discord: bG.#6985
"""
import sys
from task_template import TEXTS 

# paragraph separator
separator = "----------------------------------------"

# registered users
users= {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
# number of texts
nr_of_texts = len(TEXTS)

# login information
username = input("username:")
password = input("password:")

print(separator)

if username in users and users[username] == password:
    print(f"Welcome to the app, {username} \
          \nWe have {nr_of_texts} texts to be analyzed. \
          \n{separator}"
          )
else:
    print("unregistered user, terminating the program..")
    sys.exit() # this command terminates the program

# select text 1 to nr_of_texts
choice = (input(f"Enter a number btw. 1 and {nr_of_texts} to select: "))

print(separator)

if choice.isdigit():
    choice = int(choice)
    if choice in range(1, nr_of_texts + 1):
        selected_text = TEXTS[choice - 1]

        words = selected_text.split()
        total = [] # variable for sum of numbers in text

        # the number of words
        nr_of_words = len(words)

        # number of words starting with a capital letter
        titlecase = sum(1 for word in words if word.istitle())

        # number of capitalized words
        uppercase = sum(1 for word in words if word.isalpha() \
                        and word.isupper())
        
        # number of words written in lowercase letters
        lowercase = sum(1 for word in words if word.islower())

        # number of numbers (not digits)
        numeric_string = sum(1 for word in words if word.isdigit())

        # the sum of all numbers (not digits) in the text
        for word in words:
            if word.isdigit():
                total.append(int(word))
                sum_of_numbers = sum(total)

        print(f"There are {nr_of_words} words in the selected text.")
        print(f"There are {titlecase} titlecase words.")
        print(f"There are {uppercase} uppercase words.")
        print(f"There are {lowercase} lowercase words.")
        print(f"There are {numeric_string} numeric strings.")
        print(f"The sum of all the numbers {sum_of_numbers}")
        print(separator)

        occur_of_words = {} # frequency of different word lengths in the text

        for word in words:
            word = word.strip(".,")
            lenght = len(word)
            if lenght not in occur_of_words:
                occur_of_words[lenght] = 1
            else:
                occur_of_words[lenght] += 1

        max_count = max(occur_of_words.values())

        print(f"LEN|{('OCCURENCES'):^{max_count}}|NR.") # table header
        print(separator)

        for wr_lenght, frequency in sorted(occur_of_words.items()):

            print(f"{wr_lenght:3}|{('*' * frequency):{max_count}}|{frequency}")


    else:
        print("wrong number, terminating the program..")
else:
    print("invalid choice, terminating the program..")