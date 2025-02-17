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

# Run the function on shortStory.txt
word, count = most_common_word("shortStory.txt")
print("Most common word:", word, "appears", count, "times")
