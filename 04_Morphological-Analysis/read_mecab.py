def read_mecab(filepath) -> [[{}]]:
    with open(filepath, encoding='utf-8') as file:
        sentence = []
        sentences = []

        for morpheme in file.read().split('\n'):
            element = morpheme.split('\t')
            surface = element[0]
            if len(element) < 2:
                continue
            attr = element[1].split(',')
            word = {
                'surface': surface,
                'base': attr[6],
                'pos': attr[0],
                'pos1': attr[1],
            }
            sentence.append(word)
            if word['pos1'] == '句点' or word['pos1'] == '空白':
                sentences.append(sentence)
                sentence = []
    return sentences
