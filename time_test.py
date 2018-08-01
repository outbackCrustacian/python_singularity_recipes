#!/usr/bin/env python
import os, timeit, math

code = '''
for x in range(100):
   name = '/home/sgww/open_files_test/test/file_' + str(x).zfill(4) + '.txt'
'''
print('#%*s%*s%*s%*s' % (10, "TIME(s)", 22, "TOTAL(s)", 25, "AVG TIME(s)", 20, "SIGMA"))
sumnums = 0.0
count = 1000
nums = []
for i in range(count):
   temp = timeit.timeit(stmt = code)
   sumnums += temp
   nums.append(temp)
avg = sumnums/count
sigma = 0.0
for c in range(len(nums)):
   sigma += math.pow(nums[c]-avg, 2)
sigma = sigma / len(nums)
sigma = math.sqrt(sigma)
time = nums[0]
print('%*f%*f%*f%*f' % (11, time, 22, sumnums, 25, avg, 23, sigma))
