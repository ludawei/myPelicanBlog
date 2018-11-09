Title: python basemap库安装
Date: 2018-06-20
Tags: python, basemap, conda
Category: python
Slug: python-install-basemap

linux服务器上安装python地图库basemap：
```bash
#安装Anaconda2
wget https://repo.continuum.io/archive/Anaconda2-5.2.0-Linux-x86_64.sh（会更新python到2.7.15）
chmod +x Anaconda2-5.2.0-Linux-x86_64.sh
./Anaconda2-5.2.0-Linux-x86_64.sh

#添加环境变量
export PATH="/home/ludawei/anaconda2/bin:$PATH"

#conda安装basemap
# conda install basemap
conda install -c conda-forge proj4
conda install -c conda-forge basemap
      
#解决proj库引用问题
import conda,os
conda_file_dir = conda.__file__
conda_dir = conda_file_dir.split('lib')[0]
proj_lib = os.path.join(os.path.join(conda_dir, 'share'), 'proj')
os.environ["PROJ_LIB"] = proj_lib
from mpl_toolkits.basemap import Basemap

```