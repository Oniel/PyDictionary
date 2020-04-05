import json

escape = '-quit'

with open("dictionary.json") as dictionary_file:

    dictionary_obj = json.load(dictionary_file)
    
    print('Welcome to pyDictionary ( to end program enter "%s")' % escape)
    
    while True:
        user_question = 'Enter word to look up'
        word_to_find = input('%s: ' % user_question)
        if word_to_find == escape:
            break
        else:
            definitions = dictionary_obj.get(word_to_find, ['No definition could be found for the keyword "%s"' % word_to_find])
            for index, definition in enumerate(definitions):
                print('    %s) %s' % (index, definition))
            print()
