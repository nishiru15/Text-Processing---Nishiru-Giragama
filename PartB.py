import PartA
import sys

def main():
    #the time complexity for this is O(n) because it only goes through each files token characters once
    if len(sys.argv) <3:
        print("Need to enter in form python PartB.py <file1> <file2>")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many arguments. Need to enter in form python PartB.py <file1> <file2>")
        sys.exit(1)
    fileOne = sys.argv[1]

    fileTwo = sys.argv[2]
    try:
        tokensOne = PartA.tokenize(fileOne)
        if tokensOne is None:
            sys.exit(1)
        tokensTwo = PartA.tokenize(fileTwo)
        if tokensTwo is None:
            sys.exit(1)
        setOne = set(tokensOne) #I converted to sets here, so its easier to find which words overlap
        sharedTokens = set()
        for token in tokensTwo:
            if token in setOne:
                sharedTokens.add(token)
        print(len(sharedTokens))
    
    except FileNotFoundError:
        print("Error: File path not found")
        sys.exit(1)
    
if __name__ == "__main__":
    main()

