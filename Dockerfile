from registry.cn-shanghai.aliyuncs.com/fengzhihao/centos:7
RUN mkdir /mnt/dool
RUN pip3 install kafka-python -i https://mirrors.aliyun.com/pypi/simple/ 
RUN pip3 install websocket-client -i https://mirrors.aliyun.com/pypi/simple/ 

ADD . /mnt/dool

Workdir /mnt/dool
# docker build -f Dockerfile -t registry.cn-shanghai.aliyuncs.com/fengzhihao/centos:dool .
# docker push registry.cn-shanghai.aliyuncs.com/fengzhihao/centos:dool
# docker run -it --rm --name=dool registry.cn-shanghai.aliyuncs.com/fengzhihao/centos:dool /bin/bash


# 查看所有插件
# /mnt/dool/dool --list

# 