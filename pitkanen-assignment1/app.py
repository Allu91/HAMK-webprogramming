# Aleksi Pitkänen – HAMK Web-ohjelmointi, assignment 1
import json


# The default data for the dictionary
default_data = {"words": [
        {"english": "parrot","finnish": "papukaija"},
        {"english": "mouse","finnish": "hiiri"},
        {"english": "bunny","finnish": "pupu"},
        {"english": "dog","finnish": "koira"},
        {"english": "monkey","finnish": "apina"},
        {"english": "cat","finnish": "kissa"}]
}


# Function for the main menu
def main_menu():
    print("Dictionary application. Start by choosing app-mode.")

    # As long as user input is invalid...
    while True :
        # Keep asking for the input
        mode_select = input("Press [1] to search, [2] to add new word: ").lower()
        
        # Input for application search mode
        if mode_select == "1" or mode_select == "[1]" or mode_select == "one" :
            print("Entering search mode...\n")
            search_dictionary('dictionary.json')
            break
        # Input for application word addition mode
        elif mode_select == "2" or mode_select == "[2]" or mode_select == "two" :
            print("Entering addition mode...\n")
            add_to_dictionary('dictionary.json')
            break
        # Input for exiting the application
        elif mode_select == "exit" or mode_select == "quit" :
            print("Exiting application...")
            quit()
        # Inform the user of invalid input
        else :
            print('\nInvalid input. Please press [1] or [2] to select mode. Press "exit" to quit application.')



# Function for checking the dictionary existance
def check_dictionary(the_file) :

    # Check if dictionary.json exists
    try:
        open(the_file, "r")
        print("(Dictionary exists)\n")

    # If dictionary file doesn't exist, initialize one with default data
    except OSError:

        # Attemp to create a new file
        try:
            with open(the_file, "w") as write_file:
                json.dump(default_data, write_file, indent=4)
                print("(No dictionary file found.", the_file, "created)\n")

        # If unsuccessfull...
        except OSError:
            print("Unable to create new file. Disk space full? Dictionary-file deleted? Try to free some space.")



# Function for searching a word
def search_dictionary(the_file) :

    # As long as user input is not valid...
    while True:

        # Input the key value that you want to search
        keyval = input("Enter a word to search (english or finnish): ").lower()

        # If input left empty; return to main menu
        if keyval == "":
            print("Returning to main menu...\n")
            main_menu()
            break

        # Check if search is whitespace – return to input
        elif keyval.isspace():
            print('Search query left empty. Please try again\n')

        # If search input is valid...
        else:
            
            # Open the dictionary file
            with open(the_file) as json_file:

                # load the json data
                data = json.loads(json_file.read())
                json_object = data["words"]


                # Run the query function
                def search_word(word) :
                    for keys in json_object:

                        # Search the english key value
                        if word == keys['english']:
                            # Return the value of the corresponding translation key
                            return keys['finnish']

                        # Search the english key value
                        elif word == keys['finnish'] :
                            # Return the value of the corresponding translation key
                            return keys['english']



                # Check the return value and print success message
                if (search_word(keyval) != None):
                    print("Found the word \"", keyval, '\". Translation is: \"', search_word(keyval), '\"\n', sep='')

                else:
                    # If word could not be found, print failure message and continue while-loop
                    print("Could not find the word: \"", keyval, '\". Please try another word.\n', sep='')



# Function for adding a new word
def add_to_dictionary(the_file) :

    # Add new english word by user input
    new_word_en = input("Insert a new word in english: ").lower()

    # Check if input is empty or whitespace and return to main menu
    if new_word_en == "" or (new_word_en.isspace()):
        print('Returning to main menu...\n')
        main_menu()

    # Continue and ask for translation for the word
    else:
        
        # As long as user input is not valid...
        while True:

            # Keep asking for the finnish translation
            new_word_fi = input("Insert the translation in finnish: ").lower()

            # Check if finnish translation is empty or whitespace – return to input
            if new_word_fi == '' or new_word_fi.isspace():
                print('Translation left empty – please try again. Type "exit" to quit application.')

            # Check if user inputs "exit" – break the while loop and return to main menu
            elif new_word_fi == "exit":
                print("Returning to main menu...\n")
                main_menu()
                break

            # If user input passes all previous error checks...
            else:

                # Open file and append new data
                with open(the_file) as json_file:

                    # Select file and json object-name
                    data = json.load(json_file)
                    json_object = data["words"]

                    # Create data and append to json object
                    json_addition = {"english": new_word_en, "finnish": new_word_fi}
                    json_object.append(json_addition)
                
                # Attempt to write new data to json file...
                try :
                    with open(the_file,'w') as f: json.dump(data, f, indent=4)

                    # If succesfull, inform user with a message
                    print('Successfully added a new english word: \'', new_word_en, '\', with finnish translation: \'', new_word_fi, '\'', sep='')
                    print("Returning to main menu...\n")

                    # Return to main menu and break the while loop
                    main_menu()
                    break

                # If not succesfull
                except OSError :
                    print("Unable to save new word. Disk space full? Dictionary-file deleted? Try to reopen application or free some space.")


                
            
            

# On app startup; check the dictionary json-file existance and open main menu
check_dictionary('dictionary.json')
main_menu()
