from random import randint

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}

def draw_letters():

    letter_pool_copy = dict(LETTER_POOL)
    letter_pool_keys_list = list(letter_pool_copy.keys())
    letter_pool_length = len(letter_pool_keys_list)

    hand_list = []
    counter = 0
    length_of_hand_list = 10
    
    while counter < length_of_hand_list:

        number = randint(0, letter_pool_length - 1)
        letter = letter_pool_keys_list[number]

        if letter_pool_copy[letter] > 0:
            hand_list.append(letter)
            letter_pool_copy[letter] -= 1
            counter += 1

    return hand_list


def uses_available_letters(word, letter_bank):

    word_uppercase = word.upper()
    letter_bank_copy = letter_bank.copy()
    
    word_availabe = True
    for letter in word_uppercase:
        if letter not in letter_bank_copy:
            word_availabe = False
            break
        else:
            letter_bank_copy.remove(letter)

    return word_availabe


def score_word(word):

    word_uppercase = word.upper()

    score_chart = {
        'A': 1, 
        'E': 1, 
        'I': 1, 
        'O': 1, 
        'U': 1, 
        'L': 1, 
        'N': 1, 
        'R': 1, 
        'S': 1, 
        'T': 1, 
        'D': 2, 
        'G': 2, 
        'B': 3, 
        'C': 3, 
        'M': 3, 
        'P': 3, 
        'F': 4, 
        'H': 4, 
        'V': 4, 
        'W': 4, 
        'Y': 4, 
        'K': 5, 
        'J': 8, 
        'X': 8, 
        'Q': 10, 
        'Z': 10
    }

    points = 0

    for letter in word_uppercase:
        if letter in score_chart:
            points += score_chart[letter]

    if len(word) in [7, 8, 9, 10]:
        points += 8

    return points

def get_highest_word_score(word_list):
    
    tuple_word_sore = ()
    winner_word =''
    max_score = 0
    tuple_word_sore = (winner_word, max_score)
    if not word_list:
        return tuple_word_sore
    
    # Create a dictionary that maps each word in word_list to its score
    word_score_dict = {}
    for word in word_list:
        score = score_word(word)
        word_score_dict[word] = score

    # Find the highest score(s) in the dictionary values
    for key, value in word_score_dict.items():
        if word_score_dict[key] > max_score:
            winner_word = key
            max_score= word_score_dict[key]

    # Count the total number of maximum scores
    number_of_highest_score = 0
    for key, value in word_score_dict.items():
        if value == max_score:
            number_of_highest_score +=1

    temp_length = 0
    first_time = True
    # If there is only one winner, return the tuple
    if number_of_highest_score == 1:
        tuple_word_sore = (winner_word, max_score)
        return tuple_word_sore
    # If there are ties (multiple winners), determine the winner based on word length
    else:
        for word, score in word_score_dict.items():
            if score == max_score:
                word_length = len(word)
                if word_length == 10:
                    winner_word = word
                    break
                else:
                    if first_time:
                        winner_word = word
                        temp_length = word_length
                        first_time = False
                    else:
                        if word_length < temp_length:
                            winner_word = word
                            temp_length = word_length

    tuple_word_sore = (winner_word,max_score)
    return tuple_word_sore