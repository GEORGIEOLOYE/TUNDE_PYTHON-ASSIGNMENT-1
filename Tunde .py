import re
 #The line of code below helps to import the re module, which stands for regular expressions. 
 #It is widely used in pattern matching and for the manipulation of strings

def file_reading_process(txt_file):
    try:
        # The code line above, Opens file txt_file in read-only mode ('r') with the application of the with statement
        # the with staement ensures the proper closure of file after reading the reading process
        with open(txt_file, 'r') as file:
            
            # the code lines below reads the whole content of the file and assigns it to the variable file_content
            # The function returns file content upon successful completion of the reading process
            file_content = file.read()
            return file_content

    # The code line below catches the FileNotFoundError exception
    except FileNotFoundError:
        print(f"File '{txt_file}' not found.")

    # The code line below catches other exceptions and prints an error message
    except Exception as exp:
        print(f"There was an error while reading the file: {str(exp)}")

        
# The code line below defines a function named read_values. It takes a single argument txt_filewhich is the path to the file
def reading_values_process(txt_file):
    
    # The code line below Initializes an empty dictionary called score_card for storing key-value pairs from the file
    score_card = {}

    # Try helps to execute the block of codes underneath it
    try:
        # The code line below Opens the txt_file in read-only mode ('r') by employing the use of the with statement
        with open(txt_file, 'r') as file:
            # The code line below iterates over each line contained in the file
            for line in file:
                # After iterating over the lines of the code, the code line below splits each line into parts by employing whitespace as a delimiter
                parts = line.split()

                # This code line checks if excactly two parts are available (key and value)
                if len(parts) == 2:
                    # The code line below extracts the key (parts[0]). Therefter, it converts the value (parts[1]) into an integer
                    key = parts[0]
                    value = int(parts[1])

                    # This code line assigns the key-value pair to the score_card dictionary
                    score_card[key] = value

    # The code line below catches the FileNotFoundError exception if the specified file is not found
    except FileNotFoundError:
        print(f"The File '{txt_file}' not found.")

    # As there may be other exceptions, the code line below catches any other exceptions and prints an error message
    except Exception as exp:
        print(f"There was an error while reading the file: : {str(exp)}")

    # The code line below returns the populated score_card dictionary. This may be empty if an error occurred.
    return score_card


# The code line below defines a function with the name, txt_abbreviator. It takes a single argument file_location, which depicts the path to the file.
def txt_abbreviation_process(file_location):
    
    # The line of code below, Try, helps in the execution of the block of code beneath it
    try:
        # The code line below helps in openning the file given by file_location in read-only mode ('r') employing the with statement
        with open(file_location, 'r') as file:
            # The code line below reads individual file lines, strip leading, trails whitespaces, and helps in storing them in the list lines
            lines = [line.strip() for line in file.readlines()]

            # The code line below returns list of lines derived
            return lines

    # The code line below Catches the FileNotFoundError exception if the specified file is not found
    except FileNotFoundError:
        print(f"The file '{file_location}' was not found.")

    # The line of code below catches any other exceptions and helps to print an error message
    except Exception as exp:
        print(f"There was an error while reading the file:: {str(exp)}")


# Generation of Abbreviations as required
# The function, convert_to_uppercase helps in converting the word_list to uppercase
def conversion_to_uppercase(word_list):
    # List comprehension: This part of the code creates a new list which contans uppercase versions of individual words in word_list
    return [word.upper() for word in word_list]

# As required by the assignment, this line of code removes non-letter characters from individual words in the word_list
def removal_of_non_alphabets(word_list):
    # The line of code below calls the remove_apostrophes function to handle apostrophe removal
    word_list = apostrophes_removal_process(word_list)
    
    # List comprehension: This creates a new list. It does this by replacing non-letter characters with a space for each word in word_list
    return [re.sub(r'[^A-Za-z]+', ' ', word) for word in word_list]

# This removes apostrophes from Individual words in the word_list
def apostrophes_removal_process(word_list):
    # This calls the convert_to_uppercase function. This ensures uniform case handling
    word_list = conversion_to_uppercase(word_list)
    
    # List comprehension: This creates a new list by replacing it with an empty string for each word in word_list
    return [word.replace("'", "") for word in word_list]

# There is need for the removal of internal spaces. The code line below joins words in the word_list. It does it by removing internal spaces
def words_joining_process(word_list):
    # List comprehension: The code line below creates a new list by joining the words without spaces. It does this for individual entries in word_list
    return [''.join(entry.split()) for entry in word_list]


# This Generates abbreviations for a list of words. It updates an abbreviation dictionary
def abbreviation_generation(word_list, abbrevs_dict):
    # The code line beow is a List to store duplicate abbreviations discovered during processing
    duplicates = []

    # The code line below iterates over each word in the word_list
    for entry in word_list:
        # The code line below generates a list of abbreviations for current word
        abbrevs_list = generation_possible_abbreviations(entry)
        # The code line below removes duplicate abbreviations. It does this by changing the list into a set and subsequently back into a list
        current_abbrevs = list(set(abbrevs_list))

        # The code line below Iterates over key-value pairs in contained in the existing abbreviation dictionary
        for key, value in abbrevs_dict.items():
            # This code line checks if the current word is not the same with the key in the dictionary
            if key != entry:
                # The code line below finds duplicate abbreviations between the current word and other entries contained in the dictionary
                duplicate_abbreviations = [abbrev for abbrev in current_abbrevs if any(abbrev in entry_value for entry_value in value)]
                
                # For making the ouput properly clear, If duplicates are found, the code line below prints a message and add them to the duplicates list
                if duplicate_abbreviations:
                    print(f'Duplicate Abbreviations found in "{entry}" and "{key}": {duplicate_abbreviations}')
                    duplicates.extend(duplicate_abbreviations)

        # This code line updates the abbreviation dictionary using the abbreviations obtained for the current word
        abbrevs_dict[entry] = current_abbrevs

    # The code line below returns the updated abbreviation dictionary and subsequently, a sorted list of unique duplicates
    return abbrevs_dict, sorted(list(set(duplicates)))


# The function generates every possible combination of three-letter abbreviations that are applicable for any given word
def generation_possible_abbreviations(word):
    abbreviations = []
    # The code line below extracts the first letter of the word
    first_letter = word[0]
    
    # The code line below iterates over the indices of the word commencing from the second character
    for i in range(1, len(word)):
        # This code line Iterates over the indices following the current character
        for j in range(i + 1, len(word)):
            # The code line below creates a three-letter abbreviation applying the first letter with two other characters
            abbreviation = first_letter + word[i] + word[j]
            
            # The code line below helps to check if the abbreviation derived does not have any space
            if ' ' not in abbreviation:
                # The code line below helps to add the abbreviation to the list
                abbreviations.append(abbreviation)
                
    return abbreviations

# The function below removes duplicate entries from an abbreviation dictionary, using a list of duplicates
def removal_duplicates_from_entries(duplicates, abbreviations_dict):
    # The code line below iterates over individual duplicate entry
    for duplicate_entry in duplicates:
        # The code line below iterates over key-value pairs contained in the abbreviation dictionary
        for key, value in abbreviations_dict.items():
            # The code line below checks if duplicate entry is contained in the list of abbreviations for the current key
            if duplicate_entry in value:
                # The code line below removes duplicate entries from abbreviation list
                value.remove(duplicate_entry)

    return abbreviations_dict

# The code line below generates a relative index map for individual characters contained in a given string
def word_index(input_string):
    char_map = {}
    accumulator = 0

    # This section of the code iterates over individual characters in the input string
    for char in input_string:
        # The code line below handles the first character separately by setting the accumulator to 0
        if char == input_string[0]:
            accumulator = 0
        # The code line below sets the accumulator to -1 when spaces are encountered or when the last character is encounered
        elif char == ' ':
            accumulator = -1
        elif input_string[-1] == char:
            accumulator = -1
        # The code lines below increments the accumulator for the other characters
        else:
            accumulator += 1
        
        # The code line below creates or updates the character map with the character and their respective relative index
        if char not in char_map:
            if char != ' ':
                char_map[char] = [accumulator]
        else:
            char_map[char].append(accumulator)
    
    return char_map


# The code line below helps to get the respective indices of characters contained an abbreviation within a result dictionary
def get_respective_index(result, abbreviation):
    # This code line initializes an empty list to store the respective indices of characters contained in the abbreviation
    abbreviation_indexes = []

    # The code line below iterates over individual characters contained in the abbreviation
    for char in abbreviation:
        # The code line below checks if the character is present in the result dictionary
        if char in result:
            # The code line below retrieves the list of respective indices for the current character
            char_indexes = result[char]

            # The code line below checks if indices remains for the current character
            if char_indexes:
                # The code line below retrieves the first index and add it to the list of abbreviation indices
                index = char_indexes[0]
                abbreviation_indexes.append(index)

                # The code line below updates the list of indices for the current character, and removes the used index
                result[char] = char_indexes[1:]

    # The code line below returns the list of respective indices for characters in the abbreviation
    return abbreviation_indexes


# The function below calculates scores for the abbreviations using a score card and a dictionary of abbreviations
def calculation_scores_abbreviations(score_card, abbrevs_dict):
    # The code line below initializes an empty dictionary for storing final scores
    final_score = {}

    # The code line below iterates over individual word and its corresponding abbreviations in the dictionary
    for word, abbreviations in abbrevs_dict.items():
        # The code line below initializes an empty dictionary for storing scores for individual abbreviation for the current word
        word_scores = {}

        # The code line below iterates over individual abbreviations for the current word
        for abbreviation in abbreviations:
            # The code line below converts the word and abbreviation to uppercase for matching in a case-insensitive manner
            abbreviation = abbreviation.upper()
            word = word.upper()
            print(word)
            
            # The code line below gets the respecive indices of characters in the word
            indexes = word_index(word)
            # The code line below gets the respective indices of characters contained in the abbreviation
            abbreviationIndexes = get_respective_index(indexes, abbreviation)
            print(abbreviationIndexes)
            
            # The code line below initializes the scores for each position contained in the abbreviation
            first_score = 0
            second_score = 0
            third_score = 0

            # The code line below calculates the second_score for the second letter contained in the abbreviation
            second_letter = abbreviationIndexes[1]
            if second_letter == 0:
                second_score = 0
            elif second_letter == -1:
                if abbreviation[1] == 'E':
                    second_score = 20
                else:
                    second_score = 5
            elif second_letter == 1:
                second_score = 1 + score_card.get(abbreviation[1], 0)
            elif second_letter == 2:
                second_score = 2 + score_card.get(abbreviation[1], 0)
            else:
                second_score = 3 + score_card.get(abbreviation[1], 0)
            
            # The code line below calculates the third_score for the third letter contained in the abbreviation
            third_letter = abbreviationIndexes[2]
            if third_letter == 0:
                third_score = 0
            elif third_letter == -1:
                if abbreviation[2] == 'E':
                    third_score = 20
                else:
                    third_score = 5
            elif third_letter == 1:
                third_score = 1 + score_card.get(abbreviation[2], 0)
            elif third_letter == 2:
                third_score = 2 + score_card.get(abbreviation[2], 0)
            else:
                third_score = 3 + score_card.get(abbreviation[2], 0)

            # The code line below calculates the total score for the abbreviation
            total_score = first_score + second_score + third_score
            print(abbreviation)
            print(second_score)
            print(third_score)
            print("\n")
            # The code line below stores the score for the current abbreviation contained in the word_scores dictionary
            word_scores[abbreviation] = total_score

        # The code line below stores the scores for all abbreviations of current word in the final_score dictionary
        final_score[word] = word_scores

    # The code line returns the final dictionary of word scores
    return final_score

# The Function below's purpose is to assign entries to dictionary keys. This ensures that each entry has a corresponding key
def assign_entries_2_dictionary_keys(entry_list, target_dict):
    assigned_dict = {}
    
    # The code line below iterates over individual entry contained in the entry list
    for i, entry in enumerate(entry_list):
        # The code line below checks if there are enough keys in the target dictionary
        if i < len(target_dict):
            # The code line gets the key corresponding to current index contained in the target dictionary
            key = list(target_dict.keys())[i]
            # The code line below assigns the entry to the key in the assigned dictionary
            assigned_dict[key] = entry
        else:
            # The code line below prints a message if there are not enough keys in the target dictionary for the entries
            print(f"There is Not enough keys in the dictionary for entry: {entry}")
            
    # The code line below returns the assigned dictionary
    return assigned_dict

# The Main function below helps to execute the generation of abbreviation process.
def main():
    # The code line below prompts users to enter the name of the file that they want to read
    file_name = input("Enter the name of the file to read: ")
    # The code line below reads the content of the specified file
    file_reading = file_reading_process(file_name)
    
    # The code line below checks if the file content was read successfully
    if file_reading:
        # The code line below reads the score card values from a separate file
        value_score = reading_values_process("values.txt")
        
        # The code line below reads the abbreviations from the specified file location
        abb_file = txt_abbreviation_process(file_name)
        # The code line below removes non-alphabetic characters from the abbreviations
        final_abb_file = removal_of_non_alphabets(abb_file)
                
        # The code line initializes dictionaries for storing abbreviations and their duplicates
        final = {}
        test, duplicates = abbreviation_generation(final_abb_file, final)
        
        # The code line below removes duplicate abbreviations from previously generated abbreviations
        result_dict = removal_duplicates_from_entries(duplicates, test)
        
        # The code line below Scores the abbreviations using the provided score card
        scores = calculation_scores_abbreviations(value_score, result_dict)
        
        # The code line below specifies the output file name based on inputted file name
        output_file = f"Tunde_{file_name.split('.')[0]}_abbrevs.txt"
        
        # The code line below Writes the scores to the output file
        with open(output_file, 'w') as output_file:
            for word, word_scores in scores.items():
                output_file.write(word + ":\n")
                for abbreviation, score in word_scores.items():
                    output_file.write(f"  {abbreviation}: {score}\n")
                output_file.write("\n")
        
        print(f"Output written to {output_file}")

# The code below executes the main function if the script is run as the main module
if __name__ == "__main__":
    main()
