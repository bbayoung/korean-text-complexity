import sys
from konlpy.tag import Twitter, Kkma
from rules import rule_database

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
            if morpheme[1] in rule_database or '{}_'.format(morpheme[1][:-1]) in rule_database:
                if morpheme[1] in rule_database:
                    current_rule = rule_database[morpheme[1]]
                else:
                    current_rule = rule_database['{}_'.format(morpheme[1][:-1])]
                condition = True

                # position : RULES의 key, values : RULES 의 value
                for position, values in current_rule['RULES'].items():
                    # 규칙 데이터베이스에 정의된 모든 조건(RULES)을 만족시켜야 한다.
                    # 하나라도 만족하지 못 하면 분석 할 수 없다.
                    if morphemes[idx + position][0] not in values and morphemes[idx + position][1] not in values:
                        condition = False
                        break

                # 모든 조건을 만족하면, 이 부분에서는 분석 결과를 출력한다.
                if condition:
                    word = ''
                    for position in current_rule['RANGE']:
                        word += morphemes[idx + position][0]
                    label = current_rule['LABEL']
                    print('{} : {}'.format(word, label))
        print('')
        print('------------------------------------------------')
        cnt += 1


def main():
    # log_file = open(sys.argv[1], 'r')
    # analyzer(log_file.read())
    # log_file.close()
    analyzer("철수가 중학생이 되었다. 재민이는 대학생이 아니다. 나는 10대가 아니다. 영우가 공부한다. 영우가 재민이에게 꽃을 주다. 미국은 트럼프를 대통령으로 삼다. 술은 물과 같다. 물은 바다와 같다. 소주에 맥주를 넣다. 물을 관상용으로 두다. 아이구. 자라나는 어린이는 나라의 보배이다. 예쁜 재민이는 영우를 매우 좋아한다. 그 옷은 나에게 작다. 노란 들국화가 그에게 꺾였다.")


if __name__ == '__main__':
    main()

