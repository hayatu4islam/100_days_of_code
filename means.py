# calculating the arithmetic mean
from numpy import mean
# define the dataset
data = [0,1,2,3,4,5,6,7,8,9]
# calculate the mean
result = mean(data)
print("Arithmetic mean: %.3f" % result)

# Calculating the geometric mean
from scipy.stats import gmean
gdata = [1,2,3,40,50,60,0.7,0.88,0.9,1000]
gresult = gmean(gdata)
print('Geometric Mean: %.3f' % gresult)

# Calculating the harmonic mean
from scipy.stats import hmean
hdata = [0.11, 0.22, 0.33, 0.44, 0.55, 0.66, 0.77, 0.88, 0.99]
hresult = hmean(hdata)
print('Harmonic Mean: %.3f' % hresult)