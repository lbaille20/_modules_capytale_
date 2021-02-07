#!/usr/bin/env python
# coding: utf-8

# ### Fonctions de création/vérification de  répertoires

# In[19]:


import os

def ensure_path_validity(path_to_dst):
    head, tail = os.path.split(path_to_dst)
    #print('head =', head, 'tail =', tail)
    if head != '' and not os.path.exists(head):
        #print(head, head == '')
        ensure_path_validity(head)
    if head == '':
        head = '.'
    if tail != '' and tail not in os.listdir(head) or not os.path.isdir(path_to_dst):
        os.mkdir(path_to_dst)


# * création des répertoires par défaut

# In[20]:


ensure_path_validity("telechargements") ## warning case unsensitive => use NO capital letters, NO accents
ensure_path_validity("modules")
ensure_path_validity("capytale/modules")


# In[21]:


def download_file_as_is(src_url, dst_dir, filename):
    from urllib.request import urlopen
    f = urlopen(src_url)
    if dst_dir != '.':
        ensure_path_validity(dst_dir)
    with open(os.path.join(dst_dir, filename), 'wb') as f1:
        f1.write(f.read())


# * téléchargements des modules capytale

# In[25]:


distant_directory_url = "https://raw.githubusercontent.com/lbaille20/_modules_capytale_/main"

repertoire_modules = ["modules_test"]

fichiers_a_telecharger = ["capytale_misc",
                          "complexite"]


# In[26]:


dst_dir = 'capytale/modules'


# In[29]:


for file in fichiers_a_telecharger:
    filename = file + '.py'
    src_url = '/'.join([distant_directory_url, repertoire_modules, filename])
    try:
        download_file_as_is(src_url, dst_dir, filename)
    except:
        print(f'Module "{file}" not found')


# In[ ]:




