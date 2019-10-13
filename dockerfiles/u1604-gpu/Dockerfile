FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04

RUN apt-get update && \
    apt-get install -y sudo

RUN apt-get update && apt-get install -y tree curl wget vim git-core zsh

RUN cd /tmp && \
    wget https://download.jetbrains.com/python/pycharm-professional-2018.3.4.tar.gz && \
    tar xzf pycharm-professional-2018.3.4.tar.gz -C /opt/

RUN useradd -m -d /home/developer \
    -s /bin/bash \
    -G sudo,video \
    -u 1000 \
    -p "$(openssl passwd -1 developer)" \
    developer


USER developer
WORKDIR /home/developer

RUN echo "developer" | sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
RUN git clone https://github.com/zsh-users/zsh-history-substring-search ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-history-substring-search

RUN sed -i 's/plugins=(git)/plugins=(git history-substring-search)/' .zshrc
RUN sed -i 's/ZSH_THEME="robbyrussell"/ZSH_THEME="kphoen"/' .zshrc

RUN echo "setopt rmstarsilent" >> .zshrc

RUN echo "export CUDA_HOME=/usr/local/cuda" >> .zshrc && \
    echo "export LD_LIBRARY_PATH=\$CUDA_HOME/lib64" >> .zshrc && \
    echo "export LD_LIBRARY_PATH=\$LD_LIBRARY_PATH:\$CUDA_HOME/extras/CUPTI/lib64" >> .zshrc && \
    echo "export DYLD_LIBRARY_PATH=\$CUDA_HOME/lib64" >> .zshrc

RUN wget https://repo.anaconda.com/archive/Anaconda3-2018.12-Linux-x86_64.sh -O ~/anaconda.sh && \
    bash ~/anaconda.sh -b -p $HOME/anaconda && \
    export PATH="$HOME/anaconda/bin:$PATH" && \
    echo "source $HOME/anaconda/bin/activate" >> .zshrc

RUN ~/anaconda/bin/conda install python=3.6

RUN ~/anaconda/bin/pip install --upgrade -q tensorflow-gpu
RUN ~/anaconda/bin/pip install --upgrade -q keras
RUN ~/anaconda/bin/pip install --upgrade -q tflearn

USER root
RUN apt-get install -y libsm6 libxrender1 libfontconfig1 mlocate libxtst6 libxi-dev

USER developer
WORKDIR /home/developer

RUN ~/anaconda/bin/pip install --upgrade -q opencv-python
RUN ~/anaconda/bin/pip install --upgrade -q opencv-contrib-python

