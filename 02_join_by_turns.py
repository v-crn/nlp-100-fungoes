def join_by_turns(str_list: list):
    result = ''
    len_list = [len(s) for s in str_list]
    len_max = max(len_list)

    for i in range(len_max):
        for s in str_list:
            if i < len(s):
                result += s[i]
            else:
                None
    return result


def main():
    print('Test 1:')
    str_list = ['パトカー', 'タクシー']
    print(join_by_turns(str_list), '\n')

    print('Test 2:')
    str_list = ['スープラピー', 'スープラパー', 'からだがかってにおどりだす〜♪']
    print(join_by_turns(str_list), '\n')


if __name__ == '__main__':
    main()
