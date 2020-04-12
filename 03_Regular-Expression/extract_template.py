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
        ignore_interior_link_brackets=False,
        ignore_markup=False):
    template_list = re.findall(
        r'''
        ^\{\{基礎情報.*?$   # 「{{基礎情報」で始まる行
        (.+?)              # 抽出するテキスト部分
        ^\}\}              # 「}}」で終わる行
        ''',
        text,
        flags=re.MULTILINE + re.VERBOSE + re.DOTALL)

    if ignore_emphasis:
        template_list = [re.sub(
            r"'{2,3}|'{5}",     # '' / ''' / ''''' を除去
            "", text,
            flags=re.MULTILINE + re.VERBOSE) for text in template_list]

    if ignore_interior_link_brackets:
        # 内部リンクのパターン
        # 1. [[記事名]]
        # 2. [[記事名 | 表示文字]]
        # 3. [[記事名  # 節名|表示文字]]
        # 表示文字がない場合は記事名、ある場合は表示文字のみ抽出
        template_list = [re.sub(
            r'''
            \[{2}           # [[で始まる文字列
            ([^|\]]+?\|)    # 表示文字の手前までの文字列
            *(.*?)          # 表示文字
            \]{2}
            ''',
            r'\2',          # 上の正規表現の2番目の () 内の文字列で置換
            text,
            flags=re.MULTILINE + re.VERBOSE) for text in template_list]

    if ignore_markup:
        # 言語テンプレートから文字列のみを抽出
        # 言語テンプレートの形式: {{lang | 言語タグ | 文字列}}
        template_list = [re.sub(
            r'''
            \{{2}
            ([^|\}]+?\|)
            *(.*?)
            \}{2}
            ''',
            r'\2',
            text,
            flags=re.MULTILINE + re.VERBOSE) for text in template_list]

        # <br> タグを \n に置換
        template_list = [re.sub(
            r'<br/>', "\n", text,
            flags=re.MULTILINE + re.VERBOSE) for text in template_list]

        # タグの除去
        template_list = [re.sub(
            r'<.*?>', "", text,
            flags=re.MULTILINE + re.VERBOSE) for text in template_list]
    return reccurent_extract_as_dict(template_list[0])


def main():
    print('25. テンプレートの抽出')
    # 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
    data = load_json_gz(c.PAHT_DATA)
    data_uk = data['イギリス']
    pprint.pprint(extract_template(data_uk))

    print('26. 強調マークアップの除去')
    # 25の処理時に，テンプレートの値からMediaWikiの強調マークアップ（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ
    pprint.pprint(extract_template(data_uk, ignore_emphasis=True))

    print('27. 内部リンクの除去')
    # 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，テキストに変換せよ
    pprint.pprint(
        extract_template(
            data_uk, ignore_emphasis=True,
            ignore_interior_link_brackets=True)
    )

    print('28. MediaWikiマークアップの除去')
    # 27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
    template_dict = extract_template(
            data_uk, ignore_emphasis=True,
            ignore_interior_link_brackets=True,
            ignore_markup=True)
    pprint.pprint(template_dict)


if __name__ == '__main__':
    main()
