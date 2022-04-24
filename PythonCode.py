import re
import string

def printsomething():
    print("Hello from python!")

def PrintMe(v):
    print("You sent me: " + v)
    return 100;

def SquareValue(v):
    return v * v

def listItemNFrequency(): #function listItemFrequency goes through the text file and counts the amount of times a word is present. Displays and lists them all
    wordFrequency = {}
    documentText = open('Input_File.txt', 'r')
    textString = documentText.read().lower()
    matchPattern = re.findall(r'\b[a-z]{3,15}\b', textString)
    for word in matchPattern:
        itemCount = wordFrequency.get(word,0)
        wordFrequency[word] = itemCount + 1
     
    frequencyList = wordFrequency.keys()
 
    for words in frequencyList:
        print(words.capitalize(),wordFrequency[words])

def itemFrequency(v): #function itemFrequency takes in user input and displays the amount of time it is present in the document
    file = open("Input_File.txt", "r")
    data = file.read()
    occurrences = data.count(v.capitalize())

    print('Number of occurrences of the word :', occurrences)
       

def Histogram(): #function Histogram takes the words and their counts and displays it in a text based graph
    wordFrequency = {}
    documentText = open('Input_File.txt', 'r')
    textString = documentText.read().lower()
    matchPattern = re.findall(r'\b[a-z]{3,15}\b', textString)
    for word in matchPattern:
        itemCount = wordFrequency.get(word,0)
        wordFrequency[word] = itemCount + 1
        
    frequencyList = wordFrequency.keys()

    
    print("\nFile Histogram: \n")

    print("Counts|   Words      |Frequency")
    print("---------------------------------------------------------------------------------")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    for words in frequencyList:
        numStr = words.ljust(11, ' ')
        if(wordFrequency[words] < 10):
            print(' ', wordFrequency[words], "  |\t", numStr.capitalize(),"|", end = ' ')
        else:
            print(' ', wordFrequency[words], " |\t", numStr.capitalize(),"|", end = ' ')
        for i in range(0,wordFrequency[words]):
                print('=', end = ' ')
        print("\n")
    print("\t\t      +--------------+--------------+--------------+-------------+")
    print("\t\t       1 2 3 4 5 6 7 8 9 11 12 13 14 15 16 17 18 19 20 21 22 23 24")
   
 

    
