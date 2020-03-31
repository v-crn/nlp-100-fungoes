def extract_even_pos(s: str):
    """
    文字列の奇数番目の文字を抽出して連結した文字列を返す
    """
    result = ''
    for i, v in enumerate(s):
        if i % 2 != 0:
            result += v
    return result


def extract_even_pos_with_slice(s: str):
    """
    文字列の奇数番目の文字を抽出して連結した文字列を返す
    """
    return s[::2]


def main():
    s = "パタトクカシーー"
    print(extract_even_pos(s))


if __name__ == '__main__':
    main()
