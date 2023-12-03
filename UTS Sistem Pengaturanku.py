#!/usr/bin/env python
# coding: utf-8

# In[1]:


import control as ctrl
import matplotlib.pyplot as plt
import numpy as np
from control.matlab import step, impulse


# In[2]:


num = [60 , -120]
den = [1,1,25]
system = ctrl.TransferFunction(num, den)


# In[3]:


time, response = ctrl.impulse_response(system)


# In[4]:


plt.plot(time,response)
plt.title('Impulse Response')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()
plt.show()


# In[5]:


delay_time = time[next(i for i, t in enumerate(response) if t >= 0)]
rise_time = time[next(i for i, t in enumerate(response) if t >= 0.1 * max(response))] - delay_time
peak_time = time[response.argmax()] - delay_time
settling_time = max(t for i, t in enumerate(time) if max(response) * 0.02 < response[i]) - delay_time
max_overshoot = ((max(response) - 1) / 1) * 100

print("Delay Time: {:.2f}".format(delay_time))
print("Rise Time: {:.2f}".format(rise_time))
print("Peak Time: {:.2f}".format(peak_time))
print("Settling Time: {:.2f}".format(settling_time))
print("Maximum Overshoot: {:.2f}%".format(max_overshoot))
    


# In[ ]:




