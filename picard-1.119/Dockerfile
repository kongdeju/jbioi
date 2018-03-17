FROM kongdeju/alpine-java:stable

MAINTAINER kongdeju kongdeju@gene.ac

ADD  picard.tar.gz /tmp

RUN    mv /tmp/picard/*.jar /opt  \
    && rm -rf /tmp/*

