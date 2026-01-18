from spectral import *
img=open_image('data/92AV3C.lan')
print(img.__class__)
print(img)
arr=img.load()
print(arr.info())
print(arr.size)