import random


def random_sort_word(word: str) -> str:
    """
    文字列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替える。
    ただし，長さが４以下の単語は並び替えない。
    """
    result = word
    if len(word) > 4:
        result = word[0] + \
            ''.join(random.sample(word[1:-1], k=len(word) - 2))\
            + word[-1]
    return result


def random_sort(s: str) -> str:
    """
    スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替える。ただし，長さが４以下の単語は並び替えない。
    """
    return ' '.join(random_sort_word(s) for s in s.split())


def main():
    print('Test 1')
    s = "wonderful"
    print(random_sort_word(s))

    print('\nTest 2')
    s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(random_sort(s))


if __name__ == '__main__':
    main()
