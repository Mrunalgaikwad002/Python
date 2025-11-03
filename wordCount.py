from collections import Counter

text = input("Enter a string: ").lower()
words = text.split()
count = Counter(words)

for word, freq in count.items():
    print(f"{word}: {freq}")
