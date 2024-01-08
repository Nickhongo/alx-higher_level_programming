#!/usr/bin/python3
word = "Holberton"
word_first_3, *middle_word, word_last_2 = word
print(f"First 3 letters: {''.join(word_first_3)}")
print(f"Last 2 letters: {''.join(word_last_2)}")
print(f"Middle word: {''.join(middle_word)}")
