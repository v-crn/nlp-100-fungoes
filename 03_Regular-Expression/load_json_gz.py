import gzip
import json
import config as c


def load_json_gz(filepath):
    with gzip.open(filepath, 'rt', encoding='utf-8') as f:
        return {item['title']: item['text'] for item
                in [json.loads(line) for line in f]}


def main():
    print('20. JSONデータの読み込み')
    # Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
    data = load_json_gz(c.PAHT_DATA)
    print(data['イギリス'])


if __name__ == '__main__':
    main()
