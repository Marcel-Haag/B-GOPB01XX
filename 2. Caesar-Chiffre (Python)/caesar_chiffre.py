#!/usr/bin/env caesar_chiffre.py
import sys

upperCaseAlphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowerCaseAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Exercise 2. a)
# python3 caesar_chiffre.py "Das ist ein Text." -3
# python3 caesar_chiffre.py "Gdv lvw hlq Whaw." 26-3
def encode_text(text, key):
    result = ""
    # True for encoding text; False for decoding text
    encode = True
    try:
        key = int(key)
        if key < 0:
            key = key * -1
    except:
        key = int(key.split('-')[1])
        encode = False

    if 0 < key < 25:
        for textCharacter in text:
            if textCharacter.isupper():
                unicodeCharacter = ord(textCharacter)
                characterIndex = unicodeCharacter - ord("A")

                # Caesar Chiffre
                if encode:
                    newIndex = (characterIndex + key) % 26
                else:
                    newIndex = (characterIndex - key) % 26

                newUnicode = newIndex + ord("A")
                newCharacter = chr(newUnicode)

                result = result + newCharacter
            elif textCharacter.islower():
                unicodeCharacter = ord(textCharacter)
                characterIndex = unicodeCharacter - ord("a")

                # Caesar Chiffre
                if encode:
                    newIndex = (characterIndex + key) % 26
                else:
                    newIndex = (characterIndex - key) % 26

                newUnicode = newIndex + ord("a")
                newCharacter = chr(newUnicode)

                result = result + newCharacter
            else:
                result += textCharacter
        return result
    else:
        print('[!!] Invalid Key for Caesar Chiffre')
        exit(1)


# Exercise 2. b)
# python3 caesar_chiffre.py "Das ist ein Text"
def string_histogram(text):
    try:
        histogramDictonary = {}
        text = text.replace(" ", "")
        if text.isalpha():
            for textCharacter in text:
                if textCharacter.isupper():
                    for character in upperCaseAlphabet:
                        indexInAlphabet = upperCaseAlphabet.index(character)
                        if lowerCaseAlphabet[indexInAlphabet] in histogramDictonary:
                            if character == textCharacter:
                                histogramDictonary[lowerCaseAlphabet[indexInAlphabet]] = histogramDictonary[lowerCaseAlphabet[indexInAlphabet]] + 1
                        else:
                            if character == textCharacter:
                                indexInAlphabet = upperCaseAlphabet.index(character)
                                newCharacterEntry = {lowerCaseAlphabet[indexInAlphabet]: 1}
                                histogramDictonary.update(newCharacterEntry)
                if textCharacter.islower():
                    for character in lowerCaseAlphabet:
                        if character in histogramDictonary:
                            if character == textCharacter:
                                histogramDictonary[character] = histogramDictonary[character] + 1
                        else:
                            if character == textCharacter:
                                newCharacterEntry = {character: 1}
                                histogramDictonary.update(newCharacterEntry)
            return histogramDictonary
        else:
            print('[!!] Text includes non alphabetic characters.')
            exit(1)
    except:
        e = sys.exc_info()[0]
        print('[!!] Unhandeld Error: ', e)
        exit(1)


# Exercise 2. c)
# python3 caesar_chiffre.py "Das ist ein Text"
def frequencies(histogram):
    frequency = []
    totalOccurrences = 0
    probableOccurrences = 0
    # histogramKey has value of appeared characters
    histogramKeys = histogram.keys()
    # histogramValues has occurrences appeared characters
    histogramValues = histogram.values()
    for occurrence in histogramValues:
        totalOccurrences = totalOccurrences + occurrence
    for zeichen in lowerCaseAlphabet:
         if zeichen in histogramKeys:
            probableOccurrences = histogram[zeichen] / totalOccurrences
            frequency.append(probableOccurrences)
         else:
            frequency.append(0)
    return frequency


# Main
if __name__ == "__main__":
    if len(sys.argv) == 2:
        textInput = sys.argv[1]
        print("Histogram:")
        histogramResult = string_histogram(textInput)
        print(histogramResult)
        print("Frequency:")
        frequenciesResult = frequencies(histogramResult)
        print(frequenciesResult)
    elif len(sys.argv) == 3:
        textInput = sys.argv[1]
        if '-' in sys.argv[2]:
            keyInput = sys.argv[2]
            caesarResult = encode_text(textInput, keyInput)
            print(caesarResult)
        else:
            encodedTextInput = sys.argv[2]
            crack_caesar(textInput, encodedTextInput)
    else:
        print('[!!] Must have at least 2 Arguments.')
        exit(1)
