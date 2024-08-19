def analyze_text(sentence):
    words = sentence.split()
    num_words = len(words)
    
    num_digits = sum(char.isdigit() for char in sentence)
    num_uppercase = sum(char.isupper() for char in sentence)
    num_lowercase = sum(char.islower() for char in sentence)
    
    return num_words, num_digits, num_uppercase, num_lowercase


sentence = input("Enter a sentence: ")


words, digits, uppercase, lowercase = analyze_text(sentence)
print(f"Number of words: {words}")
print(f"Number of digits: {digits}")
print(f"Number of uppercase letters: {uppercase}")
print(f"Number of lowercase letters: {lowercase}")
