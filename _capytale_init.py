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

ensure_path_validity("telechargements")
ensure_path_validity("capytale/modules")
