# Check IP (Django)

用以IP地理位置定位的 Akamai EdgeScape 的 CIP Server, 搭配 cip Client 食用风味更佳
[English](./README_en.md)

## 1. 环境

- Python 3.8+
- django
- akadata <https://pypi.org/project/akadata/>
- uwsgi
- (应该)没有其他的了(吧...)

## 2. 工作原理

1. 使用 Python包 akadata 调用 Akamai Edgescape API 进行信息查询

## 3. 部署步骤

1. 先在服务器上部署一个 Edgescape 并确保它运行正常;
2. 将这个 repo 拉到你的 Edgescape 服务器上;
3. 参考 uwsgi.example.ini 配置 _**ini/uwsgi.ini**_;
4. 配置 nginx 或者其他 Web Server;
5. 对你服务器上的一下路径发起请求: /es?ip={{ip}}.
   举个栗子:
   | 域名        | SSL/TLS | IP      | URL     |
   | :-------------- | :------ | :------ | :------ |
   | cip.example.com | Y       | 1.1.1.1 | <http://cip.example.com/es?ip=1.1.1.1> |
   结果:

   ``` Shell
   1.1.1.1: [ country_code: AU, region_code: NSW, city: SYDNEY, company: APNIC_and_Cloudflare_DNS_Resolver_project, timezone: GMT+10, default_answer: N ]
   ```

6. 如果你觉得这个结果看起来信息不够, 或者信息太多, 或者就是看他不爽, 可以在 _**edgescape/views.py: 第 4-12 行**_ 修改成你想要的字段;
7. 根据 _**ini/django-cip.sample.service**_ 编辑一个 systemd service 文件, 并保存到 systemd 目录里;
8. 使用 systemd 服务启动, 可选性的设置开机启动;
9. 结束.
