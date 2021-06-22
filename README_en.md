# Check IP (Django)

Lookup IP to location server via Akamai EdgeScape
[中文](./README.md)

## 1. Enviourment Required

- Python 3.8+
- django
- akadata <https://pypi.org/project/akadata/>
- uwsgi
- nothing else (maybe, I forgot that...)

## 2. How It Works

1. Using akadata to check result with Akamai Edgescape API

## 3. How To Deploy

1. Deploy your Edgescape on server and make sure of it works;
2. Pull this repo to your server;
3. Update the config file at _**ini/uwsgi.ini**_ which refer to uwsgi.example.ini;
4. Config nginx or the other web server;
5. Send request to your server with path: /es?ip={{ip}}.
   For example:
   | Hostname        | SSL/TLS | IP      | URL     |
   | :-------------- | :------ | :------ | :------ |
   | cip.example.com | Y       | 1.1.1.1 | <http://cip.example.com/es?ip=1.1.1.1> |
   Result:

   ``` Shell
   1.1.1.1: [ country_code: AU, region_code: NSW, city: SYDNEY, company: APNIC_and_Cloudflare_DNS_Resolver_project, timezone: GMT+10, default_answer: N ]
   ```

6. You can also update the code in _**edgescape/views.py: Line 4-12**_ if your feel there are not enough information about this;
7. Edit service file which reffer to _**ini/django-cip.sample.service**_ and copy to your systemd path;
8. Start cip with systemd service and config boot-start if you want.
9. Cheers.
