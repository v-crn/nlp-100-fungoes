def encrypt(s: str) -> str:
    """
    与えられた文字列の各文字を，以下の仕様で変換する。
    - 引数の文字（列）が英小文字ならば(219 - 文字コード)の文字に置換
    - その他の文字はそのまま出力
    """
    return ''.join(chr(219 - ord(c)) if 'a' <= c <= 'z' else c for c in s)


def decrypt(s: str):
    return encrypt(encrypt(s))


def main():
    s = 'If I had words to make a day for you, I\'d sing you a morning golden and new.'
    print('Encrypt:', encrypt(s))

    print('Decrypt:', decrypt(s))


if __name__ == '__main__':
    main()
