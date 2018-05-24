# Write a function that asks the user for a string containing multiple words. Print
# back to the user the same string, except with the words in backwards order. 
def reverse(x):
  y = x.split()
  return " ".join(y[::-1])