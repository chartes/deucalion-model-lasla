FROM ubuntu:18.04

RUN mkdir /app
WORKDIR /app

# Base install
RUN apt-get update && apt-get install -y zip python3.6 python3.6-dev python3-venv python3-pip git
RUN pip3 install --upgrade pip

# Install Pie and Pie Webapp requirements
RUN pip3 install https://github.com/hipster-philology/pie-flask/archive/master.zip#egg=flask_pie cltk gunicorn

# Add local files
COPY templates ./templates
COPY statics ./statics
COPY flaskapp.py model-json.tar boot.sh cltk_install.py ./
RUN chmod +x boot.sh

RUN python3 cltk_install.py

# Small checkup
# RUN ls

ENV PIE_MODEL "<model-json.tar>"

EXPOSE 5000
ENTRYPOINT ["/app/boot.sh"]