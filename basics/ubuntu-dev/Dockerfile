FROM kongdeju/ubuntu-base:stable

MAINTAINER kongdeju <kongdeju@gene.ac>

RUN apt-get update && \
    apt-get install -y wget && \
    apt-get install -y bzip2 && \
    apt-get clean

ENV PATH="/opt/conda/bin:$PATH"
RUN wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -O conda.sh && \
    mkdir -p /opt/conda && \
    sh conda.sh -b -f -p /opt/conda && \
    rm conda.sh

RUN conda config --add channels  https://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/

#install jbiot
#RUN pip install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple jbiot
RUN pip install  jbiot
