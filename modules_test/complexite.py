#!/usr/bin/env python
# coding: utf-8

# ### Mesure de complexité

# * mesures de base :

# In[1]:


type(2) != tuple, type((2, )) != tuple


# In[2]:


a,  = (2, ); a


# In[3]:


def mesure_time(f, params, init = lambda x: x):
    if type(params) != tuple: params = (params, )
    from time import time
    params = init(params)
    t = time()
    f(*params)
    t = time() - t
    return t


# In[4]:


f = lambda x : x + 1
mesure_time(f, 2)


# In[5]:


def mesure_perf(f, params, init = lambda x: x):
    if type(params) != tuple: params = (params, )
    from time import perf_counter
    params = init(params)
    t = perf_counter()
    f(*params)
    t = perf_counter() - t
    return t


# In[6]:


f = lambda L: L.append(0)
mesure_perf(f, [])


# In[7]:


fmap = lambda L, f: [f(x) for x in L]
mesure_perf(fmap, ([1, 2, 3], lambda x: x**2) )


# * mesures répétées

# In[8]:


def iter_perf(f, Lparams, nbsim, init = lambda x: x):
    if type(Lparams[0]) != tuple: Lparams = [(p, ) for p in Lparams]
    return [min(mesure_perf(f, params, init) for _ in range(nbsim)) for params in Lparams]


# In[9]:


f = 0


# In[10]:


def random_perf(f, Lparams, nbsim, init = lambda x: x):
    if type(Lparams[0]) != tuple: Lparams = [(p, ) for p in Lparams]
    from random import shuffle
    Dperf = {k: float('inf') for k in range(len(Lparams))}
    randomtests = nbsim * list(range(len(Lparams))); shuffle(randomtests)
    for k in randomtests:
        Dperf[k] = min(Dperf[k], mesure_perf(f, Lparams[k], init))
    return [Dperf[k] for k in range(len(Lparams))]


# In[11]:


def random_perf_comp(Lfonctions, Lparams, nbsim, init = lambda x: x):
    if type(Lparams[0]) != tuple: Lparams = [(p, ) for p in Lparams]
    from random import shuffle
    random_tests = [        (i_f, j_params) for i_f in range(len(Lfonctions)) for j_params in range(len(Lparams))] * nbsim
    shuffle(random_tests)
    Dperf = {i_f: [float('inf') for j_params in range(len(Lparams))] for i_f in range(len(Lfonctions)) }
    for i_f, j_params in random_tests:
        Dperf[i_f][j_params] =             min(Dperf[i_f][j_params], mesure_perf(Lfonctions[i_f], Lparams[j_params], init))
    return (Dperf[k] for k in range(len(Lfonctions)))


# In[20]:


f1 = lambda L : L.append(0)
f2 = lambda L : L + [0]

def finit(params):
    n, = params
    return (n * [0], )

liste_n = [k for k in range(0, 100001, 1000)]
liste_t1, liste_t2 = random_perf_comp((f1, f2), liste_n, nbsim = 50, init = finit)

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt

plt.plot(liste_n, liste_t1, 'r-', label = "L.append(0)")
plt.plot(liste_n, liste_t2, 'g-', label = "L + [0]")
plt.legend()
plt.show()


# In[ ]:


liste_n = [k for k in range(0, 100000, 1)]
liste_t1 = iter_perf(f1, liste_n, nbsim = 10, init = finit)
plt.plot(liste_n, liste_t1, 'r-', label = "L.append(0)")

plt.legend()
plt.show()


# In[ ]:


plt.plot(liste_n[:10000], liste_t1[:10000], 'r-', label = "L.append(0)")

plt.legend()
plt.show()


# In[13]:


liste_n = [k for k in range(0, 1000001, 1000)]
liste_t1 = iter_perf(f1, liste_n, nbsim = 100, init = finit)
plt.plot(liste_n, liste_t1, 'r-', label = "L.append(0)")

plt.legend()
plt.show()


# In[14]:


liste_n = [k for k in range(0, 1000001, 1000)]
liste_t1 = random_perf(f1, liste_n, nbsim = 100, init = finit)
plt.plot(liste_n, liste_t1, 'r-', label = "L.append(0)")

plt.legend()
plt.show()


# * Normalisation

# http://www.python-simple.com/python-numpy/random-numpy.php

# In[15]:


import numpy as np


# In[16]:


# complexité linéaire
f = lambda t, n : t/n

Ln = np.arange(1, 100)
Lt = np.array([np.random.randint(0, 100) for n in Ln]) # 100 exclu
Ln.shape, Lt.shape


# In[17]:


data = np.stack([Ln, Lt], axis = 0)


# In[18]:


data


# In[19]:


f(data)


# In[ ]:


Ln


# In[ ]:




