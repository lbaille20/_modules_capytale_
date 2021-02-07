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

def download_file_as_is(src_url, dst_dir, filename):
    from urllib.request import urlopen
    f = urlopen(src_url)
    if dst_dir != '.':
        ensure_path_validity(dst_dir)
    with open(os.path.join(dst_dir, filename), 'wb') as f1:
        f1.write(f.read())
        
distant_directory_url = "https://raw.githubusercontent.com/lbaille20/_modules_capytale_/main/"
fichier_a_telecharger = "capytale_preliminaries.py"
src_url = ''.join([distant_directory_url, fichier_a_telecharger])
dst_dir = 'capytale'
download_file_as_is(src_url, dst_dir, fichier_a_telecharger)

exec(os.path.join('capytale', 'capytale_preliminaries.py'))
