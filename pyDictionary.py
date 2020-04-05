import difflib
import json

with open("dictionary.json") as dictionary_file:
    dictionary_obj = json.load(dictionary_file)

    print('Welcome to pyDictionary (click "Enter" twice in blank rows to exit program)')
    
    blank_count = 0
    while True:
        if(blank_count >= 2): break

        user_question = 'Enter word to look up'
        word_to_find = input('%s: ' % user_question)

        if word_to_find == '':
            blank_count += 1
        else:
            blank_count = 0

            definitions = dictionary_obj.get(word_to_find)
            if definitions == None:
                # find similar words
                print('\tCould not a definition for the provided word. Did you mean one of the following:')
                print('\t%s' % ', '.join(difflib.get_close_matches(word_to_find, dictionary_obj.keys(), n = 6)) )
            else:
                for index, definition in enumerate(definitions):
                    print('\t%s) %s' % (index, definition))
            print()