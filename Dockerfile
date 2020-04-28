FROM ponteineptique/pie-flask:v0.1.0

RUN apt-get install -y gcc

COPY templates ./templates
COPY statics ./statics
COPY modules ./modules
COPY flaskapp.py *.tar boot.sh requirements.txt *.json ./
RUN chmod +x boot.sh

RUN pie-extended download lasla && pip install https://github.com/PonteIneptique/cltk/archive/latin_clitics_exceptions.zip --upgrade && pie-extended install-addons lasla

# Small checkup
# RUN ls

EXPOSE 5000
ENTRYPOINT ["/app/boot.sh"]


