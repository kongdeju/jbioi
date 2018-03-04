
FROM kongdeju/alpine-base:stable

MAINTAINER kongdeju <kongdeju@gene.ac>

# add bioconda channel
RUN conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/ 
     
# change apk source 
RUN mv /etc/apk/repositories /etc/apk/repositories.bark \
    && echo "http://mirrors.ustc.edu.cn/alpine/v3.7/main/" >> /etc/apk/repositories \
    && echo "http://mirrors.ustc.edu.cn/alpine/v3.7/community/" >> /etc/apk/repositories

# add jiot                         
RUN  pip install  -i --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple jbiot 

