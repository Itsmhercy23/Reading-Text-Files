# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

"""

Problem
1.  Download the Starter Project here. You can follow the steps outlined in the guidelines. --

2.  Open “main.py”, and complete the function “read_file_content”. 
It should accept a filename as an argument and read the text contained in that file. 
It should return a string.

3.  Complete the function “count_words”. 
It uses “read_file_content” to read the text contained in “story.txt”. 
It should return a dictionary whose keys are unique words, 
and their values the count of those words in the text e.g {“as”:10, “would”:5}.


Algorithm - Steps to solve the problem
 - 

 >> - append -  allows you add to content in a file
 > - insert/write - It overwrite whats is in  the content
 echo 'Hello' >>  file.txt
 echo 'World' >  file.txt


file.txt
------------------------
Hello

 ________

 file readin
"""

def read_file_content(filename):
    # [assignment] Add your code here 
    text = []
    with open(filename) as f:
        text = f.readlines()
    print(f"1. {text}")
    for idx, line in enumerate(text):
        text[idx] = line.replace('\n','').strip()
    print(f"2. {text}")
    return " ".join(text)


def count_words():
    text = read_file_content("./story.txt")
    print(f"3 {text} \n\n")
    # [assignment] Add your code here
    wordMap = {}

    for word in text.split(' '):
        if word not in wordMap:
            wordMap[word] = 0
        wordMap[word] += 1 
    return wordMap

def main():
    print(count_words())                            

main()