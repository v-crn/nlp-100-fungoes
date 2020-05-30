def extract_verb_surface(sentences):
    verbs = []
    for sentence in sentences:
        for s in sentence:
            if s['pos'] == '動詞':
                verbs.append(s['surface'])
    return verbs


def extract_verb_base(sentences):
    verbs_origin = []
    for sentence in sentences:
        for s in sentence:
            if s['pos'] == '動詞':
                verbs_origin.append(s['base'])
    return verbs_origin


def extract_no_noun(sentences):
    nouns_joined_by_of = []
    for sentence in sentences:
        for i, s in enumerate(sentence):
            if (s['pos'] == '名詞') and \
                (sentence[i+1]['surface'] == 'の') and \
                (sentence[i+1]['pos'] == '助詞') and \
                (sentence[i+1]['pos1'] == '連体化') and \
                    (sentence[i+2]['pos'] == '名詞'):
                no_noun = s['surface'] \
                    + sentence[i + 1]['surface'] \
                    + sentence[i + 2]['surface']
                nouns_joined_by_of.append(no_noun)
    return nouns_joined_by_of


def extract_noun_series(sentences):
    noun_series = []
    for sentence in sentences:
        noun_series_unit = []
        for i, s in enumerate(sentence):
            if s['pos'] == '名詞':
                noun_series_unit.append(s['surface'])
            else:
                if len(noun_series_unit) > 1:
                    noun_series.append(''.join(noun_series_unit))
                noun_series_unit = []
        # 文が名詞で終わる場合
        if len(noun_series_unit) > 1:
            noun_series.append(''.join(noun_series_unit))
        noun_series_unit = []
    return noun_series


def count_word_frequency(sentences, pos=None, sort=True):
    """
    文章中に出現する単語の出現頻度を解析するメソッド。
    - 単語：「記号」を除く形態素とする。

    return: list
        {単語1: 単語1の出現頻度, 単語2: 単語2の出現頻度}, ...
    """
    from collections import Counter
    counter = Counter()
    for sentence in sentences:
        words = [s['surface'] for s in sentence if s['pos'] != '記号']
        counter.update(words)
    if sort:
        return counter.most_common()
    return list(counter.items())


def co_occurrence_frequency(target, sentences, sort=True):
    from collections import defaultdict

    co_frequency = defaultdict(int)
    target_exists_in_sentence = False
    for sentence in sentences:
        for i, s in enumerate(sentence):
            if s['surface'] == target:
                target_exists_in_sentence = True
                continue
            if target_exists_in_sentence:
                if s['surface'] == target:
                    continue
                if s['pos'] == '記号':
                    continue
                if s['surface'] not in co_frequency.keys():
                    co_frequency[s['surface']] = 1
                    continue
                co_frequency[s['surface']] += 1
                target_exists_in_sentence = False
    if sort:
        return sorted(co_frequency.items())
    return co_frequency


def main():
    import config as c
    from read_mecab import read_mecab

    print('30. 形態素解析結果の読み込み')
    sentences = read_mecab(c.PATH_DATA)
    print(sentences)

    print('31. 動詞Permalink')
    print('動詞の表層形をすべて抽出せよ．')
    print(extract_verb_surface(sentences))

    print('32. 動詞の原形')
    print('動詞の原形をすべて抽出せよ．')
    print(extract_verb_base(sentences))

    print('33. 「AのB」')
    print('2つの名詞が「の」で連結されている名詞句を抽出せよ．')
    print(extract_no_noun(sentences))

    print('34. 名詞の連接Permalink')
    print('名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．')
    print(extract_noun_series(sentences))

    print('35. 単語の出現頻度Permalink')
    print('文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．')
    wf = count_word_frequency(sentences, sort=True)
    print(wf)

    print('36. 頻度上位10語Permalink')
    print('出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．')
    import pandas as pd
    import matplotlib.pyplot as plt

    plt.rcdefaults()
    plt.rcParams['font.family'] = 'Hiragino Maru Gothic Pro'

    wf = count_word_frequency(sentences, sort=True)
    df = pd.DataFrame(wf, columns=['word', 'frequency'])
    print(df[:10])
    df[:10].plot.barh(x='word', y='frequency')
    plt.gca().invert_yaxis()
    plt.show()

    print('37. 「猫」と共起頻度の高い上位10語Permalink')
    print('「猫」とよく共起する（共起頻度が高い）10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．')
    import pandas as pd
    import matplotlib.pyplot as plt

    plt.rcdefaults()
    plt.rcParams['font.family'] = 'Hiragino Maru Gothic Pro'

    co = co_occurrence_frequency(
        target='猫', sentences=sentences, sort=True)
    df = pd.DataFrame(co, columns=['word', 'co_occurrence_frequency'])
    print(df[:10])
    df[:10].plot.barh(x='word', y='co_occurrence_frequency')
    plt.show()

    print('38. ヒストグラムPermalink')
    print('単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．')
    import pandas as pd
    import matplotlib.pyplot as plt

    plt.rcdefaults()
    plt.rcParams['font.family'] = 'Hiragino Maru Gothic Pro'

    wf = count_word_frequency(sentences, sort=True)
    df = pd.DataFrame(wf, columns=['word', 'frequency'])
    df['frequency'].plot.hist(bins=50, range=(0, 1000))
    plt.xlabel('出現頻度')
    plt.ylabel('単語の種類数')
    plt.show()

    print('39. Zipfの法則Permalink')
    print('単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．')
    import matplotlib.pyplot as plt

    plt.rcdefaults()
    plt.rcParams['font.family'] = 'Hiragino Maru Gothic Pro'

    wf = count_word_frequency(sentences, sort=True)
    frequencies = [e[1] for e in wf]
    wf_ranks = list(range(1, len(frequencies) + 1))
    plt.scatter(wf_ranks, frequencies)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('単語の出現頻度順位')
    plt.ylabel('出現頻度')
    plt.show()


if __name__ == '__main__':
    main()
