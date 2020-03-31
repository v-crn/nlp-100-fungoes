import re


def count_length_of_each_word(sentence):
    regex = re.compile(r'[a-zA-z]+')
    return [len(s) for s in regex.findall(sentence)]


def main():
    print('Test 1:')
    sentence = 'Now I need a drink, alcoholic of course, \
        after the heavy lectures involving quantum mechanics.'
    print(count_length_of_each_word(sentence), '\n')

    print('Test 2:')
    sentence = 'To be, or not to be: that is the question.'
    print(count_length_of_each_word(sentence), '\n')


if __name__ == '__main__':
    main()
