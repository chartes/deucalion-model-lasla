FROM ponteineptique/pie-flask:v0.0.7

RUN apt-get install -y gcc

COPY templates ./templates
COPY statics ./statics
COPY modules ./modules
COPY flaskapp.py *.tar boot.sh cltk_install.py requirements.txt *.json ./
RUN chmod +x boot.sh

RUN pip3 install cltk && python3 cltk_install.py

# Small checkup
# RUN ls

EXPOSE 5000
ENTRYPOINT ["/app/boot.sh"]


