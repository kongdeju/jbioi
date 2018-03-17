FROM kongdeju/centos-java:stable

MAINTAINER kongdeju <kongdeju@gene.ac>

RUN    conda install -y perl \
    && ln -s /opt/conda/bin/perl /usr/bin/perl \
    && conda clean -y --all

ADD fastqc_v0.11.5.zip /opt

RUN yum install -y unzip \
    && cd /opt \
    && unzip fastqc_v0.11.5.zip \
    && chmod +x FastQC/fastqc \
    && ln -s /opt/FastQC/fastqc /usr/bin/fastqc
   

