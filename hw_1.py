from collections import Counter
import re

fn = './Book.txt'
book = None

#Wrap  the file handling in a try except block
try:  
    book = open(fn)
    words = []
    for line in book.readlines():
        row = re.findall(r"\w+", line.lower())
        words.extend(row) 
    
    words_quantity = Counter(words)
    
    #sorting primarly "by value" - descending and secondary "by key" - ascending
    print(sorted(words_quantity.items(), key = lambda t: (-t[1], t[0])))
    
except (IOError, OSError):
    print("Could not read file", fn)   
    
except FileNotFoundError:
    print("File not found", fn)
    
finally:
    if book is not None:
        book.close()
