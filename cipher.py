#Cipher replacing letters with other letters

#Casear_shift moves each letter a set value to the right
def caesar_shift_en(plaintext, key):
  plaintext = plaintext.replace(" ", "")
  cipher = ""

  for i in plaintext:
    cipher += chr(ord(i) + int(key))
  
  return cipher

def caesar_shift_de(ciphertext, key):
  ciphertext = ciphertext.replace(" ", "")
  plain = ""

  for i in ciphertext:
    plain += chr(ord(i) - int(key))
  
  return plain


  