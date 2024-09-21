sudo docker build . -t img-resume
sudo docker run --name resume -d -p 8000:8000 --restart unless-stopped img-resume

