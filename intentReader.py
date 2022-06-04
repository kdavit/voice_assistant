def intentReader():
    intentList = {}
    intent = ""
    with open('intents') as f:
        lines = f.readlines()
    for line in lines:
        if line[0] == '[':
            intent = line[1:-2]
            if intent not in intentList:
                intentList[intent] = []
        elif line != "\n":
            intentList[intent].append(line.strip())
    return intentList
