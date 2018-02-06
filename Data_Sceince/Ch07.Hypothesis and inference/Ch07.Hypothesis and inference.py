import random, math
from collections import Counter
from matplotlib import pyplot as plt
from probability import normal_cdf, inverse_normal_cdf

# 귀무가설(동전은 공평하다 p = 0.5), 대립가설(동전은 공평하지 않다. p != 0.5)

def normal_approximation_to_binomial(n, p):
    mu = n * p
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma

# 누적분포함수는 확률변수가 특정 값보다 작을 확률을 나타낸다.
normal_probability_below = normal_cdf

# 확률분포가 특정 값보다 작지 않으면, 크다는 것을 의미한다.
def normal_probability_above(lo, mu = 0, sigma = 1):
    return 1 - normal_cdf(lo, mu, sigma)

# 확률변수가 lo보다 작지않고 hi보다 작을 경우 확률변수는 hi와 lo사이에 존재
def normal_probability_between(lo, hi, mu = 0, sigma = 1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

def normal_probability_outside(lo, hi, mu = 0, sigma = 1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)

# 분포의 양쪽 고리의 밀도
def normal_upper_bound(probability, mu = 0, sigma = 1): # 단측검정 상한선
    return inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability, mu = 0, sigma = 1): # 단측검정 하한선
    return inverse_normal_cdf(1 - probability, mu, sigma)

def normal_two_sided_bounds(probability, mu, sigma): # 양측검정
    tail_probability = (1 - probability) / 2
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)
    return lower_bound, upper_bound

# 동전 1000번 던지기
mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)

# 유의수준 5%
print(normal_two_sided_bounds(0.95, mu_0, sigma_0))   # (469, 531)

# 제2종 오류 (검정력)
lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)
print(lo, hi)
mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)
type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
power = 1 - type_2_probability
print(power)

# p <= 0.5인 경우를 귀무가설.
hi = normal_upper_bound(0.95, mu_0, sigma_0)
type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
power = 1 - type_2_probability
print(power)

# p-value (양측검정)

def two_sided_p_value(x, mu = 0, sigma = 1):
    if x >= mu:
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        return 2 * normal_probability_below(x, mu, sigma)
print(two_sided_p_value(529.5, mu_0, sigma_0)) # 0.062

# 시뮬레이션

extremm_value_count = 0
for _ in range(100000):
    num_heads = sum(1 if random.random() < 0.5 else 0 for _ in range(1000))
    if num_heads >= 530 or num_heads <= 470:
        extremm_value_count += 1
print(extremm_value_count) # 0.062

# p-value(단측검정)

upper_p_value = normal_probability_above
lower_p_value = normal_probability_below

print(upper_p_value(524.5, mu_0, sigma_0)) # p값은 0.061 따라서 귀무가설 기각 x


print(upper_p_value(526.5, mu_0, sigma_0)) # p값은 0.047 따라서 귀무가설 기각

# 신뢰구간

p_hat = 525 / 1000
mu = p_hat
sigma = math.sqrt(p_hat * (1 - p_hat) /1000)
print(normal_two_sided_bounds(0.95, mu, sigma))

p_hat = 540 / 1000
mu = p_hat
sigma = math.sqrt(p_hat * (1 - p_hat) /1000)
print(normal_two_sided_bounds(0.95, mu, sigma))

# p-value 해킹

def run_experiment():
    return [random.random() < 0.5 for _ in range(1000)]

def reject_fairness(experiment):
    num_heads = len([flip for flip in experiment if flip])
    return num_heads < 469 or num_heads > 531

random.seed(0)
experiments = [run(experiment) for _ in range(1000)]
num_rejections = len([experiment for experiment in experiments
                      if reject_fairness(experiment)])
print(num_rejections)
"""1. 가설은 데이터를 보기전에 세운다
   2. 데이터를 전처리할 때는 세워둔 가설을 잠시 잊는다
   3. p-value는 전부가 아니다"""

# 예제 : A/B Test 해보기

def estimated_parameters(N, n):
    p = n / N
    sigma = math.sqrt(p * (1 - p) * n)
    return p, sigma

def a_b_test_statistic(N_A, n_A, N_B, n_B):
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)

z = a_b_test_statistic(1000, 200, 1000, 150) # -1.14
print(two_sided_p_value(z)) # 이정도의 차이가 날 확률 0.254 /  A,B의 평균이 동일하다는 가설을 기각할수 없음.

z= a_b_test_statistic(1000, 200, 1000, 180) # -2.94
print(two_sided_p_value(z)) #이정도의 차이가 날 확률 0.003 / A,B의 평균이 동일하다는 가설 기각.

# 베이지안 추론

def B(alpha, beta):
    return math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha + beta)

def beta_pdf(x, alpha, beta):
    if x < 0 or x > 1:
        return 0
    return x ** (alpha - 1) * (1 - x) ** (beta -1) / B(alpha, beta)
