def reverse(s: str):
    """
    文字列を逆順に並べ替えて返す
    """
    result = ''
    for i in reversed(range(len(s))):
        result = result + s[i]
    return result


def reverse_with_slice(s: str):
    """
    文字列を逆順に並べ替えて返す
    """
    return s[::-1]


def main():
    s = "stressed"
    print(reverse(s))


if __name__ == '__main__':
    main()
