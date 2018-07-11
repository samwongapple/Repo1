import numpy as np
import math

# prints formatted price
def formatPrice(n):
	return ("-$" if n < 0 else "$") + "{0:.2f}".format(abs(n))

# returns the vector containing stock data from a fixed file
def getStockDataVec(key):
	vec = []
	lines = open("data/" + key + ".csv", "r").read().splitlines()

	for line in lines[1:]:
		vec.append(float(line.split(",")[4]))

	return vec

# returns the sigmoid
def sigmoid(x):
	return 1 / (1 + math.exp(-x))

# returns an an n-day state representation ending at time t
def getState(data, t, n):
	d = t - n + 1
	block = data[d:t + 1] if d >= 0 else -d * [data[0]] + data[0:t + 1] # pad with t0 #(d가 0이상이면 10일 동안의 데이터, 0 미만이면 0에서의 데이터 쭉 나열 + 0부터 t까지)
	res = []
	for i in range(n - 1):
		res.append(sigmoid(block[i + 1] - block[i])) #i+1번째 가격에서 i번째 가격 뺀 거를 sigmoid?? 왜 sigmoid에 넣는 거지??

	return np.array([res])

