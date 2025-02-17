import random
from collections import Counter
import string

def most_common_word(filename):
    """
    Reads a text file, processes it into words, 
    and returns the most frequent word along with its count.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read().lower()  # Convert to lowercase
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Split into words
    words = text.split()
    
    # Create a histogram (word frequency dictionary)
    hist = Counter(words)

    # Find the most common word
    max_word, max_count = hist.most_common(1)[0]
    
    return max_word, max_count

def mimic_dict(filename):
    """
    Reads the given file and builds a mimic dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read().lower()  # Convert to lowercase

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()
    mimic = {}
    prev = ''  # Start with an empty string

    for word in words:
        if prev not in mimic:
            mimic[prev] = [word]
        else:
            mimic[prev].append(word)
        prev = word

    return mimic

def print_mimic(mimic, word, num_words=200):
    """
    Given a mimic dictionary and a starting word, prints `num_words` of text.
    The next word is chosen randomly from the list of words that follow the current word.
    If the current word has no entry in the dictionary, it falls back to the empty string key.
    """
    for i in range(num_words):
        print(word, end=' ')  # Print the word without a newline
        next_words = mimic.get(word)

        if not next_words:  # If no next words, fallback
            next_words = mimic.get('', [])

        word = random.choice(next_words)  # Choose a random next word

    print("\n")  # Print a newline at the end

# Run the functions on shortStory.txt
filename = "shortStory.txt"

# Find most common word
word, count = most_common_word(filename)
print("Most common word:", word, "appears", count, "times")

# Build and print part of the mimic dictionary
mimic = mimic_dict(filename)
print("\nMimic dictionary (first 5 keys):")
for key in list(mimic.keys())[:5]:  # Show only first 5 for brevity
    print(f"'{key}': {mimic[key]}")

# Generate random text using the mimic dictionary
print("\nGenerated Random Text:")
print_mimic(mimic, word)  # Start with the most common word
