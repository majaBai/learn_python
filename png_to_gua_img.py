from turtle import width
from PIL import Image
import numpy as np

I = Image.open('./normal4.png') 
print(I)
print(I.size)
# I.show()    

I_array = np.array(I)
# I_array 长度为 32， 每个元素是长度 64 的子数组，子数组的元素是长度为 4 的数组，表示一个像素的 rgba 值
# print(I_array.shape) => (32, 64, 4)
print(len(I_array))
print(len(I_array[0]), I_array[0])
# 处理像素的 rgba
def agba_int(ar):
    r = int(ar[0])
    g = int(ar[1])
    b = int(ar[2])
    a = 255
    if(len(ar) == 4):
        a = int(ar[3])
    return (r << 24) + (g << 16) + (b << 8) + a

pixels = ''
for arr in I_array:
    for ar in arr:
        val = agba_int(ar)
        pixels += f'{val}' + ' '
pixels = pixels.strip()
print('pixels', len(pixels.split(' ')))

# 组装数据
content = ''
type = 'guaimage'
version = '1.0'
# 宽 64
width = I.size[0]
# 高 32
height = I.size[1]
print('width:', width,'height:', height)

assert len(pixels.split(' ')) == int(width) * int(height), '解析有错'

content += type + '\n'
content += version + '\n'
content += f'{width}' + '\n'
content += f'{height}' + '\n'
content += pixels

# 写入 apple.guaimage 文件
with open("normal4.guaimage","w+") as file:
    file.write(content)

