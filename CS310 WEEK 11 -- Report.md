What process did you follow for creating the dockerfile
    My first step in creating the docker file was to specify the base image. Because flask uses python I chose python:3.10-slim for the base image.The next major step was to ensure the flask application requirements were met. I used pip install -r requirements.txt to install all the dependencies which in this case was just flask.The last job of the docker file was to establish the script the container will run after setup is complete. In this case the docker file runs python simpleFlaskApp.py.

What docker commands did you use to run the image
    After installing the image of the server I was able to run the image using the command sudo docker run -d -p 5000:5000 flask_app_image:v1.2

