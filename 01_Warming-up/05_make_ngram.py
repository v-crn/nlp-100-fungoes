import re


def make_ngram(arr: [], n: int):
    """
    文字列のリストから n-gram を作成する
    """
    return [arr[i:i+n] for i in range(len(arr) + 1 - n)]


def main():
    regex = re.compile(r'[a-zA-z]+')

    print('Test 1:')
    s = 'I am an NLPer'
    word_list = regex.findall(s)
    print(make_ngram(word_list, 2))

    print('Test 2:')
    s = 'To be, or not to be: that is the question.'
    word_list = regex.findall(s)
    print(make_ngram(word_list, 3))


if __name__ == '__main__':
    main()
