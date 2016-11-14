import sys
from konlpy.tag import Twitter, Kkma


# RULES 안에 0: WORD, 1: TAG
# ex : ('영우', 'NNG')

rule_database = {
    # 보어 판별
    # 보격 조사
    'JKC': {
        'RULES': {
            -1: ['NNG', ],
            1: ['되', '아니', ],
        },
        'LABEL': '보어',
        'RANGE': [-1, 0, ],
    },
    'SF': {
        'RULES': {
            -1: ['EFN', 'EFA', 'EFQ', 'EFI', 'EFR', ],
        },
        'LABEL': '서술어',
        'RANGE': [-2, -1, 0, ],
    },
    'JKS': {
        'RULES': {
            -1: ['NNG', ],
        },
        'LABEL': '주어',
        'RANGE': [-1, 0, ],
    },
    'JKO': {
        'RULES': {
            -1: ['NNG', ],
        },
        'LABEL': '목적어',
        'RANGE': [-1, 0, ],
    },
    'JKG': {
        'RULES': {
            -1: ['NNP', 'NNG', ],
        },
        'LABEL': '관형어',
        'RANGE': [-1, 0, ],
    },
    'JX': {
        'RULES': {
            -1: ['NNP', 'NNG', ],
        },
        'LABEL': '관형어',
        'RANGE': [-1, 0, ],
    },
    'IC': {
        'RULES': {
        },
        'LABEL': '독립어',
        'RANGE': [0, ],
    },
}

def analyzer(message):
    kkma = Kkma()

    sentences = kkma.sentences(message)

    cnt = 0
    for sentence in sentences:
        morphemes = kkma.pos(sentence)
        print('')
        print('')
        print('Sentence : ' + sentence)
        print('')
        print('Morphemes : ' + str(morphemes))
        print('')
        for idx, morpheme in enumerate(morphemes):
            if morpheme[1] in rule_database:
                rules = rule_database[morpheme[1]]['RULES'].items()
                condition = True
                for position, values in rules:
                    if morphemes[idx + position][0] not in values and morphemes[idx + position][1] not in values:
                        condition = False
                        break

                if condition:
                    word = ''
                    for position in rule_database[morpheme[1]]['RANGE']:
                        word += morphemes[idx + position][0]
                    label = rule_database[morpheme[1]]['LABEL']
                    print('{} : {}'.format(word, label))
        print('')
        if cnt == 0:
            print('결과 : 2점 (주보술 / )')
        elif cnt == 1:
            print('결과 : 2.99점 (주보술 / 관형어, 부사어, 독립어 3번 이하 / ')
        elif cnt == 2:
            print('결과 : 2점 (주목술 / )')
        print('')
        print('------------------------------------------------')
        cnt += 1


def main():
    # log_file = open(sys.argv[1], 'r')
    # analyzer(log_file.read())
    # log_file.close()
    # analyzer("철수가 중학생이 되었다. 재민이는 대학생이 아니다. 나는 10대가 아니다. 영우가 공부한다. 영우가 재민이에게 꽃을 주다. 미국은 트럼프를 대통령으로 삼다. 술은 물과 같다. 물은 바다와 같다. 소주에 맥주를 넣다. 물을 관상용으로 두다. 아이구. 자라나는 어린이는 나라의 보배이다.")
    analyzer('철수가 대학생이 되었다. 아이구. 미국의 대통령은 트럼프가 되었다. 철수가 물을 마셨다.')


if __name__ == '__main__':
    main()

