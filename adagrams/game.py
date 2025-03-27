from random import randint

def draw_letters():

    letter_pool = {
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

    weighted_letter_bag= []
    for letter, frequency in letter_pool.items():
        weighted_letter_bag += letter * frequency

    hand_of_letters = []
    MAX_HAND_SIZE = 10
    
    while len(hand_of_letters) < MAX_HAND_SIZE:
        number = randint(0, len(weighted_letter_bag) - 1)
        letter = weighted_letter_bag[number]

        if letter_pool[letter] > 0:
            hand_of_letters.append(letter)
            letter_pool[letter] -= 1
    
    return hand_of_letters

def uses_available_letters(word, letter_bank):

    letter_bank_frequency = {}
    for letter in letter_bank:
        if letter in letter_bank_frequency:
            letter_bank_frequency[letter] += 1
        else:
            letter_bank_frequency[letter] = 1
    
    for letter in word.upper():
        if letter in letter_bank_frequency and letter_bank_frequency[letter] > 0:
            letter_bank_frequency[letter] -= 1
        else:
            return False
    return True
    

def score_word(word):

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

    for letter in word.upper():
        if letter in score_chart:
            points += score_chart[letter]

    if 7 <= len(word) <= 10:
        points += 8

    return points

def get_highest_word_score(word_list):
    
    winner_word =''
    top_score = 0
    if not word_list:
        return winner_word, top_score
    
    best_words = []
    for word in word_list:
        score = score_word(word)

        if score > top_score:
            top_score = score
            best_words = [word]

        elif score == top_score:
            best_words.append(word)

    if len(best_words) == 1:
        return best_words[0], top_score
    
    winner_word = best_words[0]
    for word in best_words:
        if len(word) == 10:
            return word, top_score
        elif len(word) < len(winner_word):
            winner_word = word
    
    return winner_word, top_score
