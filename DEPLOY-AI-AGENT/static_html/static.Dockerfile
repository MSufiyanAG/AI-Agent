# decalring what image to use
FROM python:alpine3.22

WORKDIR /app
# RUN mkdir -p /static_folder

# COPY ./static_html /static_folder

COPY ./src .
#RUN echo "hello" > index.html

# docker build -f Dockerfile -t pyapp .
# docker run -it pyapp

# docker build -f Dockerfile -t sufiyan19/pyapp-test:latest .
# docker push sufiyan19/pyapp-test:latest

# python -m http.server 8000 
# http://127.0.0.1:8000
#docker run -it -p 8000:8000 pyapp
CMD ["python", "-m", "http.server", "8000"]