import re  # 02で使用


def warmUp00():
    """
    文字列を逆順に表示
    """
    string = 'stressed'
    result = string[::-1]  # -1で逆順になる
    print(result)


def warmUp01():
    """
    文字列をn文字飛ばしで表示
    """
    string = 'パタトクカシーー'
    # [start:stop:step]  https://kakedashi-engineer.appspot.com/2020/02/05/step-stride/
    result = string[::2]
    print(result)


def warmUp02():
    """
    2つの文字列から1文字ずつ取得して合成
    """
    a = 'パトカー'
    b = 'タクシー'
    result = ''
    for c1, c2 in zip(a, b):  # zip関数を使う
        result += c1 + c2
    print(result)


def warmUp03():
    """
    英文を単語に分割し、文字数をカウントする
    """
    string = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    words = re.sub(',|\.|;|:', '', string).split(
        ' ')  # 正規表現で記号を削除（'.'は要エスケープ）し、スペースで分割。
    result = []
    for word in words:
        result.append(len(word))
    print(result)


def warmUp04():
    """
    単語に分割し、1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭の2文字を取り出す
    取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成
    """
    string = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
    words = re.sub(',|\.|;|:', '', string).split(' ')
    checker = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    result = {}
    for i, word in enumerate(words):  # enumerate() を使うと、インデックスとリストの内容を抽出できる
        if i in checker:
            result[word[0]] = i
        else:
            result[word[:2]] = i
    print(result)


def warmUp05():
    """
    与えられたシーケンスからn-gramを作成する
    """
    string = 'I am an NLPer'
    print('result:', create_n_gram(string, 2, 'letter'))
    print('result:', create_n_gram(string, 2, 'word'))


def create_n_gram(string, n, sequenceType):
    """
    n-gram を作成する関数。sequenceType には分割単位として 'letter' / 'word' を与える。
    """
    sequence = ''
    if sequenceType == 'letter':
        sequence = re.sub(',|\.|;|:|\s', '', string)  # 文字列の場合、スペースは除外する前提としている
    elif sequenceType == 'word':
        sequence = re.sub(',|\.|;|:', '', string).split(' ')  # 記号は除外する前提としている
    # result = []
    # for i in range(len(sequence)):
    #     result.append(sequence[i:i+n])
    return [sequence[i:i+n] for i in range(len(sequence))]  # 内包表記だとこう


if __name__ == '__main__':
    warmUp05()
