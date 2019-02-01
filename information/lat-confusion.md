
::: Evaluation report for task: Case :::

all:
  accuracy: 0.9275
  precision: 0.8805
  recall: 0.8337
  support: 141953
ambiguous-tokens:
  accuracy: 0.819
  precision: 0.8129
  recall: 0.7685
  support: 41428

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| Nom      | 2859         | Acc         | 1630            |
|          |              | Abl         | 404             |
|          |              | _           | 383             |
|          |              | Gen         | 271             |
|          |              | Voc         | 90              |
|          |              | Dat         | 76              |
|          |              | Ind         | 5               |
| Acc      | 1982         | Nom         | 1343            |
|          |              | _           | 353             |
|          |              | Abl         | 142             |
|          |              | Gen         | 100             |
|          |              | Voc         | 27              |
|          |              | Dat         | 9               |
|          |              | Ind         | 8               |
| Abl      | 1710         | Nom         | 612             |
|          |              | Dat         | 511             |
|          |              | Acc         | 309             |
|          |              | _           | 214             |
|          |              | Voc         | 33              |
|          |              | Gen         | 31              |
| Dat      | 1499         | Abl         | 1113            |
|          |              | Gen         | 258             |
|          |              | Nom         | 82              |
|          |              | _           | 26              |
|          |              | Voc         | 11              |
|          |              | Loc         | 6               |
|          |              | Acc         | 3               |
| _        | 1165         | Nom         | 464             |
|          |              | Acc         | 393             |
|          |              | Abl         | 233             |
|          |              | Dat         | 26              |
|          |              | Gen         | 25              |
|          |              | Ind         | 12              |
|          |              | Voc         | 12              |
| Gen      | 544          | Nom         | 302             |
|          |              | Dat         | 97              |
|          |              | Acc         | 69              |
|          |              | _           | 25              |
|          |              | Voc         | 24              |
|          |              | Abl         | 22              |
|          |              | Loc         | 5               |
| Voc      | 466          | Nom         | 289             |
|          |              | Acc         | 74              |
|          |              | Gen         | 43              |
|          |              | _           | 28              |
|          |              | Abl         | 26              |
|          |              | Dat         | 6               |
| Ind      | 45           | Acc         | 17              |
|          |              | _           | 11              |
|          |              | Abl         | 7               |
|          |              | Nom         | 5               |
|          |              | Gen         | 4               |
|          |              | Dat         | 1               |
| Loc      | 26           | Gen         | 21              |
|          |              | Dat         | 4               |
|          |              | Nom         | 1               |

::: Evaluation report for task: Deg :::

all:
  accuracy: 0.9811
  precision: 0.9705
  recall: 0.9733
  support: 141953
ambiguous-tokens:
  accuracy: 0.9072
  precision: 0.867
  recall: 0.8855
  support: 18021

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| Pos      | 1410         | _           | 1401            |
|          |              | Comp        | 8               |
|          |              | Sup         | 1               |
| _        | 1242         | Pos         | 1191            |
|          |              | Sup         | 26              |
|          |              | Comp        | 25              |
| Sup      | 17           | _           | 13              |
|          |              | Pos         | 3               |
|          |              | Comp        | 1               |
| Comp     | 13           | _           | 9               |
|          |              | Pos         | 4               |

::: Evaluation report for task: Mood :::

all:
  accuracy: 0.9814
  precision: 0.8678
  recall: 0.8169
  support: 141953
ambiguous-tokens:
  accuracy: 0.8123
  precision: 0.7105
  recall: 0.6613
  support: 6340

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| Ind      | 767          | Par         | 321             |
|          |              | Imp         | 222             |
|          |              | _           | 144             |
|          |              | Inf         | 65              |
|          |              | Sub         | 15              |
| Par      | 571          | _           | 264             |
|          |              | Ind         | 184             |
|          |              | Inf         | 93              |
|          |              | Imp         | 23              |
|          |              | Sub         | 7               |
| _        | 502          | Par         | 270             |
|          |              | Ind         | 126             |
|          |              | Inf         | 43              |
|          |              | Imp         | 33              |
|          |              | Sub         | 20              |
|          |              | Adj         | 5               |
|          |              | Ger         | 3               |
|          |              | SupU        | 1               |
|          |              | SupUm       | 1               |
| Imp      | 422          | Ind         | 319             |
|          |              | Par         | 44              |
|          |              | _           | 43              |
|          |              | Inf         | 14              |
|          |              | Sub         | 2               |
| Inf      | 222          | Par         | 121             |
|          |              | _           | 50              |
|          |              | Ind         | 44              |
|          |              | Imp         | 5               |
|          |              | SupU        | 1               |
|          |              | Sub         | 1               |
| Sub      | 64           | _           | 31              |
|          |              | Par         | 12              |
|          |              | Ind         | 12              |
|          |              | Inf         | 8               |
|          |              | Imp         | 1               |
| Adj      | 44           | Ger         | 40              |
|          |              | _           | 3               |
|          |              | Imp         | 1               |
| SupU     | 25           | Inf         | 9               |
|          |              | Par         | 7               |
|          |              | _           | 5               |
|          |              | Ind         | 3               |
|          |              | Imp         | 1               |
| Ger      | 21           | Adj         | 21              |
| SupUm    | 5            | _           | 5               |

::: Evaluation report for task: Numb :::

all:
  accuracy: 0.9739
  precision: 0.9718
  recall: 0.9719
  support: 141953
ambiguous-tokens:
  accuracy: 0.8729
  precision: 0.8628
  recall: 0.8594
  support: 20255

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| Sing     | 1804         | Plur        | 1183            |
|          |              | _           | 621             |
| Plur     | 1196         | Sing        | 1159            |
|          |              | _           | 37              |
| _        | 698          | Sing        | 648             |
|          |              | Plur        | 50              |

::: Evaluation report for task: Person :::

all:
  accuracy: 0.9913
  precision: 0.9769
  recall: 0.9673
  support: 141953
ambiguous-tokens:
  accuracy: 0.8687
  precision: 0.8449
  recall: 0.8008
  support: 4888

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| _        | 463          | 3           | 305             |
|          |              | 1           | 80              |
|          |              | 2           | 78              |
| 3        | 452          | _           | 429             |
|          |              | 2           | 14              |
|          |              | 1           | 9               |
| 2        | 195          | _           | 155             |
|          |              | 3           | 22              |
|          |              | 1           | 18              |
| 1        | 126          | _           | 88              |
|          |              | 3           | 32              |
|          |              | 2           | 6               |

::: Evaluation report for task: Tense :::

all:
  accuracy: 0.9859
  precision: 0.7494
  recall: 0.6389
  support: 141953
ambiguous-tokens:
  accuracy: 0.8422
  precision: 0.553
  recall: 0.4908
  support: 6072

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| _        | 555          | Perf        | 330             |
|          |              | Pres        | 194             |
|          |              | Fut         | 25              |
|          |              | Impa        | 3               |
|          |              | Pqp         | 3               |
| Perf     | 501          | _           | 246             |
|          |              | Pres        | 161             |
|          |              | Fut         | 78              |
|          |              | Pqp         | 16              |
| Pres     | 477          | _           | 199             |
|          |              | Perf        | 142             |
|          |              | Fut         | 121             |
|          |              | Impa        | 10              |
|          |              | Pqp         | 5               |
| Fut      | 252          | Perf        | 116             |
|          |              | Pres        | 105             |
|          |              | _           | 29              |
|          |              | Impa        | 2               |
| Pqp      | 182          | Perf        | 170             |
|          |              | _           | 6               |
|          |              | Impa        | 5               |
|          |              | Pres        | 1               |
| PeriPerf | 14           | Perf        | 13              |
|          |              | _           | 1               |
| PeriPqp  | 11           | Perf        | 10              |
|          |              | Pqp         | 1               |
| PeriFut  | 9            | Fut         | 6               |
|          |              | Perf        | 3               |
| Impa     | 6            | Pres        | 5               |
|          |              | Pqp         | 1               |

::: Evaluation report for task: Voice :::

all:
  accuracy: 0.9902
  precision: 0.9646
  recall: 0.9684
  support: 141953
ambiguous-tokens:
  accuracy: 0.8813
  precision: 0.8202
  recall: 0.8608
  support: 4784

| Expected | Total Errors | Predictions | Predicted times |
|----------|--------------|-------------|-----------------|
| _        | 555          | Pass        | 279             |
|          |              | Act         | 211             |
|          |              | Dep         | 59              |
|          |              | SemDep      | 6               |
| Pass     | 366          | _           | 230             |
|          |              | Act         | 91              |
|          |              | Dep         | 45              |
| Act      | 342          | _           | 198             |
|          |              | Pass        | 118             |
|          |              | Dep         | 24              |
|          |              | SemDep      | 2               |
| Dep      | 126          | _           | 55              |
|          |              | Pass        | 48              |
|          |              | Act         | 23              |
| SemDep   | 6            | Act         | 3               |
|          |              | _           | 2               |
|          |              | Dep         | 1               |

::: Evaluation report for task: lemma :::

all:
  accuracy: 0.97
  precision: 0.8027
  recall: 0.7951
  support: 141953
ambiguous-tokens:
  accuracy: 0.9049
  precision: 0.5453
  recall: 0.5976
  support: 26151
unknown-targets:
  accuracy: 0.5071
  precision: 0.3358
  recall: 0.3263
  support: 984

| Expected        | Total Errors | Predictions         | Predicted times |
|-----------------|--------------|---------------------|-----------------|
| qvi             | 212          | qvis                | 76              |
|                 |              | qvod                | 64              |
|                 |              | qvam                | 37              |
|                 |              | qvo                 | 30              |
|                 |              | qva                 | 5               |
| qvis            | 178          | qvi                 | 163             |
|                 |              | qvam                | 7               |
|                 |              | qvo                 | 4               |
|                 |              | qva                 | 2               |
|                 |              | cvivs               | 1               |
|                 |              | qvod                | 1               |
| qvod            | 104          | qvi                 | 103             |
|                 |              | qvis                | 1               |
| #               | 44           | ante                | 6               |
|                 |              | privs               | 5               |
|                 |              | benefacio           | 2               |
|                 |              | nam                 | 2               |
|                 |              | pvblicvs            | 2               |
|                 |              | in                  | 1               |
|                 |              | litvs               | 1               |
|                 |              | domator             | 1               |
|                 |              | cvm                 | 1               |
|                 |              | areospantalvs       | 1               |
|                 |              | insignis            | 1               |
|                 |              | prae                | 1               |
|                 |              | destrvo             | 1               |
|                 |              | cavsa               | 1               |
|                 |              | qvisqve             | 1               |
|                 |              | ve                  | 1               |
|                 |              | loqvor              | 1               |
|                 |              | annvs               | 1               |
|                 |              | baccinevs           | 1               |
|                 |              | vetvs               | 1               |
|                 |              | mirandvs            | 1               |
|                 |              | circvm              | 1               |
|                 |              | placeo              | 1               |
|                 |              | precono             | 1               |
|                 |              | do                  | 1               |
|                 |              | svm                 | 1               |
|                 |              | post                | 1               |
|                 |              | parcvs              | 1               |
|                 |              | ivrisconsvltvs      | 1               |
|                 |              | dispar              | 1               |
|                 |              | pallo               | 1               |
|                 |              | svper               | 1               |
| mvltvs          | 36           | mvltvm              | 19              |
|                 |              | mvlti               | 16              |
|                 |              | mvlto               | 1               |
| svi             | 33           | svvs                | 30              |
|                 |              | ipse                | 3               |
| svvs            | 33           | svi                 | 32              |
|                 |              | svvm                | 1               |
| qvam            | 32           | qvi                 | 30              |
|                 |              | qvis                | 2               |
| malvs           | 27           | malvm               | 26              |
|                 |              | male                | 1               |
| qvo             | 26           | qvi                 | 23              |
|                 |              | qvis                | 3               |
| bonvs           | 25           | bonvm               | 19              |
|                 |              | bene                | 4               |
|                 |              | boni                | 2               |
| is              | 23           | eo                  | 21              |
|                 |              | svm                 | 1               |
|                 |              | ecce                | 1               |
| cetervs         | 21           | ceteri              | 15              |
|                 |              | cetera              | 6               |
| parvvs          | 21           | parvm               | 14              |
|                 |              | minimvm             | 5               |
|                 |              | pareo               | 1               |
|                 |              | parvvm              | 1               |
| factvm          | 21           | facio               | 21              |
| boni            | 19           | bonvm               | 15              |
|                 |              | bonvs               | 4               |
| solvs           | 17           | solvm               | 14              |
|                 |              | sol                 | 3               |
| qvantvs         | 16           | qvantvm             | 14              |
|                 |              | qvanto              | 2               |
| primvs          | 16           | primvm              | 11              |
|                 |              | primo               | 5               |
| svpervs         | 15           | svmma               | 10              |
|                 |              | svmmvm              | 4               |
|                 |              | svperi              | 1               |
| mvltvm          | 15           | mvltvs              | 15              |
| pondo           | 15           | pes                 | 15              |
| romani          | 15           | romanvs             | 15              |
| modvs           | 14           | modo                | 14              |
| venio           | 14           | veneo               | 11              |
|                 |              | venia               | 2               |
|                 |              | venvs               | 1               |
| svvm            | 14           | svvs                | 14              |
| anteqvam        | 13           | qvam                | 10              |
|                 |              | qvi                 | 2               |
|                 |              | qvis                | 1               |
| vtor            | 13           | vt                  | 11              |
|                 |              | vsvra               | 1               |
|                 |              | vsvs                | 1               |
| mvlti           | 13           | mvltvs              | 13              |
| vervm           | 12           | vervs               | 10              |
|                 |              | vero                | 2               |
| opera           | 12           | opvs                | 12              |
| svm             | 12           | volo                | 2               |
|                 |              | fvtvrvm             | 2               |
|                 |              | qvo                 | 1               |
|                 |              | homo                | 1               |
|                 |              | sterpo              | 1               |
|                 |              | morigo              | 1               |
|                 |              | qvemadmo            | 1               |
|                 |              | ago                 | 1               |
|                 |              | vanilodvs           | 1               |
|                 |              | foris               | 1               |
| paro            | 11           | paratvs             | 11              |
| bonvm           | 11           | bonvs               | 7               |
|                 |              | boni                | 4               |
| lego            | 11           | lectvs              | 6               |
|                 |              | lex                 | 5               |
| qvantvm         | 10           | qvantvs             | 10              |
| tracta          | 10           | traho               | 10              |
| ego             | 10           | mevs                | 9               |
|                 |              | mino                | 1               |
| liber           | 10           | liberi              | 10              |
| sacer           | 10           | sacrvm              | 10              |
| falsvm          | 10           | falsvs              | 10              |
| eo              | 10           | is                  | 10              |
| vervs           | 10           | vervm               | 8               |
|                 |              | vero                | 2               |
| reliqvvs        | 9            | reliqvi             | 7               |
|                 |              | reliqvvm            | 2               |
| vis             | 9            | vir                 | 8               |
|                 |              | volo                | 1               |
| plervsqve       | 9            | pleriqve            | 9               |
| qva             | 9            | qvi                 | 8               |
|                 |              | qvis                | 1               |
| honestvm        | 9            | honestvs            | 9               |
| pavci           | 9            | pavcvs              | 9               |
| noster          | 9            | nos                 | 5               |
|                 |              | nostri              | 4               |
| nocte           | 9            | nox                 | 9               |
| facio           | 9            | factvm              | 8               |
|                 |              | facies              | 1               |
| volo            | 9            | vis                 | 3               |
|                 |              | volens              | 2               |
|                 |              | volvo               | 2               |
|                 |              | velvm               | 1               |
|                 |              | si                  | 1               |
| tantvs          | 9            | tantvm              | 9               |
| tantvm          | 9            | tantvs              | 9               |
| pavcvs          | 9            | pavci               | 9               |
| reliqvi         | 9            | reliqvvs            | 9               |
| solvm           | 8            | solvs               | 8               |
| honestvs        | 8            | honestvm            | 7               |
|                 |              | honeste             | 1               |
| perdo           | 8            | perditvs            | 8               |
| solitvs         | 8            | soleo               | 5               |
|                 |              | solitvm             | 3               |
| vna             | 7            | vnvs                | 7               |
| oenothea        | 7            | oenothevs           | 7               |
| privsqvam       | 7            | qvam                | 5               |
|                 |              | qvis                | 2               |
| alienvm         | 7            | alienvs             | 7               |
| medivs          | 7            | medivm              | 7               |
| ago             | 7            | age                 | 3               |
|                 |              | agite               | 2               |
|                 |              | actvm               | 2               |
| tv              | 7            | tvvs                | 6               |
|                 |              | ne                  | 1               |
| mali            | 7            | malvm               | 6               |
|                 |              | malvs               | 1               |
| vnvs            | 7            | vna                 | 5               |
|                 |              | vnvm                | 2               |
| aer             | 6            | aes                 | 6               |
| mortvvs         | 6            | morior              | 6               |
| ora             | 6            | os                  | 6               |
| dvbivm          | 6            | dvbivs              | 6               |
| viginti         | 6            | qvinqve             | 3               |
|                 |              | qvatvor             | 1               |
|                 |              | sextvs              | 1               |
|                 |              | dvo                 | 1               |
| ardens          | 6            | ardeo               | 6               |
| reliqvvm        | 6            | reliqvvs            | 6               |
| malvm           | 6            | malvs               | 6               |
| alivs           | 6            | alias               | 5               |
|                 |              | alio                | 1               |
| ivre            | 6            | ivs                 | 6               |
| tvi             | 6            | tvvs                | 6               |
| libra           | 6            | londvs              | 6               |
| natvs           | 6            | nascor              | 6               |
| altvs           | 6            | altvm               | 5               |
|                 |              | alte                | 1               |
| meritvs         | 6            | meritvm             | 3               |
|                 |              | mereor              | 3               |
| consto          | 6            | consisto            | 6               |
| aperio          | 5            | apertvs             | 5               |
| video           | 5            | visvs               | 4               |
|                 |              | ne                  | 1               |
| pareo           | 5            | paro                | 3               |
|                 |              | parro               | 2               |
| antiqvvs        | 5            | antiqvi             | 4               |
|                 |              | antiqvite           | 1               |
| fervs           | 5            | fera                | 5               |
| fvtvrvm         | 5            | fvtvrvs             | 3               |
|                 |              | svm                 | 2               |
| canvs           | 5            | cano                | 2               |
|                 |              | canis               | 2               |
|                 |              | cani                | 1               |
| svmmvm          | 5            | svpervs             | 4               |
|                 |              | svmma               | 1               |
| sacrvm          | 5            | sacer               | 5               |
| rogvs           | 5            | rogo                | 5               |
| hirnea          | 5            | hirnevs             | 3               |
|                 |              | irnevs              | 2               |
| nascor          | 5            | natvs               | 5               |
| fvtvrvs         | 5            | svm                 | 4               |
|                 |              | fvtvrvm             | 1               |
| pompeianvs      | 5            | pompeiani           | 5               |
| rapax           | 5            | rapaces             | 2               |
|                 |              | rapaci              | 1               |
|                 |              | rapacivs            | 1               |
|                 |              | rapace              | 1               |
| tvvs            | 5            | tv                  | 4               |
|                 |              | tvi                 | 1               |
| iacio           | 5            | iaceo               | 5               |
| magnvm          | 5            | magnvs              | 5               |
| regivs          | 5            | regia               | 4               |
|                 |              | regio               | 1               |
| mando           | 5            | mandatvm            | 5               |
| nymphon         | 5            | nymphvs             | 3               |
|                 |              | nympho              | 2               |
| dedo            | 5            | do                  | 4               |
|                 |              | deditvs             | 1               |
| adversvs        | 5            | adversvm            | 5               |
| bene            | 5            | bonvs               | 5               |
| secretvm        | 5            | secretvs            | 5               |
| ante            | 5            | #                   | 5               |
| falsvs          | 4            | falsvm              | 2               |
|                 |              | falso               | 1               |
|                 |              | false               | 1               |
| vargvnteivs     | 4            | vargvntivs          | 3               |
|                 |              | vargvntesivs        | 1               |
| areo            | 4            | aro                 | 4               |
| idem            | 4            | eodem               | 4               |
| consvlto        | 4            | consvltvm           | 4               |
| mala            | 4            | malvs               | 4               |
| potissimvm      | 4            | potivs              | 4               |
| ratvs           | 4            | reor                | 3               |
|                 |              | ratis               | 1               |
| infervs         | 4            | imvm                | 2               |
|                 |              | inferi              | 1               |
|                 |              | infvmvs             | 1               |
| magnvs          | 4            | maiores             | 4               |
| pvllo           | 4            | pvllvs              | 4               |
| nos             | 4            | noster              | 4               |
| veteres         | 4            | vetvs               | 4               |
| affectvs        | 4            | afficio             | 4               |
| revs            | 4            | res                 | 4               |
| svspendo        | 4            | svspensvs           | 4               |
| inanis          | 4            | inane               | 4               |
| insignis        | 4            | insigne             | 4               |
| caelestes       | 4            | caelestis           | 3               |
|                 |              | caelestia           | 1               |
| faesvlae        | 4            | faesvla             | 3               |
|                 |              | faesvli             | 1               |
| svllanvs        | 4            | syllanvs            | 4               |
| lino            | 4            | linqvo              | 3               |
|                 |              | levo                | 1               |
| ivro            | 4            | ivs                 | 2               |
|                 |              | ivratvs             | 1               |
|                 |              | ivratvra            | 1               |
| svmma           | 4            | svpervs             | 3               |
|                 |              | svmmvm              | 1               |
| catinvm         | 4            | catinvs             | 4               |
| orno            | 4            | ornatvs             | 3               |
|                 |              | ornate              | 1               |
| antiqvi         | 4            | antiqvvs            | 4               |
| propinqvi       | 4            | propinqvvs          | 4               |
| pango           | 4            | pactvm              | 3               |
|                 |              | paciscor            | 1               |
| paratvs         | 4            | paro                | 4               |
| nostri          | 4            | noster              | 4               |
| remotvs         | 4            | removeo             | 4               |
| mevs            | 4            | ego                 | 3               |
|                 |              | mei                 | 1               |
| ne              | 4            | ceres               | 1               |
|                 |              | nosco               | 1               |
|                 |              | ego                 | 1               |
|                 |              | nvllvs              | 1               |
| minimvm         | 4            | parvvs              | 4               |
| propior         | 4            | proximvm            | 3               |
|                 |              | prope               | 1               |
| armatvs         | 4            | armati              | 4               |
| medivm          | 4            | medivs              | 4               |
| mvnitvs         | 4            | mvnio               | 4               |
| exter           | 4            | extremvm            | 4               |
| refero          | 4            | refert              | 4               |
| captiva         | 4            | captivvs            | 4               |
| dicto           | 4            | dictvm              | 2               |
|                 |              | dictatvm            | 1               |
|                 |              | dico                | 1               |
| volens          | 4            | volo                | 4               |
| falernvm        | 4            | falernvs            | 4               |
| sexcenti        | 4            | sescenti            | 4               |
| apertvs         | 4            | aperio              | 4               |
| milito          | 4            | militaris           | 3               |
|                 |              | miles               | 1               |
| refert          | 4            | refero              | 4               |
| mei             | 4            | mevs                | 4               |
| bellvs          | 4            | bellvm              | 4               |
| cvrivs          | 4            | cvrvs               | 3               |
|                 |              | cvrio               | 1               |
| elorvs          | 4            | helores             | 2               |
|                 |              | helorvs             | 1               |
|                 |              | heli                | 1               |
| maiores         | 4            | magnvs              | 4               |
| graecvs         | 4            | graeci              | 4               |
| glycon          | 4            | glycvs              | 4               |
| dictvm          | 4            | dico                | 4               |
| apivm           | 4            | apivs               | 2               |
|                 |              | apis                | 1               |
|                 |              | apio                | 1               |
| nosco           | 3            | notvs               | 2               |
|                 |              | ne                  | 1               |
| thessali        | 3            | thessalvs           | 2               |
|                 |              | thessalis           | 1               |
| immensvs        | 3            | immensvm            | 3               |
| vetvs           | 3            | veteres             | 2               |
|                 |              | vetera              | 1               |
| praesentia      | 3            | praesens            | 2               |
|                 |              | praesvm             | 1               |
| cognitvs        | 3            | cognosco            | 3               |
| em              | 3            | hem                 | 3               |
| artvs           | 3            | ars                 | 2               |
|                 |              | arte                | 1               |
| qvisnam         | 3            | qvis                | 2               |
|                 |              | qvonam              | 1               |
| ferio           | 3            | fervs               | 3               |
| actvs           | 3            | ago                 | 3               |
| comitivm        | 3            | comitia             | 3               |
| consvlo         | 3            | consvltvm           | 1               |
|                 |              | consvl              | 1               |
|                 |              | consvlatvs          | 1               |
| acerronia       | 3            | acerronivs          | 3               |
| incipio         | 3            | inceptvm            | 3               |
| edo             | 3            | svm                 | 2               |
|                 |              | editvs              | 1               |
| lavtvs          | 3            | lavo                | 3               |
| coqvvs          | 3            | coqvo               | 3               |
| veto            | 3            | votvm               | 2               |
|                 |              | vetvo               | 1               |
| mervs           | 3            | mervm               | 3               |
| dico            | 3            | dictvm              | 3               |
| como            | 3            | compito             | 2               |
|                 |              | comptvs             | 1               |
| exentero        | 3            | exintero            | 3               |
| fero            | 3            | fera                | 2               |
|                 |              | ferio               | 1               |
| sponte          | 3            | spons               | 3               |
| novvs           | 3            | nosco               | 3               |
| mereor          | 3            | meritvm             | 2               |
|                 |              | merens              | 1               |
| vt              | 3            | vtor                | 3               |
| exanimis        | 3            | exanimvs            | 3               |
| tertivs         | 3            | tertio              | 3               |
| arcessitvs      | 3            | arcesso             | 3               |
| vomo            | 3            | vomens              | 2               |
|                 |              | vomer               | 1               |
| respvblica      | 3            | res                 | 2               |
|                 |              | reipvblica          | 1               |
| pasco           | 3            | pascor              | 3               |
| therapontigonvs | 3            | therapontivs        | 2               |
|                 |              | therapontinvs       | 1               |
| acceptvs        | 3            | accipio             | 2               |
|                 |              | acceps              | 1               |
| sol             | 3            | solvm               | 1               |
|                 |              | solvs               | 1               |
|                 |              | soleo               | 1               |
| nvbo            | 3            | nvpta               | 3               |
| navigans        | 3            | navigo              | 3               |
| sestertivm      | 3            | sestertivs          | 2               |
|                 |              | hic                 | 1               |
| malo            | 3            | malvm               | 2               |
|                 |              | malvs               | 1               |
| laxvs           | 3            | laxe                | 2               |
|                 |              | laxo                | 1               |
| strobilvs       | 3            | strobilis           | 3               |
| qvisqve         | 3            | qvoqve              | 2               |
|                 |              | qvisqvis            | 1               |
| testvm          | 3            | testvs              | 3               |
| perpetvvs       | 3            | perpetvo            | 3               |
| victvs          | 3            | vinco               | 3               |
| laxe            | 3            | lax                 | 3               |
| hvc             | 3            | hic                 | 3               |
| facilis         | 3            | facile              | 3               |
| sextarivs       | 3            | semis               | 3               |
| dvctvs          | 3            | dvco                | 3               |
| mille           | 3            | triginta            | 1               |
|                 |              | octo                | 1               |
|                 |              | dvo                 | 1               |
| dvodeviginti    | 3            | octo                | 1               |
|                 |              | triginta            | 1               |
|                 |              | decimvs             | 1               |
| fraces          | 3            | frax                | 3               |
| abiectvs        | 3            | abicio              | 3               |
| acta            | 3            | ago                 | 2               |
|                 |              | actvm               | 1               |
| conivngo        | 3            | conivnctvs          | 3               |
| ceteri          | 3            | cetervs             | 3               |
| alica           | 3            | alicvs              | 2               |
|                 |              | halica              | 1               |
| secvndvs        | 3            | secvndvm            | 3               |
| cycnvs          | 3            | cycna               | 3               |
| dvco            | 3            | dvcenti             | 2               |
|                 |              | dvx                 | 1               |
| qvanto          | 3            | qvantvs             | 3               |
| viso            | 3            | video               | 3               |
| liceor          | 3            | licet               | 2               |
|                 |              | liceo               | 1               |
| spons           | 3            | sponte              | 3               |
| privs           | 3            | #                   | 3               |
| placo           | 3            | placeo              | 3               |
| dexter          | 3            | dextera             | 2               |
|                 |              | dextervs            | 1               |
| alio            | 3            | alivs               | 3               |
| mane            | 3            | maneo               | 3               |
| laevvm          | 3            | laevvs              | 2               |
|                 |              | laeva               | 1               |
| nvpta           | 3            | nvbo                | 3               |
| sicvlvs         | 3            | sicvli              | 3               |
| hac             | 3            | hic                 | 3               |
| volvcris        | 3            | volvcer             | 3               |
| prodeo          | 3            | prodo               | 3               |
| avvs            | 3            | avis                | 3               |
| adversvm        | 3            | adversvs            | 3               |
| pario           | 3            | partvs              | 2               |
|                 |              | pars                | 1               |
| lectvs          | 3            | lego                | 3               |
| vrbane          | 3            | vrbanvs             | 3               |
| qviris          | 3            | qvirites            | 3               |
| desertvs        | 3            | deserta             | 3               |
| primo           | 3            | primvs              | 3               |
| decorvs         | 3            | decvs               | 3               |
| exstrvo         | 3            | extrvo              | 3               |
| proximvm        | 3            | propior             | 3               |
| arte            | 3            | ars                 | 3               |
| ardeo           | 3            | ardens              | 3               |
| commis          | 3            | cvmmis              | 3               |
| xenon           | 3            | xenonis             | 2               |
|                 |              | xenvs               | 1               |
| imvm            | 3            | infervs             | 3               |
| pendo           | 3            | pendeo              | 3               |
| certvm          | 3            | certvs              | 3               |
| alias           | 3            | alivs               | 3               |
| ivssvm          | 3            | ivbeo               | 3               |
| bomilcar        | 3            | bomilcarvs          | 2               |
|                 |              | bomilcaris          | 1               |
| debitvm         | 3            | debeo               | 3               |
| rego            | 3            | rex                 | 3               |
| pedes           | 3            | pes                 | 3               |
| gypso           | 2            | gypsatvs            | 2               |
| benefacio       | 2            | #                   | 2               |
| aversvs         | 2            | averto              | 2               |
| fera            | 2            | fervs               | 1               |
|                 |              | fero                | 1               |
| paveo           | 2            | pasco               | 2               |
| lapsvs          | 2            | labor               | 2               |
| rvbens          | 2            | rvbeo               | 2               |
| pvblicvm        | 2            | pvblicvs            | 2               |
| infectvs        | 2            | inficio             | 2               |
| lavrevs         | 2            | lavrea              | 2               |
| vlpicvm         | 2            | vlpicvs             | 2               |
| aes             | 2            | aer                 | 2               |
| afficio         | 2            | affectvs            | 2               |
| nvmqvis         | 2            | nvmqvid             | 2               |
| potis           | 2            | potivs              | 2               |
| alo             | 2            | ala                 | 1               |
|                 |              | alar                | 1               |
| pvgna           | 2            | pvgnvs              | 2               |
| svperstitiosvs  | 2            | svpersttitvs        | 1               |
|                 |              | svpersttitiosvs     | 1               |
| compositvs      | 2            | compono             | 2               |
| nvmero          | 2            | nvmervs             | 2               |
| editvs          | 2            | edo                 | 2               |
| lvdificor       | 2            | lvdifico            | 2               |
| manes           | 2            | manvs               | 2               |
| sollemnis       | 2            | sollemne            | 2               |
| svcinvm         | 2            | svcinvs             | 2               |
| confvsvs        | 2            | confvndo            | 2               |
| meto            | 2            | metor               | 1               |
|                 |              | metior              | 1               |
| achillides      | 2            | achillis            | 2               |
| vittatvs        | 2            | vitto               | 2               |
| ivdico          | 2            | ivdex               | 2               |
| spondylvs       | 2            | spondylivm          | 2               |
| malevolvs       | 2            | malivolvs           | 2               |
| ceveo           | 2            | cevo                | 1               |
|                 |              | cevio               | 1               |
| confvndo        | 2            | confvsvs            | 2               |
| gener           | 2            | genvs               | 2               |
| texo            | 2            | textvm              | 1               |
|                 |              | tego                | 1               |
| certo           | 2            | certvs              | 2               |
| modo            | 2            | modvs               | 2               |
| cetera          | 2            | cetervs             | 2               |
| fortvita        | 2            | fortvitvs           | 2               |
| exsero          | 2            | exero               | 1               |
|                 |              | exerio              | 1               |
| erectvs         | 2            | erigo               | 2               |
| niteo           | 2            | nitor               | 2               |
| fvsvs           | 2            | fvndo               | 2               |
| opto            | 2            | optatvs             | 1               |
|                 |              | optatvm             | 1               |
| fretvs          | 2            | fretvm              | 2               |
| caneo           | 2            | cano                | 2               |
| praescriptvm    | 2            | praescribo          | 2               |
| clavdiopolitani | 2            | clavdiopentia       | 1               |
|                 |              | clavdiopitani       | 1               |
| vehemens        | 2            | vehementer          | 2               |
| decretvm        | 2            | decerno             | 2               |
| servvs          | 2            | serva               | 1               |
|                 |              | servo               | 1               |
| terni           | 2            | ternvs              | 2               |
| interiacio      | 2            | intericio           | 2               |
| egero           | 2            | ago                 | 2               |
| legatvm         | 2            | legatvs             | 2               |
| regia           | 2            | regivs              | 2               |
| satvr           | 2            | sero                | 2               |
| satis           | 2            | ne                  | 1               |
|                 |              | sero                | 1               |
| svperior        | 2            | svpervs             | 2               |
| ramale          | 2            | ramalia             | 1               |
|                 |              | ramalis             | 1               |
| hospitivm       | 2            | hospes              | 2               |
| vetera          | 2            | vetvs               | 2               |
| percvnctor      | 2            | percontor           | 2               |
| hippias         | 2            | hippia              | 2               |
| macro           | 2            | macer               | 2               |
| isti            | 2            | iste                | 2               |
| confinivm       | 2            | confinis            | 2               |
| svpplex         | 2            | svpplicivm          | 2               |
| sincipvt        | 2            | sincipo             | 1               |
|                 |              | sincipitvs          | 1               |
| vos             | 2            | vester              | 2               |
| operio          | 2            | opertvs             | 2               |
| scriptvm        | 2            | scribo              | 2               |
| infortvnatvs    | 2            | infortvnvs          | 2               |
| brvttivs        | 2            | brvttia             | 2               |
| pilvs           | 2            | pilvm               | 2               |
| coeptvm         | 2            | coepio              | 2               |
| conatvs         | 2            | conor               | 2               |
| antiphanes      | 2            | antiphanvs          | 2               |
| oeta            | 2            | oeten               | 2               |
| insido          | 2            | insideo             | 2               |
| propivs         | 2            | prope               | 2               |
| derelinqvo      | 2            | derelico            | 2               |
| sacratvs        | 2            | sacrate             | 1               |
|                 |              | sacro               | 1               |
| odiose          | 2            | odiosvs             | 2               |
| vnvm            | 2            | vnvs                | 2               |
| vipstanvs       | 2            | vipsanivs           | 2               |
| promissvm       | 2            | promitto            | 2               |
| cantaber        | 2            | cantabre            | 1               |
|                 |              | cantabrvs           | 1               |
| tribvs          | 2            | tres                | 2               |
| ingemisco       | 2            | ingemo              | 1               |
|                 |              | ingemesco           | 1               |
| nitens          | 2            | nitor               | 2               |
| praeficio       | 2            | praefectvs          | 2               |
| senior          | 2            | senex               | 2               |
| orior           | 2            | oriens              | 2               |
| proiectvs       | 2            | proicio             | 2               |
| prospera        | 2            | prosper             | 2               |
| vter            | 2            | vtrvm               | 2               |
| marsyas         | 2            | marsya              | 2               |
| cornelia        | 2            | cornelivs           | 2               |
| nox             | 2            | noctv               | 2               |
| mensa           | 2            | mensis              | 2               |
| tintinnabvlvm   | 2            | tintinnalis         | 1               |
|                 |              | tintinnalivm        | 1               |
| parcvs          | 2            | parco               | 1               |
|                 |              | parce               | 1               |
| nonae           | 2            | nonvs               | 2               |
| arcas           | 2            | arcades             | 2               |
| citvs           | 2            | cito                | 2               |
| ample           | 2            | amplvs              | 2               |
| fictvs          | 2            | fingo               | 2               |
| diivngo         | 2            | diivnctvs           | 2               |
| gortynivs       | 2            | cortynivm           | 1               |
|                 |              | cortynivs           | 1               |
| dvrvm           | 2            | dvrvs               | 2               |
| iactvs          | 2            | iacio               | 1               |
|                 |              | iaciscor            | 1               |
| evergetae       | 2            | evergeta            | 2               |
| assyrivs        | 2            | assyria             | 2               |
| venia           | 2            | venio               | 2               |
| vsvs            | 2            | vtor                | 2               |
| moveo           | 2            | motvs               | 2               |
| profvndvs       | 2            | profvndvm           | 2               |
| properans       | 2            | propero             | 2               |
| scribo          | 2            | scriptvm            | 1               |
|                 |              | scriba              | 1               |
| impendo         | 2            | impendeo            | 2               |
| centvm          | 2            | triginta            | 1               |
|                 |              | clel                | 1               |
| trecenti        | 2            | octo                | 1               |
|                 |              | triginta            | 1               |
| sestertiarivs   | 2            | sestertivs          | 2               |
| sycophanta      | 2            | sycophantvs         | 2               |
| danavs          | 2            | danai               | 2               |
| rectvm          | 2            | rectvs              | 2               |
| ab              | 2            | ah                  | 2               |
| pvllvm          | 2            | pvllvs              | 2               |
| vaccenses       | 2            | vagenses            | 2               |
| diligo          | 2            | diligens            | 1               |
|                 |              | dilectvs            | 1               |
| colvbra         | 2            | colvber             | 2               |
| palleo          | 2            | pallens             | 2               |
| saeptvm         | 2            | saepio              | 2               |
| sinister        | 2            | sinistra            | 2               |
| viridans        | 2            | virido              | 2               |
| effvndo         | 2            | effvsvs             | 2               |
| dissimvlanter   | 2            | dissimvlatim        | 1               |
|                 |              | dissimvlatile       | 1               |
| contemptvs      | 2            | contemno            | 2               |
| alternvs        | 2            | alternis            | 2               |
| desero          | 2            | desertvs            | 2               |
| vanvm           | 2            | vanvs               | 2               |
| apvlvs          | 2            | apvla               | 2               |
| soleo           | 2            | solea               | 2               |
| doceo           | 2            | doctvs              | 2               |
| presse          | 2            | pressvs             | 2               |
| absvm           | 2            | absim               | 2               |
| praeceptor      | 2            | praeceptvm          | 2               |
| ea              | 2            | is                  | 2               |
| habitvs         | 2            | habeo               | 2               |
| svspensvs       | 2            | svspendo            | 2               |
| propositvm      | 2            | propono             | 2               |
| tvlingi         | 2            | tvlingvs            | 1               |
|                 |              | tvlingorvs          | 1               |
| latvs           | 2            | lateo               | 1               |
|                 |              | fero                | 1               |
| naris           | 2            | no                  | 2               |
| volvo           | 2            | volo                | 2               |
| brevis          | 2            | brevi               | 2               |
| helena          | 2            | helene              | 2               |
| sempronia       | 2            | sempronivs          | 2               |
| cavtvs          | 2            | caveo               | 2               |
| mereo           | 2            | meritvs             | 1               |
|                 |              | mereor              | 1               |
| sibylla         | 2            | sibvlla             | 2               |
| decor           | 2            | decvs               | 2               |
| egens           | 2            | egeo                | 2               |
| qvamlibet       | 2            | qvilibet            | 2               |
| commodvs        | 2            | commodvm            | 2               |
| totvm           | 2            | totvs               | 2               |
| conor           | 2            | conatvs             | 1               |
|                 |              | conatvra            | 1               |
| svbvrbanvm      | 2            | svbvrbanvs          | 2               |
| sardes          | 2            | sardi               | 2               |
| vltimvm         | 2            | vltimvs             | 2               |
| pone            | 2            | pono                | 2               |
| qvoqve          | 2            | qvisqve             | 2               |
| exqviro         | 2            | exqvisitvs          | 2               |
| compedio        | 2            | compeditvm          | 1               |
|                 |              | compeditvs          | 1               |
| iecvr           | 2            | iecvs               | 2               |
| classicvs       | 2            | classicvm           | 2               |
| venalis         | 2            | venales             | 1               |
|                 |              | nalis               | 1               |
| scio            | 2            | scisco              | 1               |
|                 |              | sciens              | 1               |
| cito            | 2            | citatvs             | 1               |
|                 |              | cieo                | 1               |
| flvctvo         | 2            | flvctvor            | 2               |
| extentvs        | 2            | extendo             | 2               |
| qvinqvaginta    | 2            | qvinqve             | 1               |
|                 |              | dvcenti             | 1               |
| sex             | 2            | sextvs              | 1               |
|                 |              | triginta            | 1               |
| svbivgivs       | 2            | svbivgivm           | 2               |
| cadvcvm         | 2            | cadvcvs             | 2               |
| cotylo          | 2            | cotylon             | 1               |
|                 |              | cotylvs             | 1               |
| tremebvndvs     | 2            | tremibvndvs         | 2               |
| coqvo           | 2            | coco                | 2               |
| calefacio       | 2            | callacio            | 1               |
|                 |              | callacito           | 1               |
| vascvlvm        | 2            | vascvla             | 2               |
| bosporvs        | 2            | bosphorvs           | 2               |
| beneficvs       | 2            | beneficivm          | 1               |
|                 |              | beneficens          | 1               |
| plvton          | 2            | plvto               | 1               |
|                 |              | plvtona             | 1               |
| sedvco          | 2            | sedvctvs            | 2               |
| solvtvs         | 2            | solvo               | 2               |
| peloponnesii    | 2            | peloponnia          | 1               |
|                 |              | peloponniensis      | 1               |
| revereor        | 2            | reverendo           | 2               |
| phoebe          | 2            | phoebvs             | 2               |
| sino            | 2            | sine                | 2               |
| aricia          | 2            | aricivs             | 2               |
| scelerati       | 2            | sceleratvs          | 2               |
| pressvs         | 2            | premo               | 2               |
| plvvivs         | 2            | plvvia              | 2               |
| sero            | 2            | satis               | 1               |
|                 |              | sera                | 1               |
| poeas           | 2            | poeans              | 2               |
| pecto           | 2            | pexvs               | 1               |
|                 |              | pecta               | 1               |
| sardonyx        | 2            | sardonyface         | 1               |
|                 |              | sardonycera         | 1               |
| svmo            | 2            | svmptvs             | 2               |
| singvla         | 2            | singvlvs            | 2               |
| pertvrbo        | 2            | pertvrbatvs         | 2               |
| mvllvs          | 2            | mvlli               | 2               |
| qvoqvo          | 2            | qvisqvis            | 2               |
| remisse         | 2            | remitto             | 2               |
| pinarvs         | 2            | pinae               | 1               |
|                 |              | pinares             | 1               |
| pingo           | 2            | pictvs              | 2               |
| horrendvm       | 2            | horrendvs           | 2               |
| natis           | 2            | natvs               | 2               |
| gravis          | 2            | graviter            | 2               |
| irascor         | 2            | iratvs              | 2               |
| nerevs          | 2            | nerea               | 2               |
| annvvm          | 2            | annvvs              | 2               |
| hervs           | 2            | svm                 | 2               |
| contexo         | 2            | contextvs           | 2               |
| grosphvs        | 2            | grosphes            | 1               |
|                 |              | grospvs             | 1               |
| patrivs         | 2            | patria              | 2               |
| fido            | 2            | fidens              | 2               |
| tvtvm           | 2            | tvtvs               | 2               |
| profvndo        | 2            | profvsvs            | 2               |
| profectvs       | 2            | proficiscor         | 2               |
| tvrbatvs        | 2            | tvrbo               | 2               |
| nvbes           | 2            | nvbo                | 2               |
| refvgvs         | 2            | refvgio             | 2               |
| sanctvs         | 2            | sancte              | 2               |
| volvcer         | 2            | volvcris            | 2               |
| convictvs       | 2            | convinco            | 2               |
| serivm          | 2            | serivs              | 2               |
| tempero         | 2            | temperatvs          | 2               |
| qvietvs         | 2            | qvies               | 2               |
| intersaepio     | 2            | intersipio          | 2               |
| fortvitvs       | 2            | fortvita            | 2               |
| commvne         | 2            | commvnis            | 2               |
| delphin         | 2            | delphina            | 1               |
|                 |              | delphines           | 1               |
| expressvs       | 2            | exprimo             | 2               |
| tarracinensis   | 2            | terracinensis       | 2               |
| mvrgantinvs     | 2            | mvrgentinvs         | 2               |
| pecco           | 2            | peccans             | 2               |
| qvatvordecim    | 2            | tredecim            | 1               |
|                 |              | tertivs             | 1               |
| lvpinvm         | 2            | lvpinvs             | 2               |
| nabdalsa        | 2            | nabdalsvs           | 2               |
| amo             | 2            | amans               | 2               |
| opvs            | 2            | opera               | 2               |
| consvo          | 2            | consvesco           | 2               |
| cydas           | 2            | cydae               | 1               |
|                 |              | cyda                | 1               |
| prior           | 2            | privs               | 2               |
| camers          | 2            | camertvs            | 1               |
|                 |              | camertes            | 1               |
| primoris        | 2            | primores            | 2               |
| albvm           | 2            | albvs               | 2               |
| vester          | 2            | vos                 | 2               |
| troivs          | 2            | troia               | 2               |
| libita          | 2            | libet               | 2               |
| incertvm        | 2            | incertvs            | 2               |
| proprivm        | 2            | proprivs            | 2               |
| qvicvmqve       | 2            | qvocvmqve           | 1               |
|                 |              | qvisqvis            | 1               |
| velvm           | 2            | volo                | 2               |
| hesperivs       | 2            | hesperia            | 2               |
| tener           | 2            | teneo               | 2               |
| licet           | 2            | liceto              | 1               |
|                 |              | licetvs             | 1               |
| svbitvm         | 2            | svbitvs             | 2               |
| altvm           | 2            | altvs               | 2               |
| vltimvs         | 2            | vltimvm             | 2               |
| germanvs        | 2            | germani             | 2               |
| clodia          | 2            | clodivs             | 2               |
| visvs           | 2            | video               | 2               |
| alienvs         | 2            | alienvm             | 2               |
| percoqvo        | 2            | percoqvor           | 1               |
|                 |              | percoco             | 1               |
| testv           | 2            | testvs              | 2               |
| tracto          | 2            | traho               | 1               |
|                 |              | tractatvs           | 1               |
| fvlgens         | 2            | fvlgeo              | 2               |
| convictolitavis | 2            | convictolitavicilas | 1               |
|                 |              | convictatio         | 1               |
| sollicitvs      | 2            | sollicite           | 1               |
|                 |              | sollicito           | 1               |
| trinacria       | 2            | trinacrivs          | 2               |
| constratvs      | 2            | consterno           | 2               |
| italvs          | 2            | itali               | 2               |
| dvodeni         | 2            | dvodenvs            | 2               |
| directvs        | 2            | dirigo              | 2               |
| parthvs         | 2            | parthi              | 2               |
| myoparon        | 2            | myoporo             | 1               |
|                 |              | myopor              | 1               |
| vacca           | 2            | vaca                | 1               |
|                 |              | vaga                | 1               |
| gallvs          | 2            | galli               | 2               |
| moror           | 2            | morior              | 1               |
|                 |              | moratvs             | 1               |
| odoro           | 2            | odoratvs            | 2               |
| vado            | 2            | vas                 | 1               |
|                 |              | vadvm               | 1               |
| actvm           | 2            | ago                 | 2               |
| intentvs        | 2            | intendo             | 2               |
| pilevm          | 2            | pilevs              | 2               |
| aveo            | 2            | haveo               | 2               |
|                 | 2            | svm                 | 2               |
| qvinqvatrvs     | 2            | qvinqvatrix         | 1               |
|                 |              | qvinqvatrivs        | 1               |
| vigilans        | 2            | vigilo              | 2               |
| qvantvlvm       | 2            | qvantvlvs           | 2               |
| svccingo        | 2            | svbcingo            | 2               |
| avla            | 2            | ille                | 1               |
|                 |              | illa                | 1               |
| pessvlvs        | 2            | pessvlo             | 1               |
|                 |              | pessvlvm            | 1               |
| arcanvm         | 2            | arcanvs             | 2               |
| praesens        | 2            | praesentia          | 1               |
|                 |              | praesvm             | 1               |
| verna           | 2            | vernvs              | 2               |
| picenvs         | 2            | picenvm             | 2               |
| pvblicvs        | 2            | pvblicvm            | 2               |
| disco           | 2            | discvm              | 1               |
|                 |              | discvs              | 1               |
| ivstvs          | 2            | ivsta               | 2               |
| erigo           | 2            | erectvs             | 2               |
| maga            | 2            | magvs               | 2               |
| servo           | 2            | servvs              | 2               |
| svesco          | 2            | svetvs              | 2               |
| nimivs          | 2            | nimivm              | 2               |
| appositvs       | 2            | appono              | 2               |
| lydivs          | 2            | lydia               | 2               |
| heracleon       | 2            | heraclevs           | 2               |
| mvlto           | 2            | mvltvs              | 2               |
| distero         | 2            | disto               | 1               |
|                 |              | disterno            | 1               |
| tvtor           | 2            | tvtvs               | 2               |
| praeparatvs     | 2            | praeparo            | 2               |
| serrana         | 2            | serranvs            | 2               |
| vaccvs          | 2            | vaccivs             | 2               |
| loqvo           | 2            | loqvor              | 2               |
| ingratvs        | 2            | ingratis            | 1               |
|                 |              | ingrate             | 1               |
| necessarivs     | 1            | necessario          | 1               |
| scelerate       | 1            | sceleratvs          | 1               |
| svgillo         | 1            | svggillatvs         | 1               |
| obsido          | 1            | obsideo             | 1               |
| perpavcvs       | 1            | perpavci            | 1               |
| echecratides    | 1            | echecraticvs        | 1               |
| qvidam          | 1            | qvamdam             | 1               |
| femen           | 1            | femina              | 1               |
| svs             | 1            | svi                 | 1               |
| fonteivs        | 1            | fonteia             | 1               |
| clodivs         | 1            | clodia              | 1               |
| thebani         | 1            | thebanvs            | 1               |
| gangaba         | 1            | gango               | 1               |
| palpor          | 1            | palpo               | 1               |
| lvdicer         | 1            | lvdicrvm            | 1               |
| poto            | 1            | poti                | 1               |
| oscitans        | 1            | oscito              | 1               |
| paphlagona      | 1            | paphlagones         | 1               |
| sinopa          | 1            | sinopes             | 1               |
| arabes          | 1            | arabs               | 1               |
| cara            | 1            | caras               | 1               |
| cretanvs        | 1            | cretani             | 1               |
| syrvs           | 1            | syri                | 1               |
| rhodia          | 1            | rhodivs             | 1               |
| perbibesia      | 1            | perbibesis          | 1               |
| centavromachia  | 1            | centavranes         | 1               |
| vnomammivs      | 1            | vnomammia           | 1               |
| conterebromnivs | 1            | conterebion         | 1               |
| paeniteo        | 1            | paenitens           | 1               |
| metrvm          | 1            | metro               | 1               |
| svevvs          | 1            | svevi               | 1               |
| foliatvm        | 1            | folio               | 1               |
| mavors          | 1            | mars                | 1               |
| sipho           | 1            | sipvs               | 1               |
| corinthii       | 1            | corinthivs          | 1               |
| medipontvs      | 1            | melipontvs          | 1               |
| qvalvm          | 1            | qvalvs              | 1               |
| controversiosvs | 1            | controversia        | 1               |
| confessvs       | 1            | confessvm           | 1               |
| porrvm          | 1            | porrvs              | 1               |
| allivm          | 1            | alivs               | 1               |
| commissvm       | 1            | committo            | 1               |
| cassivs         | 1            | cassii              | 1               |
| sicyon          | 1            | sicyo               | 1               |
| tergeminvs      | 1            | trigeminvs          | 1               |
| phileros        | 1            | phileron            | 1               |
| vacvvm          | 1            | vacvvs              | 1               |
| apertvm         | 1            | apertvs             | 1               |
| raptvs          | 1            | rapio               | 1               |
| svbeo           | 1            | svbite              | 1               |
| stvlti          | 1            | stvltvs             | 1               |
| antivm          | 1            | antivs              | 1               |
| bavli           | 1            | bavlvs              | 1               |
| rapacida        | 1            | rapacidvs           | 1               |
| exsecror        | 1            | exsecrans           | 1               |
| avdio           | 1            | avditvs             | 1               |
| fvrens          | 1            | fvro                | 1               |
| praesvm         | 1            | praesentia          | 1               |
| excors          | 1            | excordis            | 1               |
| horreo          | 1            | horrens             | 1               |
| thracivs        | 1            | thracia             | 1               |
| pavsanias       | 1            | pavsania            | 1               |
| thesavrvm       | 1            | thesavrvs           | 1               |
| piget           | 1            | pigendvs            | 1               |
| ver             | 1            | vervs               | 1               |
| tanagraevs      | 1            | tanagraea           | 1               |
| neapolitanvs    | 1            | neapolitani         | 1               |
| exsto           | 1            | exsisto             | 1               |
| amice           | 1            | amicvs              | 1               |
| ambigvvm        | 1            | ambigvvs            | 1               |
| arabs           | 1            | arabes              | 1               |
| plene           | 1            | plenvs              | 1               |
| breviter        | 1            | brevis              | 1               |
| velociter       | 1            | velox               | 1               |
| gesto           | 1            | gestor              | 1               |
| obtvro          | 1            | optvro              | 1               |
| agnosco         | 1            | agnitvs             | 1               |
| phthias         | 1            | phthi               | 1               |
| calvmnior       | 1            | calvmniaris         | 1               |
| eadem           | 1            | idem                | 1               |
| faenvs          | 1            | fenvs               | 1               |
| hederacevs      | 1            | hederacia           | 1               |
| thersites       | 1            | thersitvs           | 1               |
| tvscvlvm        | 1            | tvscvlvs            | 1               |
| florevs         | 1            | floreo              | 1               |
| lynx            | 1            | lynca               | 1               |
| delvmbis        | 1            | delvmbo             | 1               |
| verno           | 1            | vernvs              | 1               |
| soccatvs        | 1            | socco               | 1               |
| epigrvs         | 1            | epigri              | 1               |
| occipvt         | 1            | occipio             | 1               |
| circvmfodio     | 1            | circvmfvndo         | 1               |
| concitatvs      | 1            | concito             | 1               |
| phthisis        | 1            | phthisio            | 1               |
| aleivs          | 1            | aleia               | 1               |
| pvlmentarivm    | 1            | pvlmentarivs        | 1               |
| pertristis      | 1            | pertrinto           | 1               |
| incontinentia   | 1            | incontinitas        | 1               |
| philomelienses  | 1            | philomelenienses    | 1               |
| simvl           | 1            | simvlac             | 1               |
| ephemeris       | 1            | ephemeridae         | 1               |
| ivrgivm         | 1            | ivrgo               | 1               |
| neo             | 1            | neta                | 1               |
| svperi          | 1            | svpervs             | 1               |
| sicco           | 1            | siccvs              | 1               |
| progressvs      | 1            | progredior          | 1               |
| veneriae        | 1            | veneria             | 1               |
| circvmcido      | 1            | circvmcisvs         | 1               |
| phintia         | 1            | phintivs            | 1               |
| catina          | 1            | catinvs             | 1               |
| confido         | 1            | confidens           | 1               |
| alpis           | 1            | alpes               | 1               |
| positvs         | 1            | pono                | 1               |
| setinvm         | 1            | setinvs             | 1               |
| difficile       | 1            | difficilis          | 1               |
| meritvm         | 1            | mereor              | 1               |
| oxvs            | 1            | oxo                 | 1               |
| diffvsvs        | 1            | diffvndo            | 1               |
| didivs          | 1            | didia               | 1               |
| ivnivs          | 1            | ivnia               | 1               |
| cvbitvm         | 1            | cvbo                | 1               |
| iacto           | 1            | iacio               | 1               |
| appareo         | 1            | appar               | 1               |
| svpplavdo       | 1            | svpplodo            | 1               |
| patina          | 1            | patinvs             | 1               |
| hospita         | 1            | hospitvs            | 1               |
| atavvs          | 1            | atavi               | 1               |
| convador        | 1            | convado             | 1               |
| nata            | 1            | nascor              | 1               |
| cantharis       | 1            | cantharidvs         | 1               |
| enchytvm        | 1            | encytvs             | 1               |
| coloro          | 1            | coloratvs           | 1               |
| proceres        | 1            | procer              | 1               |
| inclino         | 1            | inclinatvs          | 1               |
| harvdes         | 1            | harvs               | 1               |
| comptvs         | 1            | como                | 1               |
| pacvvivs        | 1            | pacvvivm            | 1               |
| clare           | 1            | clarvs              | 1               |
| minax           | 1            | minacivm            | 1               |
| bacchis         | 1            | baccha              | 1               |
| eripio          | 1            | eripior             | 1               |
| capharevs       | 1            | capherevs           | 1               |
| harmonia        | 1            | harmonivs           | 1               |
| infimvm         | 1            | infervs             | 1               |
| arqvatvs        | 1            | arcvo               | 1               |
| vernvs          | 1            | verna               | 1               |
| antefero        | 1            | antelo              | 1               |
| annoto          | 1            | annotes             | 1               |
| sinistre        | 1            | sinister            | 1               |
| albvs           | 1            | albvm               | 1               |
| dis             | 1            | dives               | 1               |
| interqviesco    | 1            | interqveo           | 1               |
| pytho           | 1            | pythvs              | 1               |
| meio            | 1            | meies               | 1               |
| lanvvini        | 1            | lanvvinvs           | 1               |
| iole            | 1            | ioles               | 1               |
| incomitio       | 1            | incomitto           | 1               |
| obtvsvs         | 1            | obtvndo             | 1               |
| gryps           | 1            | grypes              | 1               |
| distaedet       | 1            | distaedo            | 1               |
| tantalides      | 1            | tantalis            | 1               |
| prytanis        | 1            | prytanvs            | 1               |
| svfes           | 1            | svfeo               | 1               |
| sextvs          | 1            | sex                 | 1               |
| sesama          | 1            | svi                 | 1               |
| pervngo         | 1            | pervngvo            | 1               |
| vendo           | 1            | venditvm            | 1               |
| politvs         | 1            | polio               | 1               |
| tonstrinvs      | 1            | tonstreninvs        | 1               |
| massicvm        | 1            | massicvs            | 1               |
| ciborivm        | 1            | ciboria             | 1               |
| afflvens        | 1            | afflventia          | 1               |
| scabo           | 1            | sco                 | 1               |
| olens           | 1            | oleo                | 1               |
| selectvs        | 1            | seligo              | 1               |
| dirvmpo         | 1            | disrvmpo            | 1               |
| tiresia         | 1            | tiresivs            | 1               |
| bilibris        | 1            | biliber             | 1               |
| rodevs          | 1            | rosevs              | 1               |
| damnatvs        | 1            | damno               | 1               |
| libethrides     | 1            | libethrion          | 1               |
| memorandvs      | 1            | memoro              | 1               |
| circvmspecto    | 1            | circvmspicio        | 1               |
| lvgeo           | 1            | lvceo               | 1               |
| voro            | 1            | vero                | 1               |
| latiaris        | 1            | latiar              | 1               |
| raptvm          | 1            | rapio               | 1               |
| obiecto         | 1            | obicio              | 1               |
| finitimi        | 1            | finitimvs           | 1               |
| gero            | 1            | gestor              | 1               |
| qvies           | 1            | qvietvs             | 1               |
| palilia         | 1            | palilivs            | 1               |
| dentale         | 1            | dentales            | 1               |
| qvintivs        | 1            | qvintvs             | 1               |
| frico           | 1            | fricio              | 1               |
| genesis         | 1            | genesvs             | 1               |
| petosiris       | 1            | petosier            | 1               |
| iarbas          | 1            | iarba               | 1               |
| poetris         | 1            | poetrida            | 1               |
| pegasevs        | 1            | pegaseivs           | 1               |
| andromache      | 1            | andromacha          | 1               |
| vergilivs       | 1            | virgilivs           | 1               |
| cogito          | 1            | cogitatvm           | 1               |
| servs           | 1            | sero                | 1               |
| arefacio        | 1            | arfacio             | 1               |
| lycon           | 1            | lycvs               | 1               |
| pavlvm          | 1            | pavlvs              | 1               |
| dispvdet        | 1            | dispvdo             | 1               |
| displicentia    | 1            | displiceo           | 1               |
| convenientia    | 1            | conveniens          | 1               |
| posides         | 1            | posis               | 1               |
| do              | 1            | dator               | 1               |
| vindico         | 1            | vindex              | 1               |
| corbvla         | 1            | corbvlvs            | 1               |
| devotvs         | 1            | devoveo             | 1               |
| natalis         | 1            | natales             | 1               |
| psecas          | 1            | pseca               | 1               |
| perprimo        | 1            | perpremo            | 1               |
| interpvnctio    | 1            | interpvntio         | 1               |
| amara           | 1            | amarvs              | 1               |
| attatae         | 1            | attatvs             | 1               |
| dvbivs          | 1            | dvbivm              | 1               |
| solidvs         | 1            | solidvm             | 1               |
| iactans         | 1            | iacto               | 1               |
| qvadragies      | 1            | qvadragiens         | 1               |
| consvefacio     | 1            | consvefco           | 1               |
| trivmpho        | 1            | trivmphvs           | 1               |
| repvgnantia     | 1            | repvgno             | 1               |
| tristis         | 1            | tristiter           | 1               |
| svfficio        | 1            | svfficiens          | 1               |
| colvmbvlvs      | 1            | colvmbvla           | 1               |
| vnvsetvicesimvs | 1            | vnietvicesimvs      | 1               |
| svspicio        | 1            | svspectvs           | 1               |
| adamo           | 1            | adamas              | 1               |
| hesiona         | 1            | hesione             | 1               |
| aristogiton     | 1            | aristogitvs         | 1               |
| dropides        | 1            | dropis              | 1               |
| iphicrates      | 1            | iphicrastvs         | 1               |
| afflictvs       | 1            | affligo             | 1               |
| armo            | 1            | armati              | 1               |
| inqvino         | 1            | inqvinatvs          | 1               |
| postvlo         | 1            | postvlatvm          | 1               |
| meroe           | 1            | meros               | 1               |
| vas             | 1            | vasvs               | 1               |
| dromo           | 1            | dromvs              | 1               |
| desqvamo        | 1            | destvamo            | 1               |
| machaerio       | 1            | machaerivs          | 1               |
| conger          | 1            | congrvs             | 1               |
| mvraena         | 1            | mvrena              | 1               |
| exdorsvo        | 1            | exdorsvs            | 1               |
| artopta         | 1            | artopto             | 1               |
| hamilcar        | 1            | hamilcares          | 1               |
| secvndvm        | 1            | secvndvs            | 1               |
| manifestvs      | 1            | manifesto           | 1               |
| tartarvs        | 1            | tartara             | 1               |
| vtroqve         | 1            | vterqve             | 1               |
| metior          | 1            | mensis              | 1               |
| transscribo     | 1            | transcribo          | 1               |
| plotina         | 1            | plotinvs            | 1               |
| revera          | 1            | revero              | 1               |
| archimagirvs    | 1            | archimago           | 1               |
| nastvrtivm      | 1            | nastvrcivm          | 1               |
| abrotonvm       | 1            | habrotonvs          | 1               |
| vereor          | 1            | verens              | 1               |
| moesici         | 1            | moesicvs            | 1               |
| plebiscitvm     | 1            | plebico             | 1               |
| qvinctivs       | 1            | qvintivs            | 1               |
| arcanvs         | 1            | arcanvm             | 1               |
| proficio        | 1            | proficiscor         | 1               |
| antecello       | 1            | antecellans         | 1               |
| magetobriga     | 1            | magetobicvs         | 1               |
| praesegmen      | 1            | praesegentia        | 1               |
| parce           | 1            | parco               | 1               |
| misere          | 1            | mitto               | 1               |
| svmen           | 1            | svmo                | 1               |
| rhombvs         | 1            | rhombos             | 1               |
| pavxillvm       | 1            | pavxillvs           | 1               |
| qvisqvam        | 1            | qvoqvam             | 1               |
| translatvs      | 1            | tralatvs            | 1               |
| dono            | 1            | donvm               | 1               |
| complexvs       | 1            | complector          | 1               |
| casv            | 1            | casvs               | 1               |
| rvscvm          | 1            | rvscvs              | 1               |
| simpliciter     | 1            | simplex             | 1               |
| tarraciniensis  | 1            | tarracinenses       | 1               |
| tarentinvs      | 1            | tarentini           | 1               |
| complector      | 1            | complexvs           | 1               |
| areopagites     | 1            | areopagis           | 1               |
| tvscvlanvs      | 1            | tvscvlanvm          | 1               |
| antias          | 1            | antiates            | 1               |
| colchvs         | 1            | colcha              | 1               |
| evenvs          | 1            | eveni               | 1               |
| exopto          | 1            | exoptatvs           | 1               |
| oppidvm         | 1            | oppido              | 1               |
| eligo           | 1            | elego               | 1               |
| lepos           | 1            | lepor               | 1               |
| mvndo           | 1            | mvndatvs            | 1               |
| nomencvlator    | 1            | nomenclator         | 1               |
| sexennis        | 1            | sexen               | 1               |
| retardo         | 1            | retardeo            | 1               |
| tarpezita       | 1            | trapezita           | 1               |
| proficiscor     | 1            | proficio            | 1               |
| perlego         | 1            | pelliga             | 1               |
| cornicor        | 1            | cornico             | 1               |
| inepte          | 1            | ineptvs             | 1               |
| stloppvs        | 1            | scloppvs            | 1               |
| memoro          | 1            | memorandvs          | 1               |
| accvro          | 1            | accvratvs           | 1               |
| indvlgens       | 1            | indvlgeo            | 1               |
| vlterior        | 1            | vltra               | 1               |
| colo            | 1            | cvltvs              | 1               |
| nvmida          | 1            | nvmidae             | 1               |
| peronatvs       | 1            | perono              | 1               |
| melicertes      | 1            | melicerta           | 1               |
| temetvm         | 1            | temetvs             | 1               |
| libet           | 1            | lvbeo               | 1               |
| dehavrio        | 1            | deorior             | 1               |
| ipse            | 1            | svi                 | 1               |
| dives           | 1            | ditivs              | 1               |
| aliptes         | 1            | alips               | 1               |
| dilvcesco       | 1            | dilvceo             | 1               |
| septempedalis   | 1            | septemplalis        | 1               |
| emigro          | 1            | emigreo             | 1               |
| reporto         | 1            | reporo              | 1               |
| distendo        | 1            | distineo            | 1               |
| anathymiasis    | 1            | anathymiates        | 1               |
| ferraria        | 1            | ferrarivs           | 1               |
| cvticvla        | 1            | cvticvlvm           | 1               |
| qvatio          | 1            | qvatvs              | 1               |
| areopagvs       | 1            | areospantalvs       | 1               |
| inflo           | 1            | inflatvs            | 1               |
| svbseqvor       | 1            | svpseqvor           | 1               |
| neapolitanvm    | 1            | neapolitanvs        | 1               |
| expedio         | 1            | expeditvs           | 1               |
| notvs           | 1            | nota                | 1               |
| parapamisadae   | 1            | parapamades         | 1               |
| deserta         | 1            | desertvs            | 1               |
| arimaspi        | 1            | arimaspivs          | 1               |
| afflvo          | 1            | afflvens            | 1               |
| exta            | 1            | extor               | 1               |
| obdormio        | 1            | obdormisco          | 1               |
| svbmano         | 1            | svmmanvs            | 1               |
| circvmiaceo     | 1            | circvmecio          | 1               |
| avdiens         | 1            | avdio               | 1               |
| immensvm        | 1            | immensvs            | 1               |
| vettidivs       | 1            | vettis              | 1               |
| praeterita      | 1            | praeteritvs         | 1               |
| planvm          | 1            | planvs              | 1               |
| svpervacvvs     | 1            | svpervacvvm         | 1               |
| macedo          | 1            | macedones           | 1               |
| nvgor           | 1            | nvgo                | 1               |
| propendeo       | 1            | propensvs           | 1               |
| sesqvipes       | 1            | sesqvipedes         | 1               |
| dinosco         | 1            | digosco             | 1               |
| removeo         | 1            | remotvs             | 1               |
| thessalvs       | 1            | thessalis           | 1               |
| ammon           | 1            | hammon              | 1               |
| ferrvm          | 1            | fero                | 1               |
| cadmeivs        | 1            | cadmevs             | 1               |
| dvcenti         | 1            | dvo                 | 1               |
| brisaevs        | 1            | brisaei             | 1               |
| capharis        | 1            | capherides          | 1               |
| specio          | 1            | spicio              | 1               |
| philetas        | 1            | philitae            | 1               |
| svfflo          | 1            | svfflasco           | 1               |
| silenvs         | 1            | silen               | 1               |
| plavsvs         | 1            | plavs               | 1               |
| desomnis        | 1            | desomno             | 1               |
| dirvm           | 1            | dirvs               | 1               |
| noceo           | 1            | nocens              | 1               |
| tabvm           | 1            | tabvs               | 1               |
| effvnsvs        | 1            | effvndo             | 1               |
| reperio         | 1            | reperito            | 1               |
| rectvs          | 1            | recte               | 1               |
| prosper         | 1            | prospera            | 1               |
| vasa            | 1            | vas                 | 1               |
| pollicitvm      | 1            | polliceor           | 1               |
| vinevs          | 1            | vinea               | 1               |
| statvo          | 1            | statva              | 1               |
| evnvchvs        | 1            | evnvcho             | 1               |
| cvpidvs         | 1            | cvpido              | 1               |
| svperans        | 1            | svpero              | 1               |
| inveterasco     | 1            | invetero            | 1               |
| vertico         | 1            | verticvs            | 1               |
| sebvm           | 1            | sebes               | 1               |
| cos             | 1            | coto                | 1               |
| emereo          | 1            | emereor             | 1               |
| mvstvm          | 1            | mvstvs              | 1               |
| frivolvs        | 1            | frivola             | 1               |
| coerceo         | 1            | coherceo            | 1               |
| exactvs         | 1            | exigo               | 1               |
| mvtitio         | 1            | mvttitio            | 1               |
| odi             | 1            | osvrvs              | 1               |
| bias            | 1            | biantes             | 1               |
| somnivm         | 1            | somnivs             | 1               |
| exardeo         | 1            | exardesco           | 1               |
| verto           | 1            | versvs              | 1               |
| ollovico        | 1            | ololvico            | 1               |
| avditvm         | 1            | avdio               | 1               |
| syracvsani      | 1            | syracvsanvs         | 1               |
| perivrvs        | 1            | malvs               | 1               |
| eloqvens        | 1            | eloqvor             | 1               |
| porcinvm        | 1            | poricinvs           | 1               |
| horativs        | 1            | horatia             | 1               |
| conservvs       | 1            | consero             | 1               |
| fortis          | 1            | fortiter            | 1               |
| adaperio        | 1            | adapereo            | 1               |
| femvr           | 1            | femen               | 1               |
| intellectvs     | 1            | intelligo           | 1               |
| solitvm         | 1            | solitvs             | 1               |
| receptvs        | 1            | recipio             | 1               |
| pvls            | 1            | pvltis              | 1               |
| aeqviparabilis  | 1            | aeqvipabilis        | 1               |
| desertvm        | 1            | desero              | 1               |
| lateranvs       | 1            | laterani            | 1               |
| obsedeo         | 1            | obsideo             | 1               |
| interdiv        | 1            | interdivs           | 1               |
| laridvm         | 1            | lardvs              | 1               |
| pvlpa           | 1            | pvlpvs              | 1               |
| molorchaevs     | 1            | molorchivs          | 1               |
| inavratvs       | 1            | inavro              | 1               |
| seqvanvs        | 1            | seqvani             | 1               |
| vniversvm       | 1            | vniversvs           | 1               |
| qvivis          | 1            | qvilis              | 1               |
| halophanta      | 1            | halophantia         | 1               |
| pinso           | 1            | pingo               | 1               |
| resido          | 1            | resideo             | 1               |
| incestvm        | 1            | incestvs            | 1               |
| cvstodite       | 1            | cvstoditer          | 1               |
| pateo           | 1            | patens              | 1               |
| nvmisivs        | 1            | nvmisii             | 1               |
| inqvinatvs      | 1            | inqvino             | 1               |
| velinvs         | 1            | velina              | 1               |
| tesservla       | 1            | tesservlvs          | 1               |
| sto             | 1            | statvra             | 1               |
| hvmana          | 1            | hvmanvs             | 1               |
| svpparasitor    | 1            | svpparato           | 1               |
| canorvs         | 1            | canor               | 1               |
| verisimilitvdo  | 1            | verisimtio          | 1               |
| septemplex      | 1            | septemplix          | 1               |
| cinyphivs       | 1            | cinyphia            | 1               |
| tento           | 1            | tentor              | 1               |
| bos             | 1            | bover               | 1               |
| venvm           | 1            | venor               | 1               |
| lvxvs           | 1            | lvxeo               | 1               |
| intego          | 1            | intexo              | 1               |
| longvs          | 1            | longe               | 1               |
| libero          | 1            | liberer             | 1               |
| indeprehensvs   | 1            | indeprego           | 1               |
| avara           | 1            | avarvs              | 1               |
| aqvilex         | 1            | aqvilegis           | 1               |
| hic             | 1            | ne                  | 1               |
| canto           | 1            | canta               | 1               |
| destitvo        | 1            | destitvtvm          | 1               |
| callidama       | 1            | callidamvs          | 1               |
| honoro          | 1            | honoratvs           | 1               |
| transveho       | 1            | transvecio          | 1               |
| detero          | 1            | detereo             | 1               |
| balbvs          | 1            | balba               | 1               |
| hypsipyle       | 1            | hypsipyla           | 1               |
| aristomedes     | 1            | aristomeres         | 1               |
| diverto         | 1            | diversvs            | 1               |
| qvadrantal      | 1            | qvadranta           | 1               |
| tela            | 1            | telvm               | 1               |
| temvlentvs      | 1            | temvlentvm          | 1               |
| havstvs         | 1            | havrio              | 1               |
| tanto           | 1            | tantvs              | 1               |
| hibernvm        | 1            | hiberna             | 1               |
| largior         | 1            | largvs              | 1               |
| latobrigi       | 1            | latobrigivs         | 1               |
| ignave          | 1            | ignavvs             | 1               |
| offensa         | 1            | offendo             | 1               |
| tantvmdem       | 1            | tantvsdem           | 1               |
| semirefectvs    | 1            | semirefico          | 1               |
| cevs            | 1            | cea                 | 1               |
| retracto        | 1            | retraho             | 1               |
| hippocoon       | 1            | hippocoomvs         | 1               |
| callirhoe       | 1            | callirhones         | 1               |
| ars             | 1            | arte                | 1               |
| thrax           | 1            | thraex              | 1               |
| erythrae        | 1            | erythres            | 1               |
| cicada          | 1            | cicado              | 1               |
| postvmivs       | 1            | postvmia            | 1               |
| praemvnio       | 1            | praemvntio          | 1               |
| dellivs         | 1            | dellvs              | 1               |
| nota            | 1            | notvs               | 1               |
| apameni         | 1            | apamenos            | 1               |
| exanimo         | 1            | exanimvs            | 1               |
| inhvmane        | 1            | inhvmanvs           | 1               |
| illo            | 1            | ille                | 1               |
| fallo           | 1            | falsvs              | 1               |
| citrevs         | 1            | citrevm             | 1               |
| exterritvs      | 1            | exterreo            | 1               |
| obediens        | 1            | obedio              | 1               |
| cvtis           | 1            | cvtivm              | 1               |
| donvm           | 1            | dono                | 1               |
| illi            | 1            | ille                | 1               |
| camera          | 1            | camarvs             | 1               |
| restricte       | 1            | restringo           | 1               |
| sempiterno      | 1            | sempiternvs         | 1               |
| vive            | 1            | vivo                | 1               |
| svpparvm        | 1            | siparvm             | 1               |
| classici        | 1            | classicvm           | 1               |
| destricte       | 1            | destringo           | 1               |
| pvrgo           | 1            | pvrgatvs            | 1               |
| cydippe         | 1            | cydippvs            | 1               |
| calcar          | 1            | calco               | 1               |
| obseqvor        | 1            | obseco              | 1               |
| plvrimvm        | 1            | mvltvs              | 1               |
| retero          | 1            | retritvs            | 1               |
| servm           | 1            | sero                | 1               |
| vincio          | 1            | vinco               | 1               |
| defetiscor      | 1            | defessvs            | 1               |
| epistates       | 1            | epistor             | 1               |
| qvisqvis        | 1            | qvisqvam            | 1               |
| allex           | 1            | halleces            | 1               |
| amygdalvm       | 1            | amygdalvs           | 1               |
| svccenseo       | 1            | svscenseo           | 1               |
| care            | 1            | carvs               | 1               |
| volsiniensis    | 1            | vvlsiniensis        | 1               |
| clavdivs        | 1            | clavdia             | 1               |
| inconsvmptvs    | 1            | inconsvstvs         | 1               |
| rex             | 1            | rego                | 1               |
| letovs          | 1            | letor               | 1               |
| aridvs          | 1            | ardvs               | 1               |
| ino             | 1            | inoes               | 1               |
| ivnia           | 1            | ivnivs              | 1               |
| calpvrnia       | 1            | calpvrnivs          | 1               |
| maena           | 1            | mena                | 1               |
| recompono       | 1            | recompositvs        | 1               |
| dignvs          | 1            | dignvm              | 1               |
| plias           | 1            | pleas               | 1               |
| iazyges         | 1            | iazyx               | 1               |
| consvltvm       | 1            | consvlto            | 1               |
| inchoo          | 1            | incoho              | 1               |
| consortio       | 1            | consortivm          | 1               |
| depso           | 1            | depsvo              | 1               |
| circvmtergeo    | 1            | circvmtero          | 1               |
| commercor       | 1            | commerceo           | 1               |
| elysii          | 1            | elysivs             | 1               |
| peristasis      | 1            | peristame           | 1               |
| triphallvs      | 1            | triphalla           | 1               |
| hactenvs        | 1            | hactvenvs           | 1               |
| tempestivo      | 1            | tempestivvs         | 1               |
| alexandrea      | 1            | alexandria          | 1               |
| gnosis          | 1            | gnosvs              | 1               |
| linevs          | 1            | linea               | 1               |
| ivlvs           | 1            | ivlo                | 1               |
| fvnda           | 1            | fvndvs              | 1               |
| pellitvs        | 1            | pello               | 1               |
| opvlens         | 1            | opvlentvs           | 1               |
| bellerophontevs | 1            | bellerophontes      | 1               |
| bellicvm        | 1            | bellicvs            | 1               |
| docte           | 1            | doctvs              | 1               |
| emo             | 1            | emendo              | 1               |
| emax            | 1            | emacvs              | 1               |
| sardanapallvs   | 1            | sardanapalvs        | 1               |
| opicvs          | 1            | opica               | 1               |
| corvinvs        | 1            | corvini             | 1               |
| pellis          | 1            | pello               | 1               |
| emineo          | 1            | eminens             | 1               |
| monitvs         | 1            | moneo               | 1               |
| fractvs         | 1            | frango              | 1               |
| elvmbis         | 1            | elvmbo              | 1               |
| marita          | 1            | maritvs             | 1               |
| divdico         | 1            | diivdico            | 1               |
| sabaevs         | 1            | sabaei              | 1               |
| parapanisvs     | 1            | parapandii          | 1               |
| praetento       | 1            | praetempto          | 1               |
| penso           | 1            | penseo              | 1               |
| ambio           | 1            | ambeo               | 1               |
| privato         | 1            | privatvs            | 1               |
| fvro            | 1            | fvrens              | 1               |
| genitalia       | 1            | genitalis           | 1               |
| occvltvm        | 1            | occvltvs            | 1               |
| recipio         | 1            | receptvs            | 1               |
| aeqvimaelivm    | 1            | aeqvimales          | 1               |
| hippotades      | 1            | hippotas            | 1               |
| meracvs         | 1            | meraca              | 1               |
| sollemne        | 1            | sollemnis           | 1               |
| nardvm          | 1            | nardvs              | 1               |
| calleo          | 1            | callis              | 1               |
| cornvtvs        | 1            | cornvtes            | 1               |
| rescisco        | 1            | rescio              | 1               |
| praevenio       | 1            | venio               | 1               |
| perrhaebvs      | 1            | perrhaebae          | 1               |
| svbiectvs       | 1            | svbicio             | 1               |
| natalicivs      | 1            | natalicia           | 1               |
| plasma          | 1            | plasmate            | 1               |
| infirmvs        | 1            | infirmo             | 1               |
| isevm           | 1            | iseon               | 1               |
| praepropervs    | 1            | praepropvs          | 1               |
| exsvlo          | 1            | exsvlto             | 1               |
| pvsvla          | 1            | pvssvla             | 1               |
| aegroto         | 1            | aegrotvs            | 1               |
| concito         | 1            | concitatvs          | 1               |
| serpyllvm       | 1            | serpvllvs           | 1               |
| tevtoni         | 1            | tevtonivs           | 1               |
| moeris          | 1            | moeri               | 1               |
| scvlponeae      | 1            | scvlponia           | 1               |
| gabinivs        | 1            | gabinia             | 1               |
| contemnendvs    | 1            | contemno            | 1               |
| qvotvsqvisqve   | 1            | qvotvs              | 1               |
| sterno          | 1            | stratvm             | 1               |
| relego          | 1            | religo              | 1               |
| transversvm     | 1            | transversvs         | 1               |
| divrnvm         | 1            | divrnvs             | 1               |
| ivsta           | 1            | ivstvs              | 1               |
| defvngor        | 1            | defvnctvs           | 1               |
| philtrvm        | 1            | philtra             | 1               |
| repecto         | 1            | repelo              | 1               |
| caecvbvm        | 1            | caecvba             | 1               |
| evpolis         | 1            | evpolides           | 1               |
| praegrandis     | 1            | praegro             | 1               |
| decoctior       | 1            | decoctvs            | 1               |
| librvm          | 1            | libra               | 1               |
| rvbricatvs      | 1            | rvbrico             | 1               |
| baltevm         | 1            | baltevs             | 1               |
| rigens          | 1            | rigeo               | 1               |
| minvtal         | 1            | minvtalis           | 1               |
| altercor        | 1            | alterco             | 1               |
| afri            | 1            | afer                | 1               |
| exhortor        | 1            | exorto              | 1               |
| olenivs         | 1            | olenia              | 1               |
| serpo           | 1            | serpens             | 1               |
| amentvm         | 1            | ammentvm            | 1               |
| inexercitatvs   | 1            | inexercito          | 1               |
| vsvfacio        | 1            | vsvficio            | 1               |
| qvinta          | 1            | qvintvs             | 1               |
| aemvla          | 1            | aemvlvs             | 1               |
| externvs        | 1            | externvm            | 1               |
| potior          | 1            | potis               | 1               |
| pro             | 1            | prosvm              | 1               |
| bedriacensis    | 1            | bedriacenses        | 1               |
| ambracivs       | 1            | ambracia            | 1               |
| parvvm          | 1            | parvvs              | 1               |
| salinvm         | 1            | salinvs             | 1               |
| aegaevm         | 1            | aegaevs             | 1               |
| thraca          | 1            | thrax               | 1               |
| neqve           | 1            | nec                 | 1               |
| assicco         | 1            | ascico              | 1               |
| pvngo           | 1            | pelvgio             | 1               |
| adhaeresco      | 1            | adhaereo            | 1               |
| senex           | 1            | senior              | 1               |
| eloqvor         | 1            | eloco               | 1               |
| animosvs        | 1            | animose             | 1               |
| tradvco         | 1            | transdvco           | 1               |
| lyristes        | 1            | lyristen            | 1               |
| thimiamae       | 1            | thimiama            | 1               |
| vectigalis      | 1            | vectigal            | 1               |
| hercvleivs      | 1            | hercvlevs           | 1               |
| comitor         | 1            | comitatvs           | 1               |
| refoveo         | 1            | refotvs             | 1               |
| glaber          | 1            | glabris             | 1               |
| vello           | 1            | velsvs              | 1               |
| cviatis         | 1            | qvo                 | 1               |
| cretes          | 1            | cretas              | 1               |
| sterto          | 1            | sterno              | 1               |
| evbvlidas       | 1            | evbvlidae           | 1               |
| obstino         | 1            | obstinens           | 1               |
| svbitvs         | 1            | svbito              | 1               |
| profligo        | 1            | profligatvs         | 1               |
| averto          | 1            | aversvs             | 1               |
| libraria        | 1            | librarivm           | 1               |
| cosmeta         | 1            | conmetvs            | 1               |
| vox             | 1            | voco                | 1               |
| deliciolvm      | 1            | deliciolvs          | 1               |
| sedochezi       | 1            | sedochesta          | 1               |
| regressvs       | 1            | regredior           | 1               |
| pronvs          | 1            | prone               | 1               |
| cardvelis       | 1            | cardelis            | 1               |
| mvstela         | 1            | mvstellvm           | 1               |
| lavdo           | 1            | lavs                | 1               |
| achaevs         | 1            | achaei              | 1               |
| accelero        | 1            | acceleratvs         | 1               |
| illyricvs       | 1            | illyricvm           | 1               |
| opino           | 1            | opinor              | 1               |
| comis           | 1            | coma                | 1               |
| grates          | 1            | gratis              | 1               |
| sphinx          | 1            | sphinga             | 1               |
| isto            | 1            | iste                | 1               |
| mysvs           | 1            | myse                | 1               |
| percrvcio       | 1            | percrvcvs           | 1               |
| lvdifico        | 1            | lvdificor           | 1               |
| aliorsvm        | 1            | alioversvm          | 1               |
| altare          | 1            | alto                | 1               |
| erycinvs        | 1            | erycina             | 1               |
| pharivs         | 1            | pharii              | 1               |
| senvs           | 1            | senex               | 1               |
| partior         | 1            | partio              | 1               |
| reprehensio     | 1            | reprensio           | 1               |
| vivvs           | 1            | vivo                | 1               |
| arectevs        | 1            | arectei             | 1               |
| contvmacia      | 1            | contvmax            | 1               |
| athleta         | 1            | athles              | 1               |
| svblimiter      | 1            | svblimis            | 1               |
| cvlte           | 1            | cvltvs              | 1               |
| blandior        | 1            | blanditvs           | 1               |
| sybilla         | 1            | sibylla             | 1               |
| tigillvm        | 1            | tigilles            | 1               |
| tenere          | 1            | teneo               | 1               |
| vegrandis       | 1            | vegro               | 1               |
| svber           | 1            | svbeo               | 1               |
| spernendvs      | 1            | sperno              | 1               |
| praepostere     | 1            | praeposte           | 1               |
| perdecorvs      | 1            | perdecvs            | 1               |
| contrarivs      | 1            | contrarivm          | 1               |
| escvlentvs      | 1            | escvlens            | 1               |
| cvpiens         | 1            | cvpio               | 1               |
| amedines        | 1            | amedine             | 1               |
| mammaea         | 1            | mammaevs            | 1               |
| idalivs         | 1            | idalia              | 1               |
| adolescens      | 1            | adolesco            | 1               |
| eventvra        | 1            | evenio              | 1               |
| contrarivm      | 1            | contrarivs          | 1               |
| scato           | 1            | scaton              | 1               |
| tectvm          | 1            | tego                | 1               |
| flagrans        | 1            | flagro              | 1               |
| troilvs         | 1            | troilon             | 1               |
| phrygivs        | 1            | phrygia             | 1               |
| praelargvs      | 1            | praelarabvs         | 1               |
| angvstvm        | 1            | angvstvs            | 1               |
| casevm          | 1            | casevs              | 1               |
| fabaginvs       | 1            | fabago              | 1               |
| cynthivs        | 1            | cynthia             | 1               |
| lacones         | 1            | lacon               | 1               |
| certe           | 1            | certvs              | 1               |
| ecqvid          | 1            | ecqvis              | 1               |
| sicvt           | 1            | siccvm              | 1               |
| hiberi          | 1            | iberi               | 1               |
| iapydia         | 1            | iapydivs            | 1               |
| pylivs          | 1            | pylias              | 1               |
| circvmsaepio    | 1            | circvmsedeo         | 1               |
| vaporo          | 1            | vaporatvs           | 1               |
| arretivm        | 1            | arretvs             | 1               |
| magvs           | 1            | mago                | 1               |
| phaedrvs        | 1            | phaedrivs           | 1               |
| moderor         | 1            | moderatvs           | 1               |
| levcadia        | 1            | levcadivs           | 1               |
| patior          | 1            | pateo               | 1               |
| adoleo          | 1            | adoles              | 1               |
| oeneis          | 1            | oenevs              | 1               |
| cvro            | 1            | cvra                | 1               |
| alcmaeonivs     | 1            | alcmaeonia          | 1               |
| phinevs         | 1            | phinei              | 1               |
| sitis           | 1            | svm                 | 1               |
| desperatvs      | 1            | despero             | 1               |
| baetica         | 1            | baeticvs            | 1               |
| honorificvs     | 1            | honorifice          | 1               |
| exigvvm         | 1            | exigvvs             | 1               |
| tomyris         | 1            | tamyris             | 1               |
| magyni          | 1            | magynvs             | 1               |
| stipendivm      | 1            | stipeo              | 1               |
| vniversvs       | 1            | vniversi            | 1               |
| sarisa          | 1            | sarissa             | 1               |
| qvadraginta     | 1            | dvcenti             | 1               |
| qvingenti       | 1            | septvaginta         | 1               |
| octoginta       | 1            | septvaginta         | 1               |
| granatvs        | 1            | grango              | 1               |
| libo            | 1            | libes               | 1               |
| illavdatvs      | 1            | illavdo             | 1               |
| amanicae        | 1            | amanicvs            | 1               |
| dispicio        | 1            | dispectvra          | 1               |
| redvco          | 1            | reddvco             | 1               |
| occvltvs        | 1            | occvlte             | 1               |
| mimallonevs     | 1            | mimallonia          | 1               |
| flecto          | 1            | flexvra             | 1               |
| evhivs          | 1            | evhion              | 1               |
| echo            | 1            | echvm               | 1               |
| indolentia      | 1            | indolens            | 1               |
| abvndans        | 1            | abvndo              | 1               |
| elegidion       | 1            | elegidivm           | 1               |
| gravo           | 1            | gravor              | 1               |
| dvx             | 1            | dvco                | 1               |
| cepheis         | 1            | cephevs             | 1               |
| insvo           | 1            | insvesco            | 1               |
| flagro          | 1            | flagrans            | 1               |
| hyrcanvs        | 1            | hyrcani             | 1               |
| medvs           | 1            | medi                | 1               |
| iacvlator       | 1            | iacvlatvs           | 1               |
| qvilibet        | 1            | qvolibet            | 1               |
| dissipo         | 1            | dissipio            | 1               |
| formianvm       | 1            | formianvs           | 1               |
| anser           | 1            | anseres             | 1               |
| pyrgo           | 1            | pyrgvs              | 1               |
| doryclvs        | 1            | doryclivs           | 1               |
| barbarvs        | 1            | barbare             | 1               |
| testatvs        | 1            | testor              | 1               |
| aqvvla          | 1            | aqvola              | 1               |
| cirrati         | 1            | cirratvs            | 1               |
| vivo            | 1            | vinco               | 1               |
| constitvtvs     | 1            | constitvo           | 1               |
| incepto         | 1            | incipio             | 1               |
| sicine          | 1            | sic                 | 1               |
| hera            | 1            | svm                 | 1               |
| hiberna         | 1            | hibernvs            | 1               |
| dvrvs           | 1            | dvrvm               | 1               |
| cometes         | 1            | cometen             | 1               |
| tector          | 1            | tectvs              | 1               |
| prodo           | 1            | prodeo              | 1               |
| obrigesco       | 1            | obrigo              | 1               |
| obseqvens       | 1            | obseqvor            | 1               |
| mos             | 1            | morior              | 1               |
| tactvs          | 1            | tango               | 1               |
| latens          | 1            | lateo               | 1               |
| sacro           | 1            | sacratvs            | 1               |
| indico          | 1            | indictvs            | 1               |
| chaonis         | 1            | chaon               | 1               |
| incvtio         | 1            | incvssvs            | 1               |
| perfectvs       | 1            | perficio            | 1               |
| fenebris        | 1            | fenerber            | 1               |
| bvrdvbasta      | 1            | bvrdvbatvs          | 1               |
| loripes         | 1            | loripis             | 1               |
| hyrtacides      | 1            | hyrtacidas          | 1               |
| ocvlissimvs     | 1            | ocvle               | 1               |
| elevsivm        | 1            | elevsivs            | 1               |
| detrvdo         | 1            | detero              | 1               |
| ravis           | 1            | ravvs               | 1               |
| accommodo       | 1            | accomodvs           | 1               |
| denter          | 1            | dentres             | 1               |
| occento         | 1            | occens              | 1               |
| repeto          | 1            | repetvndae          | 1               |
| sextadecimani   | 1            | sextadectia         | 1               |
| lotos           | 1            | lavo                | 1               |
| laestrygones    | 1            | laestrynos          | 1               |
| penna           | 1            | pinna               | 1               |
| disicio         | 1            | dissicio            | 1               |
| aptvs           | 1            | apte                | 1               |
| lex             | 1            | lego                | 1               |
| relentesco      | 1            | relenteo            | 1               |
| xerxes          | 1            | xerses              | 1               |
| motvs           | 1            | moveo               | 1               |
| civicvs         | 1            | civis               | 1               |
| expio           | 1            | exspo               | 1               |
| probvs          | 1            | probo               | 1               |
| samnis          | 1            | samnites            | 1               |
| trifvrcifer     | 1            | trifvrcica          | 1               |
| solo            | 1            | solor               | 1               |
| tranqvillvm     | 1            | tranqvillvs         | 1               |
| ventvs          | 1            | venio               | 1               |
| evthymia        | 1            | evthymianvs         | 1               |
| edormio         | 1            | edormo              | 1               |
| ortvs           | 1            | orior               | 1               |
| svperflvo       | 1            | svperflvens         | 1               |
| indvlgeo        | 1            | indvlgens           | 1               |
| testacevs       | 1            | testacevm           | 1               |
| tonsvs          | 1            | tondeo              | 1               |
| nasvm           | 1            | nasvs               | 1               |
| tressis         | 1            | tresa               | 1               |
| agaso           | 1            | ago                 | 1               |
| pannvcivs       | 1            | pannvcivm           | 1               |
| bavcis          | 1            | bavcvs              | 1               |
| ocimvm          | 1            | ocimvs              | 1               |
| conclvsvs       | 1            | conclvdo            | 1               |
| ivdaevs         | 1            | ivdaea              | 1               |
| solymvs         | 1            | solyma              | 1               |
| internvntia     | 1            | internvntivs        | 1               |
| pomvs           | 1            | pomvm               | 1               |
| legens          | 1            | lego                | 1               |
| administro      | 1            | administer          | 1               |
| opimivs         | 1            | opimvs              | 1               |
| depsticivs      | 1            | depsticivm          | 1               |
| secretvs        | 1            | secretvm            | 1               |
| vernvm          | 1            | vernvs              | 1               |
| betacevs        | 1            | betax               | 1               |
| phaeacvs        | 1            | phaeaces            | 1               |
| defessvs        | 1            | defetiscor          | 1               |
| noxia           | 1            | noxivs              | 1               |
| recvpero        | 1            | recipio             | 1               |
| efficio         | 1            | effectvs            | 1               |
| ratis           | 1            | reor                | 1               |
| phinides        | 1            | phinidas            | 1               |
| tvte            | 1            | tv                  | 1               |
| defrico         | 1            | defricio            | 1               |
| honeste         | 1            | honestvs            | 1               |
| popanvm         | 1            | popanvs             | 1               |
| clipeatvs       | 1            | clapeatvs           | 1               |
| detrimentosvs   | 1            | detrimentvs         | 1               |
| orbvs           | 1            | orbis               | 1               |
| lvcvs           | 1            | lvx                 | 1               |
| convestio       | 1            | convestitvs         | 1               |
| varvs           | 1            | varivs              | 1               |
| phraates        | 1            | prahates            | 1               |
| irretortvs      | 1            | irretor             | 1               |
| sane            | 1            | sanvs               | 1               |
| edoni           | 1            | edon                | 1               |
| canvtivs        | 1            | canvtivm            | 1               |
| providens       | 1            | provideo            | 1               |
| nescioqvid      | 1            | nescioqvis          | 1               |
| praetextvs      | 1            | praetexta           | 1               |
| lvpercvs        | 1            | lvperci             | 1               |
| institvo        | 1            | institvtvm          | 1               |
| laeva           | 1            | laevvs              | 1               |
| incertvs        | 1            | incertvm            | 1               |
| impvratvs       | 1            | impvro              | 1               |
| diversvs        | 1            | diverto             | 1               |
| laniatvs        | 1            | lanio               | 1               |
| ictvs           | 1            | ico                 | 1               |
| dilacero        | 1            | dilacior            | 1               |
| circvmplector   | 1            | circvmpledo         | 1               |
| vvlgo           | 1            | vvlgvs              | 1               |
| athamantis      | 1            | athamansis          | 1               |
| saperda         | 1            | saperdo             | 1               |
| ebenvs          | 1            | hebenvs             | 1               |
| datvm           | 1            | dator               | 1               |
| ingressvs       | 1            | ingredior           | 1               |
| sabinvs         | 1            | sabini              | 1               |
| tvtvs           | 1            | tvte                | 1               |
| depressvs       | 1            | depresse            | 1               |
| bactrianvs      | 1            | bactriani           | 1               |
| raster          | 1            | rastrvm             | 1               |
| seria           | 1            | serivs              | 1               |
| obligatvs       | 1            | obligo              | 1               |
| sentio          | 1            | sentis              | 1               |
| sedvctvs        | 1            | sedvctvm            | 1               |
| poliorcetes     | 1            | poliorches          | 1               |
| trepido         | 1            | trepidvs            | 1               |
| carpentvm       | 1            | carpo               | 1               |
| pediseqvvs      | 1            | pediseqvi           | 1               |
| indemnatvs      | 1            | indemno             | 1               |
| navvs           | 1            | gnavvs              | 1               |
| nvmne           | 1            | nvmdi               | 1               |
| coriolanvs      | 1            | coriolanvm          | 1               |
| amylvm          | 1            | amvlvs              | 1               |
| exvrgeo         | 1            | exsvrgo             | 1               |
| impvre          | 1            | impvrvs             | 1               |
| tetre           | 1            | teter               | 1               |
| bifariam        | 1            | bifarivs            | 1               |
| tvrbellae       | 1            | tvrbella            | 1               |
| cano            | 1            | canis               | 1               |
| rvbeta          | 1            | rvbetvs             | 1               |
| sapienter       | 1            | sapiens             | 1               |
| fabrico         | 1            | fabricor            | 1               |
| fatvvs          | 1            | fatvvm              | 1               |
| fvngvs          | 1            | fvngor              | 1               |
| anteeo          | 1            | antideo             | 1               |
| remitto         | 1            | remissvs            | 1               |
| infans          | 1            | infantia            | 1               |
| modivm          | 1            | modivs              | 1               |
| tres            | 1            | dvo                 | 1               |
| dvo             | 1            | triginta            | 1               |
| lacvnar         | 1            | lacvnor             | 1               |
| hymettivs       | 1            | hymettia            | 1               |
| attalvs         | 1            | attalivs            | 1               |
| chloris         | 1            | chlorvs             | 1               |
| cavea           | 1            | caveo               | 1               |
| manii           | 1            | manivs              | 1               |
| delector        | 1            | delecto             | 1               |
| potentatvs      | 1            | potentas            | 1               |
| pavpervs        | 1            | pavper              | 1               |
| ptolomaevs      | 1            | ptolemaevs          | 1               |
| decerno         | 1            | decretvm            | 1               |
| magnanimvs      | 1            | magnanis            | 1               |
| passennvs       | 1            | passenni            | 1               |
| interamnanvs    | 1            | interamna           | 1               |
| gaia            | 1            | gaiae               | 1               |
| divvm           | 1            | divvs               | 1               |
| verso           | 1            | versor              | 1               |
| aeternvs        | 1            | aeternvm            | 1               |
| mvltiplicatio   | 1            | mvltiplipatio       | 1               |
| ille            | 1            | illo                | 1               |
| crastinvm       | 1            | crastinvs           | 1               |
| felicio         | 1            | felicivs            | 1               |
| sigillaria      | 1            | sigillarivs         | 1               |
| rvtilans        | 1            | rvtilo              | 1               |
| obiectvs        | 1            | obicio              | 1               |
| oleaster        | 1            | oleastrvm           | 1               |
| socivs          | 1            | socia               | 1               |
| calamister      | 1            | calamistra          | 1               |
| incedo          | 1            | incesso             | 1               |
| ambigvvs        | 1            | ambigvvm            | 1               |
| castalivs       | 1            | castalia            | 1               |
| mamilivs        | 1            | mamilia             | 1               |
| irrito          | 1            | irritvs             | 1               |
| veneo           | 1            | venio               | 1               |
| pavca           | 1            | pavcvs              | 1               |
| facies          | 1            | facio               | 1               |
| impvbes         | 1            | impvbis             | 1               |
| iactanter       | 1            | iactans             | 1               |
| lycidas         | 1            | lycida              | 1               |
| svblica         | 1            | svblicvs            | 1               |
| palpvm          | 1            | palpvs              | 1               |
| rescriptvm      | 1            | rescribo            | 1               |
| concvrsvs       | 1            | concvrro            | 1               |
| qvaestvaria     | 1            | qvaestvarivs        | 1               |
| maeror          | 1            | moeror              | 1               |
| mitto           | 1            | miser               | 1               |
| caelites        | 1            | caeles              | 1               |
| pyramis         | 1            | pyramides           | 1               |
| mavsolevs       | 1            | mavsolivs           | 1               |
| tmarvs          | 1            | tmari               | 1               |
| garamantes      | 1            | garamas             | 1               |
| troianvs        | 1            | troiani             | 1               |
| geryon          | 1            | geryones            | 1               |
| tityvs          | 1            | tityon              | 1               |
| excvsse         | 1            | excvtio             | 1               |
| fvlcio          | 1            | fvlgeo              | 1               |
| concors         | 1            | concordia           | 1               |
| cratippvs       | 1            | cratippe            | 1               |
| hispanvs        | 1            | hispani             | 1               |
| decresco        | 1            | decretvm            | 1               |
| philetaevs      | 1            | philitevs           | 1               |
| ministro        | 1            | minister            | 1               |
| libidinor       | 1            | libidino            | 1               |
| hiccine         | 1            | hvc                 | 1               |
| ornvs           | 1            | orno                | 1               |
| mystes          | 1            | myste               | 1               |
| svblime         | 1            | svblimis            | 1               |
| emendo          | 1            | emendatvs           | 1               |
| evidens         | 1            | evidenter           | 1               |
| parentes        | 1            | parens              | 1               |
| triginta        | 1            | centvm              | 1               |
| restitvtvs      | 1            | restitvs            | 1               |
| exercito        | 1            | exercitatvs         | 1               |
| advltera        | 1            | advlter             | 1               |
| pavimentatvs    | 1            | pavimento           | 1               |
| peristylvm      | 1            | peristylvs          | 1               |
| defvnctvs       | 1            | defvngor            | 1               |
| samarobriva     | 1            | samarobricvs        | 1               |
| intimvs         | 1            | interior            | 1               |
| sileo           | 1            | silens              | 1               |
| seqvor          | 1            | seqvens             | 1               |
| mandatvs        | 1            | mandatvm            | 1               |
| thamyras        | 1            | thamyra             | 1               |
| introrvmpo      | 1            | introrvppo          | 1               |
| adico           | 1            | adicio              | 1               |
| vervtvm         | 1            | vervto              | 1               |
| mvricidvs       | 1            | mvricides           | 1               |
| malobathron     | 1            | malobathor          | 1               |
| tvvm            | 1            | tvvs                | 1               |
| armenivs        | 1            | armenii             | 1               |
| mensis          | 1            | mensa               | 1               |
| qverqvetvm      | 1            | qverqvetvs          | 1               |
| pacificatorivs  | 1            | pacificarivs        | 1               |
| inceptvm        | 1            | incipio             | 1               |
| qvestvs         | 1            | qveror              | 1               |
| polites         | 1            | polite              | 1               |
| itali           | 1            | italvs              | 1               |
| frvstro         | 1            | frvstror            | 1               |
| nave            | 1            | navis               | 1               |
| paco            | 1            | pacatvs             | 1               |
| fvtvri          | 1            | svm                 | 1               |
| circvmmvgio     | 1            | mvgio               | 1               |
| camena          | 1            | camenae             | 1               |
| servatvs        | 1            | servo               | 1               |
| amphitheatrvm   | 1            | amphithevm          | 1               |
| nvbilvs         | 1            | nvbilvm             | 1               |
| ernevm          | 1            | ernevs              | 1               |
| confringo       | 1            | confrigo            | 1               |
| circvmcisvs     | 1            | circvmcido          | 1               |
| apto            | 1            | aptvs               | 1               |
| insanvs         | 1            | insane              | 1               |
| nimio           | 1            | nimivs              | 1               |
| convenio        | 1            | conventvs           | 1               |
| exordior        | 1            | exorsa              | 1               |
| progne          | 1            | procnes             | 1               |
| hvmanvs         | 1            | hvmana              | 1               |
| manvs           | 1            | maneo               | 1               |
| genivs          | 1            | genvs               | 1               |
| svbsilio        | 1            | svssilio            | 1               |
| verbose         | 1            | verbosvs            | 1               |
| praemonstro     | 1            | praemostro          | 1               |
| cicaro          | 1            | cico                | 1               |
| latro           | 1            | latrato             | 1               |
| avis            | 1            | avvs                | 1               |
| vaniloqvvs      | 1            | vaniloqve           | 1               |
| aliqvo          | 1            | aliqvis             | 1               |
| delectvs        | 1            | deligo              | 1               |
| carbo           | 1            | carbvs              | 1               |
| severe          | 1            | severvs             | 1               |
| menaenvs        | 1            | menaenivs           | 1               |
| angvinvs        | 1            | angvina             | 1               |
| placitvs        | 1            | placeo              | 1               |
| salii           | 1            | salivs              | 1               |
| iniqve          | 1            | iniqvvs             | 1               |
| indemno         | 1            | indemnatvs          | 1               |
| dissolvtvs      | 1            | dissolvo            | 1               |
| porrvs          | 1            | porra               | 1               |
| avellana        | 1            | avellanvs           | 1               |
| avdens          | 1            | avdentia            | 1               |
| allego          | 1            | allectvs            | 1               |
| navigo          | 1            | navigans            | 1               |
| pegasides       | 1            | pegasis             | 1               |
| grande          | 1            | grandis             | 1               |
| ovvm            | 1            | ovis                | 1               |
| xerampelinvs    | 1            | xerampentarivs      | 1               |
| postqvam        | 1            | qvam                | 1               |
| perses          | 1            | persivs             | 1               |
| polydamas       | 1            | pvlydama            | 1               |
| profano         | 1            | profanvs            | 1               |
| devia           | 1            | devivs              | 1               |
| ementior        | 1            | emens               | 1               |
| stvltvs         | 1            | stvlte              | 1               |
| effvsvs         | 1            | effvndo             | 1               |
| scitvm          | 1            | scio                | 1               |
| obsonor         | 1            | obsono              | 1               |
| inivste         | 1            | inivstvs            | 1               |
| lanivs          | 1            | lanis               | 1               |
| opertvm         | 1            | operio              | 1               |
| ilias           | 1            | iliades             | 1               |
| centesimvs      | 1            | centesima           | 1               |
| vorenvs         | 1            | vvrenvs             | 1               |
| licinivs        | 1            | licinvs             | 1               |
| biceps          | 1            | bicipitvs           | 1               |
| althaea         | 1            | althaevs            | 1               |
| admirandvs      | 1            | admiror             | 1               |
| scriblita       | 1            | scriblo             | 1               |
| impollitvs      | 1            | impolo              | 1               |
| hedymeles       | 1            | hedymelle           | 1               |
| arroganter      | 1            | arrogans            | 1               |
| masvrivs        | 1            | masvri              | 1               |
| enthymema       | 1            | enthymemvs          | 1               |
| sphaerita       | 1            | spaeritvs           | 1               |
| sphaera         | 1            | spaero              | 1               |
| ervca           | 1            | ervcio              | 1               |
| aestiva         | 1            | aestivvs            | 1               |
| avxiliaris      | 1            | avxiliares          | 1               |
| parco           | 1            | parce               | 1               |
| primigenivs     | 1            | primigenvs          | 1               |
| exsvpero        | 1            | exspero             | 1               |
| delphinvs       | 1            | delphin             | 1               |
| balaena         | 1            | ballaena            | 1               |
| desideo         | 1            | desido              | 1               |
| svperpendens    | 1            | pendeo              | 1               |
| inaeqvatvs      | 1            | inaeqvo             | 1               |
| svrrentvm       | 1            | svrrentes           | 1               |
| origo           | 1            | originvs            | 1               |
| asicivs         | 1            | asicvs              | 1               |
| eminens         | 1            | emineo              | 1               |
| antiqvaria      | 1            | antiqvarivs         | 1               |
| cadvs           | 1            | cado                | 1               |
| vvlnero         | 1            | vvlnvs              | 1               |
| philippi        | 1            | philippvs           | 1               |
| parmvla         | 1            | parmvlvs            | 1               |
| exsecratvs      | 1            | exsecror            | 1               |
| geidvmni        | 1            | geidvmnvs           | 1               |
| improvisvm      | 1            | improvisvs          | 1               |
| socia           | 1            | socivs              | 1               |
| ariadna         | 1            | ariadne             | 1               |
| vaccensis       | 1            | vagenses            | 1               |
| plantaris       | 1            | plantarivs          | 1               |
| elysivm         | 1            | elysivs             | 1               |
| fax             | 1            | facio               | 1               |
| belias          | 1            | belivs              | 1               |
| compilo         | 1            | compilor            | 1               |
| obrvssa         | 1            | obrvteo             | 1               |
| proselenos      | 1            | proselenae          | 1               |
| lvmbifragivm    | 1            | lvmbifracivs        | 1               |
| illvceo         | 1            | illvcesco           | 1               |
| ivvenalia       | 1            | ivvenalis           | 1               |
| scriba          | 1            | scribo              | 1               |
| resisto         | 1            | resto               | 1               |
| virvs           | 1            | vir                 | 1               |
| allobrogicvs    | 1            | allobrogeni         | 1               |
| coalesco        | 1            | coaleo              | 1               |
| inqvies         | 1            | inqvio              | 1               |
| spvmo           | 1            | spvmans             | 1               |
| ibis            | 1            | ibi                 | 1               |
| nevtro          | 1            | nevter              | 1               |
| adolesco        | 1            | advltvs             | 1               |
| amplvs          | 1            | ample               | 1               |
| centies         | 1            | centiens            | 1               |
| frigida         | 1            | frigidvs            | 1               |
| deditvs         | 1            | dedo                | 1               |
| permessvs       | 1            | permessivs          | 1               |
| aones           | 1            | aonas               | 1               |
| compar          | 1            | comparis            | 1               |
| nvbilvm         | 1            | nvbila              | 1               |
| ordior          | 1            | ordor               | 1               |
| caelestis       | 1            | caelestia           | 1               |
| philomelivm     | 1            | philomelevs         | 1               |
| attonitvs       | 1            | attonitas           | 1               |
| sedeo           | 1            | sedes               | 1               |
| basilides       | 1            | basilis             | 1               |
| talaionivs      | 1            | talaionia           | 1               |
| contremo        | 1            | contremisco         | 1               |
| mercvrialis     | 1            | mercvrialia         | 1               |
| abdo            | 1            | abditvs             | 1               |
| crispvs         | 1            | crispe              | 1               |
| sallvstivs      | 1            | sallvstvs           | 1               |
| temperatvs      | 1            | tempero             | 1               |
| svpervolito     | 1            | svpervolo           | 1               |
| assido          | 1            | assideo             | 1               |
| menstrvvm       | 1            | menstrvvs           | 1               |
| certvs          | 1            | certvm              | 1               |
| vinvm           | 1            | vinipolo            | 1               |
| pollens         | 1            | vinipolo            | 1               |
| marceo          | 1            | marcens             | 1               |
| inane           | 1            | inanis              | 1               |
| misenvm         | 1            | misenvs             | 1               |
| domina          | 1            | dominvs             | 1               |
| atii            | 1            | ativs               | 1               |
| immorior        | 1            | immor               | 1               |
| mysterivm       | 1            | mysterivs           | 1               |
| fictvm          | 1            | fingo               | 1               |
| barba           | 1            | barbas              | 1               |
| petvsivs        | 1            | petvsivm            | 1               |
| praetorivs      | 1            | praetorivm          | 1               |
| ivvo            | 1            | ivta                | 1               |
| vinco           | 1            | vincio              | 1               |
| svccessvs       | 1            | svccedo             | 1               |
| beatvm          | 1            | beatvs              | 1               |
| vibex           | 1            | vibicivm            | 1               |
| flagello        | 1            | flagellvm           | 1               |
| caesarea        | 1            | caesarevs           | 1               |
| lvstrvm         | 1            | lvstro              | 1               |
| demissvs        | 1            | demitto             | 1               |
| cani            | 1            | canis               | 1               |
| circvmscriptvs  | 1            | circvmscripvs       | 1               |
| destinatvs      | 1            | destino             | 1               |
| exerceo         | 1            | exercitvs           | 1               |
| eneco           | 1            | enectvs             | 1               |
| derigo          | 1            | directvs            | 1               |
| illac           | 1            | illic               | 1               |
| hymettvs        | 1            | hymetvs             | 1               |
| avlon           | 1            | avlvs               | 1               |
| anvbis          | 1            | anvbi               | 1               |
| raro            | 1            | rare                | 1               |
| despolio        | 1            | despolivm           | 1               |
| qvindecimviri   | 1            | qvindecimvirivm     | 1               |
| hei             | 1            | ei                  | 1               |
| acer            | 1            | acriter             | 1               |
| navalis         | 1            | navalia             | 1               |
| gorgias         | 1            | gorgia              | 1               |
| gorgatas        | 1            | gorgata             | 1               |
| alcaevs         | 1            | alcae               | 1               |
| exolesco        | 1            | exoletvs            | 1               |
| caninvs         | 1            | canina              | 1               |
| svperbio        | 1            | svperbeo            | 1               |
| romanvs         | 1            | romani              | 1               |
| istvc           | 1            | istic               | 1               |
| cachinno        | 1            | cachinnvs           | 1               |
| xanthias        | 1            | xanthia             | 1               |
| serva           | 1            | servvs              | 1               |
| danais          | 1            | danai               | 1               |
| sinistra        | 1            | sinister            | 1               |
| impedio         | 1            | impeditvs           | 1               |
| dares           | 1            | dareta              | 1               |
| icarivs         | 1            | icarivm             | 1               |
| deplorabvndvs   | 1            | deplorabvs          | 1               |
| eivlo           | 1            | eivlor              | 1               |
| propediem       | 1            | #                   | 1               |
| santoni         | 1            | santonis            | 1               |
| boreas          | 1            | borevs              | 1               |
| violo           | 1            | violes              | 1               |
| flvens          | 1            | flvo                | 1               |
| angor           | 1            | ango                | 1               |
| stips           | 1            | stipes              | 1               |
| tribvnicivs     | 1            | tribvnicvs          | 1               |
| rvfio           | 1            | rvfivs              | 1               |
| ah              | 1            | ab                  | 1               |
| cogo            | 1            | cogito              | 1               |
| consvl          | 1            | consvlo             | 1               |
| lampsacenvs     | 1            | lampsacenivs        | 1               |
| indeploratvs    | 1            | impeploro           | 1               |
| sabinae         | 1            | sabinvs             | 1               |
| privo           | 1            | privatvs            | 1               |
| lvcidvm         | 1            | lvcidvs             | 1               |
| mare            | 1            | marivs              | 1               |
| pvlso           | 1            | pello               | 1               |
| menenivs        | 1            | menenii             | 1               |
| marsi           | 1            | marsvs              | 1               |
| perpetvo        | 1            | perpetvor           | 1               |
| mvtio           | 1            | mvtto               | 1               |
| abscido         | 1            | abscindo            | 1               |
| similago        | 1            | similaginvs         | 1               |
| poppysma        | 1            | poppysmvs           | 1               |
| hercvlivs       | 1            | hercvlevs           | 1               |
| stymphalidae    | 1            | stymphalis          | 1               |
| tribvo          | 1            | tribvtvm            | 1               |
| cvminvm         | 1            | cvmen               | 1               |
| chiragra        | 1            | cheragra            | 1               |
| callistvs       | 1            | callistivs          | 1               |
| reicvlvs        | 1            | reicvlvm            | 1               |
| optempero       | 1            | obtempero           | 1               |
| praefringo      | 1            | praefrigo           | 1               |
| calypso         | 1            | calypsvs            | 1               |
| phaeacia        | 1            | phaeacivs           | 1               |
| principivm      | 1            | princeps            | 1               |
| deblatero       | 1            | deblateto           | 1               |
| sidonivs        | 1            | sidonii             | 1               |
| nais            | 1            | naias               | 1               |
| morvm           | 1            | mos                 | 1               |
| prostitvtvs     | 1            | prostitvtvm         | 1               |
| beto            | 1            | bitet               | 1               |
| aliqvantvs      | 1            | aliqvanto           | 1               |
| alsiense        | 1            | alsiensis           | 1               |
| concalesco      | 1            | concaleo            | 1               |
| temperatvra     | 1            | tempero             | 1               |
| caedes          | 1            | caedo               | 1               |
| cvcvma          | 1            | cvcvs               | 1               |
| viride          | 1            | viridis             | 1               |
| fiscella        | 1            | fiscellvs           | 1               |
| oppositvs       | 1            | oppono              | 1               |
| levcas          | 1            | levca               | 1               |
| svscipio        | 1            | svccipio            | 1               |
| extrema         | 1            | extremvm            | 1               |
| caesonia        | 1            | caesonivs           | 1               |
| ivrisconsvltvs  | 1            | ivrecconsvltvs      | 1               |
| blatio          | 1            | blatvs              | 1               |
| protervitas     | 1            | protervitia         | 1               |
| bedriacvm       | 1            | bedriacvs           | 1               |
| svrripio        | 1            | svbripio            | 1               |
| patavini        | 1            | patavine            | 1               |
| navale          | 1            | navalis             | 1               |
| tevcer          | 1            | tevcri              | 1               |
| cocles          | 1            | cocvlitas           | 1               |
| prosapia        | 1            | prosapivs           | 1               |
| svbblandior     | 1            | svbblandinaris      | 1               |
| svbcrispvs      | 1            | svbcrido            | 1               |
| navcvm          | 1            | navci               | 1               |
| intelligo       | 1            | intelligens         | 1               |
| pargo           | 1            | parco               | 1               |
| exterreo        | 1            | exterritvs          | 1               |
| vvlgvs          | 1            | vvlgo               | 1               |
| for             | 1            | fatvm               | 1               |
| onomastorides   | 1            | onomastories        | 1               |
| onomas          | 1            | onomantes           | 1               |
| callicratides   | 1            | callicratida        | 1               |
| parca           | 1            | parci               | 1               |
| simias          | 1            | simianvs            | 1               |
| strvthocamelvs  | 1            | strvtholvlvs        | 1               |
| plavdo          | 1            | plodvs              | 1               |
| maxilla         | 1            | maxillvm            | 1               |
| balanatvs       | 1            | balano              | 1               |
| gavsapvm        | 1            | gavsape             | 1               |
| distingvo       | 1            | distinctvs          | 1               |
| salio           | 1            | sal                 | 1               |
| phonascvs       | 1            | phonasco            | 1               |
| latinvs         | 1            | latini              | 1               |
| reor            | 1            | reren               | 1               |
| abortivvs       | 1            | abortivvm           | 1               |
| lyrica          | 1            | lyricvs             | 1               |
| consvltvs       | 1            | consvltvm           | 1               |
| placitvm        | 1            | placeo              | 1               |
| capto           | 1            | capio               | 1               |
| ramenta         | 1            | ramentvm            | 1               |
| antiqvvm        | 1            | antiqvvs            | 1               |
| dalmaticvs      | 1            | delmaticvs          | 1               |
| ivstvm          | 1            | ivsta               | 1               |
| obmvrmvro       | 1            | obmvrmvo            | 1               |
| minvs           | 1            | parvm               | 1               |
| placatvs        | 1            | placo               | 1               |
| optatvm         | 1            | opto                | 1               |
| balitans        | 1            | balito              | 1               |
| pictvs          | 1            | pingo               | 1               |
| antitheton      | 1            | antithestes         | 1               |
| bvlevta         | 1            | bvlevtvs            | 1               |
| cavrvs          | 1            | corvs               | 1               |
| promptvs        | 1            | prompte             | 1               |
| lvcania         | 1            | lvcanivs            | 1               |
| plancvs         | 1            | plancivs            | 1               |
| profvgio        | 1            | profvgvs            | 1               |
| concha          | 1            | conca               | 1               |
| cvltvs          | 1            | colo                | 1               |
| florens         | 1            | floreo              | 1               |
| mardvs          | 1            | mardi               | 1               |
| habito          | 1            | habeo               | 1               |
| violentvs       | 1            | violente            | 1               |
| ei              | 1            | is                  | 1               |
| alphesiboevs    | 1            | alphesiboea         | 1               |
| svbito          | 1            | svbitvs             | 1               |
| defectvs        | 1            | deficio             | 1               |
| psevdophilippvs | 1            | psevdoppilvs        | 1               |
| vigens          | 1            | vigeo               | 1               |
| splendeo        | 1            | splendens           | 1               |
| intervias       | 1            | intervivs           | 1               |
| profestvs       | 1            | profesto            | 1               |
| expetesso       | 1            | expeto              | 1               |
| ivnctvs         | 1            | ivngo               | 1               |
| olla            | 1            | avla                | 1               |
| extremvm        | 1            | exter               | 1               |
| graecvli        | 1            | graecvlvs           | 1               |
| sepositvs       | 1            | sepono              | 1               |
| occvlte         | 1            | occvltvs            | 1               |
| foris           | 1            | forivm              | 1               |
| ploro           | 1            | plora               | 1               |
| antigone        | 1            | antigones           | 1               |
| melanippe       | 1            | melanippes          | 1               |
| colossvs        | 1            | colosvs             | 1               |
| avgvstiani      | 1            | avgvstani           | 1               |
| freni           | 1            | frenvm              | 1               |
| praeceptvm      | 1            | praecipio           | 1               |
| fixvs           | 1            | figo                | 1               |
| pingve          | 1            | pingvis             | 1               |
| romvlidae       | 1            | romvlida            | 1               |
| exigvvs         | 1            | exigvvm             | 1               |
| oblecto         | 1            | oblictvs            | 1               |
| davnivs         | 1            | davniae             | 1               |
| procer          | 1            | proceres            | 1               |
| praepotentes    | 1            | praepotens          | 1               |
| bvbvla          | 1            | bvbvlvs             | 1               |
| cetvs           | 1            | cetvm               | 1               |
| extollo         | 1            | effero              | 1               |
| decima          | 1            | decimvs             | 1               |
| morigervs       | 1            | moriger             | 1               |
| moneo           | 1            | monitvs             | 1               |
| exoleti         | 1            | exolesco            | 1               |
| vlcvs           | 1            | vlcor               | 1               |
| caepa           | 1            | caepe               | 1               |
| nvmqvisnam      | 1            | nvmqvis             | 1               |
| sagvlvm         | 1            | sagvla              | 1               |
| seqvens         | 1            | seqvor              | 1               |
| vniversi        | 1            | vniversvs           | 1               |
| artacie         | 1            | artacivs            | 1               |
| cimmerii        | 1            | cimmerion           | 1               |
| candeo          | 1            | candens             | 1               |
| lativs          | 1            | lativm              | 1               |
| amictvs         | 1            | amicio              | 1               |
| aeqvvs          | 1            | aeqvvm              | 1               |
| recrvdesco      | 1            | recrvdo             | 1               |
| laxo            | 1            | lax                 | 1               |
| glvtvs          | 1            | glvttvs             | 1               |
| occvpatvs       | 1            | occvpo              | 1               |
| rigeo           | 1            | rigens              | 1               |
| crvdeliter      | 1            | crvdelis            | 1               |
| externi         | 1            | externvs            | 1               |
| inavdio         | 1            | indo                | 1               |
| dinomache       | 1            | dinomachvs          | 1               |
| spisso          | 1            | spissatvs           | 1               |

::: Evaluation report for task: pos :::

all:
  accuracy: 0.964
  precision: 0.9135
  recall: 0.9015
  support: 141953
ambiguous-tokens:
  accuracy: 0.8954
  precision: 0.8163
  recall: 0.7929
  support: 35830

| Expected   | Total Errors | Predictions | Predicted times |
|------------|--------------|-------------|-----------------|
| ADJqua     | 1129         | NOM         | 722             |
|            |              | VER         | 258             |
|            |              | ADV         | 136             |
|            |              | CONcoo      | 6               |
|            |              | PRE         | 3               |
|            |              | ADJord      | 2               |
|            |              | ADVint      | 1               |
|            |              | ADJcar      | 1               |
| NOM        | 1092         | ADJqua      | 684             |
|            |              | VER         | 268             |
|            |              | ADV         | 69              |
|            |              | PROpos.ref  | 14              |
|            |              | PROind      | 13              |
|            |              | CONcoo      | 10              |
|            |              | ADJcar      | 8               |
|            |              | PRE         | 8               |
|            |              | ADJdis      | 7               |
|            |              | PROint      | 3               |
|            |              | PROref      | 2               |
|            |              | PROdem      | 2               |
|            |              | PROpos      | 2               |
|            |              |             | 1               |
|            |              | ADVint      | 1               |
| ADV        | 518          | CONcoo      | 161             |
|            |              | PROdem      | 85              |
|            |              | ADJqua      | 77              |
|            |              | PRE         | 50              |
|            |              | NOM         | 44              |
|            |              | CONsub      | 33              |
|            |              | PROind      | 23              |
|            |              | VER         | 18              |
|            |              | ADJcar      | 11              |
|            |              |             | 5               |
|            |              | ADVneg      | 4               |
|            |              | ADJord      | 2               |
|            |              | PROrel      | 2               |
|            |              | PROper      | 1               |
|            |              | ADVrel      | 1               |
|            |              | INJ         | 1               |
| VER        | 449          | NOM         | 206             |
|            |              | ADJqua      | 196             |
|            |              | CONsub      | 15              |
|            |              | ADV         | 12              |
|            |              | PROdem      | 5               |
|            |              | INJ         | 4               |
|            |              |             | 3               |
|            |              | PRE         | 3               |
|            |              | ADJcar      | 2               |
|            |              | PROper      | 1               |
|            |              | ADVint      | 1               |
|            |              | ADVrel      | 1               |
| CONsub     | 392          | ADVrel      | 118             |
|            |              | PROrel      | 118             |
|            |              | CONcoo      | 52              |
|            |              | PRE         | 51              |
|            |              | VER         | 15              |
|            |              | ADV         | 15              |
|            |              | ADVint      | 14              |
|            |              | ADVneg      | 6               |
|            |              | PROint      | 3               |
| ADVrel     | 311          | CONsub      | 156             |
|            |              | ADVint      | 71              |
|            |              | PROrel      | 70              |
|            |              | VER         | 6               |
|            |              | PROint      | 5               |
|            |              | ADV         | 2               |
|            |              | PROind      | 1               |
| PROrel     | 280          | PROint      | 112             |
|            |              | CONsub      | 74              |
|            |              | ADVrel      | 60              |
|            |              | ADVint      | 18              |
|            |              | PROind      | 10              |
|            |              | CONcoo      | 6               |
| PROint     | 238          | PROrel      | 192             |
|            |              | ADVint      | 24              |
|            |              | ADVrel      | 12              |
|            |              | PROind      | 6               |
|            |              | CONsub      | 2               |
|            |              | ADV         | 1               |
|            |              | INJ         | 1               |
| ADVint     | 167          | ADVrel      | 71              |
|            |              | CONsub      | 39              |
|            |              | PROrel      | 29              |
|            |              | PROint      | 10              |
|            |              | VER         | 6               |
|            |              | NOM         | 4               |
|            |              | PROdem      | 2               |
|            |              | ADV         | 2               |
|            |              | ADJcar      | 1               |
|            |              | PROper      | 1               |
|            |              | ADVint.neg  | 1               |
|            |              | PROind      | 1               |
| PROdem     | 87           | ADV         | 80              |
|            |              | VER         | 4               |
|            |              | NOM         | 1               |
|            |              | PROind      | 1               |
|            |              | INJ         | 1               |
| PRE        | 83           | CONsub      | 45              |
|            |              | ADV         | 33              |
|            |              | VER         | 4               |
|            |              | INJ         | 1               |
| CONcoo     | 69           | ADV         | 37              |
|            |              | CONsub      | 24              |
|            |              | PROrel      | 7               |
|            |              | ADJqua      | 1               |
| PROind     | 55           | ADV         | 17              |
|            |              | PROint      | 14              |
|            |              | PROrel      | 12              |
|            |              | NOM         | 9               |
|            |              | ADVrel      | 2               |
|            |              | VER         | 1               |
|            | 54           | ADV         | 14              |
|            |              | VER         | 10              |
|            |              | NOM         | 7               |
|            |              | ADJqua      | 7               |
|            |              | ADJadv.ord  | 7               |
|            |              | PRE         | 3               |
|            |              | CONcoo      | 2               |
|            |              | CONsub      | 2               |
|            |              | PROind      | 1               |
|            |              | INJ         | 1               |
| ADJord     | 45           | ADJqua      | 22              |
|            |              | ADJadv.ord  | 19              |
|            |              | ADJcar      | 1               |
|            |              | PRE         | 1               |
|            |              |             | 1               |
|            |              | NOM         | 1               |
| ADVneg     | 39           | CONsub      | 33              |
|            |              | CONcoo      | 4               |
|            |              | VER         | 2               |
| PROper     | 25           | PROpos      | 24              |
|            |              | VER         | 1               |
| INJ        | 15           | PRE         | 6               |
|            |              | NOM         | 3               |
|            |              | VER         | 2               |
|            |              | ADV         | 2               |
|            |              | PROdem      | 2               |
| PROpos.ref | 13           | PROref      | 12              |
|            |              | NOM         | 1               |
| PROpos     | 12           | PROper      | 12              |
| ADJcar     | 11           | ADV         | 5               |
|            |              | NOM         | 3               |
|            |              | ADJord      | 2               |
|            |              | PRE         | 1               |
| ADJdis     | 8            | NOM         | 6               |
|            |              | ADJcar      | 1               |
|            |              | ADJord      | 1               |
| PROref     | 6            | PROpos.ref  | 4               |
|            |              | PROdem      | 2               |
| ADJadv.ord | 5            | ADJord      | 5               |
| ADJmul     | 3            | ADJqua      | 2               |
|            |              | NOM         | 1               |
| ADVint.neg | 3            | ADV         | 2               |
|            |              | CONsub      | 1               |
| VERaux     | 2            | VER         | 2               |
