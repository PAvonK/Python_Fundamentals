# dictionaries - 6000, functions - 5000, iteration - 2000,
#   branching - 1000

"""
The purpose of this program is to take in the lyrics to a song and then
tell you what words are used over x number of times, currently set to 10
"""

print("*** Creating the dictionary ***")

string = input("Enter here the String that you would like parsed and counted:")


splitString = string.split()

def lyrics_to_frequencies(lyrics):  # Sets first function to count how many...
                                    #... times each word appears in the song.
    myDict = {}                     # creates and empy dictionary
    for word in lyrics:             # This for loop looks through each string...
        if word in myDict:          #... and adds each key with the number of ...
            myDict[word] += 1       #... times it appears as the value.  If ...
        else:                       #... it has already seen the word it adds...
            myDict[word] = 1        #... to the value alrady in place
    return myDict                   # Returns the result in myDict

workingSong = splitString

wordfrequency = lyrics_to_frequencies(workingSong)  # Sets the variable wordfrequency to ...
                                                #... myDict of the song "She...
                                                #... Loves you"

print(wordfrequency)                                 # Simply prints the myDict ...
                                                #... as a test.
print("*** Using the Dictionary just created ***")

def most_common_words(freqs):       # Function designed to use the dictionary...
    values = freqs.values()         #... values now stored in wordfrequency, used to ...
    mostWords = max(values)         #... which value is highest from dict
    words = []                      # Creats a empty list called words
    for k in freqs:                 # This funciton loops through the myDict...
        if freqs[k] == mostWords:   #... to determine which key matches the...
            words.append(k)         #... highest variable number, it then adds...
    return (words, mostWords)       #... it to the words list, then returns words...
                                    #... ad the mostWords values

def words_often(freqs, minTimes):   #
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
        else:
            done = True
    return result

print(words_often(wordfrequency, 10))
