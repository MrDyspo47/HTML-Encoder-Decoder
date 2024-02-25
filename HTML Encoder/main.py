import time 
logo = """
                                  
                                         
 _____     ____                  ___ ___ 
|     |___|    \ _ _ ___ ___ ___| | |_  |
| | | |  _|  |  | | |_ -| . | . |_  | | |
|_|_|_|_| |____/|_  |___|  _|___| |_| |_|
                |___|   |_| 

Type -h for help !             

"""
print(logo)

VALUES = {
    " " : "%20",
    "!" : "%21",
    "\"" : "%22",
    "#" : "%23",
    "$" : "%24",
    "%" : "%25",
    "&" : "%26",
    "\'" :"%27",
    "(" : "%28",
    ")" : "%29",
    "*" : "%2A",
    "+" : "%2B",
    "," : "%2C",
    "-" : "%2D",
    "." : "%2E",
    "/" : "%2F",
    "0" : "%30",
    "1" : "%31",
    "2" : "%32",
    "3" : "%33",
    "4" : "%34",
    "5" : "%35",
    "6" : "%36",
    "7" : "%37",
    "8" : "%38",
    "9" : "%39",
    ":" : "%3A",
    ";" : "%3B",
    "<" : "%3C",
    "=" : "%3D",
    ">" : "%3E",
    "?" : "%3F",
    "@" : "%40",
    "A" : "%41",
    "B" : "%42",
    "C" : "%43",
    "D" : "%44",
    "E" : "%45",
    "F" : "%46",
    "G" : "%47",
    "H" : "%48",
    "I" : "%49",
    "J" : "%4A",
    "K" : "%4B",
    "L" : "%4C",
    "M" : "%4D",
    "N" : "%4E",
    "O" : "%4F",
    "P" : "%50",
    "Q" : "%51",
    "R" : "%52",
    "S" : "%53",
    "T" : "%54",
    "U" : "%55",
    "V" : "%56",
    "W" : "%57",
    "X" : "%58",
    "Y" : "%59",
    "Z" : "%5A",
    "[" : "%5B",
    "\\" : "%5C",
    "]" : "%5D",
    "^" : "%5E",
    "_" : "%5F",
    "`" : "%60",
    "a" : "%61",
    "b" : "%62",
    "c" : "%63",
    "d" : "%64",
    "e" : "%65",
    "f" : "%66",
    "g" : "%67",
    "h" : "%68",
    "i" : "%69",
    "j" : "%6A",
    "k" : "%6B",
    "l" : "%6C",
    "m" : "%6D",
    "n" : "%6E",
    "o" : "%6F",
    "p" : "%70",
    "q" : "%71",
    "r" : "%72",
    "s" : "%73",
    "t" : "%74",
    "u" : "%75",
    "v" : "%76",
    "w" : "%77",
    "x" : "%78",
    "y" : "%79",
    "z" : "%7A",
}


updatedstr = ""

while True:
    user_input = input("$ : ")

    if user_input.lower() == "encode" or user_input.lower() == "-e" :
        text_to_enc = input("Enter Text : ")
        time.sleep(1)
        print("Encoding ...")
        time.sleep(1)
        for letter in text_to_enc: # Iterates through every letter in the users input
                updatedstr += VALUES[letter] # Adds the key value for character to encode the users input
        print(f"Encoded String : {updatedstr}")


    if user_input.lower() == "decode" or user_input.lower() == "-d":
        
        text_to_dec = input("Enter Text : ") 
        time.sleep(1)
        print("Decoding ...")
        decoded_str = ""
        a = 0
        b = 3
        while b <= len(text_to_dec):
            substring = text_to_dec[a:b] # Splits the users input into strings of 3 characters
            if substring in VALUES.values(): # checks if the set of 3 characters are in the values of the dictionary
                for key, value in VALUES.items(): #Gets all the keys and values
                    if value == substring: # Looks for the corresponding character to the html encoded text
                        decoded_str += key # Adds it to a string so it can be displayed in one proper sentence
            else:
                 decoded_str += substring

            a += 3
            b += 3
        time.sleep(1)
        print(f"Decoded String : {decoded_str}")

       


    if user_input.lower() == "help" or user_input.lower() == "-h" :
         
        helpvar = """

-e or encode : To encode 
-d or decode : To decode
-q or quit : To leave the program
-h or help : To show this message
        """
        print(helpvar)
    if user_input.lower() == "quit" or user_input.lower() == "-q" :
        break