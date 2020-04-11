import pprint
import re

import config as c
from load_json_gz import load_json_gz


def reccurent_extract_as_dict(text):
    d = {}
    text_list = text.split('\n|')
    for item in text_list:
        if ' = ' in item:
            item_list = item.split(' = ')
            d[item_list[0]] = item_list[1]
        else:
            d[item] = None
    return d


def extract_template(
        text, ignore_emphasis=False,
        ignore_interior_link_brackets=False):
    template_list = re.findall(
        r'''
        ^\{\{基礎情報.*?$   # 「{{基礎情報」で始まる行
        (.+?)              # 抽出するテキスト部分
        ^\}\}              # 「}}」で終わる行
        ''',
        text, re.MULTILINE + re.VERBOSE + re.DOTALL)

    if ignore_emphasis:
        template_list = [re.sub(
            r"''+",     # 「'」に「'」が1つ以上続いたもの
            "", text) for text in template_list]

    if ignore_interior_link_brackets:
        template_list = [re.sub(
            r"\[\[.+\||\[\[|\]\]",  # 「[[ ~ |」、「[[」「]]」を除去
            "", text) for text in template_list]

    return reccurent_extract_as_dict(template_list[0])


def main():
    pprint.pprint('25. テンプレートの抽出')
    # 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
    data = load_json_gz(c.PAHT_DATA)
    data_uk = data['イギリス']
    pprint.pprint(extract_template(data_uk))

    pprint.pprint('26. 強調マークアップの除去')
    # 25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ
    pprint.pprint(extract_template(data_uk, ignore_emphasis=True))

    pprint.pprint('27. 内部リンクの除去')
    # 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ
    pprint.pprint(
        extract_template(
            data_uk, ignore_emphasis=True,
            ignore_interior_link_brackets=True)
    )


if __name__ == '__main__':
    main()
