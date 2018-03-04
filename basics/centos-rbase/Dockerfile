FROM kongdeju/centos-dev

LABEL VERSION = "3.4.3"

RUN yum install -y gcc-c++ &&\
    yum install -y gcc-gfortran && \
    yum install -y libXt-devel && \
    yum install -y libcurl && \
    yum install -y libcurl-devel && \
    yum install -y libpng-devel libjpeg-devel libtiff-devel cairo cairo-devel && \
    yum install -y  texinfo.x86_64 && \
    yum install -y texlive && \
    yum install -y java-1.8.0-openjdk  


#    yum install -y glibc-headers && \
#    yum install -y libreadline6-dev gfortran && \
#    yum install -y readline-devel && \
#    yum install -y wget libXt-devel && \
#    yum install -y fonts-chinese tcl tcl-devel tclx tk tk-devel && \
#    yum install -y mesa-libGLU mesa-libGLU-devel && \
#    yum install -y install bzip2-devel && \
#    yum install -y install xz-devel.x86_64 && \
#    yum install -y install pcre-devel && \
#    yum install -y install libcurl && \
#    yum install -y install libcurl-devel && \

RUN wget https://cran.r-project.org/src/base/R-3/R-3.4.3.tar.gz && \
    tar xvzf R-3.4.3.tar.gz && \
    cd R-3.4.3

RUN yum install -y readline-devel 
RUN yum install -y bzip2-devel
RUN yum install -y xz-devel 
RUN yum install -y make

WORKDIR R-3.4.3
RUN ./configure  --with-recommended-packages=no --enable-R-shlib=yes && \
    make && \
    make install 

