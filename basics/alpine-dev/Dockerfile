
FROM frolvlad/alpine-miniconda2

MAINTAINER kongdeju <kongdeju@gene.ac>

# add bioconda channel
RUN  conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/ 

# add regular soft
RUN apk add --no-cache  git \
                        wget \
                        make 
# add jiot                         
RUN  pip install jbiot


