#itertools is python module which is used for functional tools for creating and using iterators.
# product is a class which is used to find the Cartesian product of input iterables. Equivalent to nested for-loops.

from itertools import product   
#(module) string
#A collection of string constants.
#whitespace -- a string containing all ASCII whitespace ascii_lowercase -- a string containing all ASCII lowercase letters ascii_uppercase  and more cases.
 
import string



#password mixed with alphabet of lower case ,digits ,punctuation like ,.and 
#special symbol

characters=string.ascii_lowercase +string.digits+string.punctuation   

print(characters)
min_length=1
max_length=4
counter=0

myfile=open("passwords.txt",'w')

for i in range(min_length,max_length+1):
    for j in product(characters,repeat=i):
        word="".join(j)
        myfile.write(word+"\n")
        counter+=1


       
    
print(f"Total Password generated:{counter}")
