import json

with open("dictionary.json") as dictionary_file:
    dictionary_obj = json.load(dictionary_file)
    while True:
        user_question = 'Enter word to look up (enter "-quit" to exit)'
        word_to_find = input('%s: ' % user_question)

        if word_to_find == 'quit.':
            break
        else:
            definitions = dictionary_obj.get(word_to_find)
            if definitions == None:
                print('    No definition could be found for the keyword "%s"' % word_to_find)
            else:

                for index, definition in enumerate(definitions):
                    print('    %s) %s' % (index, definition))
                print()
