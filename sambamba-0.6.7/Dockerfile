FROM kongdeju/alpine-dev:stable 

MAINTAINER kongdeju kongdeju@gene.ac

ADD sambamba_v0.6.7_linux.tar.bz2 /opt
RUN    cd /opt/ \
    && mv sambamba /usr/bin 

CMD ["/usr/bin/sambamba"]


