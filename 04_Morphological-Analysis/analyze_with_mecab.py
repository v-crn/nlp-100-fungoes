def analyze_with_mecab(input_filename: str, output_filename: str) -> None:
    """
    日本語の文章ファイルを mecab で形態素解析してファイルに保存する.
    - input_filename: 日本語の文章ファイル名
    - output_filename: 形態素解析ファイル名
    """
    import MeCab

    mecab = MeCab.Tagger("-O chasen")
    with open(input_filename, encoding='utf-8') as input_file:
        with open(output_filename, mode='w', encoding='utf-8') as output_file:
            output_file.write(mecab.parse(input_file.read()))


def main():
    import config as c

    print('形態素解析ファイルの作成')
    analyze_with_mecab(c.PAHT_DATA_RAW, c.PAHT_DATA)


if __name__ == '_mecabain__':
    main()
