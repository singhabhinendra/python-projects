'''
-->Dictionary:Key-value pair
-->For Loop: Iterating the String
--> Strings concatenations(Addition for String)



-->Text ="This is a text"




'''

text=input("enter your jaruri sandesha");#mera kimti message hai ye

morse_code_data={
 "A": ".-",'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'
                    }

data="" #thaila
for letter in text: #iteration
    if letter in morse_code_data:
        data=morse_code_data.get(letter)##error
        
print(data)
        




