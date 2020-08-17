# 이상치를 제외하고 평범한 데이터 사이의 범위 차이
# 상, 하위 25% 사이의 차이

def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x) [p_index]

def interquartile_range(x) :
    return quantile(x, 0.75) - quantile(x, 0.25)