import re

import config as c
from load_json_gz import load_json_gz


def extract_section(text):
    section_dict = {}
    section_list = re.findall(r'==(.+)==', text)
    for section in section_list:
        section_dict[re.sub(r'=', '', section)] = int(len(re.findall(r'=', section)) / 2 + 1)
    return section_dict


def main():
    print('23. セクション構造')
    # 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．

    data = load_json_gz(c.PAHT_DATA)
    data_uk = data['イギリス']
    print(extract_section(data_uk))


if __name__ == '__main__':
    main()
