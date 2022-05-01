# Author: Emil Gomez
# Course: CSc 110
# Description: This function takes in a file from the user and returns a
# infogrpahic of how many unique words there are, the small/medium/large
# words that appear the most. It also shows the ratio of small/medium/large
# based on how much they appear. In addition the infographic shows the ratio
# of capitalized and non capitalized words, and the ratio of punctuated and
# non punctuated words.
from graphics import graphics

def counting_words(words):
    '''
This function loops through the list of all the words in the text file and
adds it to a dictionary with the key being the word and the value being the
number of times it appears in the text file.
    :param words:List of all the words in the text file.
    :return:This returns the dictionary made in the function.
    '''
    words_dict = {}
    for word in words:
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1
    return words_dict
def word_sizes(dictionary):
    '''
    This function loops through the dictionary and checks if the word is either small,
    medium or large. There is a count for each size of word. It also gets the most appeared
    sized word.
    :param dictionary:The dictionary made from the list of words
    :return:This returns a string containing the most appeared word for each size and how
    many times they appear.
    '''
    #All the variables for the count of the word, and a value set to compare the values of
    #the dictionary.
    small_total = 0
    small_value = 0
    medium_total = 0
    medium_value = 0
    large_total = 0
    large_value = 0
    #Looping through the dictionary and checking each word to see it's size and then finding the
    #word that appears the most based on if the value in the dictionary is the largest.
    for word, occ in dictionary.items():
        if len(word) <= 4:
            small_total += 1
            if dictionary[word] >= small_value:
                small_word = word
                small_value = occ
        elif 5 <= len(word) <= 7:
            medium_total += 1
            if dictionary[word] >= medium_value:
                medium_word = word
                medium_value = occ
        else:
            large_total += 1
            if dictionary[word] >= large_value:
                large_word = word
                large_value = occ
    return (small_word + ' (' + str(small_value) + 'x) ' + medium_word + ' (' +
            str(medium_value) + 'x) ' + large_word + ' (' + str(large_value) + 'x)'), small_total, medium_total, large_total

def capitalized(unique_set):
    '''
    This function loops through the set of words in the file and counts how many
    capitalized and non capitalized words there are. We loop through the set so we
    dont get duplicate words.
    :param unique_set: This is the set created in the other function of all the
    words.
    :return: This function returns the count for the capitalized and non capitalized
    words.
    '''
    #Create the two counts.
    count = 0
    non_count = 0
    #Loop through the set and add to the count if there is a capital word,
    # and if not add to the non capital count.
    for word in unique_set:
        if word[0].isupper():
            count += 1
        else:
            non_count += 1
    return count, non_count
def punctuation(unique_set):
    '''
    This function does the same as the capitalize function and it just checks
    at the end of a word instead of the front. It checks for the three punctuation
    points that are used.
    :param unique_set: This is the set created in the other function of all the
    words.
    :return:
    '''
    #Make a count for both punctuated and non punctuated words.
    count = 0
    non_punct = 0
    #Loop through the set and check the end of a word if it has punctuation.
    for word in unique_set:
        if word[-1] == '.' or word[-1] == '!' or word[-1] == '?':
            count += 1
        else:
            non_punct += 1
    return count, non_punct
def unique(words):
    '''
    This function makes a set from the lists of words in the file
    to check the total amount of unique words.
    :param words: This is the list of words from the file.
    :return: This returns the actual set, and the length of the set.
    '''
    #Create empty set.
    unique_set = set()
    #Loop through the list and add each word.
    for word in words:
        unique_set.add(word)
    return unique_set, len(unique_set)
def graphics_text(file, gui, unique_len, occurences):
    '''
    This function creates the grey background for the canvas, and it also
    draws all the needed text on to the screen.
    :param file: Name of the file
    :param gui: This is the gui canvas
    :param unique_len: The length of the set
    :param occurences: This is the entire string of all the sized words
    and how many times they occur.
    :return: This draws the grey background and all the text needed.
    '''
    gui.rectangle(0, 0, 800, 800, 'grey')
    gui.text(50, 35, file, 'aqua', 20)
    gui.text(50, 80, 'Total Unique Words: ' + str(unique_len), 'white', 20)
    gui.text(50, 125, 'Most used words (s/m/l): ', 'white', 10)
    gui.text(200, 125, occurences, 'aqua', 10)
    gui.text(50, 160, 'Word Lengths', 'white', 23)
    gui.text(300, 160, 'Cap/Non-Cap', 'white', 23)
def word_length_chart(small_length, medium_length, large_length, gui):
    '''
    This draws all the rectangles to make show the ratio of all the sized words.
    The function draws the rectangles at the length of how many pixels there are
    divided by the amount of unique words there are and then multiplied by the amount
    of the sized words there is.
    :param small_length: Variable for the length calculated in main.
    :param medium_length: Variable for the length calculated in main.
    :param large_length: Variable for the length calculated in main.
    :param gui: The gui canvas.
    :return:
    '''
    gui.rectangle(48, 198, 204, 454, 'black')
    gui.rectangle(50, 200, 200, small_length, 'blue')
    gui.text(50, 200, 'small words', 'white', 10)
    y = 200 + small_length
    gui.rectangle(50, y, 200, medium_length, 'green')
    gui.text(50, y, 'medium words', 'white', 10)
    y2 = y + medium_length
    gui.rectangle(50, y2, 200, large_length, 'blue')
    gui.text(50, y2, 'large words', 'white', 10)
def capitalized_chart(gui, capitalized_length, noncap_length):
    '''
    This function draws the rectangles for the ratio of capitalized words
    to non capitalized words. Similar to the function above it draws the
    rectangle length based on the pixel length divided by the amount of unique
    words and then multiplied by the amount of capitalized or non capitalized words.
    :param gui: The gui canvas.
    :param capitalized_length: Variable for the length of each rectangle based on
    the math given to us on the spec
    :param noncap_length: Variable for the length of each rectangle based on
    the math given to us on the spec
    :return: This draws two rectangles which show the ratio of capitalized to
    non capitalized words
    '''
    gui.rectangle(298, 198, 204, 454, 'black')
    gui.rectangle(300, 200, 200, capitalized_length, 'blue')
    gui.text(300, 200, 'Capitalized', 'white', 10)
    gui.rectangle(300, 200 + capitalized_length, 200, noncap_length, 'green')
    gui.text(300, 200 + capitalized_length, 'Non Capitalized', 'white', 10)
    gui.text(550, 160, 'Punct/Non-Punct', 'white', 23)
def puncuation_chart(gui, punct_length, nonpunct_length):
    '''
    This function is exactly like the capitalized function just for the ratio
    of puncuated and non punctuated words.
    :param gui: The gui canvas.
    :param punct_length:Variable for the length calculated in main
    :param nonpunct_length: Variable for the length calculated in main
    :return: This draws the ratio of punctuated to non punctuated words
    with two rectangles.
    '''
    gui.rectangle(548, 198, 204, 454, 'black')
    gui.rectangle(550, 200, 200, punct_length, 'blue')
    gui.text(550, 200, 'Punctuated', 'white', 10)
    gui.rectangle(550, 200 + punct_length, 200, nonpunct_length, 'green')
    gui.text(550, 200 + punct_length, 'Non Punctuated', 'white', 10)
def main():
    '''
    This is the main function that creates variables which are set equal to
    things that are returned by functions. It first ask the user for an input
    and then calls other functions.
    :return:
    '''
    #Ask user for the file and then open the file. Loop through the file and create
    # a list of all the words
    file = input('What file would you like the infographic created for: \n')
    open_file = open(file, 'r')
    words = []
    for line in open_file:
        new_line = line.strip('\n').split()
        for word in new_line:
            words.append(word)
    #Set variables equal to whatever the functions created return, so it can be used in
    #graphics later
    dictionary = counting_words(words)
    unique_set, unique_len = unique(words)
    occurences, small_total, medium_total, large_total = word_sizes(dictionary)
    punct_count, non_count = punctuation(words)
    #Create all the lengths for each rectangle by using the math given in the spec.
    small_length = (450/unique_len * small_total)
    medium_length = (450/unique_len * medium_total)
    large_length = (450/unique_len * large_total)
    cap_count, non_cap = capitalized(unique_set)
    capitalized_length = (450/len(unique_set) * cap_count)
    noncap_length = (450/len(unique_set) * non_cap)
    punct_length = (450/len(unique_set) * punct_count)
    nonpunct_length = (450/unique_len * (unique_len - punct_count))
    #Create gui canvas and then call all the graphics functions to draw out the
    #whole infogrpahic
    gui = graphics(800, 800, 'Infographic')
    while True:
        gui.clear()
        graphics_text(file, gui, unique_len, occurences)
        word_length_chart(small_length, medium_length, large_length, gui)
        capitalized_chart(gui, capitalized_length, noncap_length)
        puncuation_chart(gui, punct_length, nonpunct_length)
        gui.update_frame(30)


main()
