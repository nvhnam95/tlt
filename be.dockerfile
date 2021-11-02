# set the base image 
FROM python:3.8

#add project files to the usr/src/app folder
COPY ./main /usr/src/app

#set directoty where CMD will execute 
WORKDIR /usr/src/app

COPY requirements.txt ./

# Get pip to download and install requirements:
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports
EXPOSE 80

# default command to execute    
ENTRYPOINT ["gunicorn", "main.wsgi:application", "--bind", "0.0.0.0:80", "--workers", "3"]
