
::: Evaluation report for task: Case :::

all:
  accuracy: 0.931
  precision: 0.8847
  recall: 0.8402
  support: 141348
ambiguous-tokens:
  accuracy: 0.8444
  precision: 0.8349
  recall: 0.7893
  support: 52350
unknown-tokens:
  accuracy: 0.8775
  precision: 0.6756
  recall: 0.6557
  support: 6091

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| Nom      | 2957         | Acc         | 1623            |
|          |              | Abl         | 444             |
|          |              | _           | 444             |
|          |              | Gen         | 270             |
|          |              | Voc         | 119             |
|          |              | Dat         | 55              |
|          |              | Ind         | 2               |
| Acc      | 1817         | Nom         | 1174            |
|          |              | _           | 358             |
|          |              | Abl         | 132             |
|          |              | Gen         | 92              |
|          |              | Voc         | 43              |
|          |              | Dat         | 11              |
|          |              | Ind         | 7               |
| Dat      | 1462         | Abl         | 1114            |
|          |              | Gen         | 236             |
|          |              | Nom         | 74              |
|          |              | _           | 26              |
|          |              | Voc         | 7               |
|          |              | Acc         | 3               |
|          |              | Loc         | 2               |
| Abl      | 1451         | Dat         | 478             |
|          |              | Nom         | 445             |
|          |              | Acc         | 289             |
|          |              | _           | 194             |
|          |              | Voc         | 26              |
|          |              | Gen         | 19              |
| _        | 1052         | Nom         | 397             |
|          |              | Acc         | 368             |
|          |              | Abl         | 216             |
|          |              | Gen         | 23              |
|          |              | Dat         | 21              |
|          |              | Ind         | 14              |
|          |              | Voc         | 13              |
| Gen      | 516          | Nom         | 274             |
|          |              | Dat         | 89              |
|          |              | Acc         | 70              |
|          |              | Voc         | 38              |
|          |              | _           | 30              |
|          |              | Abl         | 8               |
|          |              | Loc         | 7               |
| Voc      | 409          | Nom         | 234             |
|          |              | Acc         | 63              |
|          |              | Gen         | 42              |
|          |              | Abl         | 41              |
|          |              | _           | 21              |
|          |              | Dat         | 8               |
| Ind      | 54           | Acc         | 21              |
|          |              | _           | 17              |
|          |              | Nom         | 8               |
|          |              | Gen         | 6               |
|          |              | Abl         | 2               |
| Loc      | 28           | Gen         | 21              |
|          |              | Dat         | 5               |
|          |              | Nom         | 2               |

::: Evaluation report for task: Deg :::

all:
  accuracy: 0.9787
  precision: 0.9627
  recall: 0.9686
  support: 141348
ambiguous-tokens:
  accuracy: 0.9104
  precision: 0.8941
  recall: 0.9139
  support: 23380
unknown-tokens:
  accuracy: 0.9238
  precision: 0.9037
  recall: 0.9083
  support: 6091

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| Pos      | 1627         | _           | 1592            |
|          |              | Comp        | 19              |
|          |              | Sup         | 16              |
| _        | 1347         | Pos         | 1288            |
|          |              | Sup         | 38              |
|          |              | Comp        | 21              |
| Comp     | 20           | Pos         | 10              |
|          |              | _           | 10              |
| Sup      | 19           | _           | 10              |
|          |              | Pos         | 7               |
|          |              | Comp        | 2               |

::: Evaluation report for task: Gend :::

all:
  accuracy: 0.969
  precision: 0.9277
  recall: 0.9322
  support: 141348
ambiguous-tokens:
  accuracy: 0.8831
  precision: 0.8821
  recall: 0.8878
  support: 28491
unknown-tokens:
  accuracy: 0.9154
  precision: 0.8601
  recall: 0.8477
  support: 6091

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| _        | 1583         | MascNeut    | 499             |
|          |              | Neut        | 356             |
|          |              | Masc        | 264             |
|          |              | Fem         | 251             |
|          |              | Com         | 151             |
|          |              | MascFem     | 62              |
| Neut     | 848          | Fem         | 286             |
|          |              | MascNeut    | 271             |
|          |              | _           | 269             |
|          |              | Com         | 20              |
|          |              | Masc        | 2               |
| MascNeut | 675          | _           | 417             |
|          |              | Neut        | 201             |
|          |              | Masc        | 54              |
|          |              | Com         | 2               |
|          |              | MascFem     | 1               |
| Fem      | 512          | Neut        | 285             |
|          |              | _           | 220             |
|          |              | MascFem     | 2               |
|          |              | Masc        | 2               |
|          |              | MascNeut    | 2               |
|          |              | Com         | 1               |
| Masc     | 380          | _           | 278             |
|          |              | MascNeut    | 52              |
|          |              | Com         | 24              |
|          |              | MascFem     | 14              |
|          |              | Neut        | 11              |
|          |              | Fem         | 1               |
| Com      | 259          | _           | 140             |
|          |              | MascFem     | 63              |
|          |              | Masc        | 38              |
|          |              | Neut        | 12              |
|          |              | MascNeut    | 5               |
|          |              | Fem         | 1               |
| MascFem  | 124          | _           | 63              |
|          |              | Com         | 52              |
|          |              | Neut        | 6               |
|          |              | Masc        | 2               |
|          |              | Fem         | 1               |

::: Evaluation report for task: Mood :::

all:
  accuracy: 0.9811
  precision: 0.8623
  recall: 0.8275
  support: 141348
ambiguous-tokens:
  accuracy: 0.8782
  precision: 0.7778
  recall: 0.7285
  support: 13431
unknown-tokens:
  accuracy: 0.9251
  precision: 0.7134
  recall: 0.7183
  support: 6091

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| Ind      | 711          | Par         | 286             |
|          |              | Sub         | 213             |
|          |              | _           | 148             |
|          |              | Inf         | 48              |
|          |              | Imp         | 16              |
| Par      | 563          | Ind         | 240             |
|          |              | _           | 210             |
|          |              | Inf         | 86              |
|          |              | Sub         | 20              |
|          |              | Imp         | 6               |
|          |              | SupU        | 1               |
| _        | 511          | Par         | 261             |
|          |              | Ind         | 134             |
|          |              | Inf         | 46              |
|          |              | Imp         | 34              |
|          |              | Sub         | 22              |
|          |              | Adj         | 7               |
|          |              | SupUm       | 3               |
|          |              | Ger         | 3               |
|          |              | SupU        | 1               |
| Sub      | 505          | Ind         | 415             |
|          |              | _           | 43              |
|          |              | Par         | 37              |
|          |              | Inf         | 8               |
|          |              | Imp         | 2               |
| Inf      | 239          | Par         | 121             |
|          |              | Ind         | 57              |
|          |              | _           | 55              |
|          |              | Imp         | 3               |
|          |              | Sub         | 2               |
|          |              | SupU        | 1               |
| Imp      | 59           | _           | 26              |
|          |              | Ind         | 18              |
|          |              | Par         | 11              |
|          |              | Inf         | 4               |
| Adj      | 36           | Ger         | 34              |
|          |              | _           | 1               |
|          |              | Sub         | 1               |
| SupU     | 24           | _           | 8               |
|          |              | Inf         | 7               |
|          |              | Par         | 4               |
|          |              | Ind         | 4               |
|          |              | Sub         | 1               |
| Ger      | 23           | Adj         | 23              |
| SupUm    | 4            | _           | 4               |

::: Evaluation report for task: Numb :::

all:
  accuracy: 0.9761
  precision: 0.9743
  recall: 0.9743
  support: 141348
ambiguous-tokens:
  accuracy: 0.9118
  precision: 0.9084
  recall: 0.9088
  support: 30222
unknown-tokens:
  accuracy: 0.9481
  precision: 0.9135
  recall: 0.9283
  support: 6091

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| Sing     | 1671         | Plur        | 1026            |
|          |              | _           | 645             |
| Plur     | 1110         | Sing        | 1073            |
|          |              | _           | 37              |
| _        | 595          | Sing        | 557             |
|          |              | Plur        | 38              |

::: Evaluation report for task: Person :::

all:
  accuracy: 0.9911
  precision: 0.9766
  recall: 0.9671
  support: 141348
ambiguous-tokens:
  accuracy: 0.9187
  precision: 0.8715
  recall: 0.8405
  support: 10386
unknown-tokens:
  accuracy: 0.9713
  precision: 0.9629
  recall: 0.9469
  support: 6091

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| 3        | 476          | _           | 450             |
|          |              | 2           | 16              |
|          |              | 1           | 10              |
| _        | 464          | 3           | 309             |
|          |              | 2           | 84              |
|          |              | 1           | 71              |
| 2        | 185          | _           | 146             |
|          |              | 3           | 21              |
|          |              | 1           | 18              |
| 1        | 134          | _           | 94              |
|          |              | 3           | 32              |
|          |              | 2           | 8               |

::: Evaluation report for task: Tense :::

all:
  accuracy: 0.9864
  precision: 0.6392
  recall: 0.6289
  support: 141348
ambiguous-tokens:
  accuracy: 0.9131
  precision: 0.5546
  recall: 0.5158
  support: 13468
unknown-tokens:
  accuracy: 0.946
  precision: 0.94
  recall: 0.9358
  support: 6091

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| _        | 595          | Perf        | 344             |
|          |              | Pres        | 213             |
|          |              | Fut         | 35              |
|          |              | Impa        | 2               |
|          |              | Pqp         | 1               |
| Pres     | 435          | _           | 168             |
|          |              | Perf        | 140             |
|          |              | Fut         | 115             |
|          |              | Impa        | 10              |
|          |              | Pqp         | 2               |
| Perf     | 409          | _           | 198             |
|          |              | Pres        | 136             |
|          |              | Fut         | 59              |
|          |              | Pqp         | 16              |
| Fut      | 261          | Perf        | 136             |
|          |              | Pres        | 93              |
|          |              | _           | 29              |
|          |              | Pqp         | 2               |
|          |              | Impa        | 1               |
| Pqp      | 181          | Perf        | 175             |
|          |              | _           | 5               |
|          |              | Fut         | 1               |
| PeriPerf | 14           | Perf        | 13              |
|          |              | _           | 1               |
| PeriPqp  | 11           | Perf        | 10              |
|          |              | Pqp         | 1               |
| PeriFut  | 10           | Fut         | 7               |
|          |              | Perf        | 2               |
|          |              | Pqp         | 1               |
| Impa     | 7            | Pres        | 5               |
|          |              | Fut         | 2               |

::: Evaluation report for task: Voice :::

all:
  accuracy: 0.9904
  precision: 0.9657
  recall: 0.9685
  support: 141348
ambiguous-tokens:
  accuracy: 0.9369
  precision: 0.886
  recall: 0.9213
  support: 11572
unknown-tokens:
  accuracy: 0.9452
  precision: 0.9236
  recall: 0.8075
  support: 6091

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| _        | 623          | Pass        | 329             |
|          |              | Act         | 232             |
|          |              | Dep         | 56              |
|          |              | SemDep      | 6               |
| Pass     | 316          | _           | 169             |
|          |              | Act         | 102             |
|          |              | Dep         | 45              |
| Act      | 295          | _           | 183             |
|          |              | Pass        | 87              |
|          |              | Dep         | 25              |
| Dep      | 113          | _           | 45              |
|          |              | Pass        | 38              |
|          |              | Act         | 30              |
| SemDep   | 10           | Pass        | 4               |
|          |              | Act         | 2               |
|          |              | Dep         | 2               |
|          |              | _           | 2               |

::: Evaluation report for task: lemma :::

all:
  accuracy: 0.9711
  precision: 0.815
  recall: 0.8076
  support: 141348
ambiguous-tokens:
  accuracy: 0.9151
  precision: 0.6565
  recall: 0.665
  support: 31164
unknown-targets:
  accuracy: 0.5748
  precision: 0.4056
  recall: 0.3954
  support: 983
unknown-tokens:
  accuracy: 0.8527
  precision: 0.7065
  recall: 0.6998
  support: 6091

| Expected        | Total Errors | Predictions         | Predicted times |
|-----------------|--------------|---------------------|-----------------|
| qvis            | 181          | qvi                 | 166             |
|                 |              | qvam                | 7               |
|                 |              | qvo                 | 4               |
|                 |              | qva                 | 2               |
|                 |              | qvod                | 1               |
|                 |              | cvivs               | 1               |
| qvi             | 176          | qvis                | 66              |
|                 |              | qvod                | 50              |
|                 |              | qvam                | 34              |
|                 |              | qvo                 | 21              |
|                 |              | qva                 | 4               |
|                 |              | qvisqvam            | 1               |
| qvod            | 108          | qvi                 | 108             |
| svi             | 35           | svvs                | 31              |
|                 |              | ipse                | 4               |
| bonvs           | 33           | bonvm               | 23              |
|                 |              | boni                | 7               |
|                 |              | bene                | 3               |
| qvam            | 32           | qvi                 | 28              |
|                 |              | qvis                | 4               |
| malvs           | 27           | malvm               | 26              |
|                 |              | male                | 1               |
| qvo             | 26           | qvi                 | 25              |
|                 |              | qvis                | 1               |
| is              | 24           | eo                  | 22              |
|                 |              | svm                 | 1               |
|                 |              | ecce                | 1               |
| boni            | 23           | bonvm               | 20              |
|                 |              | bonvs               | 3               |
| svvs            | 23           | svi                 | 21              |
|                 |              | svvm                | 2               |
| noster          | 21           | nos                 | 15              |
|                 |              | nostri              | 6               |
| parvvs          | 21           | parvm               | 15              |
|                 |              | parvvm              | 3               |
|                 |              | minimvm             | 2               |
|                 |              | pareo               | 1               |
| cetervs         | 21           | ceteri              | 16              |
|                 |              | cetera              | 5               |
| paro            | 20           | paratvs             | 16              |
|                 |              | pareo               | 4               |
| mvltvs          | 19           | mvlti               | 14              |
|                 |              | mvltvm              | 5               |
| factvm          | 18           | facio               | 18              |
| svm             | 17           | volo                | 7               |
|                 |              | hervs               | 1               |
|                 |              | homo                | 1               |
|                 |              | ago                 | 1               |
|                 |              | foris               | 1               |
|                 |              | fvtvrvs             | 1               |
|                 |              | qvoio               | 1               |
|                 |              | svmmanvs            | 1               |
|                 |              | vaniloqvvs          | 1               |
|                 |              | strepitvs           | 1               |
|                 |              | scio                | 1               |
| facio           | 17           | factvm              | 12              |
|                 |              | facies              | 4               |
|                 |              | svm                 | 1               |
| mvltvm          | 16           | mvltvs              | 16              |
| lego            | 16           | lex                 | 9               |
|                 |              | lectvs              | 7               |
| tantvm          | 16           | tantvs              | 16              |
| pondo           | 15           | pes                 | 15              |
| qvantvs         | 14           | qvantvm             | 13              |
|                 |              | qvanto              | 1               |
| primvs          | 14           | primvm              | 11              |
|                 |              | primo               | 3               |
| mvlti           | 14           | mvltvs              | 14              |
| svvm            | 14           | svvs                | 14              |
| vervm           | 14           | vervs               | 12              |
|                 |              | vero                | 2               |
| anteqvam        | 13           | qvam                | 11              |
|                 |              | qvis                | 1               |
|                 |              | qvi                 | 1               |
| honestvm        | 13           | honestvs            | 13              |
| modvs           | 12           | modo                | 12              |
| ego             | 12           | mevs                | 10              |
|                 |              | min                 | 1               |
|                 |              | ne                  | 1               |
| solvs           | 11           | solvm               | 10              |
|                 |              | sol                 | 1               |
| refero          | 11           | refert              | 11              |
| eo              | 11           | is                  | 10              |
|                 |              | itvra               | 1               |
| svpervs         | 11           | svmma               | 7               |
|                 |              | svmmvm              | 3               |
|                 |              | svperi              | 1               |
| vis             | 11           | vir                 | 8               |
|                 |              | volo                | 3               |
| qva             | 10           | qvi                 | 6               |
|                 |              | qvis                | 4               |
| vervs           | 10           | vervm               | 8               |
|                 |              | vero                | 2               |
| volo            | 10           | volens              | 3               |
|                 |              | vis                 | 2               |
|                 |              | velvm               | 2               |
|                 |              | volvo               | 1               |
|                 |              | svm                 | 1               |
|                 |              | si                  | 1               |
| vtor            | 10           | vt                  | 9               |
|                 |              | vsvra               | 1               |
| vnvs            | 10           | vna                 | 10              |
| liber           | 10           | liberi              | 10              |
| romani          | 9            | romanvs             | 9               |
| plervsqve       | 9            | pleriqve            | 9               |
| qvantvm         | 9            | qvantvs             | 9               |
| tracta          | 9            | traho               | 9               |
| pavcvs          | 9            | pavci               | 9               |
| falsvm          | 9            | falsvs              | 9               |
| ne              | 9            | censeo              | 2               |
|                 |              | cereris             | 1               |
|                 |              | min                 | 1               |
|                 |              | nvllvs              | 1               |
|                 |              | ego                 | 1               |
|                 |              | hiccine             | 1               |
|                 |              | re                  | 1               |
|                 |              | spondeo             | 1               |
| reliqvi         | 8            | reliqvvs            | 8               |
| malvm           | 8            | malvs               | 7               |
|                 |              | malo                | 1               |
| perdo           | 8            | perditvs            | 8               |
| nascor          | 8            | natvs               | 8               |
| reliqvvm        | 8            | reliqvvs            | 7               |
|                 |              | relinqvo            | 1               |
| solvtvs         | 8            | solvo               | 8               |
| phoebvs         | 7            | phoebe              | 7               |
| pavci           | 7            | pavcvs              | 7               |
| mortvvs         | 7            | morior              | 7               |
| svmma           | 7            | svpervs             | 5               |
|                 |              | svmmvm              | 2               |
| sacer           | 7            | sacrvm              | 7               |
| privsqvam       | 7            | qvam                | 6               |
|                 |              | qvi                 | 1               |
| solitvs         | 7            | soleo               | 4               |
|                 |              | solitvm             | 3               |
| medivs          | 7            | medivm              | 7               |
| oenothea        | 7            | oenothevs           | 7               |
| consto          | 6            | consisto            | 6               |
| meritvs         | 6            | meritvm             | 3               |
|                 |              | mereor              | 3               |
| bene            | 6            | bonvs               | 6               |
| libra           | 6            | littera             | 6               |
| nocte           | 6            | nox                 | 6               |
| mali            | 6            | malvm               | 6               |
| nostri          | 6            | noster              | 6               |
| aer             | 6            | aes                 | 6               |
| pompeianvs      | 6            | pompeiani           | 6               |
| magnvs          | 6            | maiores             | 6               |
| secretvs        | 6            | secretvm            | 6               |
| altvs           | 6            | altvm               | 5               |
|                 |              | alte                | 1               |
| tvi             | 6            | tvvs                | 6               |
| insignis        | 6            | insigne             | 6               |
| dedo            | 6            | do                  | 4               |
|                 |              | deditvs             | 2               |
| polydamas       | 6            | polydamae           | 5               |
|                 |              | pvlydamas           | 1               |
| desertvs        | 5            | desero              | 5               |
| alica           | 5            | alicvs              | 4               |
|                 |              | halicvs             | 1               |
| testvm          | 5            | testor              | 3               |
|                 |              | testvs              | 2               |
| aperio          | 5            | apertvs             | 5               |
| egeo            | 5            | ago                 | 5               |
| svmmvm          | 5            | svpervs             | 5               |
| hic             | 5            | hac                 | 3               |
|                 |              | ne                  | 1               |
|                 |              | hiccine             | 1               |
| reliqvvs        | 5            | reliqvi             | 4               |
|                 |              | relinqvo            | 1               |
| honestvs        | 5            | honestvm            | 2               |
|                 |              | honestas            | 2               |
|                 |              | honeste             | 1               |
| scribo          | 5            | scriptvm            | 3               |
|                 |              | scriba              | 2               |
| viginti         | 5            | tres                | 2               |
|                 |              | qvinqve             | 2               |
|                 |              | sex                 | 1               |
| texo            | 5            | tego                | 3               |
|                 |              | textvm              | 2               |
| mevs            | 5            | ego                 | 5               |
| magnvm          | 5            | magnvs              | 5               |
| armatvs         | 5            | armati              | 3               |
|                 |              | armo                | 2               |
| tvvs            | 5            | tv                  | 5               |
| vna             | 5            | vnvs                | 5               |
| fervs           | 5            | fera                | 5               |
| alienvm         | 5            | alienvs             | 5               |
| serenvs         | 5            | serene              | 3               |
|                 |              | serenvm             | 2               |
| nymphon         | 5            | nympho              | 4               |
|                 |              | nymphona            | 1               |
| video           | 5            | visvs               | 3               |
|                 |              | visvm               | 1               |
|                 |              | ne                  | 1               |
| cvro            | 5            | cvra                | 5               |
| nvmqvis         | 5            | nvmqvid             | 5               |
| graecvs         | 5            | graeci              | 5               |
| hirnea          | 5            | hirnevs             | 3               |
|                 |              | irnea               | 1               |
|                 |              | irneo               | 1               |
| qvanto          | 5            | qvantvs             | 5               |
| sexcenti        | 5            | sescenti            | 5               |
| tantvs          | 5            | tantvm              | 5               |
| dvbivm          | 5            | dvbivs              | 5               |
| actvm           | 4            | ago                 | 4               |
| ago             | 4            | age                 | 3               |
|                 |              | actvm               | 1               |
| regivs          | 4            | regia               | 4               |
| rogvs           | 4            | rogo                | 4               |
| ora             | 4            | os                  | 4               |
| fvtvrvm         | 4            | fvtvrvs             | 3               |
|                 |              | svm                 | 1               |
| nox             | 4            | nocte               | 2               |
|                 |              | noctv               | 2               |
| pono            | 4            | pone                | 4               |
| decorvs         | 4            | decvs               | 4               |
| fvtvrvs         | 4            | svm                 | 4               |
| finitimvs       | 4            | finitimi            | 4               |
| brevis          | 4            | brevi               | 4               |
| cvrivs          | 4            | cvrvs               | 3               |
|                 |              | cvrio               | 1               |
| ah              | 4            | ab                  | 4               |
| mala            | 4            | malvs               | 4               |
| mei             | 4            | mevs                | 4               |
| propior         | 4            | proximvm            | 3               |
|                 |              | prope               | 1               |
| elorvs          | 4            | heli                | 3               |
|                 |              | helor               | 1               |
| adversvs        | 4            | adversvm            | 4               |
| antiqvvs        | 4            | antiqvi             | 3               |
|                 |              | antiqve             | 1               |
| antiqvi         | 4            | antiqvvs            | 4               |
| facilis         | 4            | facile              | 4               |
| sponte          | 4            | spons               | 4               |
| cavtvs          | 4            | caveo               | 4               |
| veteres         | 4            | vetvs               | 4               |
| picenvs         | 4            | picenvm             | 4               |
| pasco           | 4            | pascor              | 4               |
| pedes           | 4            | pes                 | 4               |
| novvs           | 4            | nosco               | 4               |
| compositvs      | 4            | compono             | 4               |
| falsvs          | 4            | falsvm              | 3               |
|                 |              | falso               | 1               |
| scriptvm        | 4            | scribo              | 2               |
|                 |              | scripta             | 2               |
| glycon          | 4            | glycvs              | 4               |
| cetera          | 4            | cetervs             | 4               |
| faesvlae        | 4            | faesvla             | 3               |
|                 |              | faesvlvs            | 1               |
| mando           | 4            | mandatvm            | 4               |
| alivs           | 4            | alias               | 3               |
|                 |              | alio                | 1               |
| ardeo           | 4            | ardens              | 4               |
| revs            | 4            | res                 | 4               |
| bellvs          | 4            | bellvm              | 4               |
| pendo           | 4            | pendeo              | 4               |
| apivm           | 4            | apivs               | 3               |
|                 |              | apis                | 1               |
| caelestes       | 4            | caelestis           | 2               |
|                 |              | caelestia           | 2               |
| catinvm         | 4            | catinvs             | 4               |
| fictvs          | 4            | fingo               | 4               |
| pvllo           | 4            | pvllvs              | 4               |
| orno            | 4            | ornatvs             | 4               |
| svllanvs        | 4            | syllanvs            | 4               |
| consvlto        | 4            | consvltvm           | 4               |
| pango           | 4            | pacio               | 3               |
|                 |              | paciscor            | 1               |
| orior           | 4            | oriens              | 4               |
| tv              | 4            | tvvs                | 3               |
|                 |              | ne                  | 1               |
| ivssvm          | 4            | ivbeo               | 4               |
| fera            | 4            | fervs               | 3               |
|                 |              | fero                | 1               |
| potissimvm      | 4            | potivs              | 4               |
| exter           | 4            | extremvm            | 3               |
|                 |              | extrema             | 1               |
| lino            | 4            | linio               | 2               |
|                 |              | lineo               | 1               |
|                 |              | levo                | 1               |
| fero            | 4            | fera                | 2               |
|                 |              | latvs               | 1               |
|                 |              | ferio               | 1               |
| dictvm          | 4            | dico                | 4               |
| medivm          | 4            | medivs              | 4               |
| veneo           | 4            | venio               | 4               |
| iaceo           | 4            | iacio               | 4               |
| victvs          | 4            | vinco               | 3               |
|                 |              | vivo                | 1               |
| placo           | 3            | placeo              | 3               |
| nvbo            | 3            | nvpta               | 3               |
| qviris          | 3            | qvirites            | 3               |
| incertvm        | 3            | incertvs            | 3               |
| certvm          | 3            | certvs              | 3               |
| profectvs       | 3            | proficiscor         | 3               |
| sino            | 3            | sine                | 3               |
| tener           | 3            | teneo               | 2               |
|                 |              | tenere              | 1               |
| praesentia      | 3            | praesens            | 3               |
| arcessitvs      | 3            | arcesso             | 3               |
| avvs            | 3            | avis                | 3               |
| rectvm          | 3            | rectvs              | 3               |
| xenon           | 3            | xenvs               | 3               |
| serivm          | 3            | serivs              | 3               |
| adversvm        | 3            | adversvs            | 3               |
| notvs           | 3            | nota                | 3               |
| spira           | 3            | spiro               | 3               |
| mereor          | 3            | meritvm             | 2               |
|                 |              | mereo               | 1               |
| vnvm            | 3            | vnvs                | 3               |
| triginta        | 3            | centvm              | 1               |
|                 |              | tricesimvs          | 1               |
|                 |              | trecenti            | 1               |
| doceo           | 3            | doctvs              | 3               |
| refert          | 3            | refero              | 3               |
| proximvm        | 3            | propior             | 3               |
| imvm            | 3            | infervs             | 3               |
| dvco            | 3            | dvcenti             | 2               |
|                 |              | dvx                 | 1               |
| opvs            | 3            | opera               | 3               |
| lavs            | 3            | lavdo               | 3               |
| phrygivs        | 3            | phrygia             | 3               |
| sol             | 3            | soleo               | 1               |
|                 |              | solvs               | 1               |
|                 |              | solvm               | 1               |
| prehenso        | 3            | prehendo            | 1               |
|                 |              | prehens             | 1               |
|                 |              | preheno             | 1               |
| illo            | 3            | ille                | 3               |
| exentero        | 3            | exintero            | 3               |
| strobilvs       | 3            | strobilis           | 3               |
| sicvlvs         | 3            | sicvli              | 3               |
| latvs           | 3            | fero                | 3               |
| convictvs       | 3            | convinco            | 3               |
| coeptvm         | 3            | coepio              | 3               |
| vniversi        | 3            | vniversvs           | 3               |
| dvodeviginti    | 3            | septendecim         | 1               |
|                 |              | tres                | 1               |
|                 |              | qvadraginta         | 1               |
| debitvm         | 3            | debeo               | 3               |
| mervs           | 3            | mervm               | 3               |
| navigans        | 3            | navigo              | 3               |
| ivro            | 3            | ivs                 | 2               |
|                 |              | ivratvs             | 1               |
| captiva         | 3            | captivvs            | 3               |
| satis           | 3            | ne                  | 2               |
|                 |              | sero                | 1               |
| praeparatvs     | 3            | praeparo            | 3               |
| qvisqve         | 3            | qvoqve              | 2               |
|                 |              | qvisqvis            | 1               |
| pario           | 3            | partvs              | 2               |
|                 |              | pars                | 1               |
| hvc             | 3            | hic                 | 3               |
| sthenivs        | 3            | sthenvs             | 3               |
| fraces          | 3            | frax                | 3               |
| nonae           | 3            | nonvs               | 3               |
| asto            | 3            | assisto             | 3               |
| sestertivm      | 3            | sestertivs          | 2               |
|                 |              | hic                 | 1               |
| artvs           | 3            | ars                 | 2               |
|                 |              | arte                | 1               |
| vanvm           | 3            | vanvs               | 3               |
| perpetvvs       | 3            | perpetvo            | 3               |
| bacchis         | 3            | bacchvs             | 2               |
|                 |              | baccha              | 1               |
| acceptvs        | 3            | accipio             | 3               |
| caivs           | 3            | caio                | 2               |
|                 |              | cavs                | 1               |
| viso            | 3            | video               | 3               |
| evge            | 3            | evgeo               | 3               |
| editvs          | 3            | edo                 | 3               |
| em              | 3            | hem                 | 3               |
| vniversvs       | 3            | vniversi            | 3               |
| acta            | 3            | ago                 | 2               |
|                 |              | actvm               | 1               |
| vlterior        | 3            | vltra               | 2               |
|                 |              | vlteriora           | 1               |
| canvs           | 3            | cano                | 2               |
|                 |              | canis               | 1               |
| intentvs        | 3            | intendo             | 3               |
| trecenti        | 3            | tricenti            | 1               |
|                 |              | qvadranta           | 1               |
|                 |              | trecentivm          | 1               |
| qvisnam         | 3            | qvis                | 2               |
|                 |              | qvonam              | 1               |
| solvm           | 3            | solvs               | 3               |
| commis          | 3            | cvmmim              | 3               |
| cognitvs        | 3            | cognosco            | 3               |
| apertvs         | 3            | aperio              | 3               |
| incertvs        | 3            | incertvm            | 3               |
| laevvm          | 3            | laevvs              | 2               |
|                 |              | laeva               | 1               |
| baetica         | 3            | baeticvs            | 3               |
| volens          | 3            | volo                | 3               |
| rego            | 3            | rex                 | 3               |
| bonvm           | 3            | bonvs               | 2               |
|                 |              | boni                | 1               |
| svrripio        | 3            | svbripio            | 2               |
|                 |              | svbrvpio            | 1               |
| incipio         | 3            | inceptvm            | 3               |
| pinarvs         | 3            | pinae               | 2               |
|                 |              | pinarivs            | 1               |
| conivngo        | 3            | conivnctvs          | 3               |
| arte            | 3            | ars                 | 3               |
| sextarivs       | 3            | semis               | 2               |
|                 |              | salvs               | 1               |
| ample           | 3            | amplvs              | 3               |
| gallvs          | 3            | galli               | 3               |
| altvm           | 3            | altvs               | 3               |
| bomilcar        | 3            | bomilcaris          | 2               |
|                 |              | bomilcare           | 1               |
| minimvm         | 3            | parvvs              | 3               |
| nosco           | 3            | notvs               | 2               |
|                 |              | ne                  | 1               |
| comitivm        | 3            | comitia             | 3               |
| baltevs         | 3            | baltevm             | 3               |
| edo             | 3            | svm                 | 2               |
|                 |              | editvs              | 1               |
| exanimis        | 3            | exanimvs            | 3               |
| vrbane          | 3            | vrbanvs             | 3               |
| anser           | 3            | ansero              | 2               |
|                 |              | anseres             | 1               |
| ferio           | 3            | fervs               | 3               |
| sacratvs        | 3            | sacro               | 2               |
|                 |              | sacer               | 1               |
| dicto           | 3            | dictvm              | 2               |
|                 |              | dico                | 1               |
| mille           | 3            | qvadraginta         | 2               |
|                 |              | triginta            | 1               |
| veto            | 3            | vetvo               | 1               |
|                 |              | votvm               | 1               |
|                 |              | vetemvs             | 1               |
| hesperivs       | 2            | hesperia            | 2               |
| lvdificor       | 2            | lvdifico            | 2               |
| amplector       | 2            | amplexvs            | 2               |
| thessali        | 2            | thessalvs           | 2               |
| pvgnvs          | 2            | pvgna               | 2               |
| cadvs           | 2            | cado                | 2               |
| vt              | 2            | vtor                | 2               |
| ortvs           | 2            | orior               | 2               |
| svfflo          | 2            | svffla              | 1               |
|                 |              | svfflasco           | 1               |
| hippias         | 2            | hippia              | 2               |
| sterno          | 2            | stratvm             | 2               |
| constratvs      | 2            | consterno           | 2               |
| magnanimvs      | 2            | magnanime           | 1               |
|                 |              | magnanio            | 1               |
| visvs           | 2            | video               | 2               |
| efficio         | 2            | effectvs            | 2               |
| avdaciter       | 2            | avdax               | 2               |
| blatio          | 2            | blatvm              | 2               |
| coqvo           | 2            | coqo                | 1               |
|                 |              | coco                | 1               |
| expressvs       | 2            | exprimo             | 2               |
| manes           | 2            | manvs               | 2               |
| libita          | 2            | libet               | 2               |
| alternvs        | 2            | alternis            | 2               |
| vos             | 2            | vester              | 2               |
| hospitivm       | 2            | hospes              | 2               |
| velvm           | 2            | volo                | 2               |
| fvlgens         | 2            | fvlgeo              | 2               |
| fortvita        | 2            | fortvitvs           | 2               |
| marsyas         | 2            | marsya              | 2               |
| exqviro         | 2            | exqvisitvs          | 2               |
| desertvm        | 2            | desero              | 1               |
|                 |              | deserta             | 1               |
| planvm          | 2            | planvs              | 2               |
| cito            | 2            | citatvs             | 1               |
|                 |              | cieo                | 1               |
| avris           | 2            | avra                | 2               |
| profvndo        | 2            | profvsvs            | 2               |
| prodeo          | 2            | prodo               | 2               |
| insvo           | 2            | insvtvs             | 1               |
|                 |              | insvm               | 1               |
| inanis          | 2            | inane               | 2               |
| caneo           | 2            | cano                | 2               |
| tantvmdem       | 2            | tantvsdem           | 1               |
|                 |              | tantidem            | 1               |
| dico            | 2            | dictvra             | 1               |
|                 |              | dictvm              | 1               |
| vacca           | 2            | vaga                | 1               |
|                 |              | vagvs               | 1               |
| improvisvs      | 2            | improvisvm          | 2               |
| ea              | 2            | is                  | 2               |
| praesens        | 2            | praesentia          | 1               |
|                 |              | praesvm             | 1               |
| como            | 2            | comptvs             | 1               |
|                 |              | compo               | 1               |
| alias           | 2            | alivs               | 2               |
| avla            | 2            | olla                | 2               |
| qvatvordecim    | 2            | decimvs             | 1               |
|                 |              | dvodecim            | 1               |
| praeceptor      | 2            | praeceptvm          | 2               |
| paveo           | 2            | pasco               | 2               |
| mvnitvs         | 2            | mvnio               | 2               |
| erigo           | 2            | erectvs             | 2               |
| occvltvm        | 2            | occvltvs            | 2               |
| plvvivs         | 2            | plvvia              | 2               |
| parcvs          | 2            | parco               | 1               |
|                 |              | parce               | 1               |
| dives           | 2            | ditia               | 1               |
|                 |              | divvs               | 1               |
| contexo         | 2            | contextvs           | 2               |
| calcar          | 2            | calcarivm           | 1               |
|                 |              | calco               | 1               |
| svbrepo         | 2            | svrrepio            | 2               |
| tvrbo           | 2            | tvrbatvs            | 2               |
| patrivs         | 2            | patria              | 2               |
| sardes          | 2            | sardi               | 2               |
| fvsvs           | 2            | fvndo               | 2               |
| cadmeivs        | 2            | cadmevs             | 2               |
| confinivm       | 2            | confinis            | 2               |
| tarpezita       | 2            | trapezita           | 2               |
| consvlo         | 2            | consvltvm           | 1               |
|                 |              | consvl              | 1               |
| consvl          | 2            | consvlo             | 2               |
| gortynivs       | 2            | cortynivs           | 2               |
| pecco           | 2            | peccans             | 2               |
| mvrgantinvs     | 2            | mvrgentinvs         | 2               |
| eligo           | 2            | electvs             | 1               |
|                 |              | elego               | 1               |
| stilbon         | 2            | stilbo              | 2               |
| testv           | 2            | testvs              | 2               |
| nimivs          | 2            | nimivm              | 2               |
| praeficio       | 2            | praefectvs          | 2               |
| dvrvm           | 2            | dvrvs               | 2               |
| italvs          | 2            | itali               | 2               |
| palleo          | 2            | pallens             | 2               |
| opera           | 2            | opvs                | 2               |
| vipstanvs       | 2            | vipsanvs            | 2               |
| immensvs        | 2            | immensvm            | 2               |
| laxvs           | 2            | laxe                | 2               |
| affectvs        | 2            | afficio             | 2               |
| sanctvs         | 2            | sancte              | 2               |
| insto           | 2            | insisto             | 1               |
|                 |              | instans             | 1               |
| scriba          | 2            | scribo              | 2               |
| psecas          | 2            | psecae              | 2               |
| mamilla         | 2            | mamillvs            | 2               |
| heracleon       | 2            | heraclevs           | 2               |
| sibylla         | 2            | sibvlla             | 2               |
| qvindecimviri   | 2            | qvindecimvireivm    | 1               |
|                 |              | qvindecimvir        | 1               |
| natis           | 2            | natvs               | 2               |
| myoparon        | 2            | myoparvs            | 2               |
| totvm           | 2            | totvs               | 2               |
| isto            | 2            | iste                | 2               |
| vomo            | 2            | vomens              | 1               |
|                 |              | vomer               | 1               |
| vereor          | 2            | verens              | 1               |
|                 |              | verendvs            | 1               |
| senior          | 2            | senex               | 2               |
| aveo            | 2            | havd                | 1               |
|                 |              | haveo               | 1               |
| volvcris        | 2            | volvcer             | 2               |
| colo            | 2            | cvltvs              | 2               |
| remotvs         | 2            | removeo             | 2               |
| ivs             | 2            | ivre                | 2               |
| vaccenses       | 2            | vagenses            | 2               |
| rapax           | 2            | rapaciter           | 1               |
|                 |              | rapaces             | 1               |
| directvs        | 2            | dirigo              | 2               |
| paratvs         | 2            | paro                | 2               |
| effvndo         | 2            | effvsvs             | 2               |
| tvrbatvs        | 2            | tvrbo               | 2               |
| svbicio         | 2            | svbiectvs           | 2               |
| qvantvlvm       | 2            | qvantvlvs           | 2               |
| modo            | 2            | modvs               | 2               |
| alo             | 2            | alar                | 1               |
|                 |              | ala                 | 1               |
| seqvens         | 2            | seqvor              | 2               |
| primvm          | 2            | primvs              | 2               |
| ibis            | 2            | ibides              | 1               |
|                 |              | ibidvs              | 1               |
| cloelia         | 2            | cloelivs            | 2               |
| svbvrbanvm      | 2            | svbvrbanvs          | 2               |
| prospera        | 2            | prosper             | 2               |
| commodvs        | 2            | commodvm            | 2               |
| extremvm        | 2            | exter               | 2               |
| extentvs        | 2            | extendo             | 2               |
| pertvrbo        | 2            | pertvrbatvs         | 2               |
| odoro           | 2            | odoratvs            | 2               |
| assyrivs        | 2            | assyria             | 2               |
| peiero          | 2            | peievs              | 1               |
|                 |              | peieratvs           | 1               |
| congrio         | 2            | congrion            | 2               |
| scelerati       | 2            | sceleratvs          | 2               |
| clavdiopolitani | 2            | clavdioponi         | 1               |
|                 |              | clavdioponvs        | 1               |
| nimio           | 2            | nimivs              | 2               |
| dexter          | 2            | dextera             | 2               |
| odiose          | 2            | odiosvs             | 2               |
| avdens          | 2            | avdenter            | 1               |
|                 |              | avdentia            | 1               |
| ministra        | 2            | minister            | 2               |
| pressvs         | 2            | premo               | 2               |
| svccingo        | 2            | svbcingo            | 2               |
| servo           | 2            | servvs              | 2               |
| presse          | 2            | pressvs             | 2               |
| diligo          | 2            | dilectvs            | 1               |
|                 |              | diligens            | 1               |
| egero           | 2            | ago                 | 2               |
| terni           | 2            | ternvs              | 2               |
| serrana         | 2            | serranvs            | 2               |
| macedonicvs     | 2            | macedonica          | 2               |
| praetento       | 2            | praetempto          | 2               |
| romanvs         | 2            | romani              | 2               |
| svcinvm         | 2            | svcinvs             | 2               |
| iecvr           | 2            | iecvs               | 2               |
| sollemnis       | 2            | sollemne            | 2               |
| delphinvs       | 2            | delphina            | 1               |
|                 |              | delphin             | 1               |
| caecilivs       | 2            | caecilia            | 2               |
| singvla         | 2            | singvlvs            | 2               |
| verso           | 2            | versor              | 2               |
| cadvcvm         | 2            | cadvcvs             | 2               |
| abiectvs        | 2            | abicio              | 2               |
| certo           | 2            | certvs              | 2               |
| fenerator       | 2            | feneratvs           | 2               |
| praesvm         | 2            | praesens            | 2               |
| decor           | 2            | decvs               | 2               |
| vsvs            | 2            | vtor                | 2               |
| propono         | 2            | propositvm          | 2               |
| commvne         | 2            | commvnis            | 2               |
| appositvs       | 2            | appono              | 2               |
| brvttivs        | 2            | brvttia             | 2               |
| legatvm         | 2            | legatvs             | 2               |
| percvnctor      | 2            | percontor           | 2               |
| qvinqvaginta    | 2            | qvinqve             | 1               |
|                 |              | centvm              | 1               |
| primo           | 2            | primvs              | 2               |
| lavo            | 2            | loqvor              | 1               |
|                 |              | lotvs               | 1               |
| gypso           | 2            | gypsatvs            | 2               |
| malo            | 2            | malvm               | 2               |
| idem            | 2            | eodem               | 2               |
| tremebvndvs     | 2            | tremibvndvs         | 2               |
| pilevm          | 2            | pilevs              | 2               |
| fretvs          | 2            | fretvm              | 2               |
| servvs          | 2            | servo               | 2               |
| vltimvm         | 2            | vltimvs             | 2               |
| naevolvs        | 2            | naevole             | 2               |
| gener           | 2            | genvs               | 2               |
| fido            | 2            | fidens              | 2               |
| irascor         | 2            | iratvs              | 2               |
| breviter        | 2            | brevis              | 2               |
| vivo            | 2            | vinco               | 1               |
|                 |              | vivvs               | 1               |
| refvgvs         | 2            | refvgio             | 2               |
| mane            | 2            | maneo               | 2               |
| meto            | 2            | metior              | 1               |
|                 |              | metor               | 1               |
| ramenta         | 2            | ramentvm            | 2               |
| svesco          | 2            | svetvs              | 2               |
| svspensvs       | 2            | svspendo            | 2               |
| gravo           | 2            | gravor              | 2               |
| satvr           | 2            | sero                | 2               |
| inflo           | 2            | inflatvs            | 2               |
| macro           | 2            | macer               | 2               |
| actvs           | 2            | ago                 | 2               |
| apvlvs          | 2            | apvla               | 2               |
| proiectvs       | 2            | proicio             | 2               |
| lavrevs         | 2            | lavrea              | 2               |
| nessvs          | 2            | nessivs             | 2               |
| isti            | 2            | iste                | 2               |
| primoris        | 2            | primores            | 2               |
| promissvm       | 2            | promitto            | 2               |
| respvblica      | 2            | res                 | 2               |
| praescriptvm    | 2            | praescribo          | 2               |
| vigilans        | 2            | vigilo              | 2               |
| sempronia       | 2            | sempronivs          | 2               |
| svevvs          | 2            | svevi               | 1               |
|                 |              | svevivs             | 1               |
| proprivm        | 2            | proprivs            | 2               |
| propivs         | 2            | prope               | 2               |
| britannicvs     | 2            | britannica          | 2               |
| placitvs        | 2            | placeo              | 2               |
| externi         | 2            | externvs            | 2               |
| antiphanes      | 2            | antiphanvs          | 2               |
| percoqvo        | 2            | percoco             | 1               |
|                 |              | percoqvor           | 1               |
| vetera          | 2            | vetvs               | 2               |
| habeo           | 2            | habitvs             | 2               |
| interiacio      | 2            | intericio           | 2               |
| saeptvm         | 2            | saepio              | 2               |
| ico             | 2            | ictvs               | 2               |
| troivs          | 2            | troia               | 2               |
| pareo           | 2            | parreo              | 2               |
| venia           | 2            | venio               | 2               |
| pilvs           | 2            | pilvm               | 2               |
| advatici        | 2            | advaticvs           | 2               |
| erectvs         | 2            | erigo               | 2               |
| albvm           | 2            | albvs               | 2               |
| lvpinvm         | 2            | lvpinvs             | 2               |
| ivdico          | 2            | ivdex               | 2               |
| defetiscor      | 2            | defessvs            | 2               |
| volvo           | 2            | volo                | 2               |
| scio            | 2            | sciens              | 1               |
|                 |              | scisco              | 1               |
| ingemisco       | 2            | ingemesco           | 1               |
|                 |              | ingemo              | 1               |
| flvctvo         | 2            | flvctvor            | 2               |
| victor          | 2            | vinco               | 2               |
| nos             | 2            | noster              | 2               |
| conor           | 2            | conatvra            | 1               |
|                 |              | conatvs             | 1               |
| pvllvm          | 2            | pvllvs              | 2               |
| ramale          | 2            | ramalis             | 1               |
|                 |              | ramalia             | 1               |
| mvlto           | 2            | mvltvs              | 2               |
| spernendvs      | 2            | sperno              | 2               |
| vervtvm         | 2            | vervtvs             | 2               |
| cydas           | 2            | cyda                | 2               |
| viridans        | 2            | virido              | 2               |
| servs           | 2            | sero                | 1               |
|                 |              | sera                | 1               |
| callistvs       | 2            | callistivs          | 1               |
|                 |              | callistestvs        | 1               |
| ivre            | 2            | ivs                 | 2               |
| danavs          | 2            | danai               | 2               |
| arcas           | 2            | arcades             | 2               |
| poeas           | 2            | poeans              | 2               |
| troianvs        | 2            | troiani             | 2               |
| vltimvs         | 2            | vltimvm             | 2               |
| hervs           | 2            | svm                 | 2               |
| docte           | 2            | doctvs              | 2               |
| bosporvs        | 2            | bosphorvs           | 2               |
| votvm           | 2            | voveo               | 2               |
| hvmanvs         | 2            | hvmana              | 2               |
| properans       | 2            | propero             | 2               |
| latinvs         | 2            | latini              | 2               |
| intersaepio     | 2            | interspipio         | 2               |
| trinacria       | 2            | trinacrivs          | 2               |
| defectvs        | 2            | deficio             | 2               |
| tempero         | 2            | temperatvs          | 2               |
| philoxenvs      | 2            | philoxenes          | 1               |
|                 |              | philoxene           | 1               |
| profvndvs       | 2            | profvndvm           | 2               |
| comis           | 2            | coma                | 2               |
| potis           | 2            | potivs              | 2               |
| devotvs         | 2            | devoveo             | 2               |
| vlpicvm         | 2            | vlpex               | 2               |
| vvlva           | 2            | vvlvae              | 2               |
| vter            | 2            | vtrvm               | 2               |
| impendo         | 2            | impensvs            | 1               |
|                 |              | impendeo            | 1               |
| helena          | 2            | helene              | 2               |
| amo             | 2            | amans               | 2               |
| falernvm        | 2            | falernivs           | 1               |
|                 |              | falernvs            | 1               |
| mensa           | 2            | mensis              | 2               |
| dvodeni         | 2            | dvodenvs            | 2               |
| promitto        | 2            | promissvm           | 2               |
| amaryllis       | 2            | amaryllvs           | 2               |
| dvctvs          | 2            | dvco                | 2               |
| centvm          | 2            | triginta            | 1               |
|                 |              | claber              | 1               |
| irritvm         | 2            | irritvs             | 2               |
| corydon         | 2            | corydvs             | 2               |
| aro             | 2            | ares                | 2               |
| vngven          | 2            | vngvis              | 2               |
| frvstro         | 2            | frvstror            | 2               |
| vehemens        | 2            | vehementer          | 2               |
| tvvm            | 2            | tvvs                | 2               |
| qvietvs         | 2            | qvies               | 2               |
| magis           | 2            | magnvs              | 2               |
| circvmcisvs     | 2            | circvmcido          | 2               |
| insido          | 2            | insideo             | 2               |
| loqvo           | 2            | loqvor              | 2               |
| tarracinensis   | 2            | terracinensis       | 2               |
| cvbo            | 2            | cvbitvm             | 1               |
|                 |              | cvbeo               | 1               |
| effvsvs         | 2            | effvndo             | 2               |
| hylas           | 2            | hyla                | 2               |
| svperior        | 2            | svpervs             | 2               |
| aeqvimaelivm    | 1            | aeqvimaelvs         | 1               |
| arqvatvs        | 1            | arcvo               | 1               |
| pvlmo           | 1            | pvlmvs              | 1               |
| regia           | 1            | regivs              | 1               |
| postvlo         | 1            | postvlatvm          | 1               |
| aliorsvm        | 1            | aliovorsvm          | 1               |
| destinatvs      | 1            | destino             | 1               |
| davnivs         | 1            | davnia              | 1               |
| svblica         | 1            | svblicivm           | 1               |
| parco           | 1            | parce               | 1               |
| ivvo            | 1            | ivtvm               | 1               |
| qvinqvatrvs     | 1            | qvinqvatrvvs        | 1               |
| vive            | 1            | vivo                | 1               |
| hiccine         | 1            | ne                  | 1               |
| qvisqvis        | 1            | qvaqva              | 1               |
| inficio         | 1            | infectvs            | 1               |
| andromache      | 1            | andromacha          | 1               |
| dinomache       | 1            | dinomaches          | 1               |
| redoleo         | 1            | redolens            | 1               |
| intimvs         | 1            | interior            | 1               |
| vectigalis      | 1            | vectigal            | 1               |
| vrgeo           | 1            | vrgvo               | 1               |
| eadem           | 1            | idem                | 1               |
| nerevs          | 1            | nerea               | 1               |
| graecvli        | 1            | graecvlvs           | 1               |
| gangaba         | 1            | gango               | 1               |
| pvls            | 1            | pvltis              | 1               |
| insipio         | 1            | insipito            | 1               |
| mvtvo           | 1            | mvtvvs              | 1               |
| dissolvtvs      | 1            | dissolvo            | 1               |
| aridvs          | 1            | ardvs               | 1               |
| recondo         | 1            | reconditvs          | 1               |
| derelinqvo      | 1            | derelictvs          | 1               |
| eloqvor         | 1            | eloco               | 1               |
| exigvvm         | 1            | exigvvs             | 1               |
| hei             | 1            | ei                  | 1               |
| doctvs          | 1            | doceo               | 1               |
| sabaevs         | 1            | sabaei              | 1               |
| argvtia         | 1            | argvtivm            | 1               |
| depso           | 1            | depsvo              | 1               |
| circvmtergeo    | 1            | circvmtergo         | 1               |
| infra           | 1            | infervs             | 1               |
| afflvo          | 1            | afflvens            | 1               |
| angvstvm        | 1            | angvstvs            | 1               |
| perlego         | 1            | pellega             | 1               |
| vnocvlvs        | 1            | vnocvle             | 1               |
| navale          | 1            | navalis             | 1               |
| intervias       | 1            | intervia            | 1               |
| profestvs       | 1            | profesto            | 1               |
| grates          | 1            | gratis              | 1               |
| galli           | 1            | gallvs              | 1               |
| beo             | 1            | bearis              | 1               |
| nota            | 1            | notvs               | 1               |
| vinco           | 1            | vincio              | 1               |
| memoro          | 1            | memor               | 1               |
| iapydia         | 1            | iapydivs            | 1               |
| pylivs          | 1            | pylia               | 1               |
| thrasyllvs      | 1            | thrasyllivs         | 1               |
| destino         | 1            | destinatvm          | 1               |
| concvrsvs       | 1            | concvrro            | 1               |
| felicio         | 1            | felicivs            | 1               |
| sigillaria      | 1            | sigillarivs         | 1               |
| lacones         | 1            | lacon               | 1               |
| porcinvm        | 1            | poricinvs           | 1               |
| melicertes      | 1            | melicerta           | 1               |
| calvvs          | 1            | calvis              | 1               |
| propendeo       | 1            | propensvs           | 1               |
| delvmbis        | 1            | delvmbo             | 1               |
| demordeo        | 1            | demorqveo           | 1               |
| ocvlissimvs     | 1            | ocvlvs              | 1               |
| vibex           | 1            | vibice              | 1               |
| flagello        | 1            | flagella            | 1               |
| secretvm        | 1            | secretvs            | 1               |
| cani            | 1            | canis               | 1               |
| odyssea         | 1            | odyssevs            | 1               |
| accommodo       | 1            | accomodvs           | 1               |
| natalis         | 1            | natales             | 1               |
| svbblandior     | 1            | svbblandibo         | 1               |
| emineo          | 1            | eminens             | 1               |
| conservvs       | 1            | consero             | 1               |
| barba           | 1            | barbas              | 1               |
| barbativs       | 1            | barbatii            | 1               |
| detero          | 1            | detereo             | 1               |
| competitor      | 1            | competitvs          | 1               |
| cycnvs          | 1            | cycna               | 1               |
| verisimilitvdo  | 1            | verisimilvdo        | 1               |
| animosvs        | 1            | animose             | 1               |
| avis            | 1            | avvs                | 1               |
| fvrens          | 1            | fvro                | 1               |
| amedines        | 1            | amedine             | 1               |
| plavtivs        | 1            | plavtia             | 1               |
| freni           | 1            | frenvm              | 1               |
| natvs           | 1            | nascor              | 1               |
| complexvs       | 1            | complector          | 1               |
| arcanvm         | 1            | arcanvs             | 1               |
| pacvvivs        | 1            | pacvvivm            | 1               |
| inqvinatvs      | 1            | inqvino             | 1               |
| svbeo           | 1            | svbite              | 1               |
| amylvm          | 1            | amvlvs              | 1               |
| exvrgeo         | 1            | exsvrgo             | 1               |
| alienvs         | 1            | alienvm             | 1               |
| innecto         | 1            | inneco              | 1               |
| progne          | 1            | procnes             | 1               |
| svspicio        | 1            | svspectvs           | 1               |
| salvtaris       | 1            | salvto              | 1               |
| beneficvs       | 1            | beneficivm          | 1               |
| feneror         | 1            | fenero              | 1               |
| nonarivs        | 1            | nonarivm            | 1               |
| desperatvs      | 1            | despero             | 1               |
| bombvs          | 1            | bomba               | 1               |
| bassaris        | 1            | bassar              | 1               |
| flecto          | 1            | flexvra             | 1               |
| evhivs          | 1            | evhion              | 1               |
| echo            | 1            | echvs               | 1               |
| sex             | 1            | tricesimvs          | 1               |
| dvo             | 1            | triginta            | 1               |
| lvcvs           | 1            | lvx                 | 1               |
| convestio       | 1            | convestitvs         | 1               |
| praestino       | 1            | praestineo          | 1               |
| fenebris        | 1            | feneber             | 1               |
| inhvmane        | 1            | inhvmanvs           | 1               |
| cretes          | 1            | cretae              | 1               |
| perprimo        | 1            | perpremo            | 1               |
| infectvs        | 1            | inficio             | 1               |
| parapanisvs     | 1            | parapanis           | 1               |
| soleo           | 1            | solea               | 1               |
| servm           | 1            | sero                | 1               |
| contineo        | 1            | continens           | 1               |
| obiecto         | 1            | obicio              | 1               |
| liceor          | 1            | licet               | 1               |
| svbdolvs        | 1            | svbdole             | 1               |
| hvccine         | 1            | hiccine             | 1               |
| detrvdo         | 1            | detrvo              | 1               |
| ravis           | 1            | ravvs               | 1               |
| perrhaebvs      | 1            | perrhaebes          | 1               |
| mavors          | 1            | marsertis           | 1               |
| instrvctvs      | 1            | instrvo             | 1               |
| imbvo           | 1            | imbvtvs             | 1               |
| nave            | 1            | navis               | 1               |
| fallo           | 1            | falsvs              | 1               |
| pollicitor      | 1            | pollicito           | 1               |
| tonstrinvs      | 1            | tonstrenvs          | 1               |
| serpo           | 1            | serpens             | 1               |
| ecqvis          | 1            | ecqvid              | 1               |
| legens          | 1            | lego                | 1               |
| idalivs         | 1            | idalia              | 1               |
| propositvm      | 1            | propono             | 1               |
| disicio         | 1            | dissico             | 1               |
| vipsanivs       | 1            | vipsanvs            | 1               |
| coalesco        | 1            | coalo               | 1               |
| svbmano         | 1            | svbmanvs            | 1               |
| gnosis          | 1            | cnosivs             | 1               |
| qvilibet        | 1            | qviliber            | 1               |
| svblime         | 1            | svblimis            | 1               |
| septemplex      | 1            | septempix           | 1               |
| attondeo        | 1            | attondo             | 1               |
| pavsanias       | 1            | pavsania            | 1               |
| desertor        | 1            | desertvs            | 1               |
| transscribo     | 1            | transcribo          | 1               |
| venerevs        | 1            | venerivs            | 1               |
| biennivm        | 1            | biennvs             | 1               |
| imperatvm       | 1            | impero              | 1               |
| tredecim        | 1            | tredex              | 1               |
| profvgio        | 1            | profvgvs            | 1               |
| volaginivs      | 1            | vvlaginivs          | 1               |
| orbvs           | 1            | orbis               | 1               |
| cometes         | 1            | cometen             | 1               |
| moveo           | 1            | motvs               | 1               |
| tactvs          | 1            | tango               | 1               |
| latens          | 1            | lateo               | 1               |
| plavdo          | 1            | plodo               | 1               |
| calydonivs      | 1            | calydonia           | 1               |
| mereo           | 1            | mereor              | 1               |
| liberi          | 1            | liber               | 1               |
| sicine          | 1            | ne                  | 1               |
| hera            | 1            | svm                 | 1               |
| profano         | 1            | profanvs            | 1               |
| tela            | 1            | telvm               | 1               |
| manvs           | 1            | mane                | 1               |
| genivs          | 1            | genvs               | 1               |
| gravor          | 1            | gravo               | 1               |
| vigens          | 1            | vigeo               | 1               |
| alvta           | 1            | alvo                | 1               |
| hellespontiacvs | 1            | hellespontiacvm     | 1               |
| sedeo           | 1            | sedes               | 1               |
| iactatvs        | 1            | iacto               | 1               |
| dissipo         | 1            | dissipio            | 1               |
| integer         | 1            | integrvs            | 1               |
| poeantivs       | 1            | poeans              | 1               |
| decresco        | 1            | decretvm            | 1               |
| imacharensis    | 1            | imacharenses        | 1               |
| balbvs          | 1            | balbe               | 1               |
| selectvs        | 1            | seligo              | 1               |
| antiqvvm        | 1            | antiqvvs            | 1               |
| chaos           | 1            | chao                | 1               |
| pvgna           | 1            | pvgnvs              | 1               |
| clare           | 1            | clarvs              | 1               |
| sorbvm          | 1            | sorbvs              | 1               |
| hospita         | 1            | hospitvs            | 1               |
| barbarvs        | 1            | barbare             | 1               |
| arefacio        | 1            | arfacio             | 1               |
| contremo        | 1            | contremisco         | 1               |
| ivrgivm         | 1            | ivrgvm              | 1               |
| cardo           | 1            | cardinvs            | 1               |
| repvgnantia     | 1            | repvgno             | 1               |
| svscipio        | 1            | svccipio            | 1               |
| ventilo         | 1            | ventilor            | 1               |
| atii            | 1            | ativs               | 1               |
| sardonyx        | 1            | sardonyches         | 1               |
| qvatio          | 1            | qvatvs              | 1               |
| angvinvs        | 1            | angvina             | 1               |
| cvminvm         | 1            | cvmen               | 1               |
| chiragra        | 1            | cheragra            | 1               |
| gorgias         | 1            | gorgia              | 1               |
| lyrica          | 1            | lyricvs             | 1               |
| concinno        | 1            | concinna            | 1               |
| dissolvo        | 1            | dissolvtvs          | 1               |
| decondo         | 1            | decondeo            | 1               |
| emaceratvs      | 1            | emacero             | 1               |
| retineo         | 1            | retinens            | 1               |
| echecratides    | 1            | echecratis          | 1               |
| nvmerosvs       | 1            | nvmerose            | 1               |
| sparsvs         | 1            | spargo              | 1               |
| nimivm          | 1            | nimivs              | 1               |
| deserta         | 1            | desero              | 1               |
| arretivm        | 1            | arretivs            | 1               |
| reprehensio     | 1            | reprensio           | 1               |
| emendo          | 1            | emendatvs           | 1               |
| emacitas        | 1            | emacito             | 1               |
| virdivs         | 1            | virder              | 1               |
| illyricvs       | 1            | illyricvm           | 1               |
| lvdvs           | 1            | lvdo                | 1               |
| argynnvs        | 1            | argynnis            | 1               |
| parthvs         | 1            | parthi              | 1               |
| olens           | 1            | oleo                | 1               |
| motivncvla      | 1            | motivncvlvs         | 1               |
| tavrea          | 1            | tavrevs             | 1               |
| bvrdvbasta      | 1            | bvrdvba             | 1               |
| opto            | 1            | optatvs             | 1               |
| afflictvs       | 1            | affligo             | 1               |
| ambigo          | 1            | ambigivm            | 1               |
| torqvis         | 1            | torqveo             | 1               |
| svmo            | 1            | svmptvs             | 1               |
| palladivs       | 1            | palladia            | 1               |
| vniversvm       | 1            | vniversvs           | 1               |
| saperda         | 1            | saperdo             | 1               |
| castorevm       | 1            | castorevs           | 1               |
| stvppa          | 1            | stvppo              | 1               |
| ebenvs          | 1            | hebenvs             | 1               |
| plantaris       | 1            | plantarivm          | 1               |
| tetre           | 1            | taetere             | 1               |
| pergamvs        | 1            | pergamvm            | 1               |
| cynthivs        | 1            | cynthia             | 1               |
| confessvs       | 1            | confiteor           | 1               |
| caesarea        | 1            | caesarevs           | 1               |
| phrixvs         | 1            | phrixon             | 1               |
| ino             | 1            | inois               | 1               |
| caecvbvm        | 1            | caecvba             | 1               |
| atizyes         | 1            | atizyevs            | 1               |
| vascvlvm        | 1            | vascvla             | 1               |
| penetralis      | 1            | penetrale           | 1               |
| perses          | 1            | persivs             | 1               |
| misenvs         | 1            | misenvm             | 1               |
| intelligo       | 1            | intelligens         | 1               |
| cocles          | 1            | cocvlitvs           | 1               |
| prosapia        | 1            | prosapivm           | 1               |
| offvndo         | 1            | obfvndo             | 1               |
| lateranvs       | 1            | laterani            | 1               |
| sempiterno      | 1            | sempiternvs         | 1               |
| theta           | 1            | thetvm              | 1               |
| extollo         | 1            | effero              | 1               |
| phoebevs        | 1            | phoebeivs           | 1               |
| verto           | 1            | versvs              | 1               |
| canorvs         | 1            | canor               | 1               |
| fractvs         | 1            | frango              | 1               |
| elvmbis         | 1            | elvmbo              | 1               |
| circvmmvgio     | 1            | mvgio               | 1               |
| camena          | 1            | camenae             | 1               |
| antecello       | 1            | antecellens         | 1               |
| exactvs         | 1            | exigo               | 1               |
| svbiectvs       | 1            | svbicio             | 1               |
| calpvrnia       | 1            | calpvrnivs          | 1               |
| qvinctivs       | 1            | qvintivs            | 1               |
| occento         | 1            | occens              | 1               |
| ticinvm         | 1            | ticinivs            | 1               |
| phileros        | 1            | phileron            | 1               |
| camera          | 1            | camarvs             | 1               |
| honorificvs     | 1            | honorifice          | 1               |
| parvm           | 1            | parvvs              | 1               |
| paco            | 1            | pacatvs             | 1               |
| mvtio           | 1            | mvto                | 1               |
| orivndvs        | 1            | orior               | 1               |
| verna           | 1            | vernvs              | 1               |
| dilvcesco       | 1            | dilvceo             | 1               |
| parvvm          | 1            | parvvs              | 1               |
| hesiona         | 1            | hesiones            | 1               |
| telamon         | 1            | telamvs             | 1               |
| defector        | 1            | defectvs            | 1               |
| effvnsvs        | 1            | effvsvs             | 1               |
| ostiolvm        | 1            | ostiolvs            | 1               |
| istvc           | 1            | istic               | 1               |
| motvs           | 1            | moveo               | 1               |
| expio           | 1            | exspio              | 1               |
| obrvssa         | 1            | obrvssvs            | 1               |
| ariadna         | 1            | ariadne             | 1               |
| menstrvvm       | 1            | menstrvvs           | 1               |
| defrico         | 1            | defriceo            | 1               |
| allex           | 1            | hallex              | 1               |
| amara           | 1            | amarvs              | 1               |
| praepropervs    | 1            | praepropera         | 1               |
| cvltvs          | 1            | colo                | 1               |
| plancvs         | 1            | plancivs            | 1               |
| thesavrvm       | 1            | thesavrvs           | 1               |
| oblecto         | 1            | obligo              | 1               |
| splen           | 1            | splenvs             | 1               |
| cachinno        | 1            | cachinnvs           | 1               |
| vsvfacio        | 1            | vsvlacio            | 1               |
| expedio         | 1            | expeditvs           | 1               |
| svscito         | 1            | svscitor            | 1               |
| capto           | 1            | capio               | 1               |
| heliconides     | 1            | heliconidae         | 1               |
| consvo          | 1            | consvesco           | 1               |
| mensis          | 1            | mensa               | 1               |
| amitto          | 1            | amissvs             | 1               |
| tonsvs          | 1            | tondeo              | 1               |
| emereo          | 1            | emeritvs            | 1               |
| averto          | 1            | aversvs             | 1               |
| libraria        | 1            | librarivs           | 1               |
| annvvm          | 1            | annvvs              | 1               |
| svperfio        | 1            | svpersvm            | 1               |
| gryps           | 1            | grypes              | 1               |
| svmme           | 1            | svpervs             | 1               |
| fascinvm        | 1            | fascinvs            | 1               |
| soccatvs        | 1            | socco               | 1               |
| arca            | 1            | arcas               | 1               |
| nvmqvisnam      | 1            | nvmqvidnam          | 1               |
| svs             | 1            | sve                 | 1               |
| circvmsono      | 1            | circvmsoneo         | 1               |
| ignave          | 1            | ignavvs             | 1               |
| abvndans        | 1            | abvndo              | 1               |
| svbito          | 1            | svbitvs             | 1               |
| caedes          | 1            | caedo               | 1               |
| sybilla         | 1            | sibylla             | 1               |
| illvceo         | 1            | illvcesco           | 1               |
| praetorivs      | 1            | praetorivm          | 1               |
| pecto           | 1            | pexvs               | 1               |
| natalicivs      | 1            | natalicivm          | 1               |
| plasma          | 1            | plasmas             | 1               |
| lycon           | 1            | lycvs               | 1               |
| olla            | 1            | avla                | 1               |
| opertvm         | 1            | operio              | 1               |
| ilias           | 1            | iliades             | 1               |
| fvro            | 1            | fvrens              | 1               |
| genitalia       | 1            | genitalis           | 1               |
| specio          | 1            | spicio              | 1               |
| libo            | 1            | libet               | 1               |
| manifestvs      | 1            | manifesto           | 1               |
| depleo          | 1            | depletvm            | 1               |
| indignvs        | 1            | indignvm            | 1               |
| individvvs      | 1            | individeo           | 1               |
| nardvs          | 1            | nardvm              | 1               |
| neapolitanvm    | 1            | neapolitanvs        | 1               |
| aones           | 1            | aonae               | 1               |
| medipontvs      | 1            | melipontvs          | 1               |
| bellicvm        | 1            | bellicvs            | 1               |
| tecte           | 1            | tectvs              | 1               |
| antigone        | 1            | antigones           | 1               |
| melanippe       | 1            | melanippes          | 1               |
| veneriae        | 1            | veneria             | 1               |
| circvmcido      | 1            | circvmcisvs         | 1               |
| echinvs         | 1            | echina              | 1               |
| nevtro          | 1            | nevter              | 1               |
| adolesco        | 1            | advltvs             | 1               |
| concio          | 1            | concieo             | 1               |
| declivis        | 1            | declive             | 1               |
| donvm           | 1            | dono                | 1               |
| illi            | 1            | ille                | 1               |
| pyrgo           | 1            | pyrgvs              | 1               |
| rhoetevs        | 1            | rhoeteivs           | 1               |
| rodevs          | 1            | rosevs              | 1               |
| delectvs        | 1            | deligo              | 1               |
| arroganter      | 1            | arrogans            | 1               |
| vertico         | 1            | verticvs            | 1               |
| lysias          | 1            | lysivs              | 1               |
| harvdes         | 1            | harvdvs             | 1               |
| qvatvor         | 1            | tres                | 1               |
| cano            | 1            | canis               | 1               |
| anteverto       | 1            | antevorto           | 1               |
| balitans        | 1            | balito              | 1               |
| angor           | 1            | ango                | 1               |
| ingressvs       | 1            | ingredior           | 1               |
| alsiense        | 1            | alsiensis           | 1               |
| recrvdesco      | 1            | recrvdo             | 1               |
| svppvro         | 1            | svppvratvs          | 1               |
| cevs            | 1            | cea                 | 1               |
| amentvm         | 1            | ammentvm            | 1               |
| tracto          | 1            | tractatvs           | 1               |
| coaeqvo         | 1            | coaeqvor            | 1               |
| apto            | 1            | aptvs               | 1               |
| sedvco          | 1            | sedvctvs            | 1               |
| latratvs        | 1            | latrates            | 1               |
| largior         | 1            | largvs              | 1               |
| somnivm         | 1            | somnivs             | 1               |
| erro            | 1            | erratvm             | 1               |
| trepidvs        | 1            | trepido             | 1               |
| ferrvm          | 1            | fero                | 1               |
| defvnctvs       | 1            | defvngor            | 1               |
| fabaginvs       | 1            | fabago              | 1               |
| praevenio       | 1            | venio               | 1               |
| corvinvs        | 1            | corvinivs           | 1               |
| hamilcar        | 1            | hamilcaris          | 1               |
| poetris         | 1            | poetridvs           | 1               |
| pegasevs        | 1            | pegaseivs           | 1               |
| resido          | 1            | resideo             | 1               |
| sine            | 1            | sino                | 1               |
| patavivm        | 1            | patavivs            | 1               |
| pascor          | 1            | pasco               | 1               |
| svrrentvm       | 1            | svrrens             | 1               |
| iacto           | 1            | iacio               | 1               |
| incito          | 1            | incitatvs           | 1               |
| abditvs         | 1            | abdo                | 1               |
| carsvlae        | 1            | carsvla             | 1               |
| danais          | 1            | danai               | 1               |
| tvtvm           | 1            | tvtvs               | 1               |
| balaena         | 1            | ballaena            | 1               |
| lvdifico        | 1            | lvdificor           | 1               |
| exsecratvs      | 1            | exsecror            | 1               |
| foliatvm        | 1            | folio               | 1               |
| amygdalvm       | 1            | amygaalvs           | 1               |
| datvm           | 1            | dator               | 1               |
| didivs          | 1            | didia               | 1               |
| trinvndinvm     | 1            | trinvndinvs         | 1               |
| cimmerii        | 1            | cimmerion           | 1               |
| inane           | 1            | inanis              | 1               |
| svbcrispvs      | 1            | svbcrimo            | 1               |
| ovile           | 1            | ovilis              | 1               |
| geminvs         | 1            | geminivs            | 1               |
| divvm           | 1            | divvs               | 1               |
| moror           | 1            | morior              | 1               |
| aeternvs        | 1            | aeternvm            | 1               |
| afflatvs        | 1            | afflo               | 1               |
| erigone         | 1            | erigon              | 1               |
| paeniteo        | 1            | paenitens           | 1               |
| divrnvm         | 1            | divrnvs             | 1               |
| xerxes          | 1            | xerses              | 1               |
| exsto           | 1            | exsisto             | 1               |
| opimivs         | 1            | opimvs              | 1               |
| viride          | 1            | viridis             | 1               |
| castalivs       | 1            | castalia            | 1               |
| canto           | 1            | cantvs              | 1               |
| restricte       | 1            | restricto           | 1               |
| dis             | 1            | dives               | 1               |
| patavini        | 1            | patavinvs           | 1               |
| certe           | 1            | certvs              | 1               |
| mvricidvs       | 1            | mvricides           | 1               |
| acriter         | 1            | acer                | 1               |
| negligenter     | 1            | neclegenter         | 1               |
| menenivs        | 1            | menenii             | 1               |
| gallio          | 1            | gallivs             | 1               |
| nvmisivs        | 1            | nvmisii             | 1               |
| hispanvs        | 1            | hispani             | 1               |
| dipsas          | 1            | dipsae              | 1               |
| lvpvs           | 1            | lvpes               | 1               |
| mvcivs          | 1            | mvcvs               | 1               |
| aleivs          | 1            | aleia               | 1               |
| lamina          | 1            | laminvs             | 1               |
| sallvstivs      | 1            | sallvstvs           | 1               |
| temperatvs      | 1            | tempero             | 1               |
| hercvlivs       | 1            | hercvlevs           | 1               |
| stymphalidae    | 1            | stymphalis          | 1               |
| infans          | 1            | infantia            | 1               |
| insitvs         | 1            | insero              | 1               |
| casvla          | 1            | casvlvs             | 1               |
| fvtilis         | 1            | fvttilis            | 1               |
| indeploratvs    | 1            | impeploro           | 1               |
| ventvs          | 1            | venio               | 1               |
| senex           | 1            | senior              | 1               |
| consvltvs       | 1            | consvltvm           | 1               |
| minvs           | 1            | parvm               | 1               |
| gabinivs        | 1            | gabinia             | 1               |
| exardeo         | 1            | exardesco           | 1               |
| mos             | 1            | morior              | 1               |
| alio            | 1            | alivs               | 1               |
| savillvm        | 1            | savillvs            | 1               |
| incepto         | 1            | incipio             | 1               |
| pachynvm        | 1            | pachynvs            | 1               |
| honeste         | 1            | honestvs            | 1               |
| tvsci           | 1            | tvscvs              | 1               |
| qvivis          | 1            | qvibvsqvis          | 1               |
| dvodenvs        | 1            | dvodeni             | 1               |
| do              | 1            | dato                | 1               |
| admirandvs      | 1            | admiror             | 1               |
| commodvm        | 1            | commodvs            | 1               |
| proficiscor     | 1            | profecto            | 1               |
| occvpo          | 1            | occvpatvs           | 1               |
| iarbas          | 1            | iarba               | 1               |
| argos           | 1            | argi                | 1               |
| secvris         | 1            | secvrvs             | 1               |
| evigilo         | 1            | evigilvm            | 1               |
| svra            | 1            | syra                | 1               |
| obsido          | 1            | obsideo             | 1               |
| pvblicvs        | 1            | pvblicvm            | 1               |
| hyrcanvs        | 1            | hyrcani             | 1               |
| medvs           | 1            | medi                | 1               |
| tvrpis          | 1            | tvrpe               | 1               |
| lynx            | 1            | lynca               | 1               |
| neapolitanvs    | 1            | neapolitani         | 1               |
| repeto          | 1            | repetvndae          | 1               |
| prvna           | 1            | prvnvm              | 1               |
| magnificenter   | 1            | magnificvs          | 1               |
| flavianvs       | 1            | flaviani            | 1               |
| caepa           | 1            | caepe               | 1               |
| cvpidvs         | 1            | cvpido              | 1               |
| cavtes          | 1            | cavtem              | 1               |
| principivm      | 1            | princeps            | 1               |
| derigo          | 1            | directvs            | 1               |
| illac           | 1            | illic               | 1               |
| citvs           | 1            | cieo                | 1               |
| elysii          | 1            | elysivs             | 1               |
| palpvm          | 1            | palpvs              | 1               |
| hypsipyle       | 1            | hypsipyles          | 1               |
| incedo          | 1            | incesso             | 1               |
| medicvs         | 1            | medica              | 1               |
| althaea         | 1            | althaevs            | 1               |
| immerens        | 1            | immereo             | 1               |
| sancte          | 1            | sanctvs             | 1               |
| exstrvo         | 1            | extrvo              | 1               |
| cassvs          | 1            | cassis              | 1               |
| tres            | 1            | tribvs              | 1               |
| ceres           | 1            | cereris             | 1               |
| temetvm         | 1            | temes               | 1               |
| plvmevs         | 1            | plvmea              | 1               |
| femen           | 1            | femina              | 1               |
| eventvra        | 1            | evenio              | 1               |
| contrarivm      | 1            | contrarivs          | 1               |
| salvvs          | 1            | salvivs             | 1               |
| contemnendvs    | 1            | contemno            | 1               |
| anicetvs        | 1            | anicetvm            | 1               |
| neo             | 1            | no                  | 1               |
| nescioqvid      | 1            | nescioqvis          | 1               |
| absvrde         | 1            | absvrdo             | 1               |
| prodo           | 1            | prodeo              | 1               |
| pvdendvs        | 1            | pvdeo               | 1               |
| deterivs        | 1            | deterior            | 1               |
| pannvcivs       | 1            | pannvcia            | 1               |
| bavcis          | 1            | bavci               | 1               |
| ocimvm          | 1            | ocimvs              | 1               |
| heros           | 1            | herovs              | 1               |
| laxe            | 1            | laxvs               | 1               |
| philippi        | 1            | philippvs           | 1               |
| parmvla         | 1            | parmvlvs            | 1               |
| thrax           | 1            | thraxx              | 1               |
| scriptito       | 1            | scribtito           | 1               |
| praetextvs      | 1            | praetexta           | 1               |
| polites         | 1            | politvs             | 1               |
| ratis           | 1            | reor                | 1               |
| adico           | 1            | adicio              | 1               |
| sto             | 1            | statvra             | 1               |
| praegrandis     | 1            | praegro             | 1               |
| decoctior       | 1            | decoctvs            | 1               |
| mare            | 1            | marivs              | 1               |
| metrvm          | 1            | metro               | 1               |
| qvemadmodvm     | 1            | svm                 | 1               |
| camelvs         | 1            | camela              | 1               |
| sedochezi       | 1            | sedochesimae        | 1               |
| cornelia        | 1            | cornelivs           | 1               |
| tmarvs          | 1            | tmari               | 1               |
| edisco          | 1            | ediscor             | 1               |
| aliqvantvs      | 1            | aliqvanto           | 1               |
| rvscvm          | 1            | rvscvs              | 1               |
| divdico         | 1            | diivdico            | 1               |
| pilvm           | 1            | pilvs               | 1               |
| svperi          | 1            | svpervs             | 1               |
| qvicvmqve       | 1            | qvisqve             | 1               |
| fvngvs          | 1            | fvngor              | 1               |
| anteeo          | 1            | antideo             | 1               |
| svgillo         | 1            | svggillo            | 1               |
| athamantis      | 1            | athamantides        | 1               |
| ornatvs         | 1            | orno                | 1               |
| philvs          | 1            | philivs             | 1               |
| nvmida          | 1            | nvmidae             | 1               |
| cogo            | 1            | cogito              | 1               |
| plotina         | 1            | plotinvs            | 1               |
| obirascor       | 1            | obirasco            | 1               |
| distingvo       | 1            | distinctvs          | 1               |
| adhaeresco      | 1            | adhaereo            | 1               |
| ervca           | 1            | ervcio              | 1               |
| pvlso           | 1            | pello               | 1               |
| deplorabvndvs   | 1            | deploro             | 1               |
| phoebe          | 1            | phoebvs             | 1               |
| caervlevs       | 1            | caervlvs            | 1               |
| restitvtvs      | 1            | restitvo            | 1               |
| exercito        | 1            | exercitatvs         | 1               |
| svbitvm         | 1            | svbitvs             | 1               |
| percarvs        | 1            | perco               | 1               |
| decima          | 1            | decimvs             | 1               |
| removeo         | 1            | remotvs             | 1               |
| alcippe         | 1            | alcippes            | 1               |
| demaratvs       | 1            | demarato            | 1               |
| sacrvm          | 1            | sacer               | 1               |
| cardvelis       | 1            | cardelis            | 1               |
| mvstela         | 1            | mvstellvm           | 1               |
| lvcidvs         | 1            | lvcide              | 1               |
| ephemeris       | 1            | ephemeridae         | 1               |
| iris            | 1            | irvs                | 1               |
| moneo           | 1            | monitvs             | 1               |
| bavli           | 1            | bavlvs              | 1               |
| florens         | 1            | floreo              | 1               |
| cantaber        | 1            | cantabrvs           | 1               |
| mavrvs          | 1            | mavra               | 1               |
| svccenseo       | 1            | svscendo            | 1               |
| pvngo           | 1            | parigo              | 1               |
| lydivs          | 1            | lydia               | 1               |
| vaccensis       | 1            | vagenses            | 1               |
| alexandrea      | 1            | alexandria          | 1               |
| bias            | 1            | biantes             | 1               |
| tantvlvm        | 1            | tantvlvs            | 1               |
| sera            | 1            | sero                | 1               |
| lvcidvm         | 1            | lvcidvs             | 1               |
| aqvvla          | 1            | aqvola              | 1               |
| cadvrcvm        | 1            | cadvrcvs            | 1               |
| gaia            | 1            | gaiae               | 1               |
| pvrpvratvs      | 1            | pvrpvrator          | 1               |
| prior           | 1            | privs               | 1               |
| moderor         | 1            | moderatvs           | 1               |
| ministro        | 1            | minister            | 1               |
| tigillvm        | 1            | tigillvs            | 1               |
| diverto         | 1            | diversvs            | 1               |
| impollitvs      | 1            | impolitvs           | 1               |
| inqvino         | 1            | inqvinatvs          | 1               |
| novem           | 1            | noves               | 1               |
| defringo        | 1            | defractvs           | 1               |
| deditvs         | 1            | dedo                | 1               |
| demissvs        | 1            | demitto             | 1               |
| pargo           | 1            | parco               | 1               |
| oleaster        | 1            | oleastro            | 1               |
| bifariam        | 1            | bifarivs            | 1               |
| nvmne           | 1            | nvmnvs              | 1               |
| coriolanvs      | 1            | coriolani           | 1               |
| torevma         | 1            | torevmatvs          | 1               |
| elysivm         | 1            | elysivs             | 1               |
| devia           | 1            | devivs              | 1               |
| svperpendens    | 1            | pendeo              | 1               |
| philippvs       | 1            | philippi            | 1               |
| ismenis         | 1            | ismenides           | 1               |
| fabrico         | 1            | fabricor            | 1               |
| laniatvs        | 1            | lanio               | 1               |
| dilacero        | 1            | dilacor             | 1               |
| pavpervs        | 1            | pavper              | 1               |
| sincipvt        | 1            | sincipio            | 1               |
| prandeo         | 1            | pranseo             | 1               |
| poto            | 1            | potior              | 1               |
| oscitans        | 1            | oscito              | 1               |
| tertio          | 1            | tertivs             | 1               |
| moles           | 1            | molivm              | 1               |
| obiectvs        | 1            | obicio              | 1               |
| commissvm       | 1            | committo            | 1               |
| ambracivs       | 1            | ambracias           | 1               |
| perattente      | 1            | peratto             | 1               |
| nais            | 1            | naiades             | 1               |
| morvm           | 1            | mos                 | 1               |
| ivratvs         | 1            | ivro                | 1               |
| allego          | 1            | allectvs            | 1               |
| mamilivs        | 1            | mamilia             | 1               |
| comptvs         | 1            | como                | 1               |
| samnis          | 1            | samni               | 1               |
| marsi           | 1            | marsvs              | 1               |
| cepheis         | 1            | cepheivs            | 1               |
| minax           | 1            | minacivm            | 1               |
| dispvdet        | 1            | dispvdo             | 1               |
| obediens        | 1            | obedio              | 1               |
| scvlponeae      | 1            | scvlponia           | 1               |
| factvs          | 1            | factvm              | 1               |
| vernvm          | 1            | vernvs              | 1               |
| falcvla         | 1            | falcvlvm            | 1               |
| solo            | 1            | solor               | 1               |
| rvbicvndvlvs    | 1            | rvbicvndvla         | 1               |
| intestinvm      | 1            | intestinvs          | 1               |
| crvcio          | 1            | crvcvs              | 1               |
| scabo           | 1            | sco                 | 1               |
| serpyllvm       | 1            | serpyllvs           | 1               |
| incesso         | 1            | incedo              | 1               |
| antiqvaria      | 1            | antiqvarivs         | 1               |
| repecto         | 1            | repexo              | 1               |
| metior          | 1            | mensvs              | 1               |
| cviatis         | 1            | qvoiatvs            | 1               |
| indemno         | 1            | indemnatvs          | 1               |
| armenivs        | 1            | armenii             | 1               |
| amicvs          | 1            | amice               | 1               |
| valgivs         | 1            | valgvs              | 1               |
| qverqvetvm      | 1            | qverqvetvs          | 1               |
| garganvs        | 1            | gargani             | 1               |
| phrygia         | 1            | phrygivs            | 1               |
| licymnia        | 1            | licymnivs           | 1               |
| flagro          | 1            | flagrans            | 1               |
| pavxillvm       | 1            | pavxillvs           | 1               |
| tradvco         | 1            | transdvco           | 1               |
| epistates       | 1            | epistatvs           | 1               |
| maiores         | 1            | magnvs              | 1               |
| avxiliaris      | 1            | avxiliares          | 1               |
| praeceps        | 1            | praecipio           | 1               |
| mico            | 1            | mica                | 1               |
| praetereo       | 1            | praeteritvs         | 1               |
| issos           | 1            | issvs               | 1               |
| altercor        | 1            | alterco             | 1               |
| proselenos      | 1            | proselenvs          | 1               |
| noxia           | 1            | noxivs              | 1               |
| delector        | 1            | delecto             | 1               |
| granarivm       | 1            | granarivs           | 1               |
| glvtvs          | 1            | glvttvs             | 1               |
| navcvm          | 1            | navcvs              | 1               |
| excors          | 1            | excordis            | 1               |
| setinvm         | 1            | setinvs             | 1               |
| anathymiasis    | 1            | anathymias          | 1               |
| elegidion       | 1            | elegidivm           | 1               |
| xanthias        | 1            | xanthia             | 1               |
| postvmivs       | 1            | postvmia            | 1               |
| piacvlaris      | 1            | piacvlor            | 1               |
| postvlatvm      | 1            | postvlo             | 1               |
| diversvs        | 1            | diverto             | 1               |
| pytho           | 1            | pythvs              | 1               |
| inceptvm        | 1            | incipio             | 1               |
| insideo         | 1            | insido              | 1               |
| lanvvini        | 1            | lanvvinvs           | 1               |
| stvltvs         | 1            | stvlte              | 1               |
| recvpero        | 1            | recipio             | 1               |
| vegrandis       | 1            | vegro               | 1               |
| svber           | 1            | svbeo               | 1               |
| modivm          | 1            | modivs              | 1               |
| gavdivm         | 1            | gavdeo              | 1               |
| parca           | 1            | parcvs              | 1               |
| barine          | 1            | barinvs             | 1               |
| emax            | 1            | emacio              | 1               |
| difficile       | 1            | difficilis          | 1               |
| niteo           | 1            | nitor               | 1               |
| ivsta           | 1            | ivstvs              | 1               |
| defvngor        | 1            | defvnctvs           | 1               |
| tergeminvs      | 1            | trigeminvs          | 1               |
| aestiva         | 1            | aestivvs            | 1               |
| doryclvs        | 1            | doryclivs           | 1               |
| prolabor        | 1            | prolo               | 1               |
| conatvs         | 1            | conor               | 1               |
| fvtvri          | 1            | fvtvrvs             | 1               |
| velociter       | 1            | velox               | 1               |
| rhombvs         | 1            | rhombos             | 1               |
| praetexta       | 1            | praetextvs          | 1               |
| caelestis       | 1            | caelestia           | 1               |
| calleo          | 1            | callis              | 1               |
| svbaeratvs      | 1            | svbaero             | 1               |
| hiberi          | 1            | iberi               | 1               |
| ingemo          | 1            | ingemisco           | 1               |
| reicvlvs        | 1            | reicvlvm            | 1               |
| delicatvs       | 1            | delicator           | 1               |
| perfectvs       | 1            | perficio            | 1               |
| inexsvperabilis | 1            | inexsvper           | 1               |
| abrvptvm        | 1            | abrvmpo             | 1               |
| flvens          | 1            | flvo                | 1               |
| iacio           | 1            | iaceo               | 1               |
| oppidvm         | 1            | oppido              | 1               |
| qvadragesimvs   | 1            | qvadragesima        | 1               |
| aeqvvm          | 1            | aeqvvs              | 1               |
| svpervacvvs     | 1            | svpervacvvm         | 1               |
| galeatvs        | 1            | galeo               | 1               |
| lavdo           | 1            | lavs                | 1               |
| amplvs          | 1            | ample               | 1               |
| centies         | 1            | centiens            | 1               |
| sexagesimvs     | 1            | sexagensimvs        | 1               |
| thyrsis         | 1            | thyrsvs             | 1               |
| floreo          | 1            | florens             | 1               |
| occipvt         | 1            | occipio             | 1               |
| sanna           | 1            | sannvs              | 1               |
| agito           | 1            | ago                 | 1               |
| valetvdinarivm  | 1            | valetvdinarivs      | 1               |
| capharis        | 1            | capherides          | 1               |
| cvpiens         | 1            | cvpio               | 1               |
| lvgeo           | 1            | lvceo               | 1               |
| scato           | 1            | scaton              | 1               |
| egens           | 1            | egeo                | 1               |
| tectvm          | 1            | tego                | 1               |
| abito           | 1            | abeo                | 1               |
| ei              | 1            | is                  | 1               |
| navalis         | 1            | navalia             | 1               |
| florevs         | 1            | florea              | 1               |
| palpor          | 1            | palpo               | 1               |
| oppido          | 1            | oppidvm             | 1               |
| servatvs        | 1            | servo               | 1               |
| pvlmentarivm    | 1            | pvlmentarivs        | 1               |
| ementior        | 1            | emens               | 1               |
| porrvs          | 1            | porra               | 1               |
| avellana        | 1            | avellanvs           | 1               |
| alpis           | 1            | alpes               | 1               |
| positvs         | 1            | pono                | 1               |
| scomber         | 1            | scombrvm            | 1               |
| salii           | 1            | salivs              | 1               |
| tribvo          | 1            | tribvtvm            | 1               |
| afri            | 1            | afer                | 1               |
| sedvctvs        | 1            | sedvctvm            | 1               |
| vettidivs       | 1            | vettidvs            | 1               |
| vindico         | 1            | vindex              | 1               |
| philetaevs      | 1            | philitevs           | 1               |
| habito          | 1            | habitvs             | 1               |
| vterqve         | 1            | vtroqve             | 1               |
| inaeqvatvs      | 1            | inaeqvo             | 1               |
| scelerate       | 1            | sceleratvs          | 1               |
| pollicitvm      | 1            | polliceor           | 1               |
| primigenivs     | 1            | primigenes          | 1               |
| frivolvs        | 1            | frivola             | 1               |
| philomelivm     | 1            | philomelivs         | 1               |
| geryon          | 1            | geryones            | 1               |
| nasvm           | 1            | nasvs               | 1               |
| iniqve          | 1            | iniqvvs             | 1               |
| vox             | 1            | voco                | 1               |
| spvmo           | 1            | spvmans             | 1               |
| exterreo        | 1            | exterritvs          | 1               |
| granea          | 1            | granevs             | 1               |
| cremor          | 1            | cremo               | 1               |
| prosper         | 1            | prospera            | 1               |
| sarisa          | 1            | sario               | 1               |
| atavvs          | 1            | atavi               | 1               |
| comitor         | 1            | comitatvs           | 1               |
| refoveo         | 1            | refotvs             | 1               |
| aegaevm         | 1            | aegaevs             | 1               |
| thraca          | 1            | thrax               | 1               |
| venalis         | 1            | nalis               | 1               |
| neqve           | 1            | nec                 | 1               |
| invisvs         | 1            | inviso              | 1               |
| menaenvs        | 1            | menaenivs           | 1               |
| svfficio        | 1            | svfficiens          | 1               |
| lapsvs          | 1            | labor               | 1               |
| nvndinae        | 1            | nvndina             | 1               |
| ivlia           | 1            | ivlivs              | 1               |
| eleganter       | 1            | elegans             | 1               |
| beatvm          | 1            | beatvs              | 1               |
| proceres        | 1            | procervs            | 1               |
| illavdatvs      | 1            | illavdo             | 1               |
| qvinta          | 1            | qvintvs             | 1               |
| contabvlo       | 1            | contabvlor          | 1               |
| pinna           | 1            | penna               | 1               |
| depressvs       | 1            | deprimo             | 1               |
| bvlevta         | 1            | bvlevtvs            | 1               |
| hiemo           | 1            | hiems               | 1               |
| scriblita       | 1            | scribo              | 1               |
| recipio         | 1            | receptvs            | 1               |
| arbitrarivs     | 1            | arbitrarivm         | 1               |
| acer            | 1            | acriter             | 1               |
| ithaca          | 1            | ithaces             | 1               |
| svpervado       | 1            | svpervadeo          | 1               |
| profvndvm       | 1            | profvndvs           | 1               |
| cinyphivs       | 1            | cinyphia            | 1               |
| altare          | 1            | alto                | 1               |
| raptvm          | 1            | rapio               | 1               |
| fvlgeo          | 1            | fvlgens             | 1               |
| salio           | 1            | sal                 | 1               |
| dehavrio        | 1            | deorior             | 1               |
| ferraria        | 1            | ferrarivs           | 1               |
| simvl           | 1            | simvlac             | 1               |
| rescriptvm      | 1            | rescribo            | 1               |
| mandatvm        | 1            | mando               | 1               |
| sidonivs        | 1            | sidonii             | 1               |
| distendo        | 1            | distentvs           | 1               |
| desvesco        | 1            | desvetvs            | 1               |
| svblestvs       | 1            | svbledo             | 1               |
| paphlagona      | 1            | paphlagon           | 1               |
| sinopa          | 1            | sinopes             | 1               |
| arabes          | 1            | arabs               | 1               |
| cara            | 1            | caras               | 1               |
| cretanvs        | 1            | cretani             | 1               |
| syrvs           | 1            | syri                | 1               |
| rhodia          | 1            | rhodivs             | 1               |
| lycia           | 1            | lycivs              | 1               |
| peredia         | 1            | peredivs            | 1               |
| vnomammivs      | 1            | vnomammia           | 1               |
| conterebromnivs | 1            | conterebromnia      | 1               |
| condepso        | 1            | condepseo           | 1               |
| pinso           | 1            | pinseo              | 1               |
| lativs          | 1            | lativm              | 1               |
| aqvilex         | 1            | aqvilegimes         | 1               |
| librvm          | 1            | libra               | 1               |
| rvbricatvs      | 1            | rvbrico             | 1               |
| casv            | 1            | casvs               | 1               |
| caelites        | 1            | caeles              | 1               |
| hvmervs         | 1            | hvmeo               | 1               |
| cogito          | 1            | cogitatvm           | 1               |
| stvlti          | 1            | stvltvs             | 1               |
| vtroqve         | 1            | vterqve             | 1               |
| eiecto          | 1            | eivctor             | 1               |
| qvisqvam        | 1            | qvoqvam             | 1               |
| phraates        | 1            | prahates            | 1               |
| irretortvs      | 1            | irretor             | 1               |
| prytanis        | 1            | prytanvs            | 1               |
| svfes           | 1            | svfeo               | 1               |
| fictvm          | 1            | fictvs              | 1               |
| strvthocamelvs  | 1            | strvthocamelamelame | 1               |
| obtvsvs         | 1            | optvndo             | 1               |
| bvcvla          | 1            | bvcvlvm             | 1               |
| grosphvs        | 1            | grospvs             | 1               |
| cotylo          | 1            | cotylvs             | 1               |
| aegroto         | 1            | aegrotvs            | 1               |
| hermagoras      | 1            | hermagora           | 1               |
| massicvm        | 1            | massicvs            | 1               |
| ciborivm        | 1            | ciborivs            | 1               |
| remisse         | 1            | remitto             | 1               |
| incvtio         | 1            | incvtsvs            | 1               |
| diffvsvs        | 1            | diffvndo            | 1               |
| canis           | 1            | canvs               | 1               |
| beneficivm      | 1            | beneficvs           | 1               |
| ver             | 1            | vervs               | 1               |
| ingredior       | 1            | svm                 | 1               |
| graivs          | 1            | grai                | 1               |
| sane            | 1            | sanvs               | 1               |
| edoni           | 1            | edonis              | 1               |
| arimaspi        | 1            | arimaspes           | 1               |
| piget           | 1            | pigendvs            | 1               |
| ptolomaevs      | 1            | ptolemaevs          | 1               |
| iactans         | 1            | iacto               | 1               |
| qvadragies      | 1            | qvadragiens         | 1               |
| ernevm          | 1            | ernevs              | 1               |
| confringo       | 1            | confrigo            | 1               |
| sabinvs         | 1            | sabini              | 1               |
| vincio          | 1            | vinco               | 1               |
| rvbrica         | 1            | rvbricvs            | 1               |
| secvndvm        | 1            | secvndvs            | 1               |
| parapamisadae   | 1            | parapamisada        | 1               |
| immorior        | 1            | immorivm            | 1               |
| thimiamae       | 1            | thimiama            | 1               |
| faenvs          | 1            | fenvs               | 1               |
| semirefectvs    | 1            | semirifa            | 1               |
| abscido         | 1            | abscindo            | 1               |
| psittacvs       | 1            | psittacvm           | 1               |
| chaere          | 1            | chaervs             | 1               |
| vasa            | 1            | vas                 | 1               |
| hac             | 1            | hic                 | 1               |
| inelaboratvs    | 1            | inelabor            | 1               |
| iners           | 1            | inertia             | 1               |
| rectvs          | 1            | recta               | 1               |
| oeneis          | 1            | oenevs              | 1               |
| obsero          | 1            | obsvm               | 1               |
| ictvs           | 1            | ico                 | 1               |
| interqviesco    | 1            | interqvieo          | 1               |
| beto            | 1            | bito                | 1               |
| vaccvs          | 1            | vaccivs             | 1               |
| propervs        | 1            | propera             | 1               |
| desomnis        | 1            | desomno             | 1               |
| convenientia    | 1            | conveniens          | 1               |
| sicco           | 1            | siccvs              | 1               |
| ivrisconsvltvs  | 1            | ivreconsvltvs       | 1               |
| rvfio           | 1            | rvfivs              | 1               |
| os              | 1            | ora                 | 1               |
| vvlnero         | 1            | vvlnvs              | 1               |
| tomyris         | 1            | tamyrvs             | 1               |
| magyni          | 1            | magynvs             | 1               |
| amycvs          | 1            | amyci               | 1               |
| retero          | 1            | retritvs            | 1               |
| secvndvs        | 1            | secvndvm            | 1               |
| mysterivm       | 1            | mysteria            | 1               |
| contemno        | 1            | contemptvs          | 1               |
| abicio          | 1            | abiectvs            | 1               |
| senvs           | 1            | senex               | 1               |
| partior         | 1            | partio              | 1               |
| oesypvm         | 1            | oesypvs             | 1               |
| ivstvm          | 1            | ivstvs              | 1               |
| apoecides       | 1            | apoecidivs          | 1               |
| biceps          | 1            | bicipes             | 1               |
| vvlgvs          | 1            | vvlgo               | 1               |
| latobrigi       | 1            | latobrigos          | 1               |
| maga            | 1            | magvs               | 1               |
| fvlcio          | 1            | fvlgeo              | 1               |
| vestitvs        | 1            | vestio              | 1               |
| distero         | 1            | distrido            | 1               |
| similago        | 1            | similaginis         | 1               |
| concitatvs      | 1            | concito             | 1               |
| obsonor         | 1            | obsono              | 1               |
| navvs           | 1            | gnavvs              | 1               |
| gelicidivm      | 1            | gelicidia           | 1               |
| spinther        | 1            | spintherivs         | 1               |
| nastvrtivm      | 1            | nastvrcivm          | 1               |
| abrotonvm       | 1            | abrotonvs           | 1               |
| sileo           | 1            | silens              | 1               |
| pro             | 1            | prosvm              | 1               |
| casevm          | 1            | casevs              | 1               |
| indvlgens       | 1            | indvlgeo            | 1               |
| vena            | 1            | venio               | 1               |
| masvrivs        | 1            | masvrvs             | 1               |
| sipho           | 1            | sipo                | 1               |
| constitvtvs     | 1            | constitvo           | 1               |
| plvrimvm        | 1            | mvltvs              | 1               |
| odor            | 1            | odvs                | 1               |
| pone            | 1            | pono                | 1               |
| philetas        | 1            | philitae            | 1               |
| demigro         | 1            | demigror            | 1               |
| aliqvo          | 1            | aliqvis             | 1               |
| foedvs          | 1            | foeda               | 1               |
| qvadragenvs     | 1            | qvadrageni          | 1               |
| inavdio         | 1            | indavdeo            | 1               |
| genesis         | 1            | genesvs             | 1               |
| mvtitio         | 1            | mvttitio            | 1               |
| virvs           | 1            | vir                 | 1               |
| svpparvm        | 1            | svparvm             | 1               |
| considerate     | 1            | considero           | 1               |
| psephisma       | 1            | psephismas          | 1               |
| capreae         | 1            | capreii             | 1               |
| mvndo           | 1            | mvndatvs            | 1               |
| congiarivm      | 1            | congio              | 1               |
| infimvm         | 1            | infervs             | 1               |
| albanvm         | 1            | albanvs             | 1               |
| formianvm       | 1            | formianvs           | 1               |
| harmodivs       | 1            | harmodii            | 1               |
| trapezvs        | 1            | trapezvntes         | 1               |
| vello           | 1            | velsvs              | 1               |
| coqvvs          | 1            | coqvo               | 1               |
| clipeatvs       | 1            | clapeo              | 1               |
| dinosco         | 1            | dignosco            | 1               |
| bactrianvs      | 1            | bactriani           | 1               |
| evergetae       | 1            | evergetas           | 1               |
| cirrati         | 1            | cirratvs            | 1               |
| pavca           | 1            | pavcvs              | 1               |
| exigve          | 1            | exigvvs             | 1               |
| pellis          | 1            | pello               | 1               |
| soror           | 1            | sori                | 1               |
| antefero        | 1            | antelo              | 1               |
| tressis         | 1            | tredo               | 1               |
| agaso           | 1            | agasvs              | 1               |
| parce           | 1            | parco               | 1               |
| misere          | 1            | mitto               | 1               |
| myrice          | 1            | myrica              | 1               |
| delphin         | 1            | delphina            | 1               |
| occvpatvs       | 1            | occvpo              | 1               |
| colchvs         | 1            | colcha              | 1               |
| postqvam        | 1            | qvam                | 1               |
| septimvs        | 1            | septvs              | 1               |
| nvbilvm         | 1            | nvbila              | 1               |
| necessarivs     | 1            | necessario          | 1               |
| frigida         | 1            | frigidvs            | 1               |
| obseqventia     | 1            | obseqvens           | 1               |
| macedo          | 1            | macedones           | 1               |
| visco           | 1            | viscatvs            | 1               |
| progressvs      | 1            | progredior          | 1               |
| admodvm         | 1            | admodvs             | 1               |
| simvlo          | 1            | simvlis             | 1               |
| inconsvmptvs    | 1            | inconsvm            | 1               |
| fixvs           | 1            | figo                | 1               |
| civicvs         | 1            | civica              | 1               |
| thracivs        | 1            | thracia             | 1               |
| morigervs       | 1            | moriger             | 1               |
| tantvsdem       | 1            | tantvmdem           | 1               |
| scitvm          | 1            | scio                | 1               |
| raster          | 1            | rastrvm             | 1               |
| seria           | 1            | serivs              | 1               |
| tento           | 1            | temptor             | 1               |
| seqvanvs        | 1            | seqvani             | 1               |
| accvro          | 1            | accvratvs           | 1               |
| maxilla         | 1            | magillvs            | 1               |
| balanatvs       | 1            | balano              | 1               |
| gavsapvm        | 1            | gavsape             | 1               |
| gvrgvlio        | 1            | gvrgvlivm           | 1               |
| politvs         | 1            | polio               | 1               |
| maeror          | 1            | moeror              | 1               |
| translatvs      | 1            | tranatvs            | 1               |
| nitens          | 1            | nitor               | 1               |
| maena           | 1            | mena                | 1               |
| molorchaevs     | 1            | molorchevs          | 1               |
| inavratvs       | 1            | inavro              | 1               |
| bilibris        | 1            | biliber             | 1               |
| expetesso       | 1            | expeto              | 1               |
| qvinqve         | 1            | viginti             | 1               |
| bos             | 1            | bosco               | 1               |
| hederacevs      | 1            | hederacivs          | 1               |
| nobilior        | 1            | nobilis             | 1               |
| oxathres        | 1            | oxathris            | 1               |
| criminor        | 1            | crimineris          | 1               |
| patens          | 1            | pateo               | 1               |
| horreo          | 1            | horrens             | 1               |
| svbseqvor       | 1            | svpseqvor           | 1               |
| tenere          | 1            | teneo               | 1               |
| stips           | 1            | stipes              | 1               |
| obsto           | 1            | obsisto             | 1               |
| fvnda           | 1            | fvndvs              | 1               |
| ebibo           | 1            | ebibeo              | 1               |
| svpplavdo       | 1            | svpplodo            | 1               |
| ivvenalia       | 1            | ivvenalis           | 1               |
| avxilior        | 1            | avxilio             | 1               |
| placitvm        | 1            | placeo              | 1               |
| avara           | 1            | avarvs              | 1               |
| talvs           | 1            | talvm               | 1               |
| dvcenti         | 1            | qvadraginta         | 1               |
| aptvs           | 1            | apte                | 1               |
| convenio        | 1            | conventvs           | 1               |
| symbola         | 1            | symbolvs            | 1               |
| fvcatvs         | 1            | fvco                | 1               |
| probvs          | 1            | probo               | 1               |
| bedriacvm       | 1            | bedriacvs           | 1               |
| potivncvla      | 1            | potivncvlvs         | 1               |
| efficiens       | 1            | efficio             | 1               |
| germanvs        | 1            | germani             | 1               |
| lvpercvs        | 1            | lvperci             | 1               |
| solidvs         | 1            | solidvm             | 1               |
| conclvsvs       | 1            | conclvdo            | 1               |
| mitto           | 1            | miser               | 1               |
| tempestivo      | 1            | tempestivvs         | 1               |
| dacia           | 1            | dacivs              | 1               |
| lycidas         | 1            | lycida              | 1               |
| formosvs        | 1            | formose             | 1               |
| reviso          | 1            | revideo             | 1               |
| antitheton      | 1            | antithetvs          | 1               |
| vacvvm          | 1            | vacvvs              | 1               |
| apertvm         | 1            | apertvs             | 1               |
| follis          | 1            | folla               | 1               |
| prostitvtvs     | 1            | prostitvo           | 1               |
| sellarivs       | 1            | sellarivm           | 1               |
| raptvs          | 1            | rapio               | 1               |
| porrvm          | 1            | porrvs              | 1               |
| allivm          | 1            | alivs               | 1               |
| rvta            | 1            | rvtvs               | 1               |
| bebrycivs       | 1            | bebrycia            | 1               |
| pediseqvvs      | 1            | pediseqvis          | 1               |
| malobathron     | 1            | malobathrvm         | 1               |
| penso           | 1            | penseo              | 1               |
| potior          | 1            | potis               | 1               |
| versvs          | 1            | verto               | 1               |
| sardanapallvs   | 1            | sardanapalvs        | 1               |
| respondeo       | 1            | responsvm           | 1               |
| nata            | 1            | nascor              | 1               |
| cantharis       | 1            | cantharidvs         | 1               |
| vitvlina        | 1            | vitvlinvs           | 1               |
| providens       | 1            | provideo            | 1               |
| vsvra           | 1            | vtor                | 1               |
| centesimvs      | 1            | centesima           | 1               |
| amazon          | 1            | amazona             | 1               |
| proficio        | 1            | proficiscor         | 1               |
| naris           | 1            | no                  | 1               |
| trivmpho        | 1            | trivmphvs           | 1               |
| tartarvs        | 1            | tartara             | 1               |
| pavlvm          | 1            | pavlvs              | 1               |
| noceo           | 1            | nocens              | 1               |
| avditvm         | 1            | avdio               | 1               |
| minvtal         | 1            | minvtalis           | 1               |
| damnatorivs     | 1            | damnatorivm         | 1               |
| lampsacenvs     | 1            | lampsaceni          | 1               |
| lvxvs           | 1            | lvxvvs              | 1               |
| exterritvs      | 1            | exterreo            | 1               |
| gervsia         | 1            | gervsiantvs         | 1               |
| isevm           | 1            | iseon               | 1               |
| vendo           | 1            | venditvm            | 1               |
| sollicitvs      | 1            | sollicite           | 1               |
| extrema         | 1            | extremvm            | 1               |
| carthaginienses | 1            | carthaginiensis     | 1               |
| opvlens         | 1            | opvlentvs           | 1               |
| verno           | 1            | vernvs              | 1               |
| dalmaticvs      | 1            | delmaticvs          | 1               |
| misenvm         | 1            | misenvs             | 1               |
| sisapo          | 1            | sisapon             | 1               |
| pictvs          | 1            | pingo               | 1               |
| evidens         | 1            | evidenter           | 1               |
| parentes        | 1            | parens              | 1               |
| pvto            | 1            | pvteo               | 1               |
| flagrans        | 1            | flagro              | 1               |
| libvrnica       | 1            | libvrnicvs          | 1               |
| vnvsetvicesimvs | 1            | vnietvicesimvs      | 1               |
| evthymia        | 1            | evthymian           | 1               |
| albani          | 1            | albanvs             | 1               |
| pvsvla          | 1            | pvssvlvs            | 1               |
| continens       | 1            | contineo            | 1               |
| caicvs          | 1            | caice               | 1               |
| thamyras        | 1            | thamyra             | 1               |
| barbvla         | 1            | barbvlvs            | 1               |
| concors         | 1            | concordia           | 1               |
| nvntivs         | 1            | nvntio              | 1               |
| sinister        | 1            | sinistra            | 1               |
| calefacio       | 1            | calfactvs           | 1               |
| perdecorvs      | 1            | perdecvrvs          | 1               |
| entellvs        | 1            | entelles            | 1               |
| fortis          | 1            | fortiter            | 1               |
| archimagirvs    | 1            | archimago           | 1               |
| optempero       | 1            | obtempero           | 1               |
| immensvm        | 1            | immensvs            | 1               |
| nvbilvs         | 1            | nvbilvm             | 1               |
| meritvm         | 1            | mereor              | 1               |
| certvs          | 1            | certvm              | 1               |
| onomastorides   | 1            | onomastoris         | 1               |
| onomas          | 1            | onomantes           | 1               |
| callicratides   | 1            | callicratis         | 1               |
| vicesimvs       | 1            | vicesimamvs         | 1               |
| peristasis      | 1            | peristasim          | 1               |
| apologo         | 1            | apolo               | 1               |
| svperans        | 1            | svpero              | 1               |
| dares           | 1            | dareta              | 1               |
| venio           | 1            | venia               | 1               |
| impvratvs       | 1            | impvrate            | 1               |
| inepte          | 1            | ineptvs             | 1               |
| stloppvs        | 1            | scloppvs            | 1               |
| atlantis        | 1            | atlantidvs          | 1               |
| calypso         | 1            | calypsvs            | 1               |
| phaeacia        | 1            | phaeacivs           | 1               |
| sepositvs       | 1            | sepono              | 1               |
| obligo          | 1            | obligatvs           | 1               |
| vinvm           | 1            | vinipollens         | 1               |
| pollens         | 1            | vinipollens         | 1               |
| semisomnvs      | 1            | semisomna           | 1               |
| damnatvs        | 1            | damno               | 1               |
| contrarivs      | 1            | contrarivm          | 1               |
| ivnctvs         | 1            | ivngo               | 1               |
| sesama          | 1            | sesimvm             | 1               |
| pervngo         | 1            | pervngvo            | 1               |
| destricte       | 1            | destringo           | 1               |
| inerro          | 1            | inero               | 1               |
| tribvnicivs     | 1            | tribvnicvs          | 1               |
| machaerio       | 1            | machaerivs          | 1               |
| mvraena         | 1            | mvrena              | 1               |
| exdorsvo        | 1            | exdorqveo           | 1               |
| artopta         | 1            | artoptvs            | 1               |
| dirvmpo         | 1            | disvmpo             | 1               |
| distaedet       | 1            | distaedeo           | 1               |
| inconsideratvs  | 1            | inconsidervs        | 1               |
| phaeacvs        | 1            | phaeaces            | 1               |
| pateo           | 1            | patior              | 1               |
| tvte            | 1            | tv                  | 1               |
| peristylvm      | 1            | peristylvs          | 1               |
| cognosco        | 1            | cognitvs            | 1               |
| incelebratvs    | 1            | incelebro           | 1               |
| attono          | 1            | attonitvs           | 1               |
| tevcer          | 1            | tevcri              | 1               |
| pvblicvm        | 1            | pvblicvs            | 1               |
| popanvm         | 1            | popanvs             | 1               |
| hibernvm        | 1            | hiberna             | 1               |
| tvrbellae       | 1            | tvrbella            | 1               |
| irrito          | 1            | irritvs             | 1               |
| interdiv        | 1            | interdivs           | 1               |
| laridvm         | 1            | lardvs              | 1               |
| rvtilans        | 1            | rvtilo              | 1               |
| areopagvs       | 1            | areosvs             | 1               |
| sphaerita       | 1            | spaeritvs           | 1               |
| sphaera         | 1            | spaera              | 1               |
| boreas          | 1            | borea               | 1               |
| testatvs        | 1            | testor              | 1               |
| vexo            | 1            | vexor               | 1               |
| excvsse         | 1            | excvtio             | 1               |
| langvide        | 1            | langvidvs           | 1               |
| dvx             | 1            | dvco                | 1               |
| catasta         | 1            | catastvs            | 1               |
| exoleti         | 1            | exolesco            | 1               |
| vorenvs         | 1            | vorene              | 1               |
| fonteivs        | 1            | fonteia             | 1               |
| clodivs         | 1            | clodia              | 1               |
| concito         | 1            | concitatvs          | 1               |
| obligatvs       | 1            | obligo              | 1               |
| dirvm           | 1            | dirvs               | 1               |
| tranqvillvm     | 1            | tranqvillvs         | 1               |
| avlon           | 1            | avlvs               | 1               |
| ordior          | 1            | ordvs               | 1               |
| tanto           | 1            | tantvs              | 1               |
| agathinvs       | 1            | agathines           | 1               |
| lepos           | 1            | lepor               | 1               |
| inceste         | 1            | incesto             | 1               |
| comitatvs       | 1            | comitor             | 1               |
| occvltvs        | 1            | occvlte             | 1               |
| obsedeo         | 1            | obsideo             | 1               |
| ratvs           | 1            | ratis               | 1               |
| lotos           | 1            | lavvs               | 1               |
| trepido         | 1            | trepidvs            | 1               |
| carpentvm       | 1            | carpo               | 1               |
| cophinvs        | 1            | cophinvm            | 1               |
| ivdaevs         | 1            | ivdaea              | 1               |
| solymvs         | 1            | solymae             | 1               |
| internvntia     | 1            | internvntivs        | 1               |
| prorvo          | 1            | proreo              | 1               |
| olivetvm        | 1            | olivo               | 1               |
| sertorivs       | 1            | sertor              | 1               |
| frvgi           | 1            | frvgivs             | 1               |
| allvdo          | 1            | allvs               | 1               |
| exhortor        | 1            | exortor             | 1               |
| phonascvs       | 1            | phonasco            | 1               |
| stratvm         | 1            | sterno              | 1               |
| horativs        | 1            | horatia             | 1               |
| vinevs          | 1            | vinea               | 1               |
| latro           | 1            | latratos            | 1               |
| sebvm           | 1            | sebes               | 1               |
| reor            | 1            | re                  | 1               |
| avdiens         | 1            | avdio               | 1               |
| svperflvo       | 1            | svperflvens         | 1               |
| ab              | 1            | ah                  | 1               |
| corinthii       | 1            | corinthivs          | 1               |
| volvcer         | 1            | volvcris            | 1               |
| svetvs          | 1            | sveto               | 1               |
| oppositvs       | 1            | oppono              | 1               |
| levcas          | 1            | levcvs              | 1               |
| svspendo        | 1            | svspensvs           | 1               |
| cicaro          | 1            | cicarvs             | 1               |
| rescisco        | 1            | rescio              | 1               |
| privato         | 1            | privatvs            | 1               |
| indico          | 1            | indictvs            | 1               |
| sacro           | 1            | sacratvs            | 1               |
| berytvs         | 1            | berytivs            | 1               |
| congressvs      | 1            | congredior          | 1               |
| tvscvlanvs      | 1            | tvscvlanvm          | 1               |
| antias          | 1            | antiates            | 1               |
| lvdicer         | 1            | lvdicrvm            | 1               |
| privo           | 1            | privatvs            | 1               |
| rigeo           | 1            | rigens              | 1               |
| probo           | 1            | probatvs            | 1               |
| clavdianvs      | 1            | clavdianiani        | 1               |
| concha          | 1            | conca               | 1               |
| accessvs        | 1            | accedo              | 1               |
| tarraciniensis  | 1            | tarracinienses      | 1               |
| tarentinvs      | 1            | tarentini           | 1               |
| discidivm       | 1            | discidia            | 1               |
| triarivs        | 1            | triarivm            | 1               |
| milito          | 1            | miles               | 1               |
| scitvs          | 1            | scio                | 1               |
| honoro          | 1            | honoratvs           | 1               |
| domina          | 1            | dominvs             | 1               |
| contestor       | 1            | contestatvs         | 1               |
| praemonstro     | 1            | praemontro          | 1               |
| philositvs      | 1            | philosites          | 1               |
| deliciolvm      | 1            | deliciolvs          | 1               |
| meditate        | 1            | meditor             | 1               |
| viridis         | 1            | viridvs             | 1               |
| svblimiter      | 1            | svblimis            | 1               |
| cvlte           | 1            | cvltvs              | 1               |
| sero            | 1            | satis               | 1               |
| enchytvm        | 1            | encytvs             | 1               |
| thebani         | 1            | thebanvs            | 1               |
| eneco           | 1            | enectvs             | 1               |
| avtvmo          | 1            | avtvma              | 1               |
| praepotentes    | 1            | praepotens          | 1               |
| amanicae        | 1            | amanicvs            | 1               |
| perivrvs        | 1            | maivs               | 1               |
| svbsilio        | 1            | svssilio            | 1               |
| iamiamqve       | 1            | iamiam              | 1               |
| armo            | 1            | armatvs             | 1               |
| gravis          | 1            | graviter            | 1               |
| infervs         | 1            | inferi              | 1               |
| rapacida        | 1            | rapacidvs           | 1               |
| territorivm     | 1            | territorivs         | 1               |
| coerceo         | 1            | coherceo            | 1               |
| qvotvsqvisqve   | 1            | qvotvs              | 1               |
| indeprehensvs   | 1            | indeprensvs         | 1               |
| svbolfacio      | 1            | svbolfacivm         | 1               |
| mammaea         | 1            | mammaevs            | 1               |
| tenvo           | 1            | tenvastvs           | 1               |
| tvlingi         | 1            | tvlingvs            | 1               |
| stipendivm      | 1            | stipeo              | 1               |
| ambigvvm        | 1            | ambigvvs            | 1               |
| receptvs        | 1            | recipio             | 1               |
| lyristes        | 1            | lyristen            | 1               |
| grande          | 1            | grandis             | 1               |
| ovvm            | 1            | ovis                | 1               |
| xerampelinvs    | 1            | xerampelina         | 1               |
| lvgvbris        | 1            | lvgvbrivm           | 1               |
| eloqvens        | 1            | eloqvor             | 1               |
| classicvs       | 1            | classici            | 1               |
| pingve          | 1            | pingvis             | 1               |
| fagvs           | 1            | fago                | 1               |
| vado            | 1            | vadvm               | 1               |
| ille            | 1            | illo                | 1               |
| assido          | 1            | assideo             | 1               |
| penna           | 1            | pinna               | 1               |
| tarracina       | 1            | tarracinvs          | 1               |
| rigens          | 1            | rigeo               | 1               |
| consortio       | 1            | consortivm          | 1               |
| commenticivs    | 1            | commenticivm        | 1               |
| qvadraginta     | 1            | dvcenti             | 1               |
| qvingenti       | 1            | viginti             | 1               |
| octoginta       | 1            | viginti             | 1               |
| ocinvm          | 1            | ocinvs              | 1               |

::: Evaluation report for task: pos :::

all:
  accuracy: 0.9588
  precision: 0.9142
  recall: 0.8876
  support: 141348
ambiguous-tokens:
  accuracy: 0.9022
  precision: 0.8266
  recall: 0.8113
  support: 43177
unknown-tokens:
  accuracy: 0.8782
  precision: 0.4724
  recall: 0.452
  support: 6091

| Expected   | Total Errors | Predictions | Predicted times |
|------------|--------------|-------------|-----------------|
| ADJqua     | 1164         | NOM2        | 468             |
|            |              | VER         | 280             |
|            |              | NOM3        | 152             |
|            |              | ADV         | 118             |
|            |              | NOM1        | 112             |
|            |              | NOM7        | 11              |
|            |              | ADJord      | 10              |
|            |              | CONcoo      | 7               |
|            |              | PRE         | 3               |
|            |              | NOM4        | 2               |
|            |              | PROind      | 1               |
| NOM2       | 839          | ADJqua      | 466             |
|            |              | VER         | 128             |
|            |              | NOM3        | 57              |
|            |              | NOM1        | 42              |
|            |              | ADV         | 41              |
|            |              | NOM7        | 28              |
|            |              | NOM4        | 19              |
|            |              | PROpos.ref  | 14              |
|            |              | PROind      | 13              |
|            |              | CONcoo      | 10              |
|            |              | ADJcar      | 8               |
|            |              | NOM5        | 4               |
|            |              | ADJord      | 2               |
|            |              | ADJdis      | 2               |
|            |              | PROpos      | 2               |
|            |              | PROrel      | 1               |
|            |              | PROdem      | 1               |
|            |              | PROref      | 1               |
| ADV        | 604          | CONcoo      | 174             |
|            |              | ADJqua      | 102             |
|            |              | PROdem      | 98              |
|            |              | PRE         | 73              |
|            |              | CONsub      | 40              |
|            |              | NOM2        | 29              |
|            |              | NOM3        | 25              |
|            |              | VER         | 23              |
|            |              | PROind      | 16              |
|            |              | ADJcar      | 10              |
|            |              | ADVneg      | 4               |
|            |              | NOM1        | 2               |
|            |              | NOM4        | 2               |
|            |              | ADVrel      | 1               |
|            |              | INJ         | 1               |
|            |              | NOM5        | 1               |
|            |              | PROrel      | 1               |
|            |              | PROper      | 1               |
|            |              | ADVint.neg  | 1               |
| VER        | 454          | ADJqua      | 197             |
|            |              | NOM2        | 77              |
|            |              | NOM3        | 52              |
|            |              | NOM4        | 42              |
|            |              | NOM1        | 36              |
|            |              | CONsub      | 11              |
|            |              | ADV         | 8               |
|            |              | PRE         | 7               |
|            |              | NOM5        | 7               |
|            |              | ADVint      | 6               |
|            |              | INJ         | 3               |
|            |              | ADJcar      | 3               |
|            |              | PROdem      | 3               |
|            |              | ADVneg      | 1               |
|            |              | ADVrel      | 1               |
| CONsub     | 398          | ADVrel      | 121             |
|            |              | PROrel      | 104             |
|            |              | PRE         | 64              |
|            |              | CONcoo      | 41              |
|            |              | ADVint      | 24              |
|            |              | ADV         | 16              |
|            |              | ADVneg      | 14              |
|            |              | VER         | 12              |
|            |              | PROint      | 2               |
| ADVrel     | 374          | CONsub      | 197             |
|            |              | ADVint      | 87              |
|            |              | PROrel      | 75              |
|            |              | PROint      | 5               |
|            |              | VER         | 4               |
|            |              | INJ         | 3               |
|            |              | ADV         | 2               |
|            |              | PRE         | 1               |
| NOM3       | 355          | ADJqua      | 116             |
|            |              | NOM2        | 103             |
|            |              | NOM7        | 45              |
|            |              | VER         | 40              |
|            |              | ADV         | 17              |
|            |              | NOM1        | 15              |
|            |              | NOM4        | 8               |
|            |              | PROind      | 3               |
|            |              | ADJcar      | 2               |
|            |              | NOM6        | 2               |
|            |              | PROref      | 1               |
|            |              | CONcoo      | 1               |
|            |              | PROper      | 1               |
|            |              | NOM5        | 1               |
| PROint     | 266          | PROrel      | 225             |
|            |              | ADVint      | 17              |
|            |              | PROind      | 11              |
|            |              | ADVrel      | 8               |
|            |              | CONsub      | 3               |
|            |              | ADV         | 1               |
|            |              | ADVneg      | 1               |
| NOM1       | 253          | ADJqua      | 110             |
|            |              | NOM2        | 74              |
|            |              | VER         | 34              |
|            |              | NOM3        | 19              |
|            |              | NOM7        | 11              |
|            |              | PROind      | 3               |
|            |              | ADJord      | 2               |
| PROrel     | 215          | PROint      | 86              |
|            |              | CONsub      | 56              |
|            |              | ADVrel      | 48              |
|            |              | ADVint      | 12              |
|            |              | PROind      | 7               |
|            |              | CONcoo      | 5               |
|            |              | ADJqua      | 1               |
| ADVint     | 167          | ADVrel      | 76              |
|            |              | CONsub      | 32              |
|            |              | PROrel      | 31              |
|            |              | PROint      | 12              |
|            |              | ADV         | 6               |
|            |              | NOM3        | 2               |
|            |              | ADVint.neg  | 2               |
|            |              | PROdem      | 2               |
|            |              | PROind      | 1               |
|            |              | PROper      | 1               |
|            |              | VER         | 1               |
|            |              | ADVneg      | 1               |
| NOM7       | 135          | NOM1        | 50              |
|            |              | NOM2        | 36              |
|            |              | NOM3        | 35              |
|            |              | ADJqua      | 11              |
|            |              | ADVint      | 1               |
|            |              | ADV         | 1               |
|            |              | ADJcar      | 1               |
| PROdem     | 75           | ADV         | 66              |
|            |              | VER         | 4               |
|            |              | NOM2        | 2               |
|            |              | INJ         | 2               |
|            |              | ADJqua      | 1               |
| PROind     | 71           | PROrel      | 19              |
|            |              | PROint      | 18              |
|            |              | ADV         | 13              |
|            |              | NOM2        | 10              |
|            |              | PROpos      | 5               |
|            |              | NOM3        | 3               |
|            |              | ADVrel      | 1               |
|            |              | ADVint      | 1               |
|            |              | PROper      | 1               |
| NOM4       | 69           | VER         | 43              |
|            |              | NOM2        | 12              |
|            |              | NOM6        | 5               |
|            |              | ADJqua      | 5               |
|            |              | NOM3        | 3               |
|            |              | PROref      | 1               |
| PRE        | 69           | CONsub      | 35              |
|            |              | ADV         | 26              |
|            |              | VER         | 4               |
|            |              | INJ         | 2               |
|            |              | ADJord      | 1               |
|            |              | ADJadv.ord  | 1               |
| NOM6       | 64           | NOM3        | 30              |
|            |              | NOM4        | 12              |
|            |              | NOM2        | 11              |
|            |              | ADJqua      | 2               |
|            |              | ADV         | 2               |
|            |              | NOM1        | 2               |
|            |              | PROdem      | 2               |
|            |              | NOM5        | 2               |
|            |              | CONsub      | 1               |
| CONcoo     | 64           | CONsub      | 32              |
|            |              | ADV         | 26              |
|            |              | PROrel      | 4               |
|            |              | ADJqua      | 1               |
|            |              | PROint      | 1               |
| ADVneg     | 33           | CONsub      | 29              |
|            |              | CONcoo      | 4               |
| ADJord     | 30           | ADJadv.ord  | 15              |
|            |              | ADJqua      | 12              |
|            |              | NOM2        | 1               |
|            |              | PRE         | 1               |
|            |              | NOM1        | 1               |
| PROper     | 22           | PROpos      | 21              |
|            |              | INJ         | 1               |
| INJ        | 17           | PRE         | 5               |
|            |              | ADV         | 3               |
|            |              | VER         | 2               |
|            |              | CONcoo      | 2               |
|            |              | PROdem      | 2               |
|            |              | CONsub      | 1               |
|            |              | NOM1        | 1               |
|            |              | ADJqua      | 1               |
| PROpos.ref | 15           | PROref      | 14              |
|            |              | NOM2        | 1               |
| ADJcar     | 15           | ADV         | 9               |
|            |              | NOM4        | 2               |
|            |              | NOM3        | 2               |
|            |              | ADJord      | 1               |
|            |              | ADJqua      | 1               |
| ADJdis     | 11           | ADJqua      | 6               |
|            |              | ADJcar      | 2               |
|            |              | NOM2        | 2               |
|            |              | ADJord      | 1               |
| ADJadv.ord | 11           | ADJord      | 11              |
| PROpos     | 10           | PROper      | 10              |
| PROref     | 10           | PROpos.ref  | 7               |
|            |              | NOM2        | 2               |
|            |              | ADJqua      | 1               |
| ADJmul     | 8            | ADJqua      | 8               |
| ADVint.neg | 4            | ADV         | 3               |
|            |              | CONsub      | 1               |
| VERaux     | 2            | VER         | 2               |
| NOM5       | 2            | NOM3        | 1               |
|            |              | VER         | 1               |
| ADJadv.mul | 1            | ADV         | 1               |
