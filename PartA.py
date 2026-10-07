def tokenize(textFilePath: str):
    tokens = []
    curr = []

    try:
        with open(textFilePath, 'r', encoding = 'utf-8') as file:
            for line in file:
                for char in line:
                    if char.isalnum():
                        curr.append(char.lower())
                    elif curr:
                        tokens.append(curr)
                        curr = []

            if curr:
                tokens.append(curr)

        except FileNotFoundError:
            print("Error: File path not found")

        return tokens

def computeWordFrequencies(tokenList):
    tokenOccs = {}
    for token in tokenList:
        tokenOccs[token]+=1
        
    return tokenOccs

