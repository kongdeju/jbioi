FROM centos:7

MAINTAINER kongdeju <kongdeju@gene.ac>

# set yum 
RUN sed -i.backup 's/^enabled=1/enabled=0/' /etc/yum/pluginconf.d/fastestmirror.conf && \
    curl -o /etc/yum.repos.d/CentOS-Base.repo http://mirrors.aliyun.com/repo/Centos-7.repo && \
    yum localinstall -y --nogpgcheck https://mirrors.aliyun.com/epel/epel-release-latest-7.noarch.rpm && \ 
    curl -o /etc/yum.repos.d/epel.repo http://mirrors.aliyun.com/repo/epel-7.repo 

RUN yum install -y wget && \
    yum install -y bzip2 && \
    yum clean all  
 
# install conda
ENV PATH="/opt/conda/bin:$PATH"
RUN wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -O conda.sh && \
    mkdir -p /opt/conda && \
    sh conda.sh -b -f -p /opt/conda && \
    rm conda.sh 

RUN conda config --add channels  https://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/

#install jbiot
#RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple jbiot
RUN pip install jbiot

