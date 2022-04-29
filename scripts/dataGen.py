import random

extensions = ['.pdf', '.docx', '.ppt', '.txt', '.xls']
wordBank = ['mage', 'lightning', 'gypsy', 'randy', 'nasty', 'educated', 'bottom', 'text', 'dragon', 'scimitar', 'guy']


for x in range(25, random.randint(30, 75)):
    file = open(wordBank[random.randint(0, len(wordBank))-1] + wordBank[random.randint(0, len(wordBank))-1] + extensions[random.randint(0, len(extensions))-1], "w")
    for i in range(10, random.randint(30, 200)):
        file.write("if you ever feel safe, remember im out there\r\n")
    file.close()
