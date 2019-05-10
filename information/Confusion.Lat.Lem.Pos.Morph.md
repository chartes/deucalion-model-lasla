Confusion tables
================

- [Lemma](#lemma)
- [Part-Of-Speech](#pos)
- [Voice](#voice)
- [Mood](#mood)
- [Degree](#degree)
- [Numb](#numb)
- [Person](#person)
- [Tense](#tense)
- [Case](#case)
- [Gender](#gender)

```
all:
  accuracy: 0.9752
  precision: 0.8379
  recall: 0.8307
  support: 141348
ambiguous-tokens:
  accuracy: 0.9273
  precision: 0.7114
  recall: 0.7143
  support: 31164
unknown-targets:
  accuracy: 0.6205
  precision: 0.4523
  recall: 0.442
  support: 983
unknown-tokens:
  accuracy: 0.8711
  precision: 0.7355
  recall: 0.7282
  support: 6091
```

| Expected        | Total Errors | Predictions         | Predicted times |
|-----------------|--------------|---------------------|-----------------|
| qvi             | 203          | qvod                | 88              |
|                 |              | qvis                | 54              |
|                 |              | qvo                 | 29              |
|                 |              | qvam                | 26              |
|                 |              | qva                 | 3               |
|                 |              | privsqvam           | 2               |
|                 |              | anteqvam            | 1               |
| qvis            | 166          | qvi                 | 142             |
|                 |              | qvo                 | 6               |
|                 |              | qvod                | 6               |
|                 |              | qvam                | 5               |
|                 |              | qva                 | 4               |
|                 |              | privsqvam           | 2               |
|                 |              | cvivs               | 1               |
| qvod            | 73           | qvi                 | 70              |
|                 |              | qvis                | 3               |
| mvltvs          | 33           | mvltvm              | 24              |
|                 |              | mvlti               | 9               |
| bonvs           | 28           | bonvm               | 19              |
|                 |              | boni                | 6               |
|                 |              | bene                | 3               |
| qvam            | 26           | qvi                 | 16              |
|                 |              | privsqvam           | 7               |
|                 |              | posteaqvam          | 1               |
|                 |              | qvis                | 1               |
|                 |              | anteqvam            | 1               |
| svi             | 24           | svvs                | 20              |
|                 |              | ipse                | 4               |
| svvs            | 24           | svi                 | 22              |
|                 |              | svvm                | 2               |
| is              | 22           | eo                  | 21              |
|                 |              | ecce                | 1               |
| malvs           | 19           | malvm               | 16              |
|                 |              | mali                | 1               |
|                 |              | male                | 1               |
|                 |              | mala                | 1               |
| boni            | 18           | bonvm               | 16              |
|                 |              | bonvs               | 2               |
| factvm          | 17           | facio               | 17              |
| parvvs          | 17           | parvm               | 11              |
|                 |              | minimvm             | 2               |
|                 |              | pareo               | 2               |
|                 |              | parvvm              | 2               |
| mvlti           | 16           | mvltvs              | 16              |
| solvs           | 15           | solvm               | 15              |
| pondo           | 15           | pes                 | 15              |
| qvantvs         | 15           | qvantvm             | 13              |
|                 |              | qvanto              | 2               |
| qvo             | 14           | qvi                 | 13              |
|                 |              | qvis                | 1               |
| svvm            | 13           | svvs                | 13              |
| anteqvam        | 12           | qvam                | 8               |
|                 |              | qvi                 | 2               |
|                 |              | privsqvam           | 2               |
| cetervs         | 12           | ceteri              | 10              |
|                 |              | cetera              | 2               |
| nascor          | 12           | natvs               | 9               |
|                 |              | nata                | 3               |
| noster          | 12           | nos                 | 10              |
|                 |              | nostri              | 2               |
| vervm           | 11           | vervs               | 9               |
|                 |              | vero                | 2               |
| mvltvm          | 11           | mvltvs              | 11              |
| primvs          | 11           | primvm              | 9               |
|                 |              | primo               | 2               |
| honestvs        | 11           | honestvm            | 9               |
|                 |              | honeste             | 1               |
|                 |              | honestas            | 1               |
| vnvs            | 11           | vna                 | 9               |
|                 |              | vnvm                | 2               |
| liber           | 10           | liberi              | 10              |
| facio           | 10           | factvm              | 7               |
|                 |              | facies              | 3               |
| paro            | 10           | paratvs             | 7               |
|                 |              | pareo               | 3               |
| tracta          | 10           | traho               | 10              |
| falsvm          | 9            | falsvs              | 9               |
| eo              | 9            | is                  | 9               |
| modvs           | 9            | modo                | 9               |
| svm             | 8            | fvtvrvs             | 2               |
|                 |              | vaniloqvo           | 1               |
|                 |              | foris               | 1               |
|                 |              | fvtvrvm             | 1               |
|                 |              | svmmanvs            | 1               |
|                 |              | qvemadmodvm         | 1               |
|                 |              | scio                | 1               |
| qva             | 8            | qvi                 | 6               |
|                 |              | qvis                | 2               |
| lego            | 8            | lex                 | 5               |
|                 |              | lectvs              | 3               |
| vervs           | 8            | vervm               | 6               |
|                 |              | vero                | 1               |
|                 |              | ver                 | 1               |
| volo            | 8            | vis                 | 2               |
|                 |              | volvo               | 2               |
|                 |              | velvm               | 2               |
|                 |              | volens              | 1               |
|                 |              | svm                 | 1               |
| plervsqve       | 7            | pleriqve            | 7               |
| nocte           | 7            | nox                 | 7               |
| oenothea        | 7            | oenothevs           | 7               |
| pompeianvs      | 7            | pompeiani           | 7               |
| medivs          | 7            | medivm              | 7               |
| rigeo           | 6            | rigo                | 6               |
| pavci           | 6            | pavcvs              | 6               |
| reliqvi         | 6            | reliqvvs            | 6               |
| nox             | 6            | nocte               | 4               |
|                 |              | noctv               | 2               |
| mevs            | 6            | ego                 | 6               |
| minimvm         | 6            | parvvs              | 6               |
| qvantvm         | 6            | qvantvs             | 6               |
| ego             | 6            | mevs                | 6               |
| libra           | 6            | littera             | 6               |
| meritvs         | 6            | mereor              | 3               |
|                 |              | meritvm             | 2               |
|                 |              | mereo               | 1               |
| bene            | 6            | bonvs               | 6               |
| paratvs         | 6            | paro                | 6               |
| vna             | 5            | vnvs                | 5               |
| adversvs        | 5            | adversvm            | 5               |
| triginta        | 5            | centvm              | 1               |
|                 |              | tricesimvs          | 1               |
|                 |              | octoginta           | 1               |
|                 |              | sex                 | 1               |
|                 |              | dvo                 | 1               |
| secretvs        | 5            | secretvm            | 4               |
|                 |              | secerno             | 1               |
| tvi             | 5            | tvvs                | 5               |
| mali            | 5            | malvm               | 3               |
|                 |              | malvs               | 2               |
| dictvm          | 5            | dico                | 5               |
| xenon           | 5            | xeno                | 5               |
| glycon          | 5            | glycvs              | 4               |
|                 |              | glyconis            | 1               |
| hic             | 5            | hac                 | 4               |
|                 |              | ne                  | 1               |
| svpervs         | 5            | svmma               | 3               |
|                 |              | svperi              | 1               |
|                 |              | svmmvm              | 1               |
| antiqvvs        | 5            | antiqvi             | 4               |
|                 |              | antiqve             | 1               |
| primo           | 5            | primvs              | 5               |
| fervs           | 5            | fera                | 5               |
| cetera          | 5            | cetervs             | 5               |
| privsqvam       | 5            | qvam                | 2               |
|                 |              | qvi                 | 2               |
|                 |              | anteqvam            | 1               |
| fera            | 5            | fervs               | 4               |
|                 |              | fero                | 1               |
| solitvs         | 5            | soleo               | 3               |
|                 |              | solitvm             | 2               |
| fvlgens         | 5            | fvlgeo              | 5               |
| opera           | 5            | opvs                | 5               |
| bonvm           | 5            | boni                | 4               |
|                 |              | bonvs               | 1               |
| tantvs          | 5            | tantvm              | 5               |
| maiores         | 5            | magnvs              | 5               |
| pavcvs          | 5            | pavci               | 5               |
| tvvs            | 5            | tv                  | 2               |
|                 |              | tvi                 | 2               |
|                 |              | tvvm                | 1               |
| hirnea          | 5            | hirnevs             | 3               |
|                 |              | irnevs              | 2               |
| ivre            | 5            | ivs                 | 5               |
| consto          | 5            | consisto            | 5               |
| venio           | 5            | venia               | 2               |
|                 |              | veneo               | 2               |
|                 |              | ventvs              | 1               |
| insignis        | 4            | insigne             | 4               |
| mvnitvs         | 4            | mvnio               | 4               |
| vtor            | 4            | vt                  | 4               |
| mei             | 4            | mevs                | 4               |
| sacrvm          | 4            | sacer               | 4               |
| dvbivm          | 4            | dvbivs              | 4               |
| pvllo           | 4            | pvllvs              | 4               |
| alica           | 4            | alicvs              | 4               |
| svllanvs        | 4            | syllanvs            | 4               |
| promissvm       | 4            | promitto            | 4               |
| aperio          | 4            | apertvs             | 4               |
| fero            | 4            | fera                | 2               |
|                 |              | latvs               | 1               |
|                 |              | ferrvm              | 1               |
| veneo           | 4            | venio               | 4               |
| elorvs          | 4            | helorvs             | 4               |
| pasco           | 4            | pascor              | 4               |
| vniversi        | 4            | vniversvs           | 3               |
|                 |              | vniversvm           | 1               |
| ivro            | 4            | ivs                 | 2               |
|                 |              | ivratvs             | 1               |
|                 |              | ivratvra            | 1               |
| potissimvm      | 4            | potivs              | 4               |
| mala            | 4            | malvs               | 4               |
| ago             | 4            | age                 | 1               |
|                 |              | actvm               | 1               |
|                 |              | agite               | 1               |
|                 |              | svm                 | 1               |
| orno            | 4            | ornatvs             | 3               |
|                 |              | ornate              | 1               |
| testvm          | 4            | testvs              | 3               |
|                 |              | testo               | 1               |
| perdo           | 4            | perditvs            | 4               |
| citvs           | 4            | cieo                | 2               |
|                 |              | cito                | 2               |
| alias           | 4            | alivs               | 4               |
| svmma           | 4            | svpervs             | 2               |
|                 |              | svmmvm              | 2               |
| exter           | 4            | extremvm            | 3               |
|                 |              | extrema             | 1               |
| sera            | 4            | sero                | 4               |
| volvcris        | 4            | volvcer             | 4               |
| iacio           | 4            | iaceo               | 4               |
| alienvs         | 4            | alienvm             | 4               |
| armatvs         | 4            | armati              | 3               |
|                 |              | armo                | 1               |
| refero          | 4            | refert              | 4               |
| fvtvrvm         | 4            | fvtvrvs             | 3               |
|                 |              | svm                 | 1               |
| sacer           | 4            | sacrvm              | 4               |
| vltimvs         | 4            | vltimvm             | 4               |
| opvs            | 4            | opera               | 4               |
| dicto           | 4            | dico                | 2               |
|                 |              | dictvm              | 1               |
|                 |              | dictatvm            | 1               |
| nosco           | 4            | notvs               | 2               |
|                 |              | novvs               | 1               |
|                 |              | ne                  | 1               |
| ceteri          | 4            | cetervs             | 4               |
| catinvm         | 4            | catinvs             | 4               |
| malvm           | 4            | malvs               | 4               |
| actvm           | 4            | ago                 | 4               |
| magnvm          | 4            | magnvs              | 4               |
| dedo            | 4            | do                  | 4               |
| video           | 4            | visvs               | 3               |
|                 |              | visvm               | 1               |
| pango           | 4            | paciscor            | 2               |
|                 |              | pactvs              | 1               |
|                 |              | pactvm              | 1               |
| mereor          | 3            | meritvm             | 2               |
|                 |              | merens              | 1               |
| qvisqve         | 3            | qvoqve              | 2               |
|                 |              | qvisqvis            | 1               |
| ora             | 3            | os                  | 3               |
| volens          | 3            | volo                | 3               |
| tertivs         | 3            | tertio              | 3               |
| qvoqve          | 3            | qvisqve             | 3               |
| placo           | 3            | placeo              | 3               |
| tantvm          | 3            | tantvs              | 3               |
| orior           | 3            | ortvs               | 2               |
|                 |              | oriens              | 1               |
| ne              | 3            | nvllvs              | 1               |
|                 |              | ego                 | 1               |
|                 |              | ceresis             | 1               |
| mando           | 3            | mandatvm            | 3               |
| alivs           | 3            | alio                | 3               |
| praesentia      | 3            | praesens            | 3               |
| potis           | 3            | potivs              | 2               |
|                 |              | poto                | 1               |
| scriptvm        | 3            | scribo              | 2               |
|                 |              | scripta             | 1               |
| trecenvs        | 3            | tricenvs            | 3               |
| altvs           | 3            | altvm               | 3               |
| desertvs        | 3            | desero              | 3               |
| imvm            | 3            | infervs             | 3               |
| nvntivs         | 3            | nvntivm             | 2               |
|                 |              | nvntio              | 1               |
| profvndo        | 3            | profvsvs            | 3               |
| exentero        | 3            | exintero            | 3               |
| dvco            | 3            | dvcenti             | 2               |
|                 |              | dvx                 | 1               |
| svmmvm          | 3            | svpervs             | 3               |
| soleo           | 3            | solea               | 2               |
|                 |              | soletvm             | 1               |
| reliqvvs        | 3            | reliqvvm            | 2               |
|                 |              | reliqvi             | 1               |
| conivngo        | 3            | conivnctvs          | 3               |
| como            | 3            | comptvs             | 3               |
| picenvs         | 3            | picenvm             | 3               |
| satvr           | 3            | sero                | 2               |
|                 |              | satvrvs             | 1               |
| mille           | 3            | triginta            | 1               |
|                 |              | trecenti            | 1               |
|                 |              | dvo                 | 1               |
| brevis          | 3            | brevi               | 3               |
| reliqvvm        | 3            | reliqvvs            | 3               |
| ardeo           | 3            | ardens              | 3               |
| pedes           | 3            | pes                 | 3               |
| victvs          | 3            | vinco               | 3               |
| em              | 3            | hem                 | 3               |
| lectvs          | 3            | lego                | 3               |
| dexter          | 3            | dextera             | 2               |
|                 |              | dextervs            | 1               |
| laevvm          | 3            | laevvs              | 2               |
|                 |              | laeva               | 1               |
| florens         | 3            | floreo              | 3               |
| thessali        | 3            | thessalvs           | 3               |
| acta            | 3            | actvm               | 2               |
|                 |              | ago                 | 1               |
| arcessitvs      | 3            | arcesso             | 3               |
| captiva         | 3            | captivvs            | 3               |
| prodeo          | 3            | prodo               | 3               |
| bomilcar        | 3            | bomilcaris          | 2               |
|                 |              | bomilcarvs          | 1               |
| propior         | 3            | proximvm            | 3               |
| ivs             | 3            | ivre                | 2               |
|                 |              | ivro                | 1               |
| sextarivs       | 3            | semis               | 3               |
| editvs          | 3            | edo                 | 3               |
| natvs           | 3            | nascor              | 3               |
| rectvm          | 3            | rectvs              | 3               |
| caelestes       | 3            | caelestis           | 2               |
|                 |              | caelestia           | 1               |
| magnvs          | 3            | maiores             | 3               |
| occvltvs        | 3            | occvltvm            | 1               |
|                 |              | occvlo              | 1               |
|                 |              | occvlte             | 1               |
| flavianvs       | 3            | flaviani            | 3               |
| cognitvs        | 3            | cognosco            | 3               |
| nvbo            | 3            | nvpta               | 3               |
| evge            | 3            | evgeo               | 3               |
| certvm          | 3            | certvs              | 3               |
| fvtvrvs         | 3            | svm                 | 2               |
|                 |              | fvtvrvm             | 1               |
| incertvm        | 3            | incertvs            | 3               |
| avvs            | 3            | avis                | 3               |
| lavtvs          | 3            | lavo                | 3               |
| fraces          | 3            | frax                | 2               |
|                 |              | fraceo              | 1               |
| milito          | 3            | militaris           | 2               |
|                 |              | miles               | 1               |
| secvndvm        | 3            | secvndvs            | 3               |
| gallvs          | 3            | galli               | 3               |
| mensis          | 3            | mensa               | 3               |
| stvltvs         | 3            | stvlti              | 2               |
|                 |              | stvlte              | 1               |
| hvc             | 3            | hic                 | 3               |
| veteres         | 3            | vetvs               | 3               |
| comitivm        | 3            | comitia             | 3               |
| pendo           | 3            | pendeo              | 3               |
| aer             | 3            | aes                 | 3               |
| refert          | 3            | refero              | 3               |
| nymphon         | 3            | nymphvs             | 3               |
| bellvs          | 3            | bellvm              | 3               |
| reporto         | 3            | reporior            | 3               |
| revs            | 3            | res                 | 3               |
| honestvm        | 3            | honestvs            | 3               |
| mervs           | 3            | mervm               | 3               |
| spons           | 3            | sponte              | 3               |
| philoxenvs      | 3            | philoxene           | 3               |
| commis          | 3            | cvmmim              | 2               |
|                 |              | cvmmis              | 1               |
| lino            | 3            | linitvm             | 1               |
|                 |              | linio               | 1               |
|                 |              | levo                | 1               |
| rogvs           | 3            | rogo                | 3               |
| helena          | 2            | helene              | 2               |
| regia           | 2            | regivs              | 2               |
| vniversvs       | 2            | vniversvm           | 2               |
| egero           | 2            | ago                 | 2               |
| aspectvs        | 2            | aspicio             | 2               |
| vereor          | 2            | verens              | 1               |
|                 |              | verendvs            | 1               |
| erectvs         | 2            | erigo               | 2               |
| pilvs           | 2            | pilvm               | 2               |
| tvrpis          | 2            | tvrpe               | 2               |
| hospita         | 2            | hospitvs            | 2               |
| delphinvs       | 2            | delphina            | 1               |
|                 |              | delphin             | 1               |
| tarracinensis   | 2            | terracinensis       | 2               |
| calidvs         | 2            | calidvm             | 2               |
| profvndvs       | 2            | profvndvm           | 2               |
| phoebe          | 2            | phoebvs             | 2               |
| lapsvs          | 2            | labor               | 2               |
| manes           | 2            | manvs               | 2               |
| intentvs        | 2            | intendo             | 2               |
| venia           | 2            | venio               | 2               |
| myoparon        | 2            | myoparvs            | 1               |
|                 |              | myoparvm            | 1               |
| arte            | 2            | ars                 | 2               |
| pilevm          | 2            | pilevs              | 2               |
| externi         | 2            | externvs            | 1               |
|                 |              | externvm            | 1               |
| pingo           | 2            | pictvs              | 2               |
| heracleon       | 2            | heraclevs           | 2               |
| viridans        | 2            | virido              | 2               |
| italvs          | 2            | itali               | 2               |
| palleo          | 2            | pallens             | 2               |
| proprivm        | 2            | proprivs            | 2               |
| contrarivs      | 2            | contrarivm          | 2               |
| doceo           | 2            | doctvs              | 2               |
| altvm           | 2            | altvs               | 2               |
| naevolvs        | 2            | naevole             | 2               |
| marsyas         | 2            | marsya              | 2               |
| idem            | 2            | eodem               | 2               |
| nostri          | 2            | noster              | 2               |
| abscido         | 2            | abscindo            | 1               |
|                 |              | abscidvs            | 1               |
| sedvco          | 2            | sedvctvs            | 2               |
| vinco           | 2            | victvs              | 1               |
|                 |              | vincio              | 1               |
| svrripio        | 2            | svbrvopvo           | 1               |
|                 |              | svbrvpio            | 1               |
| respvblica      | 2            | res                 | 2               |
| cvro            | 2            | cvra                | 1               |
|                 |              | cvratvs             | 1               |
| caneo           | 2            | cano                | 2               |
| avris           | 2            | avra                | 2               |
| sol             | 2            | solvm               | 1               |
|                 |              | solvs               | 1               |
| ramenta         | 2            | ramentvm            | 2               |
| habitvs         | 2            | habeo               | 2               |
| scriptito       | 2            | scribtito           | 2               |
| intersaepio     | 2            | intersapio          | 1               |
|                 |              | intersipio          | 1               |
| constratvs      | 2            | consterno           | 2               |
| vanvm           | 2            | vanvs               | 2               |
| dvodeni         | 2            | dvodenvs            | 2               |
| impendo         | 2            | impendeo            | 1               |
|                 |              | impensvm            | 1               |
| ornatvs         | 2            | orno                | 2               |
| tribvs          | 2            | tres                | 2               |
| testv           | 2            | testvs              | 2               |
| mvstela         | 2            | mvstelae            | 1               |
|                 |              | mvstella            | 1               |
| sicvlvs         | 2            | sicvli              | 2               |
| viginti         | 2            | qvatvor             | 1               |
|                 |              | tres                | 1               |
| vaccenses       | 2            | vagenses            | 2               |
| libita          | 2            | libet               | 2               |
| consvlto        | 2            | consvltvm           | 2               |
| isti            | 2            | iste                | 2               |
| centvm          | 2            | triginta            | 1               |
|                 |              | clilices            | 1               |
| dvodeviginti    | 2            | trecenti            | 1               |
|                 |              | tredecim            | 1               |
| scribo          | 2            | scriba              | 1               |
|                 |              | scriptvm            | 1               |
| devotvs         | 2            | devoveo             | 2               |
| medivm          | 2            | medivs              | 2               |
| pvllvm          | 2            | pvllvs              | 2               |
| antiqvi         | 2            | antiqvvs            | 2               |
| pinarvs         | 2            | pinae               | 2               |
| inane           | 2            | inanis              | 2               |
| effero          | 2            | extollo             | 2               |
| frango          | 2            | fractvs             | 2               |
| avis            | 2            | avvs                | 2               |
| praeparatvs     | 2            | praeparatvm         | 1               |
|                 |              | praeparo            | 1               |
| refvgvs         | 2            | refvgio             | 2               |
| bosporvs        | 2            | bosphorvs           | 2               |
| albvs           | 2            | albvm               | 2               |
| ivssvm          | 2            | ivbeo               | 2               |
| doctvs          | 2            | doceo               | 2               |
| sterno          | 2            | stratvm             | 2               |
| pertvrbo        | 2            | pertvrbatvs         | 2               |
| praeceptor      | 2            | praeceptvm          | 2               |
| propinqvi       | 2            | propinqvvs          | 2               |
| dico            | 2            | dictvm              | 2               |
| gener           | 2            | genvs               | 2               |
| svbrepo         | 2            | svrripio            | 2               |
| svspensvs       | 2            | svspendo            | 2               |
| svperior        | 2            | svpervs             | 2               |
| alienvm         | 2            | alienvs             | 2               |
| breviter        | 2            | brevis              | 2               |
| mamilla         | 2            | mamillvm            | 2               |
| praeficio       | 2            | praefectvs          | 2               |
| pareo           | 2            | parro               | 2               |
| pvgna           | 2            | pvgnvs              | 2               |
| evergetae       | 2            | evergeta            | 1               |
|                 |              | evergetas           | 1               |
| teneo           | 2            | tener               | 2               |
| propivs         | 2            | prope               | 2               |
| proximvm        | 2            | propior             | 2               |
| artvs           | 2            | artvm               | 1               |
|                 |              | ars                 | 1               |
| mvlto           | 2            | mvltvs              | 2               |
| finitimvs       | 2            | finitimi            | 2               |
| fictvs          | 2            | fingo               | 2               |
| vngo            | 2            | vnctvs              | 2               |
| expressvs       | 2            | exprimo             | 2               |
| vetvs           | 2            | veteres             | 2               |
| fretvs          | 2            | fretvm              | 2               |
| percoqvo        | 2            | percoqvor           | 1               |
|                 |              | percoco             | 1               |
| pone            | 2            | pono                | 2               |
| appositvs       | 2            | appono              | 2               |
| proceres        | 2            | procer              | 2               |
| vlterior        | 2            | vltra               | 1               |
|                 |              | vlteriora           | 1               |
| contremo        | 2            | contremisco         | 2               |
| commodvs        | 2            | commodvm            | 2               |
| svblimis        | 2            | svblime             | 1               |
|                 |              | svblimiter          | 1               |
| sthenivs        | 2            | stheni              | 2               |
| legatvm         | 2            | legatvs             | 2               |
| pleriqve        | 2            | plervsqve           | 2               |
| vos             | 2            | vestri              | 1               |
|                 |              | vester              | 1               |
| coqvvs          | 2            | coqvo               | 2               |
| pilvm           | 2            | pilvs               | 1               |
|                 |              | pila                | 1               |
| ivdex           | 2            | ivdico              | 2               |
| mane            | 2            | maneo               | 2               |
| decor           | 2            | decvs               | 2               |
| libvrnica       | 2            | libvrnicvs          | 2               |
| lvdificor       | 2            | lvdifico            | 2               |
| sestertivs      | 2            | sestertivm          | 2               |
| obsido          | 2            | obsideo             | 2               |
| qvantvlvm       | 2            | qvantvlvs           | 2               |
| amo             | 2            | amans               | 2               |
| baltevs         | 2            | baltea              | 1               |
|                 |              | baltevm             | 1               |
| exigve          | 2            | exigvvs             | 2               |
| convictvs       | 2            | convinco            | 2               |
| bacchis         | 2            | baccha              | 2               |
| tectorivm       | 2            | tectoria            | 2               |
| graecvs         | 2            | graeci              | 2               |
| proficiscor     | 2            | proficio            | 1               |
|                 |              | profecto            | 1               |
| totvs           | 2            | totvm               | 2               |
| ortvs           | 2            | orior               | 2               |
| meracvs         | 2            | meraca              | 2               |
| singvla         | 2            | singvlvs            | 2               |
| apvlvs          | 2            | apvla               | 2               |
| cavtvs          | 2            | caveo               | 2               |
| insido          | 2            | insideo             | 2               |
| trinacria       | 2            | trinacrivs          | 2               |
| nessvs          | 2            | nessivs             | 1               |
|                 |              | nessis              | 1               |
| iecvr           | 2            | iecvs               | 2               |
| solvo           | 2            | solvtvs             | 2               |
| macro           | 2            | macer               | 2               |
| saeptvm         | 2            | saepio              | 2               |
| gypso           | 2            | gypsatvs            | 2               |
| ea              | 2            | is                  | 2               |
| arcas           | 2            | arcades             | 2               |
| paveo           | 2            | pasco               | 2               |
| ceveo           | 2            | cevo                | 2               |
| gravo           | 2            | gravor              | 2               |
| troivs          | 2            | troia               | 2               |
| hesperivs       | 2            | hesperia            | 2               |
| irascor         | 2            | iratvs              | 2               |
| mortvvs         | 2            | morior              | 2               |
| flvctvo         | 2            | flvctvor            | 2               |
| defessvs        | 2            | defetiscor          | 2               |
| optatvm         | 2            | optatvs             | 2               |
| laeva           | 2            | laevvs              | 2               |
| vertico         | 2            | verticon            | 1               |
|                 |              | verticvs            | 1               |
| regivs          | 2            | regia               | 2               |
| consvo          | 2            | consvto             | 1               |
|                 |              | consvesco           | 1               |
| conor           | 2            | cono                | 1               |
|                 |              | conatvs             | 1               |
| senior          | 2            | senex               | 2               |
| danavs          | 2            | danai               | 2               |
| tv              | 2            | tvvs                | 2               |
| cito            | 2            | cite                | 1               |
|                 |              | citatvs             | 1               |
| properans       | 2            | propero             | 2               |
| modo            | 2            | modvs               | 2               |
| brvttivs        | 2            | brvttia             | 2               |
| qvinqve         | 2            | viginti             | 2               |
| nimivs          | 2            | nimivm              | 2               |
| interiacio      | 2            | intericio           | 2               |
| rvbrica         | 2            | rvbricvs            | 2               |
| annvvm          | 2            | annvvs              | 2               |
| laxvs           | 2            | laxe                | 2               |
| divvm           | 2            | divvs               | 2               |
| sollicitvs      | 2            | sollicito           | 1               |
|                 |              | sollicite           | 1               |
| nvmqvid         | 2            | nvmqvis             | 2               |
| totvm           | 2            | totvs               | 2               |
| vigilans        | 2            | vigilo              | 2               |
| seqvor          | 2            | seqvens             | 2               |
| ratvs           | 2            | ratis               | 1               |
|                 |              | reor                | 1               |
| malo            | 2            | malvm               | 2               |
| troianvs        | 2            | troiani             | 2               |
| pario           | 2            | pars                | 1               |
|                 |              | partvs              | 1               |
| edo             | 2            | svm                 | 2               |
| comissatio      | 2            | commissatio         | 2               |
| ab              | 2            | ah                  | 2               |
| incertvs        | 2            | incertvm            | 2               |
| scio            | 2            | scisco              | 1               |
|                 |              | sciens              | 1               |
| vnvm            | 2            | vnvs                | 2               |
| gortynivs       | 2            | cortynivs           | 2               |
| vehemens        | 2            | vehementer          | 2               |
| ferio           | 2            | fervs               | 2               |
| compositvs      | 2            | compono             | 2               |
| tvrbatvs        | 2            | tvrbo               | 2               |
| propono         | 2            | propositvm          | 2               |
| sardes          | 2            | sardi               | 2               |
| romani          | 2            | romanvs             | 2               |
| sibylla         | 2            | sibvlla             | 2               |
| oppono          | 2            | oppositvs           | 2               |
| coeptvm         | 2            | coepio              | 2               |
| svperflvo       | 2            | svperflvens         | 2               |
| lvpinvm         | 2            | lvpinvs             | 2               |
| licymnia        | 2            | licymnivs           | 2               |
| abiectvs        | 2            | abicio              | 2               |
| nvmqvis         | 2            | nvmqvid             | 2               |
| extentvs        | 2            | extendo             | 2               |
| desertvm        | 2            | desero              | 1               |
|                 |              | deserta             | 1               |
| meto            | 2            | metor               | 1               |
|                 |              | metior              | 1               |
| hylas           | 2            | hyla                | 2               |
| consvltvm       | 2            | consvlto            | 1               |
|                 |              | consvlo             | 1               |
| derelinqvo      | 2            | derelicio           | 1               |
|                 |              | derelictvs          | 1               |
| coqvo           | 2            | coco                | 2               |
| qvinqvaginta    | 2            | qvinqve             | 1               |
|                 |              | dvcenti             | 1               |
| percvnctor      | 2            | percontor           | 2               |
| vis             | 2            | vir                 | 2               |
| qvisnam         | 2            | qvis                | 2               |
| poeas           | 2            | poeans              | 2               |
| proiectvs       | 2            | proicio             | 2               |
| pecto           | 2            | pectvs              | 1               |
|                 |              | pecta               | 1               |
| svcinvm         | 2            | svcinvs             | 2               |
| vomo            | 2            | vomens              | 1               |
|                 |              | vomer               | 1               |
| liberi          | 2            | liber               | 2               |
| aversvs         | 2            | averto              | 2               |
| cadvcvm         | 2            | cadvcvs             | 2               |
| secretvm        | 2            | secretvs            | 2               |
| donvm           | 2            | dono                | 2               |
| svesco          | 2            | svetvs              | 2               |
| prospera        | 2            | prosper             | 2               |
| stilbon         | 2            | stilbo              | 2               |
| sexcenti        | 2            | sescenti            | 2               |
| rapax           | 2            | rapaces             | 1               |
|                 |              | rapaci              | 1               |
| efficio         | 2            | effectvs            | 2               |
| motvs           | 2            | moveo               | 2               |
| sabinvs         | 2            | sabini              | 2               |
| lavrevs         | 2            | lavrea              | 2               |
| deditvs         | 2            | dedo                | 2               |
| volvo           | 2            | volo                | 2               |
| pressvs         | 2            | premo               | 2               |
| vvlgvs          | 2            | vvlgo               | 2               |
| moror           | 2            | moratvs             | 1               |
|                 |              | morior              | 1               |
| pascor          | 2            | pasco               | 2               |
| falsvs          | 2            | falsvm              | 2               |
| vt              | 2            | vtor                | 2               |
| vlpicvm         | 2            | vlpicvs             | 2               |
| aveo            | 2            | haveo               | 2               |
| commvne         | 2            | commvnis            | 2               |
| praesens        | 2            | praesentia          | 1               |
|                 |              | praesvm             | 1               |
| vittatvs        | 2            | vitto               | 2               |
| revereor        | 2            | reverendvs          | 2               |
| scelerati       | 2            | sceleratvs          | 2               |
| affectvs        | 2            | afficio             | 2               |
| vaccvs          | 2            | vaccivs             | 2               |
| vter            | 2            | vtrvm               | 2               |
| albvm           | 2            | albvs               | 2               |
| terni           | 2            | ternvs              | 2               |
| loqvo           | 2            | loqvor              | 2               |
| pecco           | 2            | peccans             | 1               |
|                 |              | peccatvm            | 1               |
| os              | 2            | ora                 | 2               |
| colo            | 2            | cvltvs              | 1               |
|                 |              | colvs               | 1               |
| pavimentatvs    | 1            | pavimento           | 1               |
| gangaba         | 1            | gango               | 1               |
| alpis           | 1            | alpe                | 1               |
| positvs         | 1            | pono                | 1               |
| accommodo       | 1            | accomodvs           | 1               |
| nardvm          | 1            | nardvs              | 1               |
| perdecorvs      | 1            | perdecvs            | 1               |
| femen           | 1            | femina              | 1               |
| nescioqvid      | 1            | nescioqvis          | 1               |
| effvnsvs        | 1            | effvsvs             | 1               |
| phalanx         | 1            | phalangvs           | 1               |
| samnis          | 1            | samni               | 1               |
| sorbvm          | 1            | sorba               | 1               |
| psecas          | 1            | pseca               | 1               |
| decvrsvs        | 1            | decvrro             | 1               |
| balaena         | 1            | ballaena            | 1               |
| antivm          | 1            | antivs              | 1               |
| bavli           | 1            | bavlvs              | 1               |
| exsecratvs      | 1            | exsecror            | 1               |
| adolescens      | 1            | adolesco            | 1               |
| moeris          | 1            | moeri               | 1               |
| cadmeivs        | 1            | cadmevs             | 1               |
| postvlo         | 1            | postvlatvm          | 1               |
| phrvgia         | 1            | phrygia             | 1               |
| hvccine         | 1            | ne                  | 1               |
| detrvdo         | 1            | detrvro             | 1               |
| enchytvm        | 1            | encytvs             | 1               |
| coloro          | 1            | coloratvs           | 1               |
| circvmmvgio     | 1            | mvgio               | 1               |
| vvlgo           | 1            | vvlgvs              | 1               |
| sardanapallvs   | 1            | sardanapalvs        | 1               |
| immensvm        | 1            | immensvs            | 1               |
| coagvlvm        | 1            | coagvla             | 1               |
| obrigesco       | 1            | obrigo              | 1               |
| calefacio       | 1            | calefo              | 1               |
| felicio         | 1            | felicivs            | 1               |
| sigillaria      | 1            | sigillarivm         | 1               |
| sicco           | 1            | siccvs              | 1               |
| ample           | 1            | amplvs              | 1               |
| scato           | 1            | scaton              | 1               |
| svspectvs       | 1            | svspicio            | 1               |
| inexercitatvs   | 1            | inexercito          | 1               |
| bactrianvs      | 1            | bactriani           | 1               |
| bilibris        | 1            | biliber             | 1               |
| liqveo          | 1            | linqvo              | 1               |
| ictvs           | 1            | ico                 | 1               |
| dehavrio        | 1            | deorior             | 1               |
| indeprehensvs   | 1            | indeprehio          | 1               |
| plancvs         | 1            | plancivs            | 1               |
| prior           | 1            | priores             | 1               |
| popanvm         | 1            | popanvs             | 1               |
| temvlentvs      | 1            | temvlentvm          | 1               |
| antiqvarivs     | 1            | antiqvativs         | 1               |
| tvscvlanvs      | 1            | tvscvlanvm          | 1               |
| antias          | 1            | antiates            | 1               |
| planvm          | 1            | planvs              | 1               |
| factvs          | 1            | facio               | 1               |
| inflo           | 1            | inflatvs            | 1               |
| geryon          | 1            | geryones            | 1               |
| tityvs          | 1            | tityon              | 1               |
| armati          | 1            | armatvs             | 1               |
| mitto           | 1            | miser               | 1               |
| exanimis        | 1            | exanimvs            | 1               |
| amara           | 1            | amarvs              | 1               |
| perfectvs       | 1            | perficio            | 1               |
| nvbilvs         | 1            | nvbilvm             | 1               |
| lanvvivm        | 1            | lanvvivs            | 1               |
| feneror         | 1            | fenero              | 1               |
| homo            | 1            | homor               | 1               |
| garrvlvs        | 1            | garrvla             | 1               |
| penna           | 1            | pinna               | 1               |
| plias           | 1            | pleias              | 1               |
| intervias       | 1            | interviae           | 1               |
| profestvs       | 1            | profesto            | 1               |
| academici       | 1            | academica           | 1               |
| incomitio       | 1            | incomities          | 1               |
| afri            | 1            | afer                | 1               |
| victor          | 1            | vinco               | 1               |
| calydonivs      | 1            | calydonia           | 1               |
| cvminvm         | 1            | cvminvs             | 1               |
| chiragra        | 1            | cheragra            | 1               |
| scvlponeae      | 1            | scvlponia           | 1               |
| constitvtvs     | 1            | constitvo           | 1               |
| removeo         | 1            | remotvs             | 1               |
| vsvfacio        | 1            | vsvficio            | 1               |
| apivm           | 1            | apis                | 1               |
| certvs          | 1            | certvm              | 1               |
| abrvptvm        | 1            | abrvmpo             | 1               |
| longinqvvs      | 1            | longinqvvm          | 1               |
| parthvs         | 1            | parthi              | 1               |
| pica            | 1            | picvs               | 1               |
| clodia          | 1            | clodivs             | 1               |
| dedecet         | 1            | dedecesco           | 1               |
| progne          | 1            | procnes             | 1               |
| poetris         | 1            | poetridvs           | 1               |
| pegasevs        | 1            | pegaseivs           | 1               |
| consessvs       | 1            | consido             | 1               |
| eripio          | 1            | ereptvm             | 1               |
| tvscvlvm        | 1            | tvscvlvs            | 1               |
| florevs         | 1            | florea              | 1               |
| camera          | 1            | camarvs             | 1               |
| hercvlivs       | 1            | hercvlevs           | 1               |
| stymphalidae    | 1            | stymphalis          | 1               |
| emax            | 1            | emacio              | 1               |
| adversvm        | 1            | adversvs            | 1               |
| pavlina         | 1            | pavlinvs            | 1               |
| argvtia         | 1            | argvtivm            | 1               |
| mavors          | 1            | mars                | 1               |
| opvlentia       | 1            | opvlentivm          | 1               |
| tressis         | 1            | tredo               | 1               |
| agaso           | 1            | agasvm              | 1               |
| praetorivs      | 1            | praetorivm          | 1               |
| vervtvm         | 1            | vervo               | 1               |
| laestrygones    | 1            | laestrygon          | 1               |
| sebvm           | 1            | svi                 | 1               |
| dissolvtvs      | 1            | dissolvo            | 1               |
| svblimiter      | 1            | svblime             | 1               |
| nonae           | 1            | nonvs               | 1               |
| specio          | 1            | spicio              | 1               |
| balitans        | 1            | balito              | 1               |
| occvpo          | 1            | occvpatvs           | 1               |
| poeantivs       | 1            | poeantevs           | 1               |
| infectvs        | 1            | inficio             | 1               |
| honoro          | 1            | honoratvs           | 1               |
| repecto         | 1            | repexo              | 1               |
| impensa         | 1            | impensvm            | 1               |
| castalivs       | 1            | castalia            | 1               |
| irrito          | 1            | irritvs             | 1               |
| horreo          | 1            | horrens             | 1               |
| aliqvo          | 1            | aliqvis             | 1               |
| difficile       | 1            | difficilis          | 1               |
| distero         | 1            | disterno            | 1               |
| tener           | 1            | tenere              | 1               |
| dis             | 1            | dives               | 1               |
| prope           | 1            | propior             | 1               |
| hadrianvs       | 1            | hadrianvm           | 1               |
| depsticivs      | 1            | depsticivm          | 1               |
| praetereo       | 1            | praeteritvs         | 1               |
| nvmisivs        | 1            | nvmisii             | 1               |
| indemno         | 1            | indemnatvs          | 1               |
| qvintivs        | 1            | qvintvs             | 1               |
| cornvtvs        | 1            | cornvte             | 1               |
| fvngvs          | 1            | fvngor              | 1               |
| verto           | 1            | versvs              | 1               |
| phileros        | 1            | phileron            | 1               |
| baltevm         | 1            | baltea              | 1               |
| raster          | 1            | rastrvm             | 1               |
| seria           | 1            | serivs              | 1               |
| domina          | 1            | dominvs             | 1               |
| lyde            | 1            | lydes               | 1               |
| patria          | 1            | patrivs             | 1               |
| postqvam        | 1            | qvi                 | 1               |
| certo           | 1            | certvs              | 1               |
| incontinentia   | 1            | incontinens         | 1               |
| sacratvs        | 1            | sacro               | 1               |
| tisiphone       | 1            | tisiphones          | 1               |
| sitis           | 1            | svm                 | 1               |
| carthaginienses | 1            | carthaginiensis     | 1               |
| opvlens         | 1            | opvlentvs           | 1               |
| barba           | 1            | barbas              | 1               |
| commvnio        | 1            | commvnivm           | 1               |
| cometes         | 1            | cometen             | 1               |
| exercitvs       | 1            | exerceo             | 1               |
| parentes        | 1            | parens              | 1               |
| spernendvs      | 1            | sperno              | 1               |
| inaeqvatvs      | 1            | inaeqvo             | 1               |
| fictvm          | 1            | fictvs              | 1               |
| dvctvs          | 1            | dvco                | 1               |
| sestertivm      | 1            | hic                 | 1               |
| dvcenti         | 1            | dvo                 | 1               |
| caesarea        | 1            | caesarevs           | 1               |
| amens           | 1            | amo                 | 1               |
| tenere          | 1            | teneo               | 1               |
| destinatvs      | 1            | destino             | 1               |
| exterritvs      | 1            | exterreo            | 1               |
| ocvlissimvs     | 1            | ocvlis              | 1               |
| caecvbvm        | 1            | caecvba             | 1               |
| raptvs          | 1            | rapio               | 1               |
| elysivm         | 1            | elysivs             | 1               |
| odoro           | 1            | odoratvs            | 1               |
| nardvs          | 1            | nardvm              | 1               |
| iactans         | 1            | iacto               | 1               |
| qvadragies      | 1            | qvadragiens         | 1               |
| macedonicvs     | 1            | macedonica          | 1               |
| posco           | 1            | poposco             | 1               |
| horrendvm       | 1            | horrendvs           | 1               |
| implecto        | 1            | implector           | 1               |
| ivrgivm         | 1            | ivrgo               | 1               |
| coriolanvs      | 1            | coriolanvm          | 1               |
| severe          | 1            | severvs             | 1               |
| allex           | 1            | hallex              | 1               |
| memorandvs      | 1            | memoro              | 1               |
| arretivm        | 1            | arretvs             | 1               |
| pharivs         | 1            | pharii              | 1               |
| sardonyx        | 1            | sardonyches         | 1               |
| hedymeles       | 1            | hedymele            | 1               |
| optempero       | 1            | obtempero           | 1               |
| adhaeresco      | 1            | adhaereo            | 1               |
| praevenio       | 1            | venio               | 1               |
| obsedeo         | 1            | obsideo             | 1               |
| satis           | 1            | sero                | 1               |
| troilvs         | 1            | troilon             | 1               |
| lepos           | 1            | lepvs               | 1               |
| stomachor       | 1            | stomacho            | 1               |
| blandior        | 1            | blanditvs           | 1               |
| xerxes          | 1            | xerses              | 1               |
| attondeo        | 1            | attonsvs            | 1               |
| icarivs         | 1            | icarivm             | 1               |
| prvna           | 1            | prvnvm              | 1               |
| verna           | 1            | vernvs              | 1               |
| gallicvs        | 1            | gallici             | 1               |
| tvrbo           | 1            | tvrbatvs            | 1               |
| petosiris       | 1            | petosirivs          | 1               |
| qvoqvo          | 1            | qvisqvis            | 1               |
| amentvm         | 1            | ammentvm            | 1               |
| pvblicvs        | 1            | pvblicvm            | 1               |
| rego            | 1            | rex                 | 1               |
| circe           | 1            | circes              | 1               |
| porrvs          | 1            | porrvm              | 1               |
| avellana        | 1            | avellanvs           | 1               |
| issos           | 1            | issvs               | 1               |
| odiose          | 1            | odiosvs             | 1               |
| perses          | 1            | persivs             | 1               |
| pvllatvs        | 1            | pvllo               | 1               |
| tracto          | 1            | tractatvs           | 1               |
| privo           | 1            | privatvs            | 1               |
| tvte            | 1            | tv                  | 1               |
| occvltvm        | 1            | occvltvs            | 1               |
| motivncvla      | 1            | motivncvlvs         | 1               |
| sedeo           | 1            | sedes               | 1               |
| thrax           | 1            | thraex              | 1               |
| dedecoro        | 1            | dedecorans          | 1               |
| avgvstiani      | 1            | avgvstianvs         | 1               |
| infimvm         | 1            | infervs             | 1               |
| faenvs          | 1            | fenvs               | 1               |
| profectvs       | 1            | proficiscor         | 1               |
| admodvm         | 1            | admodvs             | 1               |
| trivmpho        | 1            | trivmphvs           | 1               |
| nais            | 1            | naiades             | 1               |
| morvm           | 1            | mos                 | 1               |
| tantvmdem       | 1            | tantvs              | 1               |
| pergamvs        | 1            | pergamvm            | 1               |
| mvto            | 1            | mvtvs               | 1               |
| polites         | 1            | politvs             | 1               |
| avgeo           | 1            | avctvra             | 1               |
| itali           | 1            | italvs              | 1               |
| svblime         | 1            | svblimiter          | 1               |
| genivs          | 1            | genio               | 1               |
| derigo          | 1            | directvs            | 1               |
| obsonor         | 1            | obsono              | 1               |
| emereo          | 1            | emereor             | 1               |
| accessvs        | 1            | accedo              | 1               |
| falsimonia      | 1            | falsimonivm         | 1               |
| indolentia      | 1            | indolens            | 1               |
| anathymiasis    | 1            | anathymiasa         | 1               |
| vtroqve         | 1            | vterqve             | 1               |
| rvtilans        | 1            | rvtilo              | 1               |
| exardeo         | 1            | exardesco           | 1               |
| areopagvs       | 1            | areospages          | 1               |
| censeo          | 1            | censen              | 1               |
| militariter     | 1            | millitariter        | 1               |
| afflvens        | 1            | afflventia          | 1               |
| velociter       | 1            | velox               | 1               |
| cotylo          | 1            | cotylvs             | 1               |
| impero          | 1            | imperatvs           | 1               |
| prvdenter       | 1            | prvdens             | 1               |
| solvtvs         | 1            | solvo               | 1               |
| afflvo          | 1            | afflvens            | 1               |
| externvs        | 1            | externvm            | 1               |
| heliconides     | 1            | heliconidae         | 1               |
| comparo         | 1            | compareo            | 1               |
| misenvs         | 1            | misenvm             | 1               |
| xanthias        | 1            | xanthivs            | 1               |
| serva           | 1            | servo               | 1               |
| graecvli        | 1            | graecvlvs           | 1               |
| effvsvs         | 1            | effvndo             | 1               |
| clipeatvs       | 1            | clapeo              | 1               |
| barine          | 1            | barinvs             | 1               |
| avdaciter       | 1            | avdax               | 1               |
| beo             | 1            | bearvs              | 1               |
| falernvm        | 1            | falernvs            | 1               |
| dromo           | 1            | dromvs              | 1               |
| desqvamo        | 1            | desqvo              | 1               |
| machaerio       | 1            | machaerivs          | 1               |
| mvraena         | 1            | mvrena              | 1               |
| meroe           | 1            | mero                | 1               |
| mensa           | 1            | mensis              | 1               |
| nomencvlator    | 1            | nomenclator         | 1               |
| niteo           | 1            | nitor               | 1               |
| pactvm          | 1            | paciscor            | 1               |
| clades          | 1            | cladvs              | 1               |
| beneficivm      | 1            | beneficvs           | 1               |
| svbito          | 1            | svbitvs             | 1               |
| falernvs        | 1            | falerni             | 1               |
| defector        | 1            | defectvs            | 1               |
| ptolomaevs      | 1            | ptolemaevs          | 1               |
| postvmivs       | 1            | postvmia            | 1               |
| praemvnio       | 1            | praemvnitvs         | 1               |
| exsecror        | 1            | exsecrantia         | 1               |
| fax             | 1            | facio               | 1               |
| pro             | 1            | prosvm              | 1               |
| seivnctim       | 1            | seivnctvm           | 1               |
| extollo         | 1            | effero              | 1               |
| phraates        | 1            | prahates            | 1               |
| irretortvs      | 1            | irretor             | 1               |
| argos           | 1            | argi                | 1               |
| praeceps        | 1            | praecipio           | 1               |
| pavxillvm       | 1            | pavxillvs           | 1               |
| insane          | 1            | insanvs             | 1               |
| navigans        | 1            | navigo              | 1               |
| ivdico          | 1            | ivdex               | 1               |
| spinther        | 1            | spintheri           | 1               |
| illvceo         | 1            | illvcesco           | 1               |
| avdens          | 1            | avdentia            | 1               |
| catellvs        | 1            | catellvm            | 1               |
| expedio         | 1            | expeditvs           | 1               |
| rvfio           | 1            | rvfivs              | 1               |
| interdiv        | 1            | interdivs           | 1               |
| laridvm         | 1            | lardvm              | 1               |
| avdio           | 1            | avditvs             | 1               |
| fvriose         | 1            | fvriosvs            | 1               |
| soccatvs        | 1            | socco               | 1               |
| epigrvs         | 1            | epiger              | 1               |
| cydas           | 1            | cyda                | 1               |
| consvlo         | 1            | consvltvm           | 1               |
| fido            | 1            | fidens              | 1               |
| svpervacvvs     | 1            | svpervacvvm         | 1               |
| sancte          | 1            | sanctvs             | 1               |
| eneco           | 1            | enectvs             | 1               |
| avtvmo          | 1            | avtvma              | 1               |
| oleaster        | 1            | oleastrvm           | 1               |
| nocens          | 1            | noceo               | 1               |
| mvtitio         | 1            | mvttitio            | 1               |
| fabrico         | 1            | fabricor            | 1               |
| tectvm          | 1            | tego                | 1               |
| eadem           | 1            | idem                | 1               |
| dirvm           | 1            | dirvs               | 1               |
| segrego         | 1            | segregvs            | 1               |
| aeacvs          | 1            | aeaci               | 1               |
| cretes          | 1            | cretae              | 1               |
| qvivis          | 1            | qvis                | 1               |
| magis           | 1            | magnvs              | 1               |
| dvodenvs        | 1            | dvodenvm            | 1               |
| pvsvla          | 1            | pvssvlvs            | 1               |
| rescisco        | 1            | rescio              | 1               |
| sesama          | 1            | sesimvs             | 1               |
| mereo           | 1            | mereor              | 1               |
| hvmilis         | 1            | hvmiliter           | 1               |
| menenivs        | 1            | menenii             | 1               |
| profano         | 1            | profanvs            | 1               |
| ammon           | 1            | hammon              | 1               |
| parvvm          | 1            | parvvs              | 1               |
| difflvo         | 1            | difflvens           | 1               |
| philomelivm     | 1            | philomelivs         | 1               |
| octo            | 1            | octavvs             | 1               |
| distaedet       | 1            | distaedeo           | 1               |
| apoecides       | 1            | apoecidivs          | 1               |
| datvm           | 1            | dator               | 1               |
| sabaevs         | 1            | sabaei              | 1               |
| caveo           | 1            | cavtvs              | 1               |
| svccenseo       | 1            | svscensvm           | 1               |
| improvisvs      | 1            | improvisvm          | 1               |
| propediem       | 1            | propedies           | 1               |
| lvdvs           | 1            | lvdo                | 1               |
| arqvatvs        | 1            | arcvo               | 1               |
| planvs          | 1            | planvm              | 1               |
| iaceo           | 1            | iacio               | 1               |
| nigro           | 1            | nigrans             | 1               |
| egens           | 1            | egeo                | 1               |
| fallo           | 1            | falsvs              | 1               |
| pvlso           | 1            | pello               | 1               |
| navigo          | 1            | navigans            | 1               |
| trepido         | 1            | trepidvs            | 1               |
| carpentvm       | 1            | carpo               | 1               |
| noctv           | 1            | nox                 | 1               |
| confvndo        | 1            | confvsvs            | 1               |
| philetaevs      | 1            | philitevs           | 1               |
| diploma         | 1            | diplomo             | 1               |
| prosper         | 1            | prospera            | 1               |
| freni           | 1            | frenvm              | 1               |
| patior          | 1            | passvm              | 1               |
| perivrvs        | 1            | penivrvs            | 1               |
| versvs          | 1            | verto               | 1               |
| lvsvs           | 1            | lvdo                | 1               |
| oeneis          | 1            | oenevs              | 1               |
| hei             | 1            | ei                  | 1               |
| cevs            | 1            | cea                 | 1               |
| lvgeo           | 1            | lvceo               | 1               |
| animosvs        | 1            | animose             | 1               |
| progressvs      | 1            | progredior          | 1               |
| amylvm          | 1            | amvlvs              | 1               |
| exvrgeo         | 1            | exsvrgo             | 1               |
| accvratvs       | 1            | accvro              | 1               |
| obses           | 1            | obsideo             | 1               |
| pellis          | 1            | pello               | 1               |
| praepostervs    | 1            | praeposterivs       | 1               |
| postervs        | 1            | posterivs           | 1               |
| tartarvs        | 1            | tartara             | 1               |
| exerceo         | 1            | exercitvs           | 1               |
| eloqvor         | 1            | elocor              | 1               |
| sphaerita       | 1            | spaerita            | 1               |
| sphaera         | 1            | spaera              | 1               |
| qvisqvam        | 1            | qvoqvam             | 1               |
| fetvra          | 1            | fetvrvs             | 1               |
| qvisqvis        | 1            | qvisqvam            | 1               |
| vindico         | 1            | vindex              | 1               |
| concha          | 1            | concvs              | 1               |
| cavea           | 1            | caveo               | 1               |
| nastvrtivm      | 1            | nastvrcivs          | 1               |
| abrotonvm       | 1            | abrotonvs           | 1               |
| selectvs        | 1            | seligo              | 1               |
| cviatis         | 1            | qvoiatvs            | 1               |
| cvpiens         | 1            | cvpio               | 1               |
| pax             | 1            | pacis               | 1               |
| colvmbvlvs      | 1            | colvmbvla           | 1               |
| conatvs         | 1            | conor               | 1               |
| sinistra        | 1            | sinister            | 1               |
| metrvm          | 1            | metro               | 1               |
| oppositvs       | 1            | oppono              | 1               |
| extrema         | 1            | extremvm            | 1               |
| massicvm        | 1            | massicvs            | 1               |
| instrvctvs      | 1            | instrvo             | 1               |
| exqviro         | 1            | exqvisitvs          | 1               |
| barbarvs        | 1            | barbare             | 1               |
| manifestvs      | 1            | manifesto           | 1               |
| admirandvs      | 1            | admiror             | 1               |
| triphallvs      | 1            | triphallon          | 1               |
| svrrentvm       | 1            | svrrentes           | 1               |
| praelego        | 1            | praeligo            | 1               |
| boreas          | 1            | borea               | 1               |
| dvlcis          | 1            | dvlce               | 1               |
| vagvs           | 1            | vagvm               | 1               |
| clavdianvs      | 1            | clavdiani           | 1               |
| damascvs        | 1            | damascivs           | 1               |
| gregarivs       | 1            | gregarivm           | 1               |
| vive            | 1            | vivo                | 1               |
| peracvtvs       | 1            | peracvo             | 1               |
| meritvm         | 1            | mereor              | 1               |
| fvtvri          | 1            | fvtvrvs             | 1               |
| aliqvantvs      | 1            | aliqvanto           | 1               |
| nota            | 1            | notvs               | 1               |
| pomvs           | 1            | pomvm               | 1               |
| tantvlvm        | 1            | tantvlvs            | 1               |
| accvro          | 1            | accvratvs           | 1               |
| ictericvs       | 1            | icterica            | 1               |
| bvbvla          | 1            | bvbvlvs             | 1               |
| cetvs           | 1            | cetvm               | 1               |
| verisimilitvdo  | 1            | verisimiditvdo      | 1               |
| thyrsis         | 1            | thyrsvs             | 1               |
| areo            | 1            | aro                 | 1               |
| tremebvndvs     | 1            | tremibvndvs         | 1               |
| feliciter       | 1            | felix               | 1               |
| qvestvs         | 1            | qveror              | 1               |
| tempestivo      | 1            | tempestivvs         | 1               |
| rvbens          | 1            | rvbeo               | 1               |
| epistates       | 1            | epistata            | 1               |
| albani          | 1            | albanvs             | 1               |
| testatvs        | 1            | testor              | 1               |
| fractvs         | 1            | frango              | 1               |
| elvmbis         | 1            | elvmbo              | 1               |
| aeqvimaelivm    | 1            | aeqvimaelivs        | 1               |
| echecratides    | 1            | echecratis          | 1               |
| diivngo         | 1            | diivnctvs           | 1               |
| leviter         | 1            | levis               | 1               |
| ferrvm          | 1            | fero                | 1               |
| ravola          | 1            | ravolvs             | 1               |
| evpolis         | 1            | evpolides           | 1               |
| praegrandis     | 1            | praegrandvs         | 1               |
| decoctior       | 1            | decocte             | 1               |
| extremvm        | 1            | exter               | 1               |
| intimvs         | 1            | interior            | 1               |
| conivnctvs      | 1            | conivngo            | 1               |
| istvc           | 1            | istic               | 1               |
| praesvm         | 1            | praesens            | 1               |
| phaeacvs        | 1            | phaeaces            | 1               |
| detexo          | 1            | detego              | 1               |
| servm           | 1            | sero                | 1               |
| obsto           | 1            | obsisto             | 1               |
| ariadna         | 1            | ariadne             | 1               |
| tanto           | 1            | tantvs              | 1               |
| cynthivs        | 1            | cynthia             | 1               |
| aeqvvs          | 1            | aeqvvm              | 1               |
| fonteivs        | 1            | fonteia             | 1               |
| clodivs         | 1            | clodia              | 1               |
| perditvs        | 1            | perdo               | 1               |
| aptvs           | 1            | apte                | 1               |
| spvmo           | 1            | spvmans             | 1               |
| stratvm         | 1            | sterno              | 1               |
| beto            | 1            | bito                | 1               |
| immorior        | 1            | immor               | 1               |
| lateranvs       | 1            | laterani            | 1               |
| cenacvlvm       | 1            | cenacvla            | 1               |
| navale          | 1            | navalis             | 1               |
| minax           | 1            | minacivm            | 1               |
| vir             | 1            | vis                 | 1               |
| habito          | 1            | habeo               | 1               |
| nomenclator     | 1            | nomenclatvs         | 1               |
| ollovico        | 1            | ollovicon           | 1               |
| casevm          | 1            | casevs              | 1               |
| arefacio        | 1            | arefio              | 1               |
| occvpatvs       | 1            | occvpo              | 1               |
| alexandrea      | 1            | alexandria          | 1               |
| consentiens     | 1            | consentio           | 1               |
| acrisivs        | 1            | acrisivm            | 1               |
| casvs           | 1            | casv                | 1               |
| controversia    | 1            | controvorsia        | 1               |
| transscribo     | 1            | transcribo          | 1               |
| inceste         | 1            | incestvs            | 1               |
| vincio          | 1            | vinco               | 1               |
| tanagraevs      | 1            | tanagrae            | 1               |
| minvs           | 1            | parvvs              | 1               |
| ivvo            | 1            | ivtvs               | 1               |
| nvgor           | 1            | nvgo                | 1               |
| propendeo       | 1            | propensvs           | 1               |
| licet           | 1            | licetvm             | 1               |
| iamiamqve       | 1            | iamiamvs            | 1               |
| vester          | 1            | vestri              | 1               |
| psephisma       | 1            | psephismas          | 1               |
| angor           | 1            | ango                | 1               |
| seqvanvs        | 1            | seqvani             | 1               |
| pachynvm        | 1            | pachynvs            | 1               |
| svbaeratvs      | 1            | svbaero             | 1               |
| arabicvs        | 1            | arabica             | 1               |
| arabs           | 1            | arabes              | 1               |
| frvticor        | 1            | frvtico             | 1               |
| flvens          | 1            | flvo                | 1               |
| cani            | 1            | canis               | 1               |
| figo            | 1            | fixvs               | 1               |
| pes             | 1            | pedes               | 1               |
| trecenti        | 1            | octoginta           | 1               |
| incestvm        | 1            | incestvs            | 1               |
| femvr           | 1            | femen               | 1               |
| flagrans        | 1            | flagro              | 1               |
| proficio        | 1            | proficiscor         | 1               |
| novem           | 1            | novis               | 1               |
| praepotentes    | 1            | praepotens          | 1               |
| masvrivs        | 1            | masvrvs             | 1               |
| bifariam        | 1            | bifarivs            | 1               |
| isto            | 1            | iste                | 1               |
| splen           | 1            | splena              | 1               |
| cachinno        | 1            | cachinnvs           | 1               |
| vsvs            | 1            | vtor                | 1               |
| mos             | 1            | morior              | 1               |
| cimmerii        | 1            | cimmerion           | 1               |
| candeo          | 1            | candens             | 1               |
| veto            | 1            | vetvvs              | 1               |
| inepte          | 1            | ineptvs             | 1               |
| stloppvs        | 1            | scloppvs            | 1               |
| nvmerosvs       | 1            | nvmerose            | 1               |
| inavdio         | 1            | indavdio            | 1               |
| mvnio           | 1            | mvnitvs             | 1               |
| teres           | 1            | tero                | 1               |
| isevm           | 1            | iseon               | 1               |
| complexvs       | 1            | complector          | 1               |
| aes             | 1            | aer                 | 1               |
| gero            | 1            | gestvs              | 1               |
| svbitvs         | 1            | svbitvm             | 1               |
| ordior          | 1            | ordvs               | 1               |
| tertio          | 1            | tertivs             | 1               |
| perrhaebvs      | 1            | perrhaebi           | 1               |
| alte            | 1            | altvs               | 1               |
| facilis         | 1            | facile              | 1               |
| vnocvlvs        | 1            | vnocvlvm            | 1               |
| amplvs          | 1            | ample               | 1               |
| centies         | 1            | centiens            | 1               |
| havstvs         | 1            | havrio              | 1               |
| seqvens         | 1            | seqvor              | 1               |
| stipendivm      | 1            | stipendvm           | 1               |
| chaos           | 1            | chao                | 1               |
| iarbas          | 1            | iarba               | 1               |
| vinvm           | 1            | vinipollens         | 1               |
| pollens         | 1            | vinipollens         | 1               |
| semisomnvs      | 1            | semisomna           | 1               |
| phaedrvs        | 1            | phaedrivs           | 1               |
| cvrivs          | 1            | cvrio               | 1               |
| rectvs          | 1            | recte               | 1               |
| anteverto       | 1            | antevor             | 1               |
| cornelia        | 1            | cornelivs           | 1               |
| vestitvs        | 1            | vestio              | 1               |
| valgivs         | 1            | valgvs              | 1               |
| qverqvetvm      | 1            | qverqvetvs          | 1               |
| garganvs        | 1            | gargani             | 1               |
| odi             | 1            | odvrvs              | 1               |
| bias            | 1            | biantes             | 1               |
| ivrisconsvltvs  | 1            | ivriconsvltvs       | 1               |
| averto          | 1            | aversvs             | 1               |
| libraria        | 1            | librarivm           | 1               |
| recipio         | 1            | receptvs            | 1               |
| moderor         | 1            | moderatvs           | 1               |
| incipio         | 1            | inceptvm            | 1               |
| porcinvm        | 1            | poricinvs           | 1               |
| desero          | 1            | desertvs            | 1               |
| natis           | 1            | natvs               | 1               |
| natalis         | 1            | natales             | 1               |
| laxe            | 1            | lax                 | 1               |
| sedvctvs        | 1            | sedvctvm            | 1               |
| inanis          | 1            | inane               | 1               |
| entellvs        | 1            | entellis            | 1               |
| sempiternvs     | 1            | sempiternvm         | 1               |
| matara          | 1            | matarvs             | 1               |
| texo            | 1            | tego                | 1               |
| semirefectvs    | 1            | semirefacio         | 1               |
| exoleti         | 1            | exolesco            | 1               |
| honorificvs     | 1            | honorifice          | 1               |
| longvs          | 1            | longe               | 1               |
| caepa           | 1            | caepes              | 1               |
| attono          | 1            | attonitvs           | 1               |
| lvcania         | 1            | lvcanivs            | 1               |
| palla           | 1            | pallae              | 1               |
| sempronia       | 1            | sempronivs          | 1               |
| serrana         | 1            | serranvs            | 1               |
| patavini        | 1            | patavinvs           | 1               |
| distendo        | 1            | distentvs           | 1               |
| desvesco        | 1            | desvetvs            | 1               |
| malobathron     | 1            | malobathrvm         | 1               |
| gabinivs        | 1            | gabinia             | 1               |
| finitimi        | 1            | finitimvs           | 1               |
| avditvm         | 1            | avdio               | 1               |
| pavpervs        | 1            | pavper              | 1               |
| capharis        | 1            | capherides          | 1               |
| pars            | 1            | pario               | 1               |
| casv            | 1            | casvs               | 1               |
| cornelivs       | 1            | corneliae           | 1               |
| sollemne        | 1            | sollemnis           | 1               |
| hyrcanvs        | 1            | hyrcani             | 1               |
| medvs           | 1            | medi                | 1               |
| instrvo         | 1            | instrvctvs          | 1               |
| obligatvs       | 1            | obligo              | 1               |
| ino             | 1            | inoi                | 1               |
| tribvo          | 1            | tribvtvm            | 1               |
| inqvinatvs      | 1            | inqvino             | 1               |
| calypso         | 1            | calypsvs            | 1               |
| phaeacia        | 1            | phaeacivs           | 1               |
| canvs           | 1            | canis               | 1               |
| peronatvs       | 1            | perono              | 1               |
| aones           | 1            | aonae               | 1               |
| casevs          | 1            | caseo               | 1               |
| pvlmentarivm    | 1            | pvlmentarivs        | 1               |
| parco           | 1            | parcio              | 1               |
| captivvs        | 1            | captiva             | 1               |
| simvl           | 1            | simvlac             | 1               |
| prytanis        | 1            | prytanvs            | 1               |
| thesavrvm       | 1            | thesavrvs           | 1               |
| promethevs      | 1            | promethea           | 1               |
| senex           | 1            | senior              | 1               |
| pellitvs        | 1            | pello               | 1               |
| regno           | 1            | regnatvs            | 1               |
| lacon           | 1            | laconis             | 1               |
| ministro        | 1            | minister            | 1               |
| ars             | 1            | artvs               | 1               |
| receptvs        | 1            | recipio             | 1               |
| fixvs           | 1            | figo                | 1               |
| sane            | 1            | sanvs               | 1               |
| edoni           | 1            | edonis              | 1               |
| recvpero        | 1            | recipio             | 1               |
| bvrdvbasta      | 1            | bvrdvbastvs         | 1               |
| perattente      | 1            | peratente           | 1               |
| cano            | 1            | canis               | 1               |
| saperda         | 1            | saperdvs            | 1               |
| castorevm       | 1            | castorevs           | 1               |
| antitheton      | 1            | antitheta           | 1               |
| eodem           | 1            | idem                | 1               |
| maena           | 1            | mena                | 1               |
| grates          | 1            | gratis              | 1               |
| svspicio        | 1            | svspectvs           | 1               |
| ivgervm         | 1            | ivgervs             | 1               |
| aliorsvm        | 1            | alioversvs          | 1               |
| bos             | 1            | bosvm               | 1               |
| hederacevs      | 1            | hederacia           | 1               |
| thimiamae       | 1            | thimiama            | 1               |
| inceptvm        | 1            | incipio             | 1               |
| panaetivs       | 1            | panaetivm           | 1               |
| impedio         | 1            | impeditvm           | 1               |
| ambigvvm        | 1            | ambigvvs            | 1               |
| directvs        | 1            | dirigo              | 1               |
| calide          | 1            | calidvs             | 1               |
| erratvm         | 1            | erro                | 1               |
| nata            | 1            | nascor              | 1               |
| cantharis       | 1            | cantharides         | 1               |
| qvies           | 1            | qvietvs             | 1               |
| macedo          | 1            | macedones           | 1               |
| oscitor         | 1            | oscito              | 1               |
| onomas          | 1            | onomantes           | 1               |
| frivolvs        | 1            | frivola             | 1               |
| dilvcesco       | 1            | dilvceo             | 1               |
| competitor      | 1            | competitvm          | 1               |
| servs           | 1            | sero                | 1               |
| calcar          | 1            | calco               | 1               |
| demissvs        | 1            | demitto             | 1               |
| piget           | 1            | pigeo               | 1               |
| doleo           | 1            | dolo                | 1               |
| fortvita        | 1            | fortvitvs           | 1               |
| copia           | 1            | copiaste            | 1               |
| comptvs         | 1            | como                | 1               |
| contemnendvs    | 1            | contemno            | 1               |
| mystes          | 1            | mysta               | 1               |
| sybilla         | 1            | sibylla             | 1               |
| tmarvs          | 1            | tmari               | 1               |
| nvmida          | 1            | nvmidae             | 1               |
| virvs           | 1            | vir                 | 1               |
| qvantillvs      | 1            | qvantillvm          | 1               |
| obirascor       | 1            | obirasco            | 1               |
| convenientia    | 1            | conveniens          | 1               |
| ah              | 1            | ab                  | 1               |
| torqvis         | 1            | torqveo             | 1               |
| considerate     | 1            | considero           | 1               |
| psevdophilippvs | 1            | psevdophilivs       | 1               |
| catina          | 1            | catinvs             | 1               |
| illavdatvs      | 1            | illavdo             | 1               |
| dispvdet        | 1            | dispvdo             | 1               |
| gnosis          | 1            | gnosvs              | 1               |
| vaccensis       | 1            | vagenses            | 1               |
| tonsvs          | 1            | tondeo              | 1               |
| moneo           | 1            | monitvs             | 1               |
| tvrbellae       | 1            | tvrbella            | 1               |
| desomnis        | 1            | desomno             | 1               |
| iactatvs        | 1            | iacto               | 1               |
| dissipo         | 1            | dissipio            | 1               |
| arcanvm         | 1            | arcanvs             | 1               |
| svbmano         | 1            | svmmano             | 1               |
| valetvdinarivm  | 1            | valitvdinarivs      | 1               |
| libere          | 1            | libet               | 1               |
| svbiectvs       | 1            | svbicio             | 1               |
| prodo           | 1            | prodeo              | 1               |
| aqvvla          | 1            | aqvola              | 1               |
| plantaris       | 1            | plantarivm          | 1               |
| ardens          | 1            | ardeo               | 1               |
| glans           | 1            | glanda              | 1               |
| qvadraginta     | 1            | dvcenti             | 1               |
| fenvm           | 1            | fenvs               | 1               |
| qvingenti       | 1            | octoginta           | 1               |
| ocinvm          | 1            | ocinvs              | 1               |
| ratis           | 1            | reor                | 1               |
| exhortor        | 1            | exortor             | 1               |
| lvcidvm         | 1            | lvcidvs             | 1               |
| vacvvm          | 1            | vacvvs              | 1               |
| apertvm         | 1            | apertvs             | 1               |
| therapontigonvs | 1            | therapontigonvgonvs | 1               |
| delvmbis        | 1            | delvmbo             | 1               |
| lvcvs           | 1            | lvx                 | 1               |
| convestio       | 1            | convesto            | 1               |
| tribvnicivs     | 1            | tribvnicvs          | 1               |
| consvltvs       | 1            | consvltvm           | 1               |
| primoris        | 1            | primores            | 1               |
| maeror          | 1            | moeror              | 1               |
| foliatvm        | 1            | folio               | 1               |
| alsiense        | 1            | alsiensis           | 1               |
| tarpezita       | 1            | trapezita           | 1               |
| passennvs       | 1            | passennivs          | 1               |
| pediseqvvs      | 1            | pediseqva           | 1               |
| intestinvm      | 1            | intestinvs          | 1               |
| perprimo        | 1            | perpremo            | 1               |
| grosphvs        | 1            | grospvs             | 1               |
| rescriptvm      | 1            | rescribo            | 1               |
| exigvvm         | 1            | exigvvs             | 1               |
| misenvm         | 1            | misenvs             | 1               |
| sisapo          | 1            | sisapon             | 1               |
| apenninvs       | 1            | apennini            | 1               |
| svfficio        | 1            | svfficiens          | 1               |
| vernvm          | 1            | vernvs              | 1               |
| modivm          | 1            | modivs              | 1               |
| thracia         | 1            | thracivs            | 1               |
| cvltvs          | 1            | colo                | 1               |
| oleo            | 1            | olens               | 1               |
| solo            | 1            | solor               | 1               |
| adico           | 1            | adicio              | 1               |
| minvtal         | 1            | minvtalis           | 1               |
| serpo           | 1            | serpens             | 1               |
| ivsta           | 1            | ivstvs              | 1               |
| principivm      | 1            | princeps            | 1               |
| cognosco        | 1            | cognitvs            | 1               |
| incelebratvs    | 1            | incelebro           | 1               |
| hiccine         | 1            | hic                 | 1               |
| aridvs          | 1            | ardvs               | 1               |
| pictvs          | 1            | pingo               | 1               |
| canis           | 1            | cano                | 1               |
| centesimvs      | 1            | centesima           | 1               |
| facetiae        | 1            | facetia             | 1               |
| ebibo           | 1            | ebibero             | 1               |
| aegaevm         | 1            | aegaevs             | 1               |
| thraca          | 1            | thrax               | 1               |
| medi            | 1            | medivs              | 1               |
| venalis         | 1            | nalis               | 1               |
| neqve           | 1            | nec                 | 1               |
| palpor          | 1            | palpo               | 1               |
| nvbilvm         | 1            | nvbila              | 1               |
| avxilior        | 1            | avxilio             | 1               |
| defetiscor      | 1            | defessvs            | 1               |
| verno           | 1            | vernvs              | 1               |
| cocles          | 1            | cocvlitvm           | 1               |
| prosapia        | 1            | prosapivm           | 1               |
| condo           | 1            | condio              | 1               |
| attatae         | 1            | attatvs             | 1               |
| nimio           | 1            | nimivs              | 1               |
| convenio        | 1            | conventvs           | 1               |
| vniversvm       | 1            | vniversvs           | 1               |
| cispivs         | 1            | cispivm             | 1               |
| opimivs         | 1            | opimvs              | 1               |
| repeto          | 1            | repetvndae          | 1               |
| biennivm        | 1            | biennvm             | 1               |
| commodvm        | 1            | commodvs            | 1               |
| incepto         | 1            | incipio             | 1               |
| recrvdesco      | 1            | recrvdo             | 1               |
| lativs          | 1            | lativm              | 1               |
| grande          | 1            | grandis             | 1               |
| ovvm            | 1            | ovis                | 1               |
| xerampelinvs    | 1            | xerampelina         | 1               |
| expio           | 1            | exspio              | 1               |
| veneriae        | 1            | venerivs            | 1               |
| oxathres        | 1            | oxathra             | 1               |
| depso           | 1            | depsvesco           | 1               |
| circvmtergeo    | 1            | circvmtergo         | 1               |
| campvs          | 1            | campis              | 1               |
| tomyris         | 1            | tamyris             | 1               |
| abvtor          | 1            | abvtvs              | 1               |
| divdico         | 1            | diivdico            | 1               |
| vettidivs       | 1            | vettis              | 1               |
| navcvm          | 1            | navcvs              | 1               |
| lacones         | 1            | lacon               | 1               |
| mvllvs          | 1            | mvllvm              | 1               |
| concedo         | 1            | concessvm           | 1               |
| iniqve          | 1            | iniqvvs             | 1               |
| prosvm          | 1            | prorsvm             | 1               |
| bvtes           | 1            | bvten               | 1               |
| bebrycivs       | 1            | bebrycia            | 1               |
| paphlagona      | 1            | paphlagonas         | 1               |
| sinopa          | 1            | sinopes             | 1               |
| cara            | 1            | carae               | 1               |
| cretanvs        | 1            | cretani             | 1               |
| syrvs           | 1            | syri                | 1               |
| rhodia          | 1            | rhodivs             | 1               |
| vnomammivs      | 1            | vnomammia           | 1               |
| conterebromnivs | 1            | conterebromnia      | 1               |
| molorchaevs     | 1            | molorchevs          | 1               |
| inavratvs       | 1            | inavro              | 1               |
| cerialis        | 1            | cerealis            | 1               |
| scortevs        | 1            | scortevm            | 1               |
| fascinvm        | 1            | fascinvs            | 1               |
| piper           | 1            | pipo                | 1               |
| cicaro          | 1            | cicarvs             | 1               |
| iacto           | 1            | iacio               | 1               |
| pyrgo           | 1            | pyrgvs              | 1               |
| presse          | 1            | pressvs             | 1               |
| sex             | 1            | viginti             | 1               |
| opertvm         | 1            | operio              | 1               |
| ilias           | 1            | iliades             | 1               |
| acerbvs         | 1            | acerbvm             | 1               |
| administro      | 1            | administra          | 1               |
| alo             | 1            | ala                 | 1               |
| abdo            | 1            | abditvs             | 1               |
| sallvstivs      | 1            | sallvstvs           | 1               |
| impvratvs       | 1            | impvro              | 1               |
| prolvo          | 1            | proleo              | 1               |
| nevtro          | 1            | nevter              | 1               |
| providens       | 1            | provideo            | 1               |
| rvscvm          | 1            | rvscvs              | 1               |
| rhombvs         | 1            | rhombos             | 1               |
| salvvs          | 1            | salvivs             | 1               |
| mysterivm       | 1            | mysterivs           | 1               |
| irritvm         | 1            | irritvs             | 1               |
| ivstvm          | 1            | ivstvs              | 1               |
| tvvm            | 1            | tvvs                | 1               |
| vergilivs       | 1            | vergilis            | 1               |
| ivnipervs       | 1            | ivniper             | 1               |
| foris           | 1            | forivm              | 1               |
| ivnctvs         | 1            | ivngo               | 1               |
| favstvs         | 1            | favsti              | 1               |
| salio           | 1            | sal                 | 1               |
| pingve          | 1            | pingvis             | 1               |
| plasma          | 1            | plasmas             | 1               |
| svspendo        | 1            | svspensvs           | 1               |
| achaevs         | 1            | achaei              | 1               |
| caecilivs       | 1            | caecilia            | 1               |
| didivs          | 1            | didia               | 1               |
| ivnivs          | 1            | ivnia               | 1               |
| servatvs        | 1            | servo               | 1               |
| exsto           | 1            | exsisto             | 1               |
| dinomache       | 1            | dinomaches          | 1               |
| svfflo          | 1            | svffla              | 1               |
| nave            | 1            | navis               | 1               |
| delector        | 1            | delecto             | 1               |
| propositvm      | 1            | propono             | 1               |
| andromache      | 1            | andromacha          | 1               |
| pinso           | 1            | pingo               | 1               |
| exopto          | 1            | exoptatvs           | 1               |
| gemmatvs        | 1            | gemmo               | 1               |
| setinvm         | 1            | setinvs             | 1               |
| dinosco         | 1            | dignosco            | 1               |
| disicio         | 1            | dissicio            | 1               |
| insigne         | 1            | insignis            | 1               |
| tonitrvvm       | 1            | tonitrvvs           | 1               |
| agito           | 1            | ago                 | 1               |
| sitvs           | 1            | sita                | 1               |
| decondo         | 1            | decondeo            | 1               |
| emaceratvs      | 1            | emacero             | 1               |
| plavdo          | 1            | plodo               | 1               |
| obaritvs        | 1            | obaritos            | 1               |
| comitor         | 1            | comitatvs           | 1               |
| refoveo         | 1            | refotvs             | 1               |
| acceptvs        | 1            | accipio             | 1               |
| ingratvs        | 1            | ingrate             | 1               |
| svgillo         | 1            | svggillo            | 1               |
| sepositvs       | 1            | sepono              | 1               |
| latens          | 1            | lateo               | 1               |
| sanctvs         | 1            | sancte              | 1               |
| patrivs         | 1            | patria              | 1               |
| vigens          | 1            | vigeo               | 1               |
| pvrgo           | 1            | pvrgatvs            | 1               |
| cvriosvs        | 1            | cvriose             | 1               |
| scitvm          | 1            | scio                | 1               |
| bassaris        | 1            | bassar              | 1               |
| flecto          | 1            | flexvra             | 1               |
| evhivs          | 1            | evhion              | 1               |
| philvs          | 1            | philivs             | 1               |
| tantvsdem       | 1            | tantvmdem           | 1               |
| amanicae        | 1            | amanicvs            | 1               |
| geminvs         | 1            | gemini              | 1               |
| nimivm          | 1            | nimivs              | 1               |
| circvmcisvs     | 1            | circvmcido          | 1               |
| controversiosvs | 1            | controversio        | 1               |
| confessvs       | 1            | confiteor           | 1               |
| beatvm          | 1            | beatvs              | 1               |
| vorenvs         | 1            | vorene              | 1               |
| vacca           | 1            | vaga                | 1               |
| spargo          | 1            | sparsvs             | 1               |
| orbvs           | 1            | orbis               | 1               |
| pannvcivs       | 1            | pannvcivm           | 1               |
| bavcis          | 1            | bavcvs              | 1               |
| ocimvm          | 1            | ocimvs              | 1               |
| olens           | 1            | oleo                | 1               |
| rvber           | 1            | rvbrvs              | 1               |
| litvs           | 1            | litor               | 1               |
| excelsitas      | 1            | excelsitvs          | 1               |
| excelsvs        | 1            | excelsvm            | 1               |
| impvre          | 1            | impvrvs             | 1               |
| tetre           | 1            | teter               | 1               |
| cardvelis       | 1            | cardeles            | 1               |
| ramale          | 1            | ramalis             | 1               |
| vegrandis       | 1            | vegro               | 1               |
| svber           | 1            | svbero              | 1               |
| decima          | 1            | decimvs             | 1               |
| sarisa          | 1            | sarissvs            | 1               |
| obiecto         | 1            | obicio              | 1               |
| individvvs      | 1            | individvvm          | 1               |
| marinvs         | 1            | marinvm             | 1               |
| fabaginvs       | 1            | fabago              | 1               |
| lvdicer         | 1            | lvdicrvm            | 1               |
| nasvm           | 1            | nasvs               | 1               |
| congrio         | 1            | congrion            | 1               |
| cantaber        | 1            | cantabrvs           | 1               |
| magvs           | 1            | magnvs              | 1               |
| placitvm        | 1            | placeo              | 1               |
| baccar          | 1            | bacco               | 1               |
| mintvrnae       | 1            | mintvrni            | 1               |
| solvm           | 1            | solvs               | 1               |
| sipho           | 1            | sipo                | 1               |
| avara           | 1            | avarvs              | 1               |
| resideo         | 1            | resido              | 1               |
| carsvlae        | 1            | carsvlas            | 1               |
| tres            | 1            | tribvs              | 1               |
| nvmqvisnam      | 1            | nvmqvidnam          | 1               |
| elegidion       | 1            | elegidivm           | 1               |
| cirrati         | 1            | cirrator            | 1               |
| illo            | 1            | ille                | 1               |
| infervs         | 1            | inferi              | 1               |
| rapacida        | 1            | rapacidvs           | 1               |
| contego         | 1            | contectvs           | 1               |
| rodevs          | 1            | rosevs              | 1               |
| devia           | 1            | devivs              | 1               |
| potior          | 1            | potis               | 1               |
| volvcer         | 1            | volvcris            | 1               |
| dvrvm           | 1            | dvrvs               | 1               |
| primigenivs     | 1            | primigenes          | 1               |
| svccessvs       | 1            | svccedo             | 1               |
| ementior        | 1            | emens               | 1               |
| ceres           | 1            | ceresis             | 1               |
| strobilvs       | 1            | strobilis           | 1               |
| temetvm         | 1            | temes               | 1               |
| obrvssa         | 1            | obrvssvs            | 1               |
| thebani         | 1            | thebanvs            | 1               |
| vinevs          | 1            | vinea               | 1               |
| statvo          | 1            | statva              | 1               |
| formianvm       | 1            | formianvs           | 1               |
| libethrides     | 1            | libethris           | 1               |
| privato         | 1            | privatvs            | 1               |
| defvnctvs       | 1            | defvngor            | 1               |
| allego          | 1            | alligo              | 1               |
| canorvs         | 1            | canor               | 1               |
| allvdo          | 1            | allvs               | 1               |
| maxilla         | 1            | maxillvm            | 1               |
| gavsapvm        | 1            | gavsapes            | 1               |
| catvs           | 1            | catvm               | 1               |
| praestino       | 1            | praestineo          | 1               |
| cremor          | 1            | cremo               | 1               |
| salii           | 1            | salivs              | 1               |
| palpvm          | 1            | palpos              | 1               |
| philippi        | 1            | philippvs           | 1               |
| plvrimvm        | 1            | mvltvs              | 1               |
| venafrvm        | 1            | venafer             | 1               |
| decretvm        | 1            | decerno             | 1               |
| cerva           | 1            | cervvs              | 1               |
| linea           | 1            | linevs              | 1               |
| tolerabilis     | 1            | tolerabiliter       | 1               |
| gavdivm         | 1            | gavdvs              | 1               |
| hesiona         | 1            | hesione             | 1               |
| sedochezi       | 1            | sedochezorvs        | 1               |
| pvto            | 1            | pvteo               | 1               |
| apto            | 1            | aptvs               | 1               |
| insanvs         | 1            | insane              | 1               |
| ibis            | 1            | ibi                 | 1               |
| tergeminvs      | 1            | trigeminvs          | 1               |
| allivm          | 1            | alivs               | 1               |
| rvta            | 1            | rvtvs               | 1               |
| decresco        | 1            | decerno             | 1               |
| parvm           | 1            | parvvs              | 1               |
| hiberi          | 1            | iberi               | 1               |
| obliviscor      | 1            | oblino              | 1               |
| ingemo          | 1            | ingemisco           | 1               |
| volsiniensis    | 1            | vvlsiniensis        | 1               |
| clavdivs        | 1            | clavdia             | 1               |
| remotvs         | 1            | removeo             | 1               |
| indvlgens       | 1            | indvlgeo            | 1               |
| honor           | 1            | honi                | 1               |
| atavvs          | 1            | atavi               | 1               |
| occento         | 1            | occens              | 1               |
| olla            | 1            | avla                | 1               |
| assido          | 1            | assideo             | 1               |
| svpplex         | 1            | svpplicivm          | 1               |
| svs             | 1            | svi                 | 1               |
| fanvm           | 1            | fanvs               | 1               |
| diaria          | 1            | diarivm             | 1               |
| leonidas        | 1            | leonida             | 1               |
| xystvs          | 1            | xystvm              | 1               |
| idalivs         | 1            | idalia              | 1               |
| serivm          | 1            | serivs              | 1               |
| abies           | 1            | abeo                | 1               |
| lycidas         | 1            | lycida              | 1               |
| agnosco         | 1            | agnitvs             | 1               |
| qvinta          | 1            | qvintvs             | 1               |
| gryps           | 1            | grypes              | 1               |
| ingressvs       | 1            | ingredior           | 1               |
| velinvs         | 1            | velina              | 1               |
| cvtis           | 1            | cvtvs               | 1               |
| praefringo      | 1            | praefrigo           | 1               |
| advltera        | 1            | advlter             | 1               |
| diversvs        | 1            | diverto             | 1               |
| conclvsvs       | 1            | conclvdo            | 1               |
| verona          | 1            | verones             | 1               |
| profligo        | 1            | profligatvs         | 1               |
| lvpvs           | 1            | lvpe                | 1               |
| noxia           | 1            | noxivs              | 1               |
| ervca           | 1            | ervco               | 1               |
| liceor          | 1            | liceo               | 1               |
| bellerophontevs | 1            | bellerophontes      | 1               |
| admoveo         | 1            | admoro              | 1               |
| pylivs          | 1            | pylia               | 1               |
| antigone        | 1            | antigones           | 1               |
| hypsipyle       | 1            | hypsipylas          | 1               |
| vocito          | 1            | vocitetvm           | 1               |
| potivncvla      | 1            | potivncvlvs         | 1               |
| ernevm          | 1            | ernevs              | 1               |
| confringo       | 1            | confrigo            | 1               |
| contamino       | 1            | contaminatvs        | 1               |
| perlego         | 1            | perlega             | 1               |
| forma           | 1            | formo               | 1               |
| destino         | 1            | destinatvm          | 1               |
| svperans        | 1            | svpero              | 1               |
| occipvt         | 1            | occipio             | 1               |
| posticvs        | 1            | postica             | 1               |
| arroganter      | 1            | arrogans            | 1               |
| ephemeris       | 1            | ephemeridae         | 1               |
| senvs           | 1            | senex               | 1               |
| partior         | 1            | partio              | 1               |
| vivo            | 1            | vinco               | 1               |
| danais          | 1            | danai               | 1               |
| vltimvm         | 1            | vltimvs             | 1               |
| rex             | 1            | rego                | 1               |
| svbripio        | 1            | svrripio            | 1               |
| antiqvaria      | 1            | antiqvarivs         | 1               |
| concio          | 1            | concieo             | 1               |
| tranqvillvm     | 1            | tranqvillvs         | 1               |
| eligo           | 1            | elego               | 1               |
| tarraciniensis  | 1            | tarracinienses      | 1               |
| tarentinvs      | 1            | tarentini           | 1               |
| lydivs          | 1            | lydia               | 1               |
| scamnvm         | 1            | scamnvs             | 1               |
| sileo           | 1            | silens              | 1               |
| apameni         | 1            | apamenorvs          | 1               |
| svbvrbanvm      | 1            | svbvrbanvs          | 1               |
| opto            | 1            | optatvs             | 1               |
| secvris         | 1            | secvrvs             | 1               |
| frvstro         | 1            | frvstror            | 1               |
| cassvs          | 1            | cassa               | 1               |
| novvs           | 1            | nosco               | 1               |
| dvrvs           | 1            | dvrvm               | 1               |
| sempiterno      | 1            | sempiternvm         | 1               |
| athamantis      | 1            | athamas             | 1               |
| oesypvm         | 1            | oesypa              | 1               |
| sicine          | 1            | ne                  | 1               |
| hera            | 1            | svm                 | 1               |
| amedines        | 1            | amedinvm            | 1               |
| pvblicvm        | 1            | pvblicvs            | 1               |
| cophinvs        | 1            | cophinvm            | 1               |
| ivdaevs         | 1            | ivdaea              | 1               |
| solymvs         | 1            | solymae             | 1               |
| hippias         | 1            | hippivs             | 1               |
| fvlcio          | 1            | fvlgeo              | 1               |
| fenebris        | 1            | feneber             | 1               |
| capharevs       | 1            | capherevs           | 1               |
| obtvsvs         | 1            | obtvndo             | 1               |
| concors         | 1            | concordia           | 1               |
| raptvm          | 1            | rapio               | 1               |
| qvatvordecim    | 1            | qvatvor             | 1               |
| dipsas          | 1            | dipsae              | 1               |
| svevvs          | 1            | svebi               | 1               |
| hirpinvs        | 1            | hirpine             | 1               |
| qvinctivs       | 1            | qvintivs            | 1               |
| translatvs      | 1            | tralatvs            | 1               |
| nitens          | 1            | nitor               | 1               |
| exercito        | 1            | exercitatvs         | 1               |
| vnvsetvicesimvs | 1            | vnietvicesimvs      | 1               |
| simias          | 1            | simia               | 1               |
| metior          | 1            | mensvs              | 1               |
| gaia            | 1            | gaivs               | 1               |
| vasa            | 1            | vas                 | 1               |
| frvstvm         | 1            | frvsta              | 1               |
| escvlentvs      | 1            | escvlo              | 1               |
| acer            | 1            | acriter             | 1               |
| origo           | 1            | origines            | 1               |
| evilesco        | 1            | evilio              | 1               |
| secvndvs        | 1            | secvndvm            | 1               |
| hac             | 1            | hic                 | 1               |
| secreto         | 1            | secretvm            | 1               |
| neo             | 1            | neto                | 1               |
| prandeo         | 1            | pransvs             | 1               |
| poto            | 1            | potivm              | 1               |
| oscitans        | 1            | oscito              | 1               |
| damnatvs        | 1            | damno               | 1               |
| peristasis      | 1            | peristasimo         | 1               |
| caelestis       | 1            | caelestia           | 1               |
| iole            | 1            | ioles               | 1               |
| mare            | 1            | marivs              | 1               |
| amygdalvm       | 1            | amygdalvs           | 1               |
| fvro            | 1            | fvrens              | 1               |
| genitalia       | 1            | genitalis           | 1               |
| sentio          | 1            | sentis              | 1               |
| amans           | 1            | amo                 | 1               |
| atii            | 1            | ativs               | 1               |
| dilectvs        | 1            | diligo              | 1               |
| cadvrcvm        | 1            | cadvrcvs            | 1               |
| pavca           | 1            | pavcvs              | 1               |
| indico          | 1            | indictvs            | 1               |
| alternvs        | 1            | alternis            | 1               |
| convador        | 1            | convado             | 1               |
| venerevs        | 1            | venerivs            | 1               |
| vibex           | 1            | vibic               | 1               |
| flagello        | 1            | flagella            | 1               |
| dirvmpo         | 1            | discvmpo            | 1               |
| phrygia         | 1            | phrygivs            | 1               |
| flagro          | 1            | flagrans            | 1               |
| accipio         | 1            | acceptvm            | 1               |
| sincipvt        | 1            | sinceps             | 1               |
| do              | 1            | dator               | 1               |
| intellectvs     | 1            | intelligo           | 1               |
| hervs           | 1            | svm                 | 1               |
| praetexta       | 1            | praetexo            | 1               |
| allobrogicvs    | 1            | allobrogici         | 1               |
| reprehensio     | 1            | repreheo            | 1               |
| svpplavdo       | 1            | svpplodo            | 1               |
| impollitvs      | 1            | impolitvs           | 1               |
| philetas        | 1            | philitas            | 1               |
| abito           | 1            | abeo                | 1               |
| appareo         | 1            | appar               | 1               |
| comitia         | 1            | comitivm            | 1               |
| moles           | 1            | molivm              | 1               |
| obiectvs        | 1            | obicio              | 1               |
| ille            | 1            | illo                | 1               |
| comperio        | 1            | compertvs           | 1               |
| oleitas         | 1            | oleita              | 1               |
| medipontvs      | 1            | melipontvs          | 1               |
| compono         | 1            | compositvs          | 1               |
| navalis         | 1            | navalia             | 1               |
| pvngo           | 1            | parco               | 1               |
| retardo         | 1            | retardeo            | 1               |
| magnificenter   | 1            | magnificvs          | 1               |
| belides         | 1            | belis               | 1               |
| legens          | 1            | lego                | 1               |
| qvotvsqvisqve   | 1            | qvotvs              | 1               |
| laevvs          | 1            | laevvm              | 1               |
| delectvs        | 1            | deligo              | 1               |
| vivvs           | 1            | vivo                | 1               |
| morior          | 1            | mortvvs             | 1               |
| diligo          | 1            | diligens            | 1               |
| geidvmni        | 1            | geidimni            | 1               |
| vado            | 1            | vadvm               | 1               |
| abvndans        | 1            | abvndo              | 1               |
| amplio          | 1            | amplvaris           | 1               |
| conservvs       | 1            | consero             | 1               |
| indeploratvs    | 1            | indeploro           | 1               |
| vlcvs           | 1            | vlcero              | 1               |
| pargo           | 1            | parco               | 1               |
| monitvs         | 1            | moneo               | 1               |
| camers          | 1            | camertvs            | 1               |
| deficio         | 1            | deficiens           | 1               |
| prostitvtvs     | 1            | prostitvtvm         | 1               |
| cepheis         | 1            | cephevs             | 1               |
| laniatvs        | 1            | lanio               | 1               |
| dilacero        | 1            | dilacior            | 1               |
| lavdo           | 1            | lavs                | 1               |
| callistvs       | 1            | callistivs          | 1               |
| reicvlvs        | 1            | reicvlvm            | 1               |
| dives           | 1            | divia               | 1               |
| lynx            | 1            | lynca               | 1               |
| scienter        | 1            | sciente             | 1               |
| neapolitanvm    | 1            | neapolitanvs        | 1               |
| pessvlvs        | 1            | pessvl              | 1               |
| lvdivs          | 1            | lvdo                | 1               |
| svbsilio        | 1            | svssilio            | 1               |
| parapamisadae   | 1            | parapamisades       | 1               |
| appetens        | 1            | appeto              | 1               |
| expetesso       | 1            | expetior            | 1               |
| altercor        | 1            | alterco             | 1               |
| archimagirvs    | 1            | archimagivs         | 1               |
| linevs          | 1            | linea               | 1               |
| fvsvs           | 1            | fvndo               | 1               |
| applavdo        | 1            | applavdeo           | 1               |
| tela            | 1            | telvm               | 1               |
| considero       | 1            | consido             | 1               |
| vetera          | 1            | vetvs               | 1               |
| polydamas       | 1            | pvlydamas           | 1               |
| lanivs          | 1            | lanis               | 1               |
| versor          | 1            | verso               | 1               |
| exigo           | 1            | exactvs             | 1               |
| septimvs        | 1            | septimvm            | 1               |
| observo         | 1            | observvs            | 1               |
| abrvptvs        | 1            | abrvmpo             | 1               |
| secrete         | 1            | secretvm            | 1               |
| parcvs          | 1            | parce               | 1               |
| concinno        | 1            | concinnvs           | 1               |
| librvm          | 1            | libra               | 1               |
| rvbricatvs      | 1            | rvbrico             | 1               |
| seco            | 1            | secandvs            | 1               |
| strvo           | 1            | strvm               | 1               |
| vipsanivs       | 1            | vipsanvs            | 1               |
| coalesco        | 1            | coalio              | 1               |
| sto             | 1            | statvra             | 1               |
| angvinvs        | 1            | angvina             | 1               |
| inertia         | 1            | iners               | 1               |
| svscipio        | 1            | svccipio            | 1               |
| sidonivs        | 1            | sidonii             | 1               |
| infra           | 1            | infervs             | 1               |
| paco            | 1            | pacatvs             | 1               |
| eleganter       | 1            | elegans             | 1               |
| commissvm       | 1            | committo            | 1               |
| altare          | 1            | alto                | 1               |
| tempero         | 1            | temperatvs          | 1               |
| noceo           | 1            | nocens              | 1               |
| caivs           | 1            | cavs                | 1               |
| arverni         | 1            | avernni             | 1               |
| qvatio          | 1            | qvatvs              | 1               |
| dediticivs      | 1            | dediticivm          | 1               |
| syrtis          | 1            | syrti               | 1               |
| despolio        | 1            | despolivm           | 1               |
| cycnvs          | 1            | cycna               | 1               |
| infirmvs        | 1            | infirmo             | 1               |
| viso            | 1            | video               | 1               |
| hibernvm        | 1            | hiberna             | 1               |
| iners           | 1            | inertia             | 1               |
| visvs           | 1            | video               | 1               |
| primvm          | 1            | primvs              | 1               |
| farinarivs      | 1            | farinarivm          | 1               |
| cadvs           | 1            | cado                | 1               |
| praemonstro     | 1            | praemostro          | 1               |
| diverto         | 1            | diversvs            | 1               |
| accelero        | 1            | acceleratvs         | 1               |
| desideo         | 1            | desido              | 1               |
| svperpendens    | 1            | pendeo              | 1               |
| caelites        | 1            | caeles              | 1               |
| eventvra        | 1            | evenio              | 1               |
| contrarivm      | 1            | contrarivs          | 1               |
| debitvm         | 1            | debeo               | 1               |
| arimaspi        | 1            | arimaspes           | 1               |
| apertvs         | 1            | aperio              | 1               |
| manvs           | 1            | maneo               | 1               |
| verso           | 1            | versor              | 1               |
| praetento       | 1            | praetempto          | 1               |
| fortiter        | 1            | fortis              | 1               |
| tonstrinvs      | 1            | tonstrentvm         | 1               |
| elysii          | 1            | elysivs             | 1               |
| resido          | 1            | resideo             | 1               |
| phoebevs        | 1            | phoebeivs           | 1               |
| complector      | 1            | complexvs           | 1               |

# POS

```
all:
  accuracy: 0.9655
  precision: 0.9225
  recall: 0.9141
  support: 141348
ambiguous-tokens:
  accuracy: 0.9169
  precision: 0.8482
  recall: 0.8358
  support: 43177
unknown-tokens:
  accuracy: 0.8966
  precision: 0.5304
  recall: 0.5129
  support: 6091
```

| Expected   | Total Errors | Predictions | Predicted times |
|------------|--------------|-------------|-----------------|
| ADJqua     | 1076         | NOM2        | 459             |
|            |              | VER         | 257             |
|            |              | NOM3        | 136             |
|            |              | ADV         | 103             |
|            |              | NOM1        | 95              |
|            |              | NOM7        | 10              |
|            |              | NOM4        | 9               |
|            |              | CONcoo      | 4               |
|            |              | ADJord      | 2               |
|            |              | PRE         | 1               |
| NOM2       | 605          | ADJqua      | 295             |
|            |              | VER         | 117             |
|            |              | NOM3        | 49              |
|            |              | NOM7        | 30              |
|            |              | ADV         | 30              |
|            |              | NOM1        | 29              |
|            |              | PROpos.ref  | 12              |
|            |              | CONcoo      | 10              |
|            |              | NOM4        | 8               |
|            |              | PROind      | 5               |
|            |              | ADJcar      | 4               |
|            |              | ADJdis      | 4               |
|            |              | NOM5        | 4               |
|            |              | NOM6        | 3               |
|            |              | PROpos      | 2               |
|            |              | PROref      | 1               |
|            |              | PROdem      | 1               |
|            |              | ADJord      | 1               |
| ADV        | 477          | CONcoo      | 137             |
|            |              | ADJqua      | 91              |
|            |              | PROdem      | 78              |
|            |              | PRE         | 38              |
|            |              | NOM2        | 31              |
|            |              | CONsub      | 29              |
|            |              | PROind      | 22              |
|            |              | NOM3        | 17              |
|            |              | VER         | 10              |
|            |              | ADJcar      | 8               |
|            |              | NOM4        | 3               |
|            |              | NOM1        | 2               |
|            |              | ADVneg      | 2               |
|            |              | ADVint.neg  | 2               |
|            |              | INJ         | 1               |
|            |              | PROper      | 1               |
|            |              | PROint      | 1               |
|            |              | NOM5        | 1               |
|            |              | PROrel      | 1               |
|            |              | ADJord      | 1               |
|            |              | ADVrel      | 1               |
| VER        | 399          | ADJqua      | 190             |
|            |              | NOM2        | 73              |
|            |              | NOM3        | 40              |
|            |              | NOM1        | 33              |
|            |              | NOM4        | 33              |
|            |              | ADV         | 8               |
|            |              | NOM5        | 4               |
|            |              | CONsub      | 4               |
|            |              | PRE         | 3               |
|            |              | INJ         | 3               |
|            |              | PROdem      | 2               |
|            |              | ADJcar      | 2               |
|            |              | ADVint      | 2               |
|            |              | ADVrel      | 1               |
|            |              | NOM7        | 1               |
| CONsub     | 354          | ADVrel      | 132             |
|            |              | PROrel      | 86              |
|            |              | PRE         | 40              |
|            |              | CONcoo      | 39              |
|            |              | ADVint      | 17              |
|            |              | ADVneg      | 16              |
|            |              | ADV         | 14              |
|            |              | VER         | 9               |
|            |              | PROint      | 1               |
| NOM3       | 318          | NOM2        | 101             |
|            |              | ADJqua      | 98              |
|            |              | VER         | 45              |
|            |              | NOM7        | 30              |
|            |              | ADV         | 16              |
|            |              | NOM1        | 12              |
|            |              | NOM6        | 5               |
|            |              | PROind      | 5               |
|            |              | NOM4        | 3               |
|            |              | PROint      | 1               |
|            |              | PROper      | 1               |
|            |              | PROref      | 1               |
| PROrel     | 242          | PROint      | 95              |
|            |              | CONsub      | 65              |
|            |              | ADVrel      | 58              |
|            |              | PROind      | 11              |
|            |              | ADVint      | 8               |
|            |              | CONcoo      | 5               |
| ADVrel     | 223          | CONsub      | 110             |
|            |              | ADVint      | 64              |
|            |              | PROrel      | 37              |
|            |              | PROint      | 7               |
|            |              | VER         | 2               |
|            |              | PROind      | 1               |
|            |              | ADJqua      | 1               |
|            |              | ADV         | 1               |
| PROint     | 209          | PROrel      | 170             |
|            |              | ADVint      | 18              |
|            |              | ADVrel      | 10              |
|            |              | PROind      | 6               |
|            |              | CONsub      | 4               |
|            |              | PROdem      | 1               |
| NOM1       | 177          | ADJqua      | 70              |
|            |              | NOM2        | 56              |
|            |              | VER         | 20              |
|            |              | NOM7        | 18              |
|            |              | NOM3        | 12              |
|            |              | ADJdis      | 1               |
| ADVint     | 140          | ADVrel      | 63              |
|            |              | CONsub      | 31              |
|            |              | PROrel      | 26              |
|            |              | PROint      | 12              |
|            |              | ADV         | 3               |
|            |              | PROind      | 1               |
|            |              | ADVint.neg  | 1               |
|            |              | PROdem      | 1               |
|            |              | NOM1        | 1               |
|            |              | NOM3        | 1               |
| CONcoo     | 91           | ADV         | 54              |
|            |              | CONsub      | 28              |
|            |              | PROrel      | 6               |
|            |              | ADJqua      | 3               |
| PRE        | 87           | CONsub      | 42              |
|            |              | ADV         | 37              |
|            |              | VER         | 5               |
|            |              | INJ         | 2               |
|            |              | ADJord      | 1               |
| PROdem     | 81           | ADV         | 73              |
|            |              | VER         | 5               |
|            |              | PROref      | 1               |
|            |              | ADVint      | 1               |
|            |              | INJ         | 1               |
| NOM7       | 75           | NOM2        | 27              |
|            |              | NOM1        | 25              |
|            |              | NOM3        | 18              |
|            |              | ADJqua      | 5               |
| NOM4       | 66           | VER         | 45              |
|            |              | ADJqua      | 6               |
|            |              | NOM2        | 6               |
|            |              | NOM6        | 4               |
|            |              | NOM3        | 4               |
|            |              | ADJcar      | 1               |
| PROind     | 50           | PROrel      | 16              |
|            |              | NOM2        | 11              |
|            |              | ADV         | 11              |
|            |              | PROint      | 11              |
|            |              | ADVrel      | 1               |
| NOM6       | 41           | NOM3        | 23              |
|            |              | NOM2        | 8               |
|            |              | NOM4        | 5               |
|            |              | ADV         | 2               |
|            |              | NOM1        | 2               |
|            |              | ADJqua      | 1               |
| ADVneg     | 33           | CONsub      | 25              |
|            |              | CONcoo      | 6               |
|            |              | PROind      | 2               |
| ADJord     | 31           | ADJadv.ord  | 15              |
|            |              | ADJqua      | 12              |
|            |              | NOM1        | 2               |
|            |              | NOM6        | 1               |
|            |              | PRE         | 1               |
| PROper     | 17           | PROpos      | 16              |
|            |              | ADV         | 1               |
| INJ        | 15           | PRE         | 7               |
|            |              | VER         | 3               |
|            |              | NOM2        | 1               |
|            |              | ADV         | 1               |
|            |              | ADJqua      | 1               |
|            |              | NOM1        | 1               |
|            |              | PROdem      | 1               |
| PROpos     | 13           | PROper      | 12              |
|            |              | NOM2        | 1               |
| ADJcar     | 10           | ADV         | 4               |
|            |              | NOM3        | 2               |
|            |              | NOM1        | 2               |
|            |              | NOM4        | 1               |
|            |              | PRE         | 1               |
| PROref     | 10           | PROpos.ref  | 8               |
|            |              | PROdem      | 2               |
| ADJadv.ord | 9            | ADJord      | 9               |
| PROpos.ref | 6            | PROref      | 4               |
|            |              | NOM2        | 2               |
| ADJdis     | 6            | ADJqua      | 3               |
|            |              | ADJcar      | 1               |
|            |              | ADJord      | 1               |
|            |              | NOM3        | 1               |
| ADVint.neg | 4            | ADV         | 3               |
|            |              | CONsub      | 1               |
| VERaux     | 2            | VER         | 2               |
| ADJmul     | 2            | NOM3        | 2               |
| NOM5       | 1            | NOM3        | 1               |

# Voice

```
all:
  accuracy: 0.9918
  precision: 0.9736
  recall: 0.9754
  support: 141348
ambiguous-tokens:
  accuracy: 0.9453
  precision: 0.9034
  recall: 0.9277
  support: 11572
unknown-tokens:
  accuracy: 0.9562
  precision: 0.9443
  recall: 0.8632
  support: 6091
``` 

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| _        | 499          | Pass        | 270             |
|          |              | Act         | 164             |
|          |              | Dep         | 62              |
|          |              | SemDep      | 3               |
| Pass     | 285          | _           | 194             |
|          |              | Act         | 68              |
|          |              | Dep         | 23              |
| Act      | 276          | _           | 181             |
|          |              | Pass        | 80              |
|          |              | Dep         | 15              |
| Dep      | 93           | _           | 47              |
|          |              | Pass        | 34              |
|          |              | Act         | 12              |
| SemDep   | 5            | _           | 3               |
|          |              | Act         | 2               |

# Mood

```
all:
  accuracy: 0.9836
  precision: 0.9004
  recall: 0.8656
  support: 141348
ambiguous-tokens:
  accuracy: 0.8895
  precision: 0.8365
  recall: 0.8045
  support: 13431
unknown-tokens:
  accuracy: 0.9338
  precision: 0.807
  recall: 0.8101
  support: 6091
```

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| Ind      | 702          | Par         | 308             |
|          |              | Sub         | 190             |
|          |              | _           | 135             |
|          |              | Inf         | 49              |
|          |              | Imp         | 18              |
|          |              | SupU        | 2               |
| Par      | 493          | _           | 201             |
|          |              | Ind         | 185             |
|          |              | Inf         | 85              |
|          |              | Sub         | 15              |
|          |              | Imp         | 5               |
|          |              | SupU        | 2               |
| _        | 443          | Par         | 256             |
|          |              | Ind         | 99              |
|          |              | Inf         | 39              |
|          |              | Imp         | 24              |
|          |              | Sub         | 16              |
|          |              | Adj         | 5               |
|          |              | SupUm       | 2               |
|          |              | Ger         | 1               |
|          |              | SupU        | 1               |
| Sub      | 363          | Ind         | 282             |
|          |              | Par         | 39              |
|          |              | _           | 33              |
|          |              | Inf         | 9               |
| Inf      | 207          | Par         | 120             |
|          |              | Ind         | 47              |
|          |              | _           | 35              |
|          |              | Sub         | 3               |
|          |              | SupU        | 1               |
|          |              | Imp         | 1               |
| Imp      | 52           | _           | 23              |
|          |              | Ind         | 17              |
|          |              | Par         | 7               |
|          |              | Inf         | 5               |
| Adj      | 29           | Ger         | 27              |
|          |              | Sub         | 1               |
|          |              | _           | 1               |
| SupU     | 15           | Inf         | 5               |
|          |              | Par         | 4               |
|          |              | _           | 3               |
|          |              | Ind         | 3               |
| Ger      | 12           | Adj         | 12              |
| SupUm    | 5            | _           | 5               |

# Degree

```
all:
  accuracy: 0.983
  precision: 0.9759
  recall: 0.9758
  support: 141348
ambiguous-tokens:
  accuracy: 0.9266
  precision: 0.9232
  recall: 0.9286
  support: 23380
unknown-tokens:
  accuracy: 0.9452
  precision: 0.9386
  recall: 0.9304
  support: 6091
```

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| Pos      | 1344         | _           | 1335            |
|          |              | Comp        | 8               |
|          |              | Sup         | 1               |
| _        | 1033         | Pos         | 998             |
|          |              | Sup         | 19              |
|          |              | Comp        | 16              |
| Sup      | 16           | _           | 14              |
|          |              | Pos         | 1               |
|          |              | Comp        | 1               |
| Comp     | 7            | _           | 6               |
|          |              | Pos         | 1               |

# Numb

```
all:
  accuracy: 0.9788
  precision: 0.978
  recall: 0.9761
  support: 141348
ambiguous-tokens:
  accuracy: 0.9225
  precision: 0.9229
  recall: 0.9157
  support: 30222
unknown-tokens:
  accuracy: 0.9567
  precision: 0.9341
  recall: 0.9314
  support: 6091
```

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| Sing     | 1290         | Plur        | 866             |
|          |              | _           | 424             |
| Plur     | 1079         | Sing        | 1045            |
|          |              | _           | 34              |
| _        | 628          | Sing        | 593             |
|          |              | Plur        | 35              |

# Person

```
all:
  accuracy: 0.9918
  precision: 0.9791
  recall: 0.9723
  support: 141348
ambiguous-tokens:
  accuracy: 0.9247
  precision: 0.8812
  recall: 0.8631
  support: 10386
unknown-tokens:
  accuracy: 0.975
  precision: 0.9694
  recall: 0.9549
  support: 6091
```

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| _        | 459          | 3           | 313             |
|          |              | 2           | 77              |
|          |              | 1           | 69              |
| 3        | 434          | _           | 417             |
|          |              | 2           | 9               |
|          |              | 1           | 8               |
| 2        | 153          | _           | 127             |
|          |              | 3           | 17              |
|          |              | 1           | 9               |
| 1        | 107          | _           | 70              |
|          |              | 3           | 30              |
|          |              | 2           | 7               |

# Tense

```
all:
  accuracy: 0.9875
  precision: 0.6406
  recall: 0.6324
  support: 141348
ambiguous-tokens:
  accuracy: 0.9191
  precision: 0.5486
  recall: 0.5288
  support: 13468
unknown-tokens:
  accuracy: 0.9493
  precision: 0.9444
  recall: 0.9392
  support: 6091
```

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| _        | 507          | Perf        | 309             |
|          |              | Pres        | 172             |
|          |              | Fut         | 18              |
|          |              | Pqp         | 6               |
|          |              | Impa        | 2               |
| Perf     | 430          | _           | 234             |
|          |              | Pres        | 106             |
|          |              | Fut         | 52              |
|          |              | Pqp         | 38              |
| Pres     | 405          | _           | 167             |
|          |              | Perf        | 151             |
|          |              | Fut         | 77              |
|          |              | Impa        | 7               |
|          |              | Pqp         | 3               |
| Fut      | 216          | Perf        | 123             |
|          |              | Pres        | 60              |
|          |              | _           | 25              |
|          |              | Pqp         | 5               |
|          |              | Impa        | 2               |
|          |              | PeriFut     | 1               |
| Pqp      | 168          | Perf        | 161             |
|          |              | _           | 7               |
| PeriPerf | 14           | Perf        | 13              |
|          |              | _           | 1               |
| PeriPqp  | 11           | Perf        | 11              |
| PeriFut  | 10           | Fut         | 7               |
|          |              | Perf        | 2               |
|          |              | Pqp         | 1               |
| Impa     | 1            | Pres        | 1               |

# Case

```
all:
  accuracy: 0.9374
  precision: 0.9
  recall: 0.8636
  support: 141348
ambiguous-tokens:
  accuracy: 0.8596
  precision: 0.8565
  recall: 0.8161
  support: 52350
unknown-tokens:
  accuracy: 0.8913
  precision: 0.6981
  recall: 0.6703
  support: 6091
```

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| Nom      | 2629         | Acc         | 1461            |
|          |              | Abl         | 401             |
|          |              | _           | 396             |
|          |              | Gen         | 234             |
|          |              | Voc         | 79              |
|          |              | Dat         | 53              |
|          |              | Ind         | 3               |
|          |              | Loc         | 2               |
| Acc      | 1630         | Nom         | 1072            |
|          |              | _           | 301             |
|          |              | Abl         | 131             |
|          |              | Gen         | 88              |
|          |              | Voc         | 23              |
|          |              | Dat         | 8               |
|          |              | Ind         | 7               |
| Abl      | 1477         | Dat         | 551             |
|          |              | Nom         | 425             |
|          |              | Acc         | 284             |
|          |              | _           | 184             |
|          |              | Gen         | 21              |
|          |              | Voc         | 11              |
|          |              | Loc         | 1               |
| Dat      | 1123         | Abl         | 826             |
|          |              | Gen         | 199             |
|          |              | Nom         | 58              |
|          |              | _           | 31              |
|          |              | Voc         | 7               |
|          |              | Ind         | 1               |
|          |              | Acc         | 1               |
| _        | 1022         | Nom         | 424             |
|          |              | Acc         | 355             |
|          |              | Abl         | 179             |
|          |              | Dat         | 22              |
|          |              | Gen         | 19              |
|          |              | Voc         | 12              |
|          |              | Ind         | 11              |
| Gen      | 495          | Nom         | 254             |
|          |              | Dat         | 114             |
|          |              | Acc         | 69              |
|          |              | _           | 24              |
|          |              | Voc         | 14              |
|          |              | Abl         | 12              |
|          |              | Loc         | 8               |
| Voc      | 400          | Nom         | 255             |
|          |              | Acc         | 59              |
|          |              | Gen         | 42              |
|          |              | Abl         | 20              |
|          |              | _           | 18              |
|          |              | Dat         | 6               |
| Ind      | 48           | Acc         | 22              |
|          |              | _           | 15              |
|          |              | Abl         | 4               |
|          |              | Nom         | 4               |
|          |              | Gen         | 2               |
|          |              | Dat         | 1               |
| Loc      | 18           | Gen         | 12              |
|          |              | Dat         | 3               |
|          |              | Nom         | 3               |

# Gender

```
all:
  accuracy: 0.9727
  precision: 0.9378
  recall: 0.9387
  support: 141348
ambiguous-tokens:
  accuracy: 0.8958
  precision: 0.8963
  recall: 0.8985
  support: 28491
unknown-tokens:
  accuracy: 0.9283
  precision: 0.8886
  recall: 0.8548
  support: 6091
```

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| _        | 1291         | MascNeut    | 400             |
|          |              | Neut        | 289             |
|          |              | Fem         | 236             |
|          |              | Masc        | 188             |
|          |              | Com         | 119             |
|          |              | MascFem     | 59              |
| Neut     | 817          | Fem         | 315             |
|          |              | MascNeut    | 242             |
|          |              | _           | 235             |
|          |              | Com         | 18              |
|          |              | Masc        | 4               |
|          |              | MascFem     | 3               |
| MascNeut | 609          | _           | 392             |
|          |              | Neut        | 179             |
|          |              | Masc        | 35              |
|          |              | Fem         | 2               |
|          |              | MascFem     | 1               |
| Fem      | 409          | Neut        | 238             |
|          |              | _           | 164             |
|          |              | MascNeut    | 4               |
|          |              | MascFem     | 2               |
|          |              | Com         | 1               |
| Masc     | 357          | _           | 272             |
|          |              | MascNeut    | 43              |
|          |              | Com         | 20              |
|          |              | MascFem     | 12              |
|          |              | Neut        | 10              |
| Com      | 280          | _           | 183             |
|          |              | MascFem     | 46              |
|          |              | Masc        | 34              |
|          |              | Neut        | 14              |
|          |              | MascNeut    | 3               |
| MascFem  | 92           | _           | 47              |
|          |              | Com         | 36              |
|          |              | Neut        | 5               |
|          |              | Masc        | 4               |
