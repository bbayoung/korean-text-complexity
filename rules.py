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
