#!/usr/bin/python3.8

import matplotlib.pyplot as plt

w =[1,2,3,4,5,6,7,8,9,10]
time_scen1_1 = [2.999,1.823,1.931,1.766,1.891,1.845,1.785,1.715,1.877,1.729]
time_scen1_2 = [3.628,2.064,2.057,2.087,2.149,2.096,2.018,2.075,2.014,1.931]

time_scen2_1 = [17.801,6.412,6.902,6.826,7.029,7.241,7.086,7.170,7.217,6.989]
time_scen2_2 = [23.604,10.978,15.033,15.685,15.676,15.643,15.467,15.675,16.259,15.246]

time_scen3_1 = [14.287,8.119,7.557,7.597,7.652,7.711,7.547,7.603,7.841,7.419]
time_scen3_2 = [36.571,38.752,42.207,43.285,43.263,42.796,42.852,43.312,42.721,42.841]



fig, ax = plt.subplots(3, sharex=True)
fig.suptitle('A* Search')
ax[0].plot(w,time_scen1_1,label='Octile Distance')
ax[0].plot(w,time_scen1_2,label='Euclidean Distance')
ax[0].set_title("Scenario 1")
ax[0].set(ylabel='times(s)')


ax[1].plot(w,time_scen2_1,label='Octile Distance')
ax[1].plot(w,time_scen2_2,label='Euclidean Distance')
ax[1].set_title("Scenario 2")
ax[1].set(ylabel='times(s)')

ax[2].plot(w,time_scen3_1,label='Octile Distance')
ax[2].plot(w,time_scen3_2,label='Euclidean Distance')
ax[2].set_title("Scenario 3")
ax[2].set(xlabel='w',ylabel='times(s)')
plt.legend(loc='center right')




plt.show()


