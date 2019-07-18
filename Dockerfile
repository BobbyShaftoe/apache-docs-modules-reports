#FROM centos/httpd-24-centos7:latest
FROM httpd-new
USER 1001

RUN yum update -y --skip-broken && \
      yum install -y discount


