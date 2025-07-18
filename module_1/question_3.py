user_input = input("Enter a sequence of whitespace separated words:")
words = user_input.split()
unique_words = list(dict.fromkeys(words))
sorted_output = " ".join(sorted(unique_words))
print(sorted_output)

 #hello world and practice makes perfect and hello world again
