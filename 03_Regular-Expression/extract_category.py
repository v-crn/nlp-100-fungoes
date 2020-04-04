import re

import config as c
from load_json_gz import load_json_gz


def extract_category(text):
    return [re.sub(r'\|\*', '', c) for c in re.findall(r'\[\[Category:(.+)\]\]', text)]


def main():
    print('22. カテゴリ名の抽出')
    # 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

    data = load_json_gz(c.PAHT_DATA)
    data_uk = data['イギリス']
    print(extract_category(data_uk))


if __name__ == '__main__':
    main()
