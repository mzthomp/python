word = input()
password = ''

characters = {'i': '1', 'a': '@', 'm': 'M', 'B': '8', 's': '$'}
length = len(word)

print(length)
for x in range(length):
    letter = word[x]
    if letter in characters:
        new_letter = characters [letter]    
        password += new_letter
    else:
        password += letter
print(password)
