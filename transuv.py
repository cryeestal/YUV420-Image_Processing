#!/usr/bin/env python
# coding: utf-8

# In[6]:


import cv2
import numpy as np

img = cv2.imread('sanan.jpeg')

#to y,u,v and split separately
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
y, u, v = cv2.split(img_yuv)

#multiple procession between three channels y,u,v
lut = np.array([[[i, i, i] for i in range(256)]], dtype=np.uint8)

# Convert back to BGR 
u = cv2.cvtColor(u, cv2.COLOR_GRAY2BGR)
v = cv2.cvtColor(v, cv2.COLOR_GRAY2BGR)

# for u & v apply the grayscale LUT respectively
u_mapped = cv2.LUT(u, lut)
v_mapped = cv2.LUT(v, lut)

# display the result images
result = np.vstack([img, u_mapped, v_mapped])
cv2.imwrite('sananout.jpg', result)


# In[ ]:




