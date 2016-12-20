# RULES 안에 0: WORD, 1: TAG
# ex : ('영우', 'NNG')

rule_database = {
    # 보격조사
    'JKC': {
        'LABEL': '보어',
        'RULES': {
            -1: ['NNG', ],
            1: ['되', '아니', ],
        },
        'RANGE': [-1, 0, 1],
    },

    # 마침표, 느낌표, 물음표
    'SF': {
        'LABEL': '술어',
        'RULES': {
            -1: ['EFN', 'EFA', 'EFQ', 'EFI', 'EFR', 'EFO', ],
        },
        'RANGE': [-2, -1, 0, ],
    },
    # 대등적 연결어미 : VV(VA) + ECE
    'ECE': {
        'LABEL' : '술어',
        'RULES': {
            -1: ['VV', 'VA', ],
        },
        'RANGE': [-1, 0, ],
    },
    # 대등적 연결어미 + 선어말 어미 가능성 : VV(VA) + EPT(EPP, EPH) + ECE
    'ECE': {
        'LABEL' : '술어',
        'RULES': {
            -2: ['VV', 'VA', ],
            -1: ['EPT', 'EPP', 'EPH', ],
        },
        'RANGE': [-2, -1, 0, ],
    },

    # 주격조사
    'JKS': {
        'LABEL': '주어',
        'RULES': {
            -1: ['NNG', ],
        },
        'RANGE': [-1, 0, ],
    },

    # 목적격 조사
    'JKO': {
        'LABEL': '목적어',
        'RULES': {
            -1: ['NNG', ],
        },
        'RANGE': [-1, 0, ],
    },

    # 부사격 조사
    'JKM': {
        'LABEL': '부사어',
        'RULES': { },
        'RANGE': [-1, 0, ],
    },

    # 관형격 조사
    'JKG': {
        'LABEL': '관형어',
        'RULES': { },
        'RANGE': [-1, 0, ],
    },

    # 부사
    'MA_': {
        'LABEL': '부사어',
        'RULES': { },
        'RANGE': [0, ],
    },

    # 관형사
    'MD_': {
        'LABEL': '관형어',
        'RULES': { },
        'RANGE': [0, ],
    },

    # 관형사
    'ETD': {
        'LABEL': '관형어',
        'RULES': { },
        'RANGE': [-1, 0, ],
    },

    # 인용격 조사
    'JKQ': {
        'LABEL': '인용절',
        'RULES': {
        },
        'RANGE': [-1, 0, ],
    },
    # 관형형 전성어미
    'ETD': {
        'LABEL': '관형절',
        'RULES': {
        },
        'RANGE': [-1, 0, ],
    },
    # 명사형 전성어미
    'ETN': {
        'LABEL': '명사절',
        'RULES': {
        },
        'RANGE': [-1, 0, ],
    },
    # 의존적 연결어미
    'ECD': {
        'LABEL': '부사절',
        'RULES': {
        },
        'RANGE': [-1, 0, ],
    },
    # 감탄사
    'IC': {
        'LABEL': '독립어',
        'RULES': {
        },
        'RANGE': [0, ],
    },
}
