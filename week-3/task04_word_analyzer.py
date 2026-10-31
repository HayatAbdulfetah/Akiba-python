def clean_text(text):
    punctuation = ".,!?;:"
    cleaned = ""
    for char in text:
        if char not in punctuation:
            cleaned += char
        else:
            cleaned += " "
    return cleaned

def count_words(paragraph):
    cleaned_paragraph = clean_text(paragraph)
    words = cleaned_paragraph.split()
    word_count = 0
    for word in words:
        word_count += 1
    return word_count

def count_character(paragraph):
    character_count = 0
    for letter in paragraph:
        if letter != " " and letter != "\n":
            character_count += 1
    return character_count

def count_vowel_and_consonant(paragraph):
    vowels = ["a", "e", "i", "o", "u"]
    vowel_count = 0
    consonant_count = 0
    for letter in paragraph.lower():
        if letter in vowels:
            vowel_count += 1
        elif letter.isalpha():
            consonant_count += 1
    return vowel_count, consonant_count

def find_longest_word(paragraph):
    cleaned_paragraph = clean_text(paragraph)
    words = cleaned_paragraph.split()
    if not words:
        return ""
        
    longest_word = words[0]
    for word in words:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word

def get_word_frequencies_and_top_5(paragraph):
    cleaned_paragraph = clean_text(paragraph)
    words = cleaned_paragraph.lower().split()
    
    unique_words = []
    frequencies = []

    # Count how many times each word appears
    for word in words:
        if word not in unique_words:
            # Count appearances
            count = 0
            for other_word in words:
                if word == other_word:
                    count += 1
            
            unique_words.append(word)
            frequencies.append([word, count])

    # Challenge: Sort to get the top 5 most frequent words
    # A simple bubble sort that matches your style!
    for i in range(len(frequencies)):
        for j in range(0, len(frequencies) - i - 1):
            if frequencies[j][1] < frequencies[j + 1][1]: 
                # Swap them
                temp = frequencies[j]
                frequencies[j] = frequencies[j + 1]
                frequencies[j + 1] = temp

    top_5 = frequencies[:5]
    return frequencies, top_5

def find_repeated_words(paragraph):
    cleaned_paragraph = clean_text(paragraph)
    words = cleaned_paragraph.lower().split()
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

# 1. Run all your functions to gather data
total_words = count_words(paragraph)
total_chars = count_character(paragraph)
vowels, consonants = count_vowel_and_consonant(paragraph)
longest = find_longest_word(paragraph)
all_frequencies, top_5_words = get_word_frequencies_and_top_5(paragraph)
repeated = find_repeated_words(paragraph)

print("=========================================")
print("             TEXT ANALYSIS               ")
print("=========================================")
print(f"Total Words        : {total_words}")
print(f"Total Characters   : {total_chars} (no spaces)")
print(f"Vowels Count       : {vowels}")
print(f"Consonants Count   : {consonants}")
print(f"Longest Word       : {longest}")

if len(repeated) > 0:
    repeated_string = ", ".join(repeated)
else:
    repeated_string = "None"
print(f"Repeated Words     : {repeated_string}")

print("-----------------------------------------")
print("          TOP FREQUENT WORDS             ")
print("-----------------------------------------")
for item in top_5_words:
    word = item[0]
    count = item[1]
    print(f" * '{word}' appears {count} time(s)")
print("=========================================")
