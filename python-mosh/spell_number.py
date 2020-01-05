spelled_number = ""
word_number = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eigth",
    "9": "Nine"
}

phone = input("Phone: ")

for number in phone:
    spelled_number += word_number.get(number, "*") + " "

print(spelled_number)
