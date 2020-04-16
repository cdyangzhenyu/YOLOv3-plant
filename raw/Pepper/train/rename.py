import os

path = 'pepper_healthy/'
name = 'pepper_healthy'
counter = 1
for f in os.listdir(path):
    suffix = f.split('.')[-1]
    #if suffix == 'jpg' or suffix == 'png' or suffix == 'JPG'or suffix == 'jpeg':
    if suffix == 'JPG':
        new = '{}.{}'.format(name+str(counter), 'jpg')
        os.rename(path + f, path + new)
        counter = int(counter) + 1

"""
tomato_bacterial/
tomato_curl_virus/
tomato_eb/
tomato_healthy/
tomato_lb/
tomato_leaf_mold/
tomato_mosaic_virus/
tomato_septoria_leaf/
tomato_spider_mite/
tomato_target_spot/
"""
