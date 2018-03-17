FROM kongdeju/ubuntu-rbase:stable

RUN Rscript -e 'source("http://bioconductor.org/biocLite.R");' && \
    Rscript -e 'biocLite("ComplexHeatmap");' && \
    Rscript -e 'biocLite("VariantAnnotation"); ' && \
    Rscirpt -e 'biocLite("Biostrings");'



