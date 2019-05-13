FROM alpine:3.9

RUN apk update && apk upgrade
RUN pip3 install --upgrade pip
RUN apk --no-cache --update-cache add git python3 python3-dev python3-numpy gcc gfortran musl-dev g++ libxslt-dev libxml2-dev

RUN mkdir /app
WORKDIR /app

# Add local files
COPY templates ./templates
COPY statics ./statics
COPY flaskapp.py *.tar boot.sh cltk_install.py requirements.txt ./
RUN chmod +x boot.sh

# Install Pie and Pie Webapp requirements
RUN pip3 install $(cat requirements.txt) \
    https://download.pytorch.org/whl/cpu/torch-1.1.0-cp37-cp37m-linux_x86_64.whl \
    gunicorn

RUN python3 cltk_install.py

# Small checkup
# RUN ls

EXPOSE 5000
ENTRYPOINT ["/app/boot.sh"]