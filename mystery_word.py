import random
words = [line.strip().lower() for line in open("words.txt").readlines()]

def mystery_word(words = words):
  word = random.choice(words)
  print ("Word has ", len(word), "characters")
  total_chances = len(word)
  chances = 0
  word_bucket = [""] * len(word)
  selected_choices = []
  while "" in word_bucket:
    value = input("Enter letter: ").lower()
    if len(value) != 1 or not value.isalpha():
      print("Invalid value. Single letters only")
      continue
    selected_choices.append(value)
    i = word.find(value)
    if i < 0:
      chances += 1
      if chances == total_chances:
        print("Ouch!. The word was ", word)
        return
      else:
        print("Nope. ", str(total_chances - chances), " chances remaining" )
    while i >= 0:
      word_bucket[i] = value
      i = word.find(value, i + 1)
    print("Word is ", ''.join([w or '_' for w in word_bucket]))
    print("Letters selected so far", ",".join(selected_choices))
  print("Yaay! you guessed it! right")

mystery_word()