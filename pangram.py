def pangram(sentence):
 normalisestring = "".join(char.lower()for char in sentence if char.isalpha())
 unique_char = set(normalisestring)
 if len(unique_char) == 26:
  print("It is a pangram")
 else:
  print("It is not a pangram")
pangram("abcdefghijklmnopqrstuvwxyz")