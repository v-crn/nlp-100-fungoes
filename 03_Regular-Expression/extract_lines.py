import config as c
from load_json_gz import load_json_gz


def extract_lines(keyword, text):
    text_list = text.splitlines()
    lines = []
    for line in text_list:
        if keyword in line:
            lines.append(line)
    return lines


def main():
    print('21. カテゴリ名を含む行を抽出')
    # 記事中でカテゴリ名を宣言している行を抽出せよ．
    data = load_json_gz(c.PAHT_DATA)
    data_uk = data['イギリス']
    print(extract_lines('[[Category:', data_uk))


if __name__ == '__main__':
    main()
