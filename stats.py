from collections import Counter

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    text = text.lower()
    
    char_count = Counter(text)

    char_count = {char: count for char, count in char_count.items() if char.isalpha()}
    
    return char_count

def sort_char_count(char_count):
    sorted_counts = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    
    sorted_char_count = [{"char": char, "count": count} for char, count in sorted_counts]
    
    return sorted_char_count
