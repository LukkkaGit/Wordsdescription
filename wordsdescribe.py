import json
from difflib import get_close_matches

def describe(word):
    with open('data.json', 'r') as file:
        data = json.load(file)

    word = word.lower()

    if word in data:
        return data[word]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        word_list = get_close_matches(word, data.keys(), n=10)
        for index, item in enumerate(word_list, 1):
            print(f"{index}. {item}")

        option = input("Please choose an option number (or enter '99' to add a new word): ")
        option = option.strip()

        if option == "99":
            new_word = input("Enter additional word: ")
            new_description = input("Enter description: ")
            data[new_word.lower()] = [new_description]

            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)

            return [new_description]

        if option.isnumeric() and int(option) in range(1, len(word_list) + 1):
            selected_word = word_list[int(option) - 1]
            return data[selected_word]

    return ["The entered word does not exist!"]

word = input("Word: ")
output = describe(word)

for index, item in enumerate(output, 1):
    print(f"{index}. {item}")

