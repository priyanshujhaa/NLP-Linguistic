import re

# To tokenize sentences into words
def tokenize(data):
  word = []
  word = re.split('; |, |\*|\n| ',data)
  return word
	