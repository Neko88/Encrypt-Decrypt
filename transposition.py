#Scrambling text into a pattern
import math

#rail_fence turns plaintext into a zigzag and combines each line
def rail_fence_en(plaintext):
  plaintext = plaintext.replace(" ","")
  first_half = ""
  second_half = ""
  for i in range(len(plaintext)):
    if i%2 == 0:
      first_half += plaintext[i]
    else:
      second_half += plaintext[i]
  return first_half + second_half

def rail_fence_de(cipher):
  split = math.ceil(len(cipher)/2)
  first_half = cipher[:split]
  second_half = cipher[split:]
  count = 0
  plain_text = ""

  for i in range(len(cipher)):
    if i%2 == 0:
      plain_text += first_half[count]
    else:
      plain_text += second_half[count]
      count += 1
  return plain_text

#red_fence is like rail_fence but with more zig zags and with a key
def red_fence_en(plaintext, key):
  plaintext = plaintext.replace(" ","")
  
  length = len(key)
  rows = {}
  for i in range(length):
    rows[i+1] = ""
  
  down = True
  current_row = 0

  for i in range(len(plaintext)):
    rows[current_row+1] += plaintext[i]

    if down:
      current_row += 1
    else:
      current_row -= 1

    if current_row == 0:
      down = True

    elif current_row == length-1:
      down = False
    
    cipher_text = ""

    for i in key:
      cipher_text += rows[int(i)] 

  return cipher_text

def red_fence_de(ciphertext, key):
  lengths = {}
  rows = {}

  for i in key:
    lengths[int(i)] = 0
    rows[int(i)] = ""
  
  down = True
  cycle = 0

  for i in ciphertext:

    if down:
      cycle += 1
    else:
      cycle -= 1
    
    if cycle == 1:
      down = True

    if cycle == len(key):
      down = False

    lengths[cycle] += 1
  
  start = 0
  end = 0

  for i in key:
    end = start + lengths[int(i)]
    rows[int(i)] = ciphertext[start:end]

    start = end

  down = True
  cycle = 1
  top_bot = 0
  mid = 0

  plaintext = ""

  for i in range(len(ciphertext)):
    if cycle == 1:
      down = True
      plaintext += rows[cycle][top_bot]
      if top_bot != 0:
        mid += 1

    elif cycle == len(key):
      down = False
      plaintext += rows[cycle][top_bot]
      top_bot += 1
      mid += 1
    
    else:       
      plaintext += rows[cycle][mid]
    
    if down:
      cycle += 1
    else:
      cycle -= 1

  return plaintext
  



#four winds makes text into a wheel 
def four_winds_en(plaintext, key):
  plaintext = plaintext.replace(" ","")
  split_1 = ""
  split_2 = ""
  split_3 = ""
  cycle = 0

  for i in range(len(plaintext)):
    if i + 1 - cycle*4 == 1:
      split_1 += plaintext[i]

    elif i + 1 - cycle*4 == 2:
      if key == "Clockwise":
        split_2 += plaintext[i]
      else:
        split_3 += plaintext[i]

    elif i + 1 - cycle*4 == 3:
      split_1 += plaintext[i]

    else:
      if key == "Clockwise":
        split_3 += plaintext[i]
      else:
        split_2 += plaintext[i]
      cycle += 1
  
  return split_2 + split_1 + split_3

def split_creator(cipher, first, second, key):
  split_2 = cipher[first:second]
  if key == "Clockwise":
    split_1 = cipher[:first] 
    split_3 = cipher[second:]

  else:
    split_1 = cipher[second:]
    split_3 = cipher[:first]
  
  return split_1, split_2, split_3


def four_winds_de(cipher, key):
  #The cycle for four winds is split2,split1,split2,split3
  split_1 = ""
  split_2 = ""
  split_3 = ""
  split = int(len(cipher) / 4)
  if len(cipher)% 4 == 0 or len(cipher)%4 == 1 :    
    split_1, split_2, split_3 = split_creator(cipher, split, -split, key)
  else:
    split_1, split_2, split_3 = split_creator(cipher, split+1, -split, key) 
  
  cycle = 0
  plaintext = ""
  cycled_mid = 0

  for i in range(len(cipher)):
    if i + 1 - cycle*4 == 1:
      plaintext += split_2[cycle + cycled_mid]
      cycled_mid += 1       
              
    elif i + 1 - cycle*4 == 2:
      plaintext += split_1[cycle]

    elif i + 1 - cycle*4 == 3:
      plaintext += split_2[cycle + cycled_mid]

    else:
      plaintext += split_3[cycle]

      cycle += 1

  return plaintext

#Complete Columnar - Plain text is written in columns
def complete_columnar_en(plaintext, key):
  columns = []

  for i in range(len(key)):
    columns.append("")
  
  cycle = 0
  for i in plaintext:
    columns[cycle] += i
    
    if cycle == len(key)-1:
      cycle = 0
    else:
      cycle += 1
    
  sorting = {}
  cycle = 0
  for i in key:
    sorting[int(i)] = columns[cycle]
    cycle += 1

  ciphertext = ""

  for i in range(1, len(key)+1):
    ciphertext += sorting[i]
    
  return ciphertext

def complete_columnar_de(ciphertext, key):
  columns = {}

  extra = len(ciphertext) % len(key)
  split = len(ciphertext) // len(key)

  start = 0
  end = 0

  for i in range(len(key)):
    end = start + split

    if key.find(str(i+1)) <= extra - 1:
      end += 1
    
    columns[i+1] = ciphertext[start:end]

    start = end

  plaintext = ""

  cycle = 0
  for i in range(len (columns[int(key[-1])] ) ):
    for j in key:
      plaintext += columns[int(j)][cycle]

    cycle += 1
  
  for i in range(extra):
    plaintext += columns[int(key[i])][-1]    

  
  return plaintext
