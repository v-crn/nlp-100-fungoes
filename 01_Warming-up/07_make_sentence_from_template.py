def make_sentence_from_template(x, y, z):
    """
    「x時のyはz」という文字列を返す
    """
    return '{}時の{}は{}'.format(x, y, z)


def main():
    x = 12
    y = "気温"
    z = 22.4
    print(make_sentence_from_template(x, y, z))


if __name__ == '__main__':
    main()
