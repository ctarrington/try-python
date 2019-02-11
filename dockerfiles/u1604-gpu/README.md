sandbox for ML and opencv with python

# run in host 
```bash
cd dockerfiles/u1604-gpu
docker build -t ct/u1604-gpu .
nvidia-docker run --rm -h u1604-gpu --device=/dev/video0:/dev/video0 -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -p 5000:5000 -p 8888:8888 -v ~/github/try-python/dockerfiles/notebooks:/home/developer/notebooks -it ct/u1604-gpu /bin/zsh
```

# run in guest
```bash
# once to setup editor
sh /opt/pycharm-professional-2018.3.4/bin/pycharm.sh

# setup and log in
```

# run in host before exiting guest
```bash
docker commit <container_id> ct/u1604-gpu-pycharm
```

# normal use
```bash
host > nvidia-docker run --rm -h u1604-gpu --device=/dev/video0:/dev/video0 -v /tmp/.X11-unix:/tmp/.X11-unix -e DISPLAY=$DISPLAY -p 5000:5000 -p 8888:8888 -v ~/github/try-python/dockerfiles/notebooks:/home/developer/notebooks -it ct/u1604-gpu-pycharm /bin/zsh
guest > /opt/pycharm-professional-2018.3.4/bin/pycharm.sh &
guest > cd notebooks && jupyter notebook --ip 0.0.0.0 &
```


# Handy docker scripts
```bash
docker rmi (docker images|grep none| sed 's/\s\+/ /g' | cut -d' ' -f3)
```

# TODO