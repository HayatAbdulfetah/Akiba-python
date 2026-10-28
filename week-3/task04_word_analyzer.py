
def count_words(paragraph):
    words = paragraph.split()
    word_count = 0
    for word in words:
        word_count += 1

    return word_count

def count_character(paragraph):
    character_count = 0
    for letters in paragraph.lower():
        if letters.isalpha():
            character_count+=1
        else:
            continue

    return character_count

def count_vowel_and_consonant(paragraph):
    vowels = ["a","e","i","o","u"]
    vowel_count = 0
    consonant_count = 0
    for letter in paragraph.lower():
        if letter in vowels:
            vowel_count += 1
        elif letter.isalpha():
            consonant_count += 1
            
    return vowel_count,consonant_count

def longest_word(paragraph):
    words=paragraph.split()
    longest_word=words[0]
    for word in words:
        if len(word)>len(longest_word):
            longest_word=word

    return longest_word
    
def count_repeated_words(paragraph):
    words = paragraph.lower().split()
    checked_words = []

    for word in words:
        if word not in checked_words:
            count = 0

            for other_word in words:
                if word == other_word:
                    count += 1

            checked_words.append(word)
            print(f"{word}: {count}")

def find_repeated_words(paragraph):
    words = paragraph.lower().split()
    checked_words = []
    repeated_words = []

    for word in words:
        if word in checked_words:
            if word not in repeated_words:
                repeated_words.append(word)
        else:
            checked_words.append(word)

    return repeated_words


paragraph = "Python is useful and Python is powerful."
print(count_words(paragraph))
print(count_character(paragraph))
print(count_vowel_and_consonant(paragraph))
print(longest_word(paragraph))
print(count_repeated_words(paragraph))
print(find_repeated_words(paragraph))