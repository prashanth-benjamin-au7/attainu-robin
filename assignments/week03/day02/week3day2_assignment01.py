def dictionairy():  

 key_marks ={}     
  

 key_marks[2] = 56       
 key_marks[1] = 2 
 key_marks[5] = 12 
 key_marks[4] = 24
 key_marks[6] = 18      
 key_marks[3] = 323 
  
 print ("\n") 
 print ("Keys are") 
   
 
 for i in sorted (key_marks.keys()) :  
     print(i, end = " ") 
  
def main(): 
   
    dictionairy()              
      

if __name__=="__main__":       
    main() 