import re


def get_atominc_number(sentence):
    result = {}
    pos_single_char_atomic_symbol = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    regex = re.compile(r'[a-zA-z]+')
    word_list = regex.findall(sentence)
    for i, word in enumerate(word_list):
        if i + 1 in pos_single_char_atomic_symbol:
            result[word[0]] = i + 1
        else:
            result[word[:2]] = i + 1
    return result


def main():
    print('Test 1:')
    sentence = 'Hi He Lied Because Boron Could Not Oxidize Fluorine.\
        New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
    print(get_atominc_number(sentence), '\n')

    print('Test 2:')
    sentence = 'To be, or not to be: that is the question.'
    print(get_atominc_number(sentence), '\n')


if __name__ == '__main__':
    main()
