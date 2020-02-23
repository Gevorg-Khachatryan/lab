
import numpy as np
import matplotlib.pyplot as plt
import json
with open('data.json') as f:
    perf = json.load(f)
n_results = perf['meta']['numberOfResults']
print (n_results, 'results')
hourly_perf_total = np.zeros(n_results, dtype=float)
for i in range(n_results):
    print (i, perf['data'][i]['averageTotal'])
    hourly_perf_total[i] = perf['data'][i]['averageTotal']
plt.plot(hourly_perf_total)
plt.xticks(np.arange(0, n_results + 1, 24.0))
plt.ylabel('Average Total Milliseconds')
plt.xlabel('Hours Since ' + perf['meta']['endPeriod'])
title = 'Monitor 1572020 Past Week Performance'
plt.title(title)
# log y axis
plt.semilogy()
plt.grid(True)
plt.show()