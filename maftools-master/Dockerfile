FROM kongdeju/ubuntu-rbase:stable

MAINTAINER kongdeju <kongdeju@gene.ac>

RUN apt-get install -y \
        libcurl4-openssl-dev \
        libxml2-dev \
        apt-transport-https \
        libssl-dev \
        libmariadb-dev \
    &&  apt-get clean 

ADD install.r /tmp/
RUN Rscript /tmp/install.r





