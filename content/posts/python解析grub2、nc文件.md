Title: python解析grub2、nc文件
Date: 2019-03-08
Tags: python
Category: python
Slug: python-decode-grub2_nc

一些工作中常用到的ffmpeg命令：
```python

# grub2数据
import pygrib

filename = 'filename.GRB2'
grbs = pygrib.open(filename)
# grb = grbs.select()[0]#grbs.message(1)
for grb in grbs:
    print grb

# nc数据
from netCDF4 import Dataset

file_path = 'filename.nc'
nc = Dataset(file_path)
for key in nc.variables.keys():
    data = nc.variables[key]
    print key, len(data)

```

#### 未完待续...