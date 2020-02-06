string = 'Python is a widely used high-level, general-purpose, interpreted, dynamic programming language.' 
dict = {}
for letter in string:
     dict[letter] = dict.get(letter, 0) + 1
print(dict)
