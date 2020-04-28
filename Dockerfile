FROM ponteineptique/pie-flask:v0.1.0

RUN apt-get install -y gcc

COPY templates ./templates
COPY statics ./statics
COPY modules ./modules
COPY flaskapp.py boot.sh ./
RUN chmod +x boot.sh

RUN pie-extended download lasla && pip install cltk==0.1.117 && pie-extended install-addons lasla

# Small checkup
# RUN ls

EXPOSE 5000
ENTRYPOINT ["/app/boot.sh"]


