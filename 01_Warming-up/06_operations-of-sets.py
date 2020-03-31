def make_ngram(arr: [], n: int):
    """
    文字列のリストから n-gram を作成する
    """
    return [arr[i:i+n] for i in range(len(arr) + 1 - n)]


def main():
    print('Test 1:')
    x = 'paraparaparadise'
    y = 'paragraph'

    print('和集合')
    print(set(make_ngram(x, 2)) | set(make_ngram(y, 2)))

    print('積集合')
    print(set(make_ngram(x, 2)) & set(make_ngram(y, 2)))

    print('差集合')
    print(set(make_ngram(x, 2)) - set(make_ngram(y, 2)))

    print("'se'というbi-gramがXおよびYに含まれるか")
    print('se' in (set(make_ngram(x, 2)) | set(make_ngram(y, 2))))


if __name__ == '__main__':
    main()
