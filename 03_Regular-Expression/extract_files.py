import re

import config as c
from load_json_gz import load_json_gz


def extract_files(text):
    """
    以下の filename において2番目の要素にファイル名が格納されている。3,4番目要素はオプション情報。
    """
    return [filename[1] for filename in re.findall(r'\[\[(File|ファイル):([^]|]+?)(\|.*?)+\]\]', text)]


def main():
    print('24. ファイル参照の抽出')
    # 記事から参照されているメディアファイルをすべて抜き出せ．

    data = load_json_gz(c.PAHT_DATA)
    data_uk = data['イギリス']
    print(extract_files(data_uk))


if __name__ == '__main__':
    main()
