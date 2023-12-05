from string import ascii_lowercase as alphabet

def caeser(c):
  shift_by = 3
  c = c.lower()

  if c not in alphabet:
    return c
  idx_shift=(alphabet.index(c) + shift_by)%len(alphabet)

  print(f"{alphabet.index(c)} {len(alphabet)}")

  return alphabet[idx_shift]

def remove_punctuation(word):
  return word.strip("!?.:;,'\"()- ")

quote = """On a visit to the NASA space center, President Kennedy spoke to a man sweeping \
up in one of the buildings.  "What's your job here?" asked Kennedy.  "Well Mr. President," \
the janitor replied, "I'm helping to put a man on the moon"."""

words = quote.split()

print(list(map(remove_punctuation, words)))

remove_punctuation = lambda w: w.strip("!?.:;,'\"()- ")
print(" ".join(map(remove_punctuation, words)))

print(caeser('c'))
