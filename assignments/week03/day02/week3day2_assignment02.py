dict1 = {'apple': 12, 'orange': 25, 'mango': 9} 
dict2 = {'apple': 100, 'mango': 200, 'orange': 300} 
for key in dict2: 
    if key in dict1: 
        dict2[key] = dict2[key] + dict1[key] 
    else: 
        pass
          
print(dict2) 