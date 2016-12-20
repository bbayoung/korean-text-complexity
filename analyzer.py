import sys
from konlpy.tag import Twitter, Kkma
from rules import rule_database

def analyzer(message):
    kkma = Kkma()

    sentences = kkma.sentences(message)

    max_score = 0
    total_score = 0
    total_line = 0
    for sentence in sentences:
        morphemes = kkma.pos(sentence)
        print('')
        print('')
        print('Sentence : ' + sentence)
        print('')
        print('Morphemes : ' + str(morphemes))
        print('')
        labels = []
        score = 0
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
                    labels.append(label)
                    print('{} : {}'.format(word, label))

        check = {
            '주어': False,
            '목적어' : False,
            '보어': False,
            '술어': False,
        }
        cnt_condition_1 = 0  # 첨가조건1 의 갯수
        cnt_condition_2 = 0  # 첨가조건2의 갯수

        for label in labels:
            if label in check:
                check[label] = True
            elif label in ['관형어', '부사어', '독립어']:
                cnt_condition_1 += 1
            elif label in ['명사절', '관형절', '부사절', '인용절', '서술절']:
                cnt_condition_2 += 1

        if check['주어'] and check['목적어'] and check['보어'] and check['술어']:
            score = 3
        elif check['주어'] and check['술어'] and (check['목적어'] or check['보어']):
            score = 2
        else:
            score = 1  # 주어 + 술어

        if cnt_condition_1 <= 3:
            score += 0.99
        elif cnt_condition_1 <= 6:
            score += 1.99
        else:
            score += (0.33 * cnt_condition_1)

        score += (3 * cnt_condition_2)

        total_score += score
        total_line += 1
        max_score = score if score > max_score else max_score

        print(' score : ' + str(score))
        print('')
        print('------------------------------------------------')

    print('total_score : {}'.format(total_score))
    print('total_line : {}'.format(total_line))
    print('max_score : {}'.format(max_score))
    print('avg_score : {}'.format(total_score/total_line))


def main():
    if len(sys.argv) > 1:
        log_file = open(sys.argv[1], 'r')
        analyzer(log_file.read())
        log_file.close()
    else:
        print("파일명을 입력해주세요.")


if __name__ == '__main__':
    main()

