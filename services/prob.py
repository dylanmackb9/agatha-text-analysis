

from main import *

# PROBABILITY 


metric = (unique_words / total_words) * 100 # METRIC WE ARE CURRENTLY USING

# MEAN AND SAMPLE MEANS 

#print(metric)

pop_mean = np.average(metric)  # mean of all of data
sample = []
for i, year in enumerate(years):
  if int(year) >= 1960:
    sample.append(metric[i])


sample = np.asarray(sample)  # our sample
sample_mean = np.average(sample)  # mean of our sample

print(metric[-1])




# T TEST

sample_size = len(sample)
sample_std = np.std(sample)


t, p = stats.ttest_1samp(sample, pop_mean)
print(t, p)
print("The likelihood that our sample would be drawn under the null hypothesis is %"+str(p*100))



average_random_sample = 0
for i in range(100):
  random_sample = np.random.choice(metric, len(sample))
  t, p = stats.ttest_1samp(random_sample, pop_mean)
  average_random_sample += p

print((average_random_sample/100))





# Z Score

est_std_of_mean = sample_std / np.sqrt(sample_size)
z = (pop_mean - sample_mean) / est_std_of_mean  # Probability of getting more extreme
print(z)




# Chebyshev

k = 2.782

u = pop_mean
var = np.var(metric)
maximum = np.max(metric)


to_exceed = k * np.sqrt(var) 
prob = 1 / (k**2)
print("The probability that Random Variable X differs from its expectation " + str(u) + " by more ", end="")
print("than " + str(to_exceed) + " is less than " + str(prob) + " .")
print()
print("The max differ in the metric is "+ str(maximum - pop_mean))








