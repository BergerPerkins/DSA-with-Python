######    problem-1     ########
i = 1
while i < 10:
    i=i*2
#timecomplexity = O(log n)



######    problem-2     ########
i = n
while i > 0:
    i = i - 1
#timecomplexity = O(n)



######    problem-3     ########
for i in range(n): # O(n)
    k = 2
    while k < n:   # O(log log n)
        k = k * k
#timecomplexity = O(n log log n)
