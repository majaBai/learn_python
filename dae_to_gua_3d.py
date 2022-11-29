#!/usr/bin/python3

from xml.dom.minidom import parse
import xml.dom.minidom

# 转成 gua3d
file_type = 'gua3d'
# 版本
version = ''
# 顶点数
vtc_count = ''
# 所有顶点信息: x, y, z, nx, ny, nz, u, v
vtc_info = []
vtc_nrml = []
# uv 坐标
uv = []
# 三角形个数
tri_count = ''
# 所用三角形顶点序号
tri_used = []


# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse("Obj_Fruit_Apple_A_01.dae")
collection = DOMTree.documentElement
# print('collection', collection)

# 版本信息
if collection.hasAttribute('version'):
    version = collection.getAttribute("version")
    print('version', version)


mesh = collection.getElementsByTagName("mesh")[0]
sources = mesh.getElementsByTagName('source')
print('sources.length--', len(sources))

# 所有顶点的坐标
vtc_info = sources[0].getElementsByTagName('float_array')[0]
vtc_count = sources[0].getElementsByTagName('accessor')[0].getAttribute("count")
print('vtc_count***************', vtc_count)
vtc_info = vtc_info.childNodes[0].data.split(' ')
assert len(vtc_info) == int(vtc_count) * 3, '顶点信息有错'

# 所有顶点法向量
nml_info = sources[1].getElementsByTagName('float_array')[0]
vtc_nrml = nml_info.childNodes[0].data.split(' ')
# print('vtc_nrml', len(vtc_nrml), vtc_nrml)
assert len(vtc_nrml) == int(vtc_count) * 3, '法向量信息有错'

# 所有 uv 贴图坐标
uv_info = sources[4].getElementsByTagName('float_array')[0]
uv = uv_info.childNodes[0].data.split(' ')
print('uv ---', len(uv), uv)


# 组装顶点数据：每个顶点的坐标 + 法向量坐标 + uv坐标
vtc_str = ''
for i in range(int(vtc_count)):
    idx = i * 3
    vtc_str += vtc_info[idx] + ' '
    vtc_str += vtc_info[idx + 1] + ' '
    vtc_str += vtc_info[idx + 2] + ' '

    vtc_str += vtc_nrml[idx] + ' '
    vtc_str += vtc_nrml[idx + 1] + ' '
    vtc_str += vtc_nrml[idx + 2] + ' '

    u = float(uv[idx])
    v = float(uv[idx + 1])
    vtc_str += f'{u}' + ' ' if u < 1 else '1 '
    vtc_str += f'{v}' + '\n' if v < 1 else '1' + '\n'

assert len(vtc_str.strip().split('\n')) == int(vtc_count), '组装顶点数据出错'

# 三角形信息
tri_info = mesh.getElementsByTagName('triangles')[0]
tri_count = tri_info.getAttribute("count")

tri_p = tri_info.getElementsByTagName('p')[0].childNodes[0].data.split(' ')

# 获取所用三角形顶点
i = 0 
while i < len(tri_p):
    tri_used.append(tri_p[i])
    i += 4

# 组装所用三角形的顶点序号
tri_vtc = ''
for i in range(int(tri_count)):
    idx = i * 3
    tri_vtc += f'{int(tri_used[idx])}' + ' '
    tri_vtc += f'{int(tri_used[idx + 1])}' + ' '
    tri_vtc += f'{int(tri_used[idx + 2])}' + '\n'
tri_vtc = tri_vtc.strip()
assert len(tri_vtc.split('\n')) == int(tri_count), '组装所用三角形出错'

# 组装信息
content = ''
content += file_type + '\n'
content += 'version ' + version + '\n'
content += 'vertices ' + vtc_count + '\n'
content += 'triangles ' + tri_count + '\n'
content += vtc_str
content += tri_vtc


# 写入 apple.gua3d 文件
with open("apple.gua3d","w+") as file:
    file.write(content)