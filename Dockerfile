# imagem basica 'Debian Stretch'
FROM debian:stretch

# configura repositorios e troca locale para 'pt_BR.UTF-8'
RUN echo 'deb http://sft.if.usp.br/debian/ stretch main' > /etc/apt/sources.list \
    && echo 'deb-src http://sft.if.usp.br/debian/ stretch main' >> /etc/apt/sources.list \
    && echo 'deb http://sft.if.usp.br/debian/ stretch-updates main' >> /etc/apt/sources.list \
    && echo 'deb-src http://sft.if.usp.br/debian/ stretch-updates main' >> /etc/apt/sources.list \
    && echo 'deb http://sft.if.usp.br/debian-security/ stretch/updates main' >> /etc/apt/sources.list \
    && echo 'deb-src http://sft.if.usp.br/debian-security/ stretch/updates main' >> /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends locales \
    && localedef -i pt_BR -c -f UTF-8 -A /usr/share/locale/locale.alias pt_BR.UTF-8
ENV LANG pt_BR.UTF-8

# adiciona os pacotes necessarios para a execucao do simplexpy
RUN apt-get install -y --no-install-recommends \
	bash-completion vim-nox mc \
	python2.7 python2.7-minimal \
	python-pip python-setuptools \
	python-ipython python-ipython-doc python-ipython-genutils \
	python-flask \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/cache/apt/archives/*

# configura o ambiente
ENV SHELL /bin/bash
ENV HOME /root
USER root
RUN mkdir -p /opt/simplexpy/
WORKDIR /opt/simplexpy/
EXPOSE 80
ENV FLASK_APP simplex.py

# adiciona arquivos do simplexpy
ADD ../app/ /opt/simplexpy/

# executa o simplexpy
CMD flask run --host 0.0.0.0 --port 80
