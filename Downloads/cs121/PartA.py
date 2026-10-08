import sys
def tokenize(textFilePath: str):
    #the time complexity for this is O(n) because each character is only being iterated through once
    tokens = [] #token list
    curr = [] #current token

    try:
        with open(textFilePath, 'r', encoding = 'utf-8', errors = 'ignore') as file: #opens file in read
            for line in file: 
                for char in line: #for every line, it reads each individual character and checks if it is alphanumerical
                    if ('a'<= char <= 'z') or ('A' <= char <= 'Z') or ('0' <= char <= '9'):
                        curr.append(char.lower()) #if the character is alphanumerical, it turns it to lowercase, and adds it to the current token
                    elif curr:
                        tokens.append("".join(curr)) #if the character is not alphanumerical it combines the curr list into one string, and adds it to the tokens list
                        curr = []

            if curr: #this adds any leftover word stored in curr
                tokens.append("".join(curr))

    except FileNotFoundError:  #this handles if the user enters an invalid file
            print("Error: File path not found")
            return None

    return tokens

def computeWordFrequencies(tokenList):
    #the time complexity is O(n) because each token in is only being iterated once
    tokenOccs = {}
    for token in tokenList: #goes through each token, and adds 1 to the value of the token, or otherwise creates a key with a value of one if it doesn't exist
        if token in tokenOccs:
            tokenOccs[token]+=1
        else:
            tokenOccs[token] =1
        
    return tokenOccs

def printFreq(frequencies):
    #the time complexity is O(nlogn) because each item in frequencies is only being iterated through once
    sortedFreq = sorted(frequencies.items(), key = lambda x: (-x[1], x[0])) #sorts the items in frequencies, and prints each key and value with '->' seperating them
    for key, value in sortedFreq:
        print(key + " -> " + str(value))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Need to enter in form python PartA.py <file>")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many arguments. Need to enter in form python PartA.py <file>")
        sys.exit(1)

    file = sys.argv[1]
    tokens = tokenize(file)
    frequencies = computeWordFrequencies(tokens)
    printFreq(frequencies)
