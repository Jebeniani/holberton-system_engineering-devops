#Web server

![alt text](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/266/8Gu52Qv.png)

n this project, some of the tasks will be graded on 2 aspects:

    Is your web-01 server configured according to requirements
    Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)

For example, if I need to create a file /tmp/test containing the string hello world and modify the configuration of Nginx to listen on port 8080 instead of 80, I can use emacs on my server to create the file and to modify the Nginx configuration file /etc/nginx/sites-enabled/default.

But my answer file would contain:
```bash
jebeniani@ubuntu cat 88-script_example
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default
jebeniani@ubuntu
```

##General
* What is the main role of a web server
* What is a child process
* Why web servers usually have a parent process and child processes
* What are the main HTTP requests
##DNS
* A
* CNAME
* TXT
* MX
