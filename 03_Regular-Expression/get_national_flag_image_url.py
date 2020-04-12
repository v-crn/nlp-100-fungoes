import pprint
import re

import config as c
from load_json_gz import load_json_gz
from extract_template import extract_template

def get_national_flag_image_url(template_dict: dict):
    import requests
    import json

    filename = template_dict['国旗画像']

    S = requests.Session()

    ROOT_URL = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "titles": 'File:{}'.format(filename),
        "iiprop": "url"
    }
    html = S.get(url=ROOT_URL, params=params)
    json_encoded = json.loads(html.text)
    url = json_encoded['query']['pages'].popitem()[1]['imageinfo'][0]['url']
    return url


def main():
    data = load_json_gz(c.PAHT_DATA)
    data_uk = data['イギリス']
    pprint.pprint(extract_template(data_uk))

    template_dict = extract_template(
            data_uk, ignore_emphasis=True,
            ignore_interior_link_brackets=True,
            ignore_markup=True)

    print('29. 国旗画像のURLを取得する')
    # テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
    print(get_national_flag_image_url(template_dict))


if __name__ == '__main__':
    main()
