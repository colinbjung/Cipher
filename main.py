# Author: Colin
# Python text-based caesar and substitution cipher

from art import logo

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
SUBCIPHER = 'niBTNZOydQgqbhWwUGmpYxIHLuPSavDjMkRzKFCVfroXEclAeJts'
MAX_KEY_SIZE = len(SYMBOLS)

# Prompts user to choose encryption/decryption and caesar/substitution
def getInfo():
    ciphertype = input("Would you like to use (C)aesar Cipher or (S)ubstitution Cipher? ")
    if ciphertype == 'S':
      mode = input("Would you like to (e)ncrypt or (d)ecrypt? ")
      message = input('Please enter your message: ')
      return subcipher(mode, message)
    elif ciphertype == 'C':
      mode = input("Would you like to (e)ncrypt or (d)ecrypt? ")
      if mode == 'd':
        mode = input("Would you like to try all decryptions? (y)es or (n)o: ")
      message = input("Please enter your message: ")
      key = 0
      if mode != 'y':
        while key < 1 or key > 52:
          key = int(input("Enter your key (1 - 26): "))
      return caesarcipher(mode, message, key)

# Substitution Cipher
def subcipher(mode, message):
  # Encryption
  if mode == 'e':
    newmessage = ''
    # Takes in each letter and substitutes with the replacement letter
    for x in message:
      if x in SYMBOLS:
        index = SYMBOLS.find(x)
        newmessage += SUBCIPHER[index]
      else:
        newmessage += x
    return newmessage
  # Decryption
  if mode == 'd':
    newmessage = ''
    # Takes each replacement letter and replaces it with the original letter
    for x in message:
      if x in SUBCIPHER:
        index = SUBCIPHER.find(x)
        newmessage += SYMBOLS[index]
      else:
        newmessage += x
    return newmessage

# Caesar Cipher (Shifting)
def caesarcipher(mode, message, key):
  # Attemps all possible shifts
  if mode == 'y':
    for keyval in range(52):
      newmessage = ''
      for x in message:
        if x in SYMBOLS:
          index = SYMBOLS.find(x)
          index += keyval
          if index >= MAX_KEY_SIZE:
            index -= MAX_KEY_SIZE
            newmessage += SYMBOLS[index] # move 
          elif index < 0:
            index += MAX_KEY_SIZE 
            newmessage += SYMBOLS[index]
          else:
            newmessage += SYMBOLS[index]
        else:
          newmessage += x
      print(newmessage)
  # Attempts a specific shift (user prompted)
  if mode == 'n':
    key = key * (-1)
  newmessage = ''
  for x in message: # SYMBOLS.find(character) -> index of character in SYMBOLS 
    if x in SYMBOLS:
      index = SYMBOLS.find(x)
      index += key
      if index >= MAX_KEY_SIZE:
        index -= MAX_KEY_SIZE
        newmessage += SYMBOLS[index] # move 
      elif index < 0:
        index += MAX_KEY_SIZE 
        newmessage += SYMBOLS[index]
      else:
        newmessage += SYMBOLS[index]  
    else:
      newmessage += x
  return newmessage
  
# Loop allows user to play again
while True:
  print(logo)
  print(getInfo())
  playAgain = input("Would you like to continue playing? (y)es or (n)o: ")
  if playAgain == 'n':
    break


