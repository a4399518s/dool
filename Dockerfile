from registry.cn-shanghai.aliyuncs.com/fengzhihao/centos:7
RUN mkdir /mnt/dool
Workdir /mnt/dool
# docker build -f Dockerfile -t registry.cn-shanghai.aliyuncs.com/fengzhihao/centos:dool .
# docker push registry.cn-shanghai.aliyuncs.com/fengzhihao/centos:dool
# docker run -it --rm -v /Users/fzh/project/fzh/dool:/mnt/dool --name=dool registry.cn-shanghai.aliyuncs.com/fengzhihao/centos:dool /bin/bash


# /mnt/dool/dool --list