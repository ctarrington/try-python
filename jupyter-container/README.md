## README

### Links
* https://www.tensorflow.org/install/docker
* https://github.com/NVIDIA/nvidia-docker

### Run
```bash

docker run --runtime=nvidia -it -p 8888:8888 -v /home/ctarrington/github/try-python/jupyter-container/notebooks:/notebooks tensorflow/tensorflow:latest-gpu-py3
```