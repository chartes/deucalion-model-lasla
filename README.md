Deucalion Model Latin ENC - LASLA
===================================

[![Lien Docker](https://img.shields.io/docker/pulls/ponteineptique/deucalion-model-lasla.svg)](https://cloud.docker.com/repository/docker/ponteineptique/deucalion-model-lasla)

# Credits

*   D. Longrée, C. Philippart de Foy & G. Purnelle. « Structures phrastiques et analyse automatique des données morphosyntaxiques : le projet LatSynt », in S. Bolasco, I. Chiari & L. Giuliano (eds), Statistical Analysis of Textual Data, Proceedings of 10th International Conference Journées d'Analyse statistique des Données Textuelles, 9-11 June 2010, Sapienza University of Rome, Rome, LED, pp. 433-442.
*   D. Longrée & C. Poudat, « New Ways of Lemmatizing and Tagging Classical and post-Classical Latin: the LATLEM project of the LASLA », in P. Anreiter & M. Kienpointner (éd.), Proceedings of the 15th International Colloquium on Latin Linguistics, (Innsbrucker Beiträge zur Sprachwissenschaft), Innsbruck, 2010, pp. 683-694.
*   D. Longrée & C. Philippart de Foy & G. Purnelle, « Subordinate clause boundaries and word order in Latin: the contribution of the L.A.S.L.A. syntactic parser project LatSynt », in P. Anreiter & M. Kienpointner, éd.), Proceedings of the 15th International Colloquium on Latin Linguistics, (Innsbrucker Beiträge zur Sprachwissenschaft), Innsbruck, 2010, pp. 673-681.
*   D. Longrée & Poudat C., « Variations langagières et annotation morphosyntaxique du latin classique », TAL, 50 – n° 2/2009, Special issue on "Natural Language Processing and Ancient Languages", pp. 129-148.
*   Enrique Manjavacas & Mike Kestemont. (2019, January 17). emanjavacas/pie v0.1.3 (Version v0.1.3). Zenodo. http://doi.org/10.5281/zenodo.2542537 _Check the latest version here :_[Zenodo DOI](https://doi.org/10.5281/zenodo.1637877)
*   Thibault Clérice. (2019, February 1). chartes/deucalion-model-lasla: LASLA Latin Lemmatizer - Alpha (Version 0.0.1). Zenodo. http://doi.org/10.5281/zenodo.2554847 _Check the latest version here :_[Zenodo DOI](https://doi.org/10.5281/zenodo.2554846)

The web application and its maintenance is done by Thibault Clérice ( @ponteineptique ). To learn how to cite this repository, go check [our releases](https://github.com/chartes/deucalion-model-af/releases).

# Information about the model

[![LASLA Logo](statics/LogoLASLA2019.png)](http://web.philo.ulg.ac.be/lasla/textes-latins-traites/)

The model is based on the LASLA data.

For more details about the errors, see the [information](information) folder.


# Install

## Locally, without docker: 

```shell script
pip install -r requirements.txt
pie-extended download lasla # Downloads the model
pie-extended install-addons lasla # Install required addons
```
then run with `python flaskapp.py`

## With docker 

To run, you'll need to install Docker. Then, you can simply run the following commands:

```shell
docker pull ponteineptique/deucalion-model-lasla:latest
```

or build locally from source (much longer, more freedom in changing some code source):

```shell
docker build -t deucalion-lasla:latest .
docker run -p 5001:5000 deucalion-lasla:latest
```

You can replace 5001 with any port you want to run the service on.

Then, simply go to  http://127.0.0.1:5001 or directly to http://127.0.0.1:5001/api?data=Quid%20faciat%20volt%20scire%20Lyris%3A%20quod%20sobria%3A%20fellat. or post any data to the same URI with `data` parameters containing your plain text.