import sys
from konlpy.tag import Twitter, Kkma


def analyzer(message):
    twitter = Twitter()
    kkma = Kkma()

    sentences = kkma.sentences(message)

    for sentence in sentences:
        print('')
        print('')
        print('')
        print(sentence)
        print('Twitter : ' + str(twitter.pos(sentence)))
        print('Kkma : ' + str(kkma.pos(sentence)))


def main():
    log_file = open(sys.argv[1], 'r')
    analyzer(log_file.read())
    log_file.close()


if __name__ == '__main__':
    main()
