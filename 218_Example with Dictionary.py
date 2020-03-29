# dictionaries - 6000

print("*** Creating the dictionary ***")

def lyrics_to_frequencies(lyrics):  # Sets first function to count how many...
                                    #... times each word appears in the song.
    myDict = {}                     # creates and empy dictionary
    for word in lyrics:             # This for loop looks through each string...
        if word in myDict:          #... and adds each key with the number of ...
            myDict[word] += 1       #... times it appears as the value.  If ...
        else:                       #... it has already seen the word it adds...
            myDict[word] = 1        #... to the value alrady in place
    return myDict                   # Returns the result in myDict

she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',

'you', 'think', "you've", 'lost', 'your', 'love',
'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
"it's", 'you', "she's", 'thinking', 'of',
'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'she', 'said', 'you', 'hurt', 'her', 'so',
'she', 'almost', 'lost', 'her', 'mind',
'and', 'now', 'she', 'says', 'she', 'knows',
"you're", 'not', 'the', 'hurting', 'kind',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',

'you', 'know', "it's", 'up', 'to', 'you',
'i', 'think', "it's", 'only', 'fair',
'pride', 'can', 'hurt', 'you', 'too',
'pologize', 'to', 'her',

'Because', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'Yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'yeah', 'yeah', 'yeah',
'yeah', 'yeah', 'yeah', 'yeah'
]

beatles = lyrics_to_frequencies(she_loves_you)  # Sets the variable beatles to ...
                                                #... myDict of the song "She...
                                                #... Loves you"

print(beatles)                                 # Simply prints the myDict ...
                                                #... as a test.
print("*** Using the Dictionary just created ***")

def most_common_words(freqs):       # Function designed to use the dictionary...
    values = freqs.values()         #... values now stored in beatles, used to ...
    mostWords = max(values)         #... which value is highest from dict
    words = []                      # Creates an empty list called words
    for k in freqs:                 # This funciton loops through the myDict...
        if freqs[k] == mostWords:   #... to determine which key matches the...
            words.append(k)         #... highest variable number, it then adds...
    return (words, mostWords)       #... it to the words list, then returns words...
                                    #... and the mostWords values

def words_often(freqs, minTimes):   # This function takes in the arguments of ...
    result = []                     #... the frequency of words and set the ...
    done = False                    #... threshold above the minTimes. It does...
    while not done:                 #... by taking the top used song first, ...
        temp = most_common_words(freqs) #... adding it to the result, and then...
        if temp[1] >= minTimes:     #... deleting it off the temp list. It then...
            result.append(temp)     #... repeats the process until all of the...
            for w in temp[0]:       #... words above the threshold have been ...
                del(freqs[w])       #... placed on the result list.
        else:
            done = True
    return result

print(words_often(beatles, 15))     # The final print shows all of the words that...
                                    #... that appeared more than minTimes.
