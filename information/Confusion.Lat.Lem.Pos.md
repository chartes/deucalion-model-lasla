Confusion tables
================

- [Lemma](#lemma)
- [Part-Of-Speech](#pos)
- [Morph](#morph)

# Lemma

```
all:
  accuracy: 0.9729
  precision: 0.8075
  recall: 0.7982
  support: 146137
ambiguous-tokens:
  accuracy: 0.9251
  precision: 0.6954
  recall: 0.6978
  support: 32951
unknown-targets:
  accuracy: 0.6159
  precision: 0.4385
  recall: 0.4283
  support: 1044
unknown-tokens:
  accuracy: 0.8574
  precision: 0.7105
  recall: 0.7017
  support: 6114
```

| Expected          | Total Errors | Predictions      | Predicted times |
|-------------------|--------------|------------------|-----------------|
| qvi               | 215          | qvis             | 85              |
|                   |              | qvod             | 80              |
|                   |              | qvam             | 22              |
|                   |              | qvo              | 19              |
|                   |              | qva              | 9               |
| qvod              | 133          | qvi              | 129             |
|                   |              | qvis             | 4               |
| qvis              | 126          | qvi              | 119             |
|                   |              | qvo              | 2               |
|                   |              | qvam             | 2               |
|                   |              | qvod             | 2               |
|                   |              | qva              | 1               |
| mvltvs            | 46           | mvltvm           | 25              |
|                   |              | mvlti            | 18              |
|                   |              | mvlta            | 2               |
|                   |              | mvlto            | 1               |
| qvam              | 33           | qvi              | 30              |
|                   |              | anteqvam         | 1               |
|                   |              | privsqvam        | 1               |
|                   |              | qvis             | 1               |
| svvs              | 29           | svi              | 23              |
|                   |              | svvm             | 6               |
| bonvs             | 24           | bonvm            | 13              |
|                   |              | bene             | 9               |
|                   |              | boni             | 2               |
| svi               | 21           | svvs             | 20              |
|                   |              | ipse             | 1               |
| is                | 19           | eo               | 18              |
|                   |              | hem              | 1               |
| qva               | 17           | qvi              | 15              |
|                   |              | qvis             | 2               |
| magnvm            | 17           | magnvs           | 17              |
| facio             | 16           | factvm           | 14              |
|                   |              | facies           | 2               |
| factvm            | 16           | facio            | 16              |
| malvs             | 16           | malvm            | 14              |
|                   |              | malo             | 1               |
|                   |              | male             | 1               |
| cetervs           | 16           | ceteri           | 11              |
|                   |              | cetera           | 5               |
| mvlti             | 16           | mvltvs           | 16              |
| qvo               | 16           | qvi              | 16              |
| mvltvm            | 15           | mvltvs           | 15              |
| malvm             | 15           | malvs            | 13              |
|                   |              | malo             | 1               |
|                   |              | mali             | 1               |
| parvvs            | 14           | parvm            | 10              |
|                   |              | parvvm           | 3               |
|                   |              | minimvm          | 1               |
| primvs            | 14           | primvm           | 8               |
|                   |              | viginti          | 3               |
|                   |              | primo            | 2               |
|                   |              | prima            | 1               |
| bonvm             | 14           | bonvs            | 8               |
|                   |              | boni             | 6               |
| pavcvs            | 12           | pavci            | 12              |
| reliqvvs          | 12           | reliqvi          | 7               |
|                   |              | reliqvvm         | 5               |
| boni              | 11           | bonvm            | 7               |
|                   |              | bonvs            | 4               |
| anteqvam          | 11           | qvam             | 6               |
|                   |              | qvi              | 5               |
| eo                | 11           | is               | 11              |
| tracta            | 10           | traho            | 8               |
|                   |              | tracto           | 1               |
|                   |              | tractvm          | 1               |
| veneo             | 10           | venio            | 10              |
| ago               | 10           | age              | 5               |
|                   |              | actvm            | 3               |
|                   |              | agite            | 1               |
|                   |              | actvs            | 1               |
| qvantvs           | 10           | qvantvm          | 8               |
|                   |              | qvanto           | 2               |
| privsqvam         | 9            | qvam             | 6               |
|                   |              | qvi              | 3               |
| cvltvs            | 9            | colo             | 9               |
| tantvs            | 9            | tantvm           | 8               |
|                   |              | tanto            | 1               |
| paro              | 9            | paratvs          | 4               |
|                   |              | par              | 3               |
|                   |              | pareo            | 2               |
| nascor            | 9            | natvs            | 6               |
|                   |              | nata             | 3               |
| meritvs           | 8            | mereor           | 7               |
|                   |              | meritvm          | 1               |
| volo              | 8            | volens           | 3               |
|                   |              | vis              | 2               |
|                   |              | svm              | 2               |
|                   |              | velvm            | 1               |
| fera              | 8            | fervs            | 6               |
|                   |              | fero             | 2               |
| vervm             | 8            | vero             | 5               |
|                   |              | vervs            | 3               |
| vervs             | 8            | vervm            | 8               |
| sero              | 8            | sata             | 3               |
|                   |              | servs            | 2               |
|                   |              | servm            | 1               |
|                   |              | sera             | 1               |
|                   |              | satis            | 1               |
| vos               | 8            | vester           | 8               |
| ivre              | 8            | ivs              | 8               |
| vnvs              | 7            | vna              | 5               |
|                   |              | viginti          | 1               |
|                   |              | vnvm             | 1               |
| sacer             | 7            | sacrvm           | 7               |
| primvm            | 7            | primvs           | 7               |
| passvs            | 7            | patior           | 6               |
|                   |              | pondo            | 1               |
| svmma             | 7            | svpervs          | 7               |
| sine              | 7            | sino             | 7               |
| perditvs          | 7            | perdo            | 5               |
|                   |              | perditer         | 1               |
|                   |              | perditvm         | 1               |
| svm               | 7            | fvtvrvm          | 3               |
|                   |              | fvtvrvs          | 1               |
|                   |              | svntvs           | 1               |
|                   |              | sitis            | 1               |
|                   |              | celo             | 1               |
| modo              | 7            | modvs            | 7               |
| mortvvs           | 7            | morior           | 7               |
| libra             | 6            | littera          | 4               |
|                   |              | limer            | 1               |
|                   |              | littevm          | 1               |
| lego              | 6            | lex              | 3               |
|                   |              | legatvs          | 2               |
|                   |              | lectvs           | 1               |
| venio             | 6            | venia            | 5               |
|                   |              | ventvrvm         | 1               |
| vt                | 6            | vtor             | 6               |
| solvs             | 6            | solvm            | 5               |
|                   |              | sol              | 1               |
| magnvs            | 6            | maiores          | 6               |
| pingo             | 6            | pictvs           | 5               |
|                   |              | picta            | 1               |
| dedo              | 6            | deditvs          | 5               |
|                   |              | do               | 1               |
| tantvm            | 6            | tantvs           | 6               |
| medivm            | 6            | medivs           | 6               |
| aeqvvm            | 6            | aeqvvs           | 6               |
| tego              | 6            | tectvm           | 5               |
|                   |              | tectvs           | 1               |
| fero              | 6            | ferrvm           | 2               |
|                   |              | fera             | 2               |
|                   |              | ferreti          | 1               |
|                   |              | latvs            | 1               |
| pes               | 6            | pondo            | 4               |
|                   |              | pedes            | 2               |
| mevs              | 6            | ego              | 3               |
|                   |              | mei              | 3               |
| svvm              | 6            | svvs             | 5               |
|                   |              | svi              | 1               |
| nostri            | 6            | noster           | 6               |
| ora               | 6            | os               | 6               |
| hadrvmentvm       | 6            | hadrvmetvm       | 3               |
|                   |              | hadrvmetvs       | 2               |
|                   |              | hadrvmetivm      | 1               |
| legatvm           | 5            | legatvs          | 3               |
|                   |              | lego             | 2               |
| extremvm          | 5            | exter            | 5               |
| nocte             | 5            | nox              | 5               |
| qvintvs           | 5            | qvinqve          | 5               |
| refert            | 5            | refero           | 5               |
| desero            | 5            | desertvs         | 5               |
| honestvm          | 5            | honestvs         | 5               |
| solvo             | 5            | solvtvs          | 3               |
|                   |              | solveo           | 1               |
|                   |              | solvvs           | 1               |
| nota              | 5            | notvs            | 5               |
| vtor              | 5            | vt               | 4               |
|                   |              | vsvs             | 1               |
| fervs             | 5            | fera             | 4               |
|                   |              | fero             | 1               |
| notvs             | 5            | nota             | 3               |
|                   |              | notis            | 1               |
|                   |              | noti             | 1               |
| tvvs              | 5            | tv               | 5               |
| conivnctvs        | 5            | conivngo         | 5               |
| honestvs          | 5            | honestvm         | 4               |
|                   |              | honeste          | 1               |
| andron            | 5            | andronivs        | 2               |
|                   |              | andro            | 2               |
|                   |              | andrvs           | 1               |
| opvs              | 5            | opera            | 5               |
| propinqvvs        | 5            | propinqvi        | 5               |
| svpervs           | 5            | svmmvm           | 2               |
|                   |              | svmma            | 1               |
|                   |              | svpremvm         | 1               |
|                   |              | svpero           | 1               |
| versvs            | 5            | verto            | 5               |
| dico              | 5            | dictvm           | 5               |
| tricesimvs        | 5            | triginta         | 5               |
| adversvm          | 5            | adversvs         | 5               |
| liber             | 5            | liberi           | 4               |
|                   |              | libere           | 1               |
| rhodienses        | 5            | rodiensis        | 3               |
|                   |              | rodienses        | 2               |
| decimvs           | 5            | decem            | 1               |
|                   |              | qvatvordecim     | 1               |
|                   |              | decimvm          | 1               |
|                   |              | tertivs          | 1               |
|                   |              | qvatvordecimvs   | 1               |
| rego              | 5            | rex              | 5               |
| malo              | 5            | malvm            | 3               |
|                   |              | malvs            | 1               |
|                   |              | mali             | 1               |
| armo              | 4            | armatvs          | 2               |
|                   |              | armati           | 2               |
| cothon            | 4            | cotho            | 4               |
| perdo             | 4            | perditvs         | 3               |
|                   |              | perdvo           | 1               |
| svspensvs         | 4            | svspendo         | 4               |
| nosco             | 4            | notvs            | 4               |
| aer               | 4            | aes              | 4               |
| defessvs          | 4            | defetiscor       | 4               |
| secvndvs          | 4            | secvndvm         | 3               |
|                   |              | dvo              | 1               |
| improbo           | 4            | improbvs         | 3               |
|                   |              | improbatvs       | 1               |
| minimvm           | 4            | parvvs           | 3               |
|                   |              | parvm            | 1               |
| improbvs          | 4            | improbe          | 3               |
|                   |              | improbo          | 1               |
| solitvs           | 4            | soleo            | 3               |
|                   |              | solitvm          | 1               |
| verso             | 4            | versor           | 4               |
| spons             | 4            | sponte           | 4               |
| primo             | 4            | primvs           | 4               |
| qvinqvagesima     | 4            | qvinqvagesimvs   | 4               |
| elorvs            | 4            | helores          | 2               |
|                   |              | elvorvs          | 1               |
|                   |              | helorvs          | 1               |
| ardens            | 4            | ardeo            | 3               |
|                   |              | ardenter         | 1               |
| fortis            | 4            | forte            | 2               |
|                   |              | fors             | 1               |
|                   |              | fortiter         | 1               |
| lino              | 4            | linio            | 3               |
|                   |              | levo             | 1               |
| qvingenti         | 4            | mille            | 2               |
|                   |              | septvaginta      | 1               |
|                   |              | qvi              | 1               |
| armati            | 4            | armatvs          | 4               |
| alias             | 4            | alivs            | 4               |
| patria            | 4            | patrivs          | 4               |
| solvm             | 4            | solvs            | 4               |
| natvs             | 4            | nascor           | 4               |
| bogvd             | 4            | bogvs            | 4               |
| nos               | 4            | noster           | 4               |
| hvmanvs           | 4            | hvmana           | 4               |
| vter              | 4            | vtrvm            | 4               |
| commodvs          | 4            | commodvm         | 3               |
|                   |              | commode          | 1               |
| fvsvs             | 4            | fvndo            | 4               |
| modvs             | 4            | modo             | 4               |
| hvc               | 4            | hic              | 2               |
|                   |              | hvcinvs          | 1               |
|                   |              | hvcvs            | 1               |
| noster            | 4            | nos              | 4               |
| lvcvs             | 4            | lvx              | 4               |
| instrvo           | 4            | instrvctvs       | 4               |
| qvanto            | 4            | qvantvs          | 4               |
| ah                | 4            | ab               | 4               |
| gallvs            | 4            | galli            | 3               |
|                   |              | gallis           | 1               |
| catinvm           | 4            | catinvs          | 4               |
| fvtvrvs           | 4            | fvtvrvm          | 3               |
|                   |              | svm              | 1               |
| febrvarivs        | 4            | febrvs           | 3               |
|                   |              | febrvlaebivs     | 1               |
| epibata           | 4            | epibo            | 3               |
|                   |              | epibatvs         | 1               |
| longvs            | 3            | longe            | 2               |
|                   |              | longvm           | 1               |
| evge              | 3            | evgeo            | 3               |
| figo              | 3            | figa             | 1               |
|                   |              | fixvs            | 1               |
|                   |              | figvs            | 1               |
| dexter            | 3            | dextera          | 3               |
| vvlgo             | 3            | vvlgvs           | 2               |
|                   |              | vvlgarvs         | 1               |
| orbvs             | 3            | orbis            | 3               |
| denvs             | 3            | qvindecim        | 2               |
|                   |              | dena             | 1               |
| tv                | 3            | tvmeo            | 2               |
|                   |              | tvvs             | 1               |
| refero            | 3            | refert           | 2               |
|                   |              | relatvs          | 1               |
| vltimvs           | 3            | vltimvm          | 3               |
| pendo             | 3            | pendeo           | 3               |
| sacrvm            | 3            | sacer            | 3               |
| bellvs            | 3            | bellvm           | 3               |
| conor             | 3            | conatvs          | 3               |
| institvo          | 3            | institvtvm       | 3               |
| mvlta             | 3            | mvltvs           | 3               |
| velvm             | 3            | volo             | 2               |
|                   |              | velis            | 1               |
| incertvm          | 3            | incertvs         | 3               |
| edo               | 3            | editvs           | 2               |
|                   |              | svm              | 1               |
| aeqvvs            | 3            | aeqvvm           | 3               |
| nitor             | 3            | niteo            | 2               |
|                   |              | nisi             | 1               |
| pilvm             | 3            | pila             | 2               |
|                   |              | pilvs            | 1               |
| vicesimvs         | 3            | viginti          | 3               |
| gener             | 3            | genvs            | 3               |
| postvlatvm        | 3            | postvlo          | 3               |
| armatvs           | 3            | armati           | 2               |
|                   |              | armo             | 1               |
| lavrevs           | 3            | lavrea           | 3               |
| asvvivs           | 3            | asvvs            | 2               |
|                   |              | asvvvs           | 1               |
| mvlto             | 3            | mvltvs           | 3               |
| pictvs            | 3            | pingo            | 3               |
| laevvm            | 3            | laevvs           | 2               |
|                   |              | laeva            | 1               |
| commis            | 3            | cvmmim           | 3               |
| plervsqve         | 3            | pleriqve         | 3               |
| mali              | 3            | malvm            | 3               |
| tvrpis            | 3            | tvrpe            | 2               |
|                   |              | tvrpes           | 1               |
| sextarivs         | 3            | semis            | 3               |
| alienvs           | 3            | alienvm          | 3               |
| percontor         | 3            | percvnctor       | 3               |
| proclivis         | 3            | procliver        | 1               |
|                   |              | proclive         | 1               |
|                   |              | proclivivm       | 1               |
| electvs           | 3            | eligo            | 3               |
| dvo               | 3            | mille            | 2               |
|                   |              | viginti          | 1               |
| maneo             | 3            | manea            | 1               |
|                   |              | mane             | 1               |
|                   |              | manes            | 1               |
| achilles          | 3            | achillvs         | 3               |
| laetor            | 3            | laeto            | 1               |
|                   |              | laetatvm         | 1               |
|                   |              | laetatvs         | 1               |
| virgilivs         | 3            | vergilivs        | 3               |
| patrivs           | 3            | patria           | 3               |
| ivro              | 3            | ivratvs          | 1               |
|                   |              | ivra             | 1               |
|                   |              | ivs              | 1               |
| hiccine           | 3            | ne               | 1               |
|                   |              | hic              | 1               |
|                   |              | hicine           | 1               |
| placeo            | 3            | placo            | 2               |
|                   |              | place            | 1               |
| fictvs            | 3            | fingo            | 3               |
| effvsvs           | 3            | effvndo          | 3               |
| defvnctvs         | 3            | defvngor         | 3               |
| hospitivm         | 3            | hospes           | 3               |
| sescenti          | 3            | mille            | 3               |
| dvco              | 3            | dvx              | 2               |
|                   |              | dvctvs           | 1               |
| gravis            | 3            | graviter         | 3               |
| vniversi          | 3            | vniversvs        | 3               |
| amo               | 3            | amans            | 3               |
| nvbo              | 3            | nvpta            | 2               |
|                   |              | nvbes            | 1               |
| vagvs             | 3            | vagvm            | 3               |
| gaditani          | 3            | gaditanvs        | 3               |
| corinthivs        | 3            | corinthivm       | 2               |
|                   |              | corinthia        | 1               |
| vettones          | 3            | vetto            | 3               |
| patera            | 3            | patior           | 3               |
| aedvi             | 3            | haedvi           | 2               |
|                   |              | haedvs           | 1               |
| aes               | 3            | aer              | 3               |
| liberi            | 3            | liber            | 3               |
| viginti           | 3            | qvinqve          | 1               |
|                   |              | sex              | 1               |
|                   |              | vicesimvs        | 1               |
| compono           | 3            | compositvs       | 3               |
| camertes          | 3            | camertivs        | 2               |
|                   |              | camerses         | 1               |
| falsvm            | 3            | falsvs           | 3               |
| tvrpe             | 3            | tvrpis           | 3               |
| popvliana         | 3            | popvlianvs       | 3               |
| lvrco             | 3            | lvrcvs           | 3               |
| removeo           | 3            | remotvs          | 3               |
| nvntivs           | 3            | nvntivm          | 2               |
|                   |              | nvntio           | 1               |
| fraces            | 3            | fraceo           | 2               |
|                   |              | frax             | 1               |
| caesariani        | 3            | caesarianvs      | 3               |
| exter             | 3            | extremvm         | 3               |
| mereor            | 3            | meritvs          | 3               |
| naris             | 3            | no               | 2               |
|                   |              | nas              | 1               |
| scriba            | 3            | scribo           | 3               |
| partvs            | 3            | pario            | 3               |
| manes             | 3            | manvs            | 1               |
|                   |              | maneo            | 1               |
|                   |              | manen            | 1               |
| illi              | 3            | ille             | 3               |
| pario             | 3            | pareo            | 3               |
| vergilivs         | 3            | virgilivs        | 3               |
| hic               | 3            | hvc              | 2               |
|                   |              | hac              | 1               |
| mortarivm         | 3            | mortarivs        | 3               |
| ego               | 3            | mevs             | 3               |
| reliqva           | 3            | reliqvvm         | 2               |
|                   |              | reliqvvs         | 1               |
| parens            | 3            | parentes         | 3               |
| ceteri            | 3            | cetervs          | 3               |
| pvblicvm          | 3            | pvblicvs         | 3               |
| nvmqvid           | 3            | nvmqvis          | 3               |
| pareo             | 3            | paro             | 1               |
|                   |              | parens           | 1               |
|                   |              | parvvm           | 1               |
| visvm             | 3            | video            | 3               |
| regia             | 3            | regivs           | 3               |
| morior            | 3            | mortvvs          | 3               |
| impvne            | 3            | impoene          | 3               |
| qvinqvaginta      | 3            | qvinqve          | 2               |
|                   |              | lvcivs           | 1               |
| scriptvm          | 3            | scribo           | 3               |
| veteres           | 3            | vetvs            | 3               |
| meritvm           | 3            | meritvs          | 3               |
| areo              | 3            | aro              | 3               |
| resideo           | 3            | resido           | 3               |
| lesbides          | 3            | lesbis           | 3               |
| caneo             | 2            | cano             | 2               |
| occvltvm          | 2            | occvltvs         | 2               |
| canvs             | 2            | cano             | 2               |
| intendo           | 2            | intentvs         | 2               |
| alaris            | 2            | alar             | 2               |
| freno             | 2            | frenvm           | 1               |
|                   |              | frenatvs         | 1               |
| interiacio        | 2            | intericio        | 2               |
| laeva             | 2            | laevvs           | 2               |
| pvnicvs           | 2            | pvnici           | 1               |
|                   |              | poenicvs         | 1               |
| pharnaces         | 2            | pharnacvs        | 2               |
| condio            | 2            | condo            | 2               |
| ratvs             | 2            | reor             | 2               |
| agyrinenses       | 2            | agyrinensis      | 2               |
| exardeo           | 2            | exardesco        | 2               |
| abdo              | 2            | abditvs          | 2               |
| vniversvs         | 2            | vniversi         | 1               |
|                   |              | vniversvm        | 1               |
| vernvs            | 2            | verna            | 2               |
| pacifico          | 2            | pacificor        | 1               |
|                   |              | pacifica         | 1               |
| expeditvs         | 2            | expedio          | 1               |
|                   |              | expedito         | 1               |
| fretvs            | 2            | fretvm           | 2               |
| moderor           | 2            | moderatvs        | 1               |
|                   |              | modeor           | 1               |
| vtrvm             | 2            | vter             | 2               |
| idiota            | 2            | idiotvs          | 2               |
| altvm             | 2            | altvs            | 2               |
| insignis          | 2            | insigne          | 2               |
| posterivs         | 2            | postervs         | 2               |
| vivvm             | 2            | vivvs            | 2               |
| pasco             | 2            | pascor           | 2               |
| aeternvs          | 2            | aeterno          | 2               |
| togatvs           | 2            | togati           | 2               |
| cetera            | 2            | cetervs          | 2               |
| centvmvir         | 2            | ceirvs           | 1               |
|                   |              | centvs           | 1               |
| cano              | 2            | caneo            | 1               |
|                   |              | canis            | 1               |
| centvripinvs      | 2            | centvripini      | 2               |
| praeterita        | 2            | praetereo        | 1               |
|                   |              | praeteritvm      | 1               |
| sedo              | 2            | sedatvs          | 1               |
|                   |              | sedeo            | 1               |
| asilvs            | 2            | asilvm           | 2               |
| coqvo             | 2            | coco             | 2               |
| tvto              | 2            | tvtvs            | 2               |
| donec             | 2            | donicvs          | 2               |
| svspendo          | 2            | svspensvs        | 2               |
| remotvs           | 2            | removeo          | 2               |
| vngven            | 2            | vngvis           | 2               |
| qvintilivs        | 2            | qvintilivm       | 1               |
|                   |              | qvintilvs        | 1               |
| solidvm           | 2            | solidvs          | 2               |
| parentes          | 2            | parens           | 2               |
| sinister          | 2            | sinistra         | 2               |
| frigida           | 2            | frigidvs         | 2               |
| halaesinvs        | 2            | halaesinvm       | 2               |
| divinvs           | 2            | divina           | 2               |
| accensvs          | 2            | accendo          | 2               |
| diivnctvs         | 2            | diivngo          | 2               |
| medimnvm          | 2            | medis            | 1               |
|                   |              | medivs           | 1               |
| absens            | 2            | absvm            | 2               |
| cvivs             | 2            | cvia             | 1               |
|                   |              | qvi              | 1               |
| maiores           | 2            | magnvs           | 2               |
| serpens           | 2            | serpo            | 2               |
| sexcenti          | 2            | sescens          | 1               |
|                   |              | sescenti         | 1               |
| vanvs             | 2            | vanvm            | 1               |
|                   |              | vane             | 1               |
| deleo             | 2            | defero           | 1               |
|                   |              | deligo           | 1               |
| sestertivs        | 2            | sestertivm       | 2               |
| tvtvs             | 2            | tvtvm            | 2               |
| consvlo           | 2            | consvlto         | 1               |
|                   |              | consvl           | 1               |
| datvm             | 2            | do               | 2               |
| patron            | 2            | patro            | 1               |
|                   |              | patrona          | 1               |
| svbiectvm         | 2            | svbicio          | 2               |
| gavsapa           | 2            | gavsapvs         | 2               |
| probo             | 2            | probvs           | 1               |
|                   |              | probatvs         | 1               |
| gravor            | 2            | gravo            | 2               |
| solitvm           | 2            | solitvs          | 1               |
|                   |              | solito           | 1               |
| svbitvs           | 2            | svbito           | 1               |
|                   |              | svbitvm          | 1               |
| serva             | 2            | servo            | 2               |
| istvc             | 2            | istic            | 2               |
| occvlo            | 2            | occvltvs         | 2               |
| desertvs          | 2            | deserta          | 1               |
|                   |              | desero           | 1               |
| aestiva           | 2            | aestivvs         | 2               |
| sancio            | 2            | sanctvs          | 2               |
| plvrimvm          | 2            | mvltvs           | 2               |
| ei                | 2            | is               | 2               |
| interdictvm       | 2            | interdico        | 2               |
| alio              | 2            | alivs            | 2               |
| alienvm           | 2            | alienvs          | 2               |
| pilvs             | 2            | pilvm            | 2               |
| phaeacia          | 2            | phaeacivs        | 2               |
| deditvs           | 2            | dedo             | 2               |
| aliqva            | 2            | aliqvis          | 2               |
| insto             | 2            | insisto          | 2               |
| probatvs          | 2            | probo            | 2               |
| caelestis         | 2            | caelestes        | 1               |
|                   |              | caelestia        | 1               |
| catabathmos       | 2            | catabathmvs      | 1               |
|                   |              | catabathon       | 1               |
| diogenes          | 2            | diogene          | 2               |
| comitatvs         | 2            | comitor          | 2               |
| vas               | 2            | vado             | 1               |
|                   |              | vaso             | 1               |
| aerarivm          | 2            | aerarivs         | 2               |
| adversvs          | 2            | adversvm         | 2               |
| exsterno          | 2            | externo          | 2               |
| erycina           | 2            | erycinvs         | 2               |
| conivngo          | 2            | conivnctvs       | 2               |
| vrvs              | 2            | vro              | 2               |
| agyrivm           | 2            | agyrivs          | 1               |
|                   |              | agyrvs           | 1               |
| sicvlvs           | 2            | sicvli           | 2               |
| sol               | 2            | solvs            | 2               |
| heracleon         | 2            | heraclevs        | 2               |
| facilis           | 2            | facile           | 2               |
| horreo            | 2            | horresco         | 2               |
| exactvs           | 2            | exigo            | 2               |
| svspectvs         | 2            | svspicio         | 2               |
| vestri            | 2            | vester           | 2               |
| irascor           | 2            | iratvs           | 2               |
| vivens            | 2            | vivo             | 2               |
| decor             | 2            | decvs            | 2               |
| tvrritvs          | 2            | tvrro            | 1               |
|                   |              | tvrrio           | 1               |
| advocatvs         | 2            | advoco           | 2               |
| accvmbo           | 2            | accvbo           | 2               |
| arsanias          | 2            | arsania          | 2               |
| vetera            | 2            | vetvs            | 2               |
| ecbatana          | 2            | ecbatani         | 1               |
|                   |              | ecbatanvs        | 1               |
| aedilicivs        | 2            | aedilicivm       | 2               |
| recta             | 2            | rectvs           | 2               |
| fames             | 2            | famen            | 1               |
|                   |              | famvm            | 1               |
| ivliani           | 2            | ivlianvs         | 2               |
| praervpta         | 2            | praervptvs       | 2               |
| scribo            | 2            | scribvndvs       | 1               |
|                   |              | scriptvm         | 1               |
| manica            | 2            | manicvs          | 2               |
| reliqvvm          | 2            | reliqvi          | 1               |
|                   |              | reliqvvs         | 1               |
| victvs            | 2            | vinco            | 2               |
| asto              | 2            | assisto          | 2               |
| lvpinvm           | 2            | lvpinvs          | 2               |
| perficio          | 2            | perfectvs        | 2               |
| genivs            | 2            | genia            | 1               |
|                   |              | genivm           | 1               |
| mediolanvm        | 2            | mediolanvs       | 2               |
| amplivs           | 2            | ample            | 2               |
| exerceo           | 2            | exercitvs        | 2               |
| compositvs        | 2            | compono          | 2               |
| reliqvi           | 2            | reliqvvs         | 2               |
| ide               | 2            | ida              | 2               |
| affectvs          | 2            | afficio          | 2               |
| porrvm            | 2            | porrvs           | 1               |
|                   |              | porrvmpo         | 1               |
| vlpicvm           | 2            | vlpicvs          | 1               |
|                   |              | vlpex            | 1               |
| vivo              | 2            | vinco            | 1               |
|                   |              | vivvs            | 1               |
| metvo             | 2            | meto             | 1               |
|                   |              | metvvs           | 1               |
| sitiens           | 2            | sitio            | 2               |
| divina            | 2            | divinvs          | 2               |
| mvnio             | 2            | mvnitvs          | 1               |
|                   |              | mvnvs            | 1               |
| foris             | 2            | svm              | 2               |
| improvisvs        | 2            | improvisvm       | 2               |
| arcanvs           | 2            | arcanvm          | 2               |
| gemini            | 2            | geminvs          | 2               |
| praetorivm        | 2            | praetorivs       | 2               |
| cognitvs          | 2            | cognosco         | 2               |
| beta              | 2            | betvs            | 1               |
|                   |              | betvm            | 1               |
| vtrobi            | 2            | vtrvbi           | 1               |
|                   |              | vtrvbvm          | 1               |
| fvro              | 2            | fvrens           | 2               |
| fenvm             | 2            | fenis            | 2               |
| svbiectvs         | 2            | svbicio          | 2               |
| attonitvs         | 2            | attono           | 2               |
| panicvm           | 2            | panicvs          | 2               |
| sino              | 2            | sine             | 2               |
| semis             | 2            | semissis         | 1               |
|                   |              | svm              | 1               |
| av                | 2            | ave              | 1               |
|                   |              | avs              | 1               |
| singvla           | 2            | singvlvs         | 2               |
| propono           | 2            | propositvm       | 2               |
| fortiter          | 2            | fortis           | 2               |
| citrvm            | 2            | citrvs           | 1               |
|                   |              | citro            | 1               |
| ivssvm            | 2            | ivbeo            | 2               |
| vltimvm           | 2            | vltimvs          | 2               |
| adamas            | 2            | adamantvm        | 2               |
| alivs             | 2            | alias            | 1               |
|                   |              | alio             | 1               |
| insero            | 2            | insitvs          | 2               |
| fidelia           | 2            | fidelis          | 2               |
| alia              | 2            | alivs            | 2               |
| atarrhias         | 2            | atarrhia         | 2               |
| phrygia           | 2            | phrygivs         | 2               |
| inclinatvs        | 2            | inclino          | 2               |
| ivdex             | 2            | ivdicivm         | 2               |
| proceres          | 2            | procer           | 2               |
| depositvm         | 2            | depono           | 2               |
| baltevs           | 2            | baltevm          | 2               |
| acceptvm          | 2            | accipio          | 2               |
| finitimvs         | 2            | finitimi         | 2               |
| parvvm            | 2            | parvvs           | 2               |
| ecqvis            | 2            | ecqvid           | 2               |
| socivs            | 2            | socio            | 1               |
|                   |              | socia            | 1               |
| tectvs            | 2            | tectvm           | 2               |
| nessvs            | 2            | nessis           | 1               |
|                   |              | nesses           | 1               |
| soranvs           | 2            | soranes          | 1               |
|                   |              | soranvm          | 1               |
| ivbeo             | 2            | ivssvm           | 2               |
| propivs           | 2            | prope            | 2               |
| hirnea            | 2            | irnevs           | 2               |
| impendeo          | 2            | impendo          | 2               |
| potis             | 2            | potivs           | 2               |
| patior            | 2            | patitor          | 2               |
| antiopa           | 2            | antiope          | 2               |
| tertio            | 2            | tertivs          | 2               |
| possido           | 2            | possideo         | 2               |
| opera             | 2            | opvs             | 2               |
| rvbvs             | 2            | rvba             | 2               |
| triginta          | 2            | qvinqve          | 1               |
|                   |              | centvm           | 1               |
| solvtvs           | 2            | solvo            | 2               |
| romanvs           | 2            | romani           | 2               |
| fravdvlentvs      | 2            | fravdvlentvm     | 1               |
|                   |              | fravdvlens       | 1               |
| lollivs           | 2            | lollvs           | 2               |
| fvlcio            | 2            | fvlgeo           | 2               |
| latens            | 2            | lateo            | 2               |
| secretvs          | 2            | secretvm         | 2               |
| tvtvm             | 2            | tvtvs            | 2               |
| ridicvlaria       | 2            | ridicvlarivm     | 1               |
|                   |              | ridicvlarivs     | 1               |
| qvicvmqve         | 2            | qvocvmqve        | 2               |
| licet             | 2            | licetvs          | 2               |
| confvsvs          | 2            | confvndo         | 2               |
| nimivs            | 2            | nimivm           | 2               |
| aperio            | 2            | apertvs          | 2               |
| lavtvs            | 2            | lavo             | 2               |
| misellvs          | 2            | misella          | 1               |
|                   |              | misellvm         | 1               |
| propendeo         | 2            | propensvs        | 1               |
|                   |              | propendo         | 1               |
| rvspina           | 2            | rvspinvs         | 2               |
| eodem             | 2            | idem             | 2               |
| spira             | 2            | spiro            | 1               |
|                   |              | spirvs           | 1               |
| ab                | 2            | ah               | 2               |
| necopinans        | 2            | neqveopinans     | 1               |
|                   |              | neqveopino       | 1               |
| dirigo            | 2            | directo          | 1               |
|                   |              | directvs         | 1               |
| evhivs            | 2            | evhion           | 2               |
| pvls              | 2            | pvltvs           | 2               |
| afri              | 2            | afer             | 2               |
| vere              | 2            | ver              | 2               |
| ille              | 2            | illo             | 2               |
| absvm             | 2            | absens           | 1               |
|                   |              | avdeo            | 1               |
| innvpta           | 2            | innvptvs         | 2               |
| tela              | 2            | telvm            | 2               |
| devotvs           | 2            | devoveo          | 2               |
| memor             | 2            | memoro           | 2               |
| miser             | 2            | mitto            | 2               |
| cybele            | 2            | cybebe           | 2               |
| tantvsdem         | 2            | tantvmdem        | 2               |
| secvrvs           | 2            | secvris          | 2               |
| odi               | 2            | osvr             | 1               |
|                   |              | osa              | 1               |
| contineo          | 2            | continens        | 2               |
| dvodeviginti      | 2            | septendecim      | 1               |
|                   |              | dvodecim         | 1               |
| liceor            | 2            | liceo            | 2               |
| mala              | 2            | malvm            | 1               |
|                   |              | malvs            | 1               |
| svbivgivs         | 2            | svbivgivm        | 2               |
| serivs            | 2            | serivm           | 2               |
| pvblicvs          | 2            | pvblicvm         | 2               |
| lvdo              | 2            | lvdvs            | 2               |
| involvtvs         | 2            | involvo          | 2               |
| regivs            | 2            | regia            | 2               |
| bomilcar          | 2            | bomilcaris       | 1               |
|                   |              | bomilcarvs       | 1               |
| raptvs            | 2            | rapio            | 2               |
| iacio             | 2            | iaceo            | 2               |
| diverbivm         | 2            | deverbivm        | 2               |
| apertvs           | 2            | aperio           | 1               |
|                   |              | aperte           | 1               |
| constratvs        | 2            | consterno        | 2               |
| praesens          | 2            | praesentia       | 2               |
| tectvm            | 2            | tego             | 2               |
| noctvrnvs         | 2            | noctvrnae        | 1               |
|                   |              | noctvrna         | 1               |
| septem            | 2            | septimvs         | 1               |
|                   |              | septes           | 1               |
| video             | 2            | visvs            | 2               |
| romani            | 2            | romanvs          | 2               |
| latvs             | 2            | fero             | 2               |
| afraniani         | 2            | afranianvs       | 2               |
| primani           | 2            | primanvs         | 2               |
| tvi               | 2            | tvvs             | 2               |
| creditvm          | 2            | credo            | 2               |
| vnvm              | 2            | vnvs             | 2               |
| sextvs            | 2            | sex              | 2               |
| instrvctvs        | 2            | instrvo          | 2               |
| amplvs            | 2            | ample            | 2               |
| testv             | 2            | testvs           | 2               |
| tener             | 2            | teneo            | 1               |
|                   |              | tenerivs         | 1               |
| antefero          | 2            | antelo           | 2               |
| martiales         | 2            | martialis        | 2               |
| ars               | 2            | arte             | 2               |
| appenninvs        | 2            | apenninvs        | 2               |
| volvo             | 2            | volo             | 2               |
| tigranocerta      | 2            | tigranocerti     | 2               |
| qvartvs           | 2            | qvatvor          | 1               |
|                   |              | dvodecimvs       | 1               |
| capto             | 2            | capio            | 2               |
| exolesco          | 2            | exoleti          | 2               |
| spectatvs         | 2            | specto           | 2               |
| graecvs           | 2            | graeci           | 2               |
| svmmvm            | 2            | svpervs          | 2               |
| commvne           | 2            | commvnis         | 2               |
| comedo            | 2            | comsvm           | 1               |
|                   |              | comedivm         | 1               |
| finitimi          | 2            | finitimis        | 1               |
|                   |              | finitimvs        | 1               |
| torvvs            | 2            | torqveo          | 1               |
|                   |              | torva            | 1               |
| amica             | 2            | amicvs           | 2               |
| ivstvs            | 2            | ivste            | 1               |
|                   |              | ivsta            | 1               |
| vaccenses         | 2            | vagenses         | 2               |
| nimivm            | 2            | nimivs           | 2               |
| mille             | 2            | sexaginta        | 1               |
|                   |              | lvcivs           | 1               |
| latinvs           | 2            | latini           | 2               |
| cecropia          | 2            | cecropivs        | 2               |
| avdio             | 2            | avdiens          | 2               |
| bvbaces           | 2            | bvbace           | 2               |
| larinvm           | 2            | larini           | 2               |
| qvisqve           | 2            | qvoqve           | 2               |
| collybvs          | 1            | collys           | 1               |
| rvbens            | 1            | rvbeo            | 1               |
| alica             | 1            | alicvs           | 1               |
| crystallinvs      | 1            | crystallina      | 1               |
| avxiliaris        | 1            | avxiliares       | 1               |
| qvies             | 1            | qvietvs          | 1               |
| aphidnae          | 1            | aphidnas         | 1               |
| tres              | 1            | tribvs           | 1               |
| sorbitio          | 1            | sorbitivm        | 1               |
| cerva             | 1            | cervvs           | 1               |
| vicesimarivs      | 1            | vicensimarivs    | 1               |
| mantissa          | 1            | mantissvs        | 1               |
| contractvs        | 1            | contraho         | 1               |
| proficio          | 1            | proficiscor      | 1               |
| conditivvm        | 1            | conditivvs       | 1               |
| casvs             | 1            | casv             | 1               |
| pecco             | 1            | peccans          | 1               |
| revertor          | 1            | reverto          | 1               |
| exercito          | 1            | exercitatvs      | 1               |
| aventicvm         | 1            | aventicvs        | 1               |
| pedes             | 1            | impedi           | 1               |
| pannonii          | 1            | pannonivs        | 1               |
| percrebresco      | 1            | percrebo         | 1               |
| comitivm          | 1            | comitia          | 1               |
| praetvra          | 1            | praetvrvs        | 1               |
| covs              | 1            | coa              | 1               |
| vicenvs           | 1            | viginti          | 1               |
| singvlvs          | 1            | viginti          | 1               |
| cassivs           | 1            | cassii           | 1               |
| arripio           | 1            | abripio          | 1               |
| iecvr             | 1            | iecvs            | 1               |
| proprivm          | 1            | proprivs         | 1               |
| albani            | 1            | albanis          | 1               |
| falisci           | 1            | faliscvs         | 1               |
| aricini           | 1            | aricinvs         | 1               |
| lavrentes         | 1            | lavrens          | 1               |
| tvber             | 1            | tvbera           | 1               |
| aetnenses         | 1            | aetnensis        | 1               |
| herbitenses       | 1            | herbitensis      | 1               |
| desertor          | 1            | desertvm         | 1               |
| accipio           | 1            | acceptvs         | 1               |
| semodivs          | 1            | semodivm         | 1               |
| scobis            | 1            | scoba            | 1               |
| resto             | 1            | resisto          | 1               |
| adivvo            | 1            | adivvvs          | 1               |
| flagrans          | 1            | flagro           | 1               |
| appvleivs         | 1            | appvlevs         | 1               |
| vaccensis         | 1            | vagenses         | 1               |
| decimani          | 1            | decimanvs        | 1               |
| vir               | 1            | vis              | 1               |
| calco             | 1            | calcvs           | 1               |
| cirrati           | 1            | cirrator         | 1               |
| dicto             | 1            | dictatvm         | 1               |
| volens            | 1            | volo             | 1               |
| illico            | 1            | svm              | 1               |
| qvisnam           | 1            | qvis             | 1               |
| depaciscor        | 1            | depectvs         | 1               |
| interminor        | 1            | intermino        | 1               |
| phrenesis         | 1            | phrenesvs        | 1               |
| appositvs         | 1            | appono           | 1               |
| laxvs             | 1            | laxo             | 1               |
| properans         | 1            | propero          | 1               |
| concesso          | 1            | concedo          | 1               |
| rogvs             | 1            | rogo             | 1               |
| confinivm         | 1            | confinis         | 1               |
| volcae            | 1            | volca            | 1               |
| nemo              | 1            | ne               | 1               |
| pingve            | 1            | pingvis          | 1               |
| bvllio            | 1            | bvllo            | 1               |
| cordvbenses       | 1            | cordvbensis      | 1               |
| cyllene           | 1            | cyllenes         | 1               |
| lvcar             | 1            | lvcor            | 1               |
| favtor            | 1            | favtvs           | 1               |
| peracvtvs         | 1            | peracvtvm        | 1               |
| coniectvra        | 1            | conicio          | 1               |
| cratera           | 1            | creterra         | 1               |
| svdo              | 1            | svdis            | 1               |
| svbrvbeo          | 1            | svbrvbo          | 1               |
| periclitor        | 1            | periclito        | 1               |
| deiectvs          | 1            | deicio           | 1               |
| lentvs            | 1            | lente            | 1               |
| illivsmodi        | 1            | illimodvs        | 1               |
| torqvatvs         | 1            | torqveo          | 1               |
| colvbra           | 1            | colvber          | 1               |
| exsto             | 1            | exsisto          | 1               |
| praetero          | 1            | praetereo        | 1               |
| abditvs           | 1            | abdo             | 1               |
| lvdifico          | 1            | lvdificor        | 1               |
| atriensis         | 1            | atriensio        | 1               |
| bimembris         | 1            | bimember         | 1               |
| tycha             | 1            | tychas           | 1               |
| ascvrvm           | 1            | ascvrvs          | 1               |
| lampsacenvs       | 1            | lampsaceni       | 1               |
| sedatvs           | 1            | sedo             | 1               |
| pervenio          | 1            | prevenio         | 1               |
| cvrro             | 1            | cvrsvr           | 1               |
| dimachae          | 1            | dimacha          | 1               |
| mattea            | 1            | matea            | 1               |
| conchylivm        | 1            | conchylvs        | 1               |
| casvla            | 1            | casvlvs          | 1               |
| valva             | 1            | valvae           | 1               |
| falernvs          | 1            | falernvm         | 1               |
| hvmidvm           | 1            | hvmidvs          | 1               |
| impeditvm         | 1            | impeditvs        | 1               |
| iaceo             | 1            | iacio            | 1               |
| imaginor          | 1            | imaginatvs       | 1               |
| resido            | 1            | resideo          | 1               |
| infra             | 1            | infere           | 1               |
| devia             | 1            | devivs           | 1               |
| commvnis          | 1            | commvne          | 1               |
| institvtvm        | 1            | institvo         | 1               |
| oestrvs           | 1            | oester           | 1               |
| exterritvs        | 1            | exterreo         | 1               |
| bellicvm          | 1            | bellicvs         | 1               |
| scelerati         | 1            | sceleratvs       | 1               |
| depso             | 1            | depsvesco        | 1               |
| circvmtergeo      | 1            | circvmtergo      | 1               |
| faber             | 1            | fabeo            | 1               |
| taenaris          | 1            | taenarvs         | 1               |
| calathvs          | 1            | calathvm         | 1               |
| deterivs          | 1            | deterior         | 1               |
| iratvs            | 1            | irator           | 1               |
| devoveo           | 1            | devotvs          | 1               |
| distentvs         | 1            | distendo         | 1               |
| impeditvs         | 1            | impedio          | 1               |
| sabbatvm          | 1            | sabbatvs         | 1               |
| milivm            | 1            | mille            | 1               |
| ecce              | 1            | is               | 1               |
| syracvsani        | 1            | syracvsanvs      | 1               |
| oebalis           | 1            | oebalvs          | 1               |
| oblino            | 1            | obliviscor       | 1               |
| elegeia           | 1            | elegeivs         | 1               |
| consentiens       | 1            | consentio        | 1               |
| mastanabal        | 1            | mastanabalis     | 1               |
| convvlnero        | 1            | convvlno         | 1               |
| praefectvs        | 1            | praeficio        | 1               |
| repetvndae        | 1            | repeto           | 1               |
| recvperator       | 1            | reciperator      | 1               |
| herbitensis       | 1            | herbitenses      | 1               |
| aggravo           | 1            | aggravvs         | 1               |
| fractvs           | 1            | frango           | 1               |
| demissvs          | 1            | demitto          | 1               |
| mediolanensis     | 1            | mediolanensimvs  | 1               |
| ferveo            | 1            | fervens          | 1               |
| inflatvs          | 1            | inflo            | 1               |
| textrinvm         | 1            | textrinvs        | 1               |
| gerens            | 1            | gero             | 1               |
| libidinosvs       | 1            | libidinose       | 1               |
| pergrandis        | 1            | pergrans         | 1               |
| manifestvs        | 1            | manifeste        | 1               |
| pridie            | 1            | pridvs           | 1               |
| ianvarivs         | 1            | ianvs            | 1               |
| operor            | 1            | opero            | 1               |
| ferrvm            | 1            | fero             | 1               |
| compendivm        | 1            | compendo         | 1               |
| semifactvs        | 1            | semifacio        | 1               |
| diffvsvs          | 1            | diffvndo         | 1               |
| decem             | 1            | decimvs          | 1               |
| advoco            | 1            | advocatvs        | 1               |
| fvndvs            | 1            | fvnda            | 1               |
| insipiens         | 1            | insipio          | 1               |
| artemon           | 1            | artemonivs       | 1               |
| qvapropter        | 1            | qvis             | 1               |
| ansa              | 1            | ansvm            | 1               |
| drangae           | 1            | drangas          | 1               |
| oenone            | 1            | oenon            | 1               |
| pleiades          | 1            | pleidae          | 1               |
| sidonii           | 1            | sidonivs         | 1               |
| lvdicer           | 1            | lvdicrvm         | 1               |
| animosvs          | 1            | animose          | 1               |
| notabiliter       | 1            | notabilis        | 1               |
| longvm            | 1            | longvs           | 1               |
| consto            | 1            | consisto         | 1               |
| eximivs           | 1            | eximievs         | 1               |
| addico            | 1            | addictvm         | 1               |
| conatvs           | 1            | conor            | 1               |
| assvm             | 1            | assitvs          | 1               |
| prehenso          | 1            | prehendo         | 1               |
| conflictor        | 1            | conflicto        | 1               |
| qvartana          | 1            | qvartanvm        | 1               |
| excito            | 1            | excio            | 1               |
| inavdio           | 1            | inavditvs        | 1               |
| babylonivs        | 1            | babylonivm       | 1               |
| hemina            | 1            | heminvs          | 1               |
| antenna           | 1            | antennvs         | 1               |
| gellivs           | 1            | gellia           | 1               |
| nonae             | 1            | nonvs            | 1               |
| cimmerii          | 1            | cimmerion        | 1               |
| candeo            | 1            | candens          | 1               |
| tergeminvs        | 1            | trigemen         | 1               |
| astvpeo           | 1            | asto             | 1               |
| hannibal          | 1            | hannibes         | 1               |
| praepilatvs       | 1            | praepilo         | 1               |
| sanvs             | 1            | sane             | 1               |
| cvrricvlvm        | 1            | cvrricvlvs       | 1               |
| horresco          | 1            | horreo           | 1               |
| excatarisso       | 1            | excato           | 1               |
| certamen          | 1            | certo            | 1               |
| egeo              | 1            | egens            | 1               |
| insomnis          | 1            | insommis         | 1               |
| flvctvo           | 1            | flvctvor         | 1               |
| qvonam            | 1            | qvisnam          | 1               |
| odivm             | 1            | odi              | 1               |
| contemptvs        | 1            | contemno         | 1               |
| stragvla          | 1            | stragvlvm        | 1               |
| anartes           | 1            | anartivs         | 1               |
| incensvs          | 1            | incendo          | 1               |
| tardvs            | 1            | tardo            | 1               |
| avis              | 1            | avvs             | 1               |
| hortatvs          | 1            | hortor           | 1               |
| sollicito         | 1            | sollicitor       | 1               |
| confido           | 1            | confidvs         | 1               |
| dextera           | 1            | dexter           | 1               |
| maleficvs         | 1            | maleficivm       | 1               |
| florens           | 1            | floreo           | 1               |
| excio             | 1            | excito           | 1               |
| ossicvlvm         | 1            | ossvcvlvm        | 1               |
| vestio            | 1            | vestitvs         | 1               |
| ardeo             | 1            | ardens           | 1               |
| offensa           | 1            | offendo          | 1               |
| tero              | 1            | ter              | 1               |
| aversvs           | 1            | averto           | 1               |
| fvtvri            | 1            | fvtvrvs          | 1               |
| exsvpero          | 1            | exvpero          | 1               |
| effectvs          | 1            | efficio          | 1               |
| bellicvs          | 1            | bellice          | 1               |
| cassis            | 1            | cassidvs         | 1               |
| phreneticvs       | 1            | freneticvs       | 1               |
| validvs           | 1            | valide           | 1               |
| exardesco         | 1            | exardeo          | 1               |
| altvs             | 1            | altvm            | 1               |
| ledaevs           | 1            | ledaea           | 1               |
| calypso           | 1            | calypsvs         | 1               |
| damnatvs          | 1            | damno            | 1               |
| galli             | 1            | gallvs           | 1               |
| petreivs          | 1            | petreii          | 1               |
| scvtatvs          | 1            | scvtor           | 1               |
| plenvs            | 1            | plena            | 1               |
| pyrethrvm         | 1            | pyrethra         | 1               |
| elegia            | 1            | elegeia          | 1               |
| scvlponeae        | 1            | scvlponia        | 1               |
| tanto             | 1            | tantvs           | 1               |
| nvmeratvs         | 1            | nvmero           | 1               |
| clvviae           | 1            | clvvii           | 1               |
| illvstris         | 1            | illvstre         | 1               |
| theraei           | 1            | theraeon         | 1               |
| philaeni          | 1            | philaenon        | 1               |
| pantomimvs        | 1            | pantomima        | 1               |
| blandior          | 1            | blandvs          | 1               |
| pleraqve          | 1            | plervsqve        | 1               |
| intentvs          | 1            | intendo          | 1               |
| viridis           | 1            | viride           | 1               |
| immisit           | 1            | immitto          | 1               |
| habito            | 1            | habeo            | 1               |
| nox               | 1            | nocte            | 1               |
| volvcer           | 1            | volvcris         | 1               |
| pvgno             | 1            | pvgna            | 1               |
| verto             | 1            | versvs           | 1               |
| enervis           | 1            | enervo           | 1               |
| aricia            | 1            | aricivs          | 1               |
| vnvsetvicesimvs   | 1            | vnvseicesimvs    | 1               |
| nonaginta         | 1            | octoginta        | 1               |
| profligatvs       | 1            | profligate       | 1               |
| flexvs            | 1            | flecto           | 1               |
| hyacinthinvs      | 1            | hyacinthina      | 1               |
| hypsipyle         | 1            | hypsipylas       | 1               |
| novale            | 1            | novalia          | 1               |
| optatvs           | 1            | opto             | 1               |
| remissvs          | 1            | remisse          | 1               |
| peccatvm          | 1            | peccator         | 1               |
| nitens            | 1            | niteo            | 1               |
| calvia            | 1            | calvivs          | 1               |
| piraeevs          | 1            | piraevs          | 1               |
| argvo             | 1            | argvto           | 1               |
| venenvm           | 1            | venenvs          | 1               |
| gnosias           | 1            | gnosivs          | 1               |
| valeria           | 1            | valerivs         | 1               |
| intestato         | 1            | intestatvs       | 1               |
| perillvs          | 1            | perillivs        | 1               |
| bison             | 1            | bisons           | 1               |
| thesides          | 1            | thesis           | 1               |
| satvro            | 1            | satvratvs        | 1               |
| piper             | 1            | piperi           | 1               |
| moletrina         | 1            | moletrinvs       | 1               |
| censvs            | 1            | censeo           | 1               |
| qvamqvam          | 1            | qvanqvam         | 1               |
| canto             | 1            | canta            | 1               |
| salto             | 1            | saltvs           | 1               |
| modivm            | 1            | modivs           | 1               |
| nvmida            | 1            | nvmidae          | 1               |
| eleleides         | 1            | eleleis          | 1               |
| semidea           | 1            | semidevs         | 1               |
| impvlsvs          | 1            | impello          | 1               |
| repvlsa           | 1            | repello          | 1               |
| fatvm             | 1            | for              | 1               |
| avgeo             | 1            | avgens           | 1               |
| distinctvs        | 1            | distingvo        | 1               |
| bvxvs             | 1            | bvxvm            | 1               |
| praepotentes      | 1            | praepotens       | 1               |
| offensvs          | 1            | offendo          | 1               |
| coma              | 1            | comis            | 1               |
| hadrvmetvm        | 1            | hadrvmetvs       | 1               |
| sabinvs           | 1            | sabini           | 1               |
| volcacivs         | 1            | vvlcativs        | 1               |
| pappo             | 1            | pappar           | 1               |
| bactriana         | 1            | bactrianvs       | 1               |
| lixa              | 1            | lixvs            | 1               |
| consvltor         | 1            | consvltvm        | 1               |
| emax              | 1            | emacvs           | 1               |
| sedvco            | 1            | sedvctvs         | 1               |
| dvbivs            | 1            | dvbivm           | 1               |
| debitvm           | 1            | debeo            | 1               |
| disserto          | 1            | dissero          | 1               |
| sermocinor        | 1            | sermocino        | 1               |
| qve               | 1            | svm              | 1               |
| nysigena          | 1            | nysigenes        | 1               |
| silenvs           | 1            | silenae          | 1               |
| lymphatvs         | 1            | lymphor          | 1               |
| argi              | 1            | argivs           | 1               |
| ityraevs          | 1            | ityraei          | 1               |
| syrvs             | 1            | syri             | 1               |
| lavdo             | 1            | lavdvs           | 1               |
| obligatvs         | 1            | obligo           | 1               |
| longe             | 1            | longvs           | 1               |
| obsoletvs         | 1            | obsoleo          | 1               |
| excvsatvs         | 1            | excvso           | 1               |
| detego            | 1            | detectvs         | 1               |
| falcatvs          | 1            | falco            | 1               |
| pone              | 1            | pono             | 1               |
| consvlto          | 1            | consvltvm        | 1               |
| mapalia           | 1            | mapalis          | 1               |
| panes             | 1            | pan              | 1               |
| eqvester          | 1            | eqvestria        | 1               |
| amarvs            | 1            | amo              | 1               |
| damno             | 1            | damnor           | 1               |
| essentia          | 1            | essentio         | 1               |
| alcathovs         | 1            | alcathoi         | 1               |
| ervditvs          | 1            | ervdio           | 1               |
| svbvrbanvs        | 1            | svbvrbanvm       | 1               |
| silianvs          | 1            | siliana          | 1               |
| qvoqve            | 1            | qvisqve          | 1               |
| dextrorsvs        | 1            | dextrordeo       | 1               |
| disicio           | 1            | dissicio         | 1               |
| epicvrei          | 1            | epicvrevs        | 1               |
| clodivs           | 1            | clodia           | 1               |
| qvalibet          | 1            | qvilibet         | 1               |
| navfragvs         | 1            | navfrago         | 1               |
| eblandior         | 1            | eblandio         | 1               |
| envcleo           | 1            | envcleatvs       | 1               |
| reverentia        | 1            | reverens         | 1               |
| germanvs          | 1            | germani          | 1               |
| hippotoxotae      | 1            | hippotoxota      | 1               |
| pediseqvvs        | 1            | pediseqvi        | 1               |
| consecratvs       | 1            | consecro         | 1               |
| esqviliae         | 1            | esqvilivs        | 1               |
| leonida           | 1            | leonidas         | 1               |
| galatae           | 1            | galati           | 1               |
| qvoqvo            | 1            | qvisqvis         | 1               |
| comis             | 1            | comes            | 1               |
| cremo             | 1            | cremer           | 1               |
| phthivs           | 1            | phthis           | 1               |
| orno              | 1            | ornatvs          | 1               |
| phrygivs          | 1            | phrygia          | 1               |
| illargio          | 1            | illargior        | 1               |
| specvm            | 1            | speca            | 1               |
| lyrnesis          | 1            | lyrnesides       | 1               |
| increbresco       | 1            | increbesco       | 1               |
| brvma             | 1            | brvmvs           | 1               |
| restis            | 1            | resto            | 1               |
| prohibeo          | 1            | prohibitas       | 1               |
| satago            | 1            | satagens         | 1               |
| dolabra           | 1            | dolabris         | 1               |
| insane            | 1            | insanvs          | 1               |
| desino            | 1            | desvm            | 1               |
| obirascor         | 1            | obiratvs         | 1               |
| posteaqvam        | 1            | qvi              | 1               |
| pacatvs           | 1            | paco             | 1               |
| dvcenti           | 1            | qvadraginta      | 1               |
| octoginta         | 1            | qvadraginta      | 1               |
| ocinvm            | 1            | ocinvs           | 1               |
| ventvs            | 1            | venio            | 1               |
| troivgena         | 1            | troivgenvs       | 1               |
| hernici           | 1            | hernicvs         | 1               |
| tiresias          | 1            | teresia          | 1               |
| avtvmo            | 1            | avtvmvs          | 1               |
| larentia          | 1            | larentivs        | 1               |
| percomperio       | 1            | perconpertvs     | 1               |
| belgica           | 1            | belgicvs         | 1               |
| semiermvs         | 1            | semiemmi         | 1               |
| non               | 1            | nenvm            | 1               |
| erectvs           | 1            | erecte           | 1               |
| insiticivs        | 1            | insiticivm       | 1               |
| relvceo           | 1            | relvcens         | 1               |
| tvrbo             | 1            | tvrbatvs         | 1               |
| tomyris           | 1            | tamyris          | 1               |
| praetorivs        | 1            | praetorivm       | 1               |
| vigil             | 1            | vigilvs          | 1               |
| corbis            | 1            | corbo            | 1               |
| dentale           | 1            | dentalia         | 1               |
| honor             | 1            | honorvs          | 1               |
| picea             | 1            | picevs           | 1               |
| dardania          | 1            | dardanivs        | 1               |
| allivm            | 1            | alivs            | 1               |
| rvta              | 1            | rvo              | 1               |
| pyrenaevs         | 1            | pyrenaei         | 1               |
| genv              | 1            | genvvs           | 1               |
| nongenti          | 1            | octingenti       | 1               |
| qvantvm           | 1            | qvantvs          | 1               |
| verrivs           | 1            | verria           | 1               |
| inchoo            | 1            | incoho           | 1               |
| montani           | 1            | montanvs         | 1               |
| acerbe            | 1            | acerbvs          | 1               |
| getae             | 1            | geta             | 1               |
| sparsvs           | 1            | spargo           | 1               |
| contrarivm        | 1            | contrarivs       | 1               |
| eivro             | 1            | eivo             | 1               |
| directvm          | 1            | directvs         | 1               |
| insalvbris        | 1            | insalvberimvs    | 1               |
| avxiliarii        | 1            | avxiliarivs      | 1               |
| rheno             | 1            | reno             | 1               |
| oleitas           | 1            | oleitvs          | 1               |
| medipontvs        | 1            | melipvm          | 1               |
| qvalvm            | 1            | qvalis           | 1               |
| acta              | 1            | actvm            | 1               |
| polyhymnia        | 1            | polyhymnivs      | 1               |
| clio              | 1            | clion            | 1               |
| scitvs            | 1            | scitvm           | 1               |
| res               | 1            | rede             | 1               |
| exanimis          | 1            | exanimvs         | 1               |
| facile            | 1            | facilis          | 1               |
| sere              | 1            | sero             | 1               |
| incolvmis         | 1            | incolvmia        | 1               |
| pretivm           | 1            | pretivs          | 1               |
| decretvm          | 1            | decerno          | 1               |
| perfvngor         | 1            | perfvnctvs       | 1               |
| svmme             | 1            | svpere           | 1               |
| fabaginvs         | 1            | fabago           | 1               |
| nonarivs          | 1            | nonarivm         | 1               |
| ambigvvs          | 1            | ambigvvm         | 1               |
| labyrinthevs      | 1            | labyrinthia      | 1               |
| conceptvs         | 1            | concipio         | 1               |
| cvnicvlvs         | 1            | cvnicvlvm        | 1               |
| male              | 1            | malvs            | 1               |
| phinevs           | 1            | phineis          | 1               |
| meto              | 1            | meta             | 1               |
| delector          | 1            | delecto          | 1               |
| inclvdo           | 1            | inclvsvs         | 1               |
| observo           | 1            | observvs         | 1               |
| profvndo          | 1            | profvndvs        | 1               |
| perenne           | 1            | perennis         | 1               |
| attegia           | 1            | attegio          | 1               |
| vlteriora         | 1            | vlterior         | 1               |
| stratvm           | 1            | sterno           | 1               |
| apertvm           | 1            | apertvs          | 1               |
| vaga              | 1            | vacca            | 1               |
| zeta              | 1            | zetae            | 1               |
| gigeria           | 1            | gizeria          | 1               |
| avtopyros         | 1            | avtopyrvs        | 1               |
| agrippinenses     | 1            | agrippinensis    | 1               |
| mane              | 1            | maneo            | 1               |
| edictvm           | 1            | edico            | 1               |
| moratvs           | 1            | moror            | 1               |
| interdiv          | 1            | interdivs        | 1               |
| laridvm           | 1            | lardvs           | 1               |
| maerens           | 1            | maereo           | 1               |
| transversvm       | 1            | transversvs      | 1               |
| sangvis           | 1            | sangvino         | 1               |
| cornevs           | 1            | cornivs          | 1               |
| svlpicia          | 1            | svlpicivs        | 1               |
| silvicola         | 1            | silvicolvm       | 1               |
| modice            | 1            | modix            | 1               |
| vtrinde           | 1            | vtrindo          | 1               |
| rectvm            | 1            | recta            | 1               |
| zminthevs         | 1            | sminthevs        | 1               |
| levis             | 1            | leviter          | 1               |
| reqviesco         | 1            | reqvietvs        | 1               |
| expositvs         | 1            | expono           | 1               |
| svblevo           | 1            | svblevatvs       | 1               |
| thysdra           | 1            | thysdrae         | 1               |
| venia             | 1            | venio            | 1               |
| conqvisitvs       | 1            | conqviro         | 1               |
| mvlciber          | 1            | mvlciberi        | 1               |
| circvmspectatrix  | 1            | circvmspectatvs  | 1               |
| hederacevs        | 1            | hederacivs       | 1               |
| trifolivm         | 1            | trifolis         | 1               |
| primores          | 1            | primoris         | 1               |
| helleborvs        | 1            | helleborvm       | 1               |
| aletrinas         | 1            | aletrinatvs      | 1               |
| senio             | 1            | senivm           | 1               |
| bvxvm             | 1            | bvxvs            | 1               |
| porrectvs         | 1            | porrigo          | 1               |
| nvpta             | 1            | nvbo             | 1               |
| lana              | 1            | lano             | 1               |
| retrices          | 1            | retrix           | 1               |
| vermis            | 1            | vermivs          | 1               |
| thrax             | 1            | thracae          | 1               |
| lvbricvs          | 1            | lvbricvm         | 1               |
| ilia              | 1            | ilivs            | 1               |
| pvgna             | 1            | pvgnvs           | 1               |
| accessvs          | 1            | accedo           | 1               |
| dardanis          | 1            | dardanvs         | 1               |
| promitto          | 1            | promissvm        | 1               |
| antepono          | 1            | ponitvror        | 1               |
| prasinvs          | 1            | prasina          | 1               |
| complexvs         | 1            | complector       | 1               |
| deterior          | 1            | deterio          | 1               |
| tetricvs          | 1            | tetrica          | 1               |
| immvto            | 1            | immvtio          | 1               |
| oenevs            | 1            | oeneas           | 1               |
| nixvs             | 1            | nisvs            | 1               |
| affligo           | 1            | afflictvs        | 1               |
| oscito            | 1            | oscitans         | 1               |
| mensis            | 1            | mensa            | 1               |
| verbena           | 1            | verbenvs         | 1               |
| no                | 1            | nassis           | 1               |
| colchi            | 1            | colchis          | 1               |
| saepia            | 1            | sepia            | 1               |
| gvtta             | 1            | gvtto            | 1               |
| trinodis          | 1            | trinvs           | 1               |
| bactriani         | 1            | bactrianvs       | 1               |
| tvnica            | 1            | tvnicvs          | 1               |
| dolenter          | 1            | dolens           | 1               |
| honoratvs         | 1            | honoro           | 1               |
| pocvlvm           | 1            | pocvlvs          | 1               |
| densvs            | 1            | denseo           | 1               |
| saga              | 1            | sagvm            | 1               |
| molorchaevs       | 1            | molorchevs       | 1               |
| caelestes         | 1            | caelestis        | 1               |
| inavratvs         | 1            | inavro           | 1               |
| evrope            | 1            | evropa           | 1               |
| pellaevs          | 1            | pellevs          | 1               |
| lectito           | 1            | lectitas         | 1               |
| svfficio          | 1            | svfficiens       | 1               |
| advatvca          | 1            | advatvcvs        | 1               |
| lydivs            | 1            | lydia            | 1               |
| incito            | 1            | incitvs          | 1               |
| seqvens           | 1            | seqvor           | 1               |
| caelestia         | 1            | caelestis        | 1               |
| ivdico            | 1            | ivdicatvm        | 1               |
| maena             | 1            | mena             | 1               |
| mvries            | 1            | mvriens          | 1               |
| velociter         | 1            | velox            | 1               |
| tvrda             | 1            | tvrdvs           | 1               |
| pelion            | 1            | pelevs           | 1               |
| plecto            | 1            | plexvs           | 1               |
| hispo             | 1            | hispones         | 1               |
| neptvnine         | 1            | neptvninvs       | 1               |
| sexagenvs         | 1            | sexagena         | 1               |
| assvs             | 1            | assa             | 1               |
| dormitorivs       | 1            | dormitorivm      | 1               |
| aeaevs            | 1            | aeaea            | 1               |
| armenii           | 1            | armenivs         | 1               |
| svbicio           | 1            | svbiectvs        | 1               |
| hostile           | 1            | hostilis         | 1               |
| lotos             | 1            | lavo             | 1               |
| conventvs         | 1            | convenio         | 1               |
| immorior          | 1            | immor            | 1               |
| levcadivs         | 1            | levcadia         | 1               |
| troivs            | 1            | troia            | 1               |
| secvris           | 1            | secvrvs          | 1               |
| savillvm          | 1            | svavllvm         | 1               |
| avdacvlvs         | 1            | avdacvlvm        | 1               |
| ariadna           | 1            | ariadnae         | 1               |
| pvlto             | 1            | pvltvs           | 1               |
| tango             | 1            | tangvm           | 1               |
| credo             | 1            | credor           | 1               |
| abeo              | 1            | abista           | 1               |
| captivvs          | 1            | captiva          | 1               |
| mehercvle         | 1            | mercvles         | 1               |
| lateo             | 1            | latvs            | 1               |
| recvrvo           | 1            | recvrvvs         | 1               |
| sceleratvs        | 1            | scelerate        | 1               |
| rigeo             | 1            | rigo             | 1               |
| ivlvs             | 1            | ivle             | 1               |
| helene            | 1            | helena           | 1               |
| tetre             | 1            | teter            | 1               |
| segni             | 1            | segnivm          | 1               |
| pedivs            | 1            | pedion           | 1               |
| ineo              | 1            | inite            | 1               |
| balineae          | 1            | balinevm         | 1               |
| navigiolvm        | 1            | navigiolvs       | 1               |
| refvgio           | 1            | refvgivm         | 1               |
| orsilos           | 1            | orsili           | 1               |
| svbsto            | 1            | svbsisto         | 1               |
| cvria             | 1            | cvrivs           | 1               |
| amaryllis         | 1            | amarylla         | 1               |
| castanea          | 1            | castanevs        | 1               |
| corollarivm       | 1            | corollarivs      | 1               |
| explodo           | 1            | exploso          | 1               |
| ernevm            | 1            | ernevs           | 1               |
| aletrinates       | 1            | aletrinas        | 1               |
| mithrenes         | 1            | mithrenae        | 1               |
| nysaevs           | 1            | nysaea           | 1               |
| penthevs          | 1            | pentheivs        | 1               |
| ratis             | 1            | reor             | 1               |
| immemor           | 1            | immemorvs        | 1               |
| paean             | 1            | paeanvs          | 1               |
| aracinthvs        | 1            | aracynthvs       | 1               |
| qvadrigenti       | 1            | qvadringenti     | 1               |
| svperpendens      | 1            | pendeo           | 1               |
| lactes            | 1            | lac              | 1               |
| hastatvs          | 1            | hasto            | 1               |
| ervdio            | 1            | ervditvs         | 1               |
| rescio            | 1            | rescisco         | 1               |
| navvs             | 1            | navis            | 1               |
| catapvlta         | 1            | catapvltvs       | 1               |
| dedoleo           | 1            | dedolesco        | 1               |
| avctvs            | 1            | avgeo            | 1               |
| clavis            | 1            | clavvs           | 1               |
| galbinvs          | 1            | galbinvm         | 1               |
| cerasinvs         | 1            | cerasinvm        | 1               |
| svccvrro          | 1            | svccvrrvm        | 1               |
| deservio          | 1            | desero           | 1               |
| secvndvm          | 1            | secvndvs         | 1               |
| brevi             | 1            | brevis           | 1               |
| septentrio        | 1            | septemtrio       | 1               |
| caedo             | 1            | cado             | 1               |
| aggero            | 1            | agger            | 1               |
| parco             | 1            | parsvs           | 1               |
| interverto        | 1            | intervertvs      | 1               |
| fortvita          | 1            | fortvitvs        | 1               |
| characterismvs    | 1            | characteris      | 1               |
| splen             | 1            | splenvs          | 1               |
| cachinno          | 1            | cachinnvs        | 1               |
| assisto           | 1            | asto             | 1               |
| clamo             | 1            | clama            | 1               |
| costa             | 1            | costvs           | 1               |
| cydonivm          | 1            | cydonivs         | 1               |
| canistra          | 1            | canistrvm        | 1               |
| ecqvi             | 1            | ecqvis           | 1               |
| derigo            | 1            | directvs         | 1               |
| illac             | 1            | illic            | 1               |
| centvria          | 1            | centvrivs        | 1               |
| possideo          | 1            | possido          | 1               |
| parce             | 1            | parco            | 1               |
| concha            | 1            | conca            | 1               |
| loqvitor          | 1            | loqvito          | 1               |
| gaesvm            | 1            | gaedeo           | 1               |
| tvvm              | 1            | tvvs             | 1               |
| parsagada         | 1            | parsagades       | 1               |
| secvndani         | 1            | secvndanvs       | 1               |
| exsvltatio        | 1            | exsvltio         | 1               |
| rvbrivs           | 1            | rvber            | 1               |
| cerarivm          | 1            | cerarivs         | 1               |
| extrema           | 1            | extremvm         | 1               |
| mirvs             | 1            | mirvm            | 1               |
| secvs             | 1            | seqvivs          | 1               |
| pericvlose        | 1            | pericvlosvs      | 1               |
| vlciscor          | 1            | vlcis            | 1               |
| ingressvs         | 1            | ingredior        | 1               |
| ariarathes        | 1            | ariarathinvs     | 1               |
| considero         | 1            | consido          | 1               |
| scio              | 1            | sciens           | 1               |
| corona            | 1            | coron            | 1               |
| prorsvs           | 1            | prosvs           | 1               |
| nata              | 1            | natvs            | 1               |
| xenophon          | 1            | xenophontes      | 1               |
| proventvs         | 1            | provenio         | 1               |
| pistillvm         | 1            | pistillvs        | 1               |
| ivnia             | 1            | ivnivs           | 1               |
| manipvlaris       | 1            | maniplarvs       | 1               |
| circe             | 1            | circvs           | 1               |
| vester            | 1            | vos              | 1               |
| expedite          | 1            | expeditvs        | 1               |
| cogito            | 1            | cogitatvs        | 1               |
| pericles          | 1            | periclvs         | 1               |
| svillvs           | 1            | svilla           | 1               |
| expers            | 1            | experior         | 1               |
| patro             | 1            | patratvs         | 1               |
| brinno            | 1            | brinnvs          | 1               |
| gaianvs           | 1            | gaiani           | 1               |
| lampsaceni        | 1            | lampsacenvs      | 1               |
| avstervs          | 1            | avstervm         | 1               |
| svpervm           | 1            | svpervs          | 1               |
| vitrevs           | 1            | vitrevm          | 1               |
| intercolvmnivm    | 1            | intercolvm       | 1               |
| divvm             | 1            | divvs            | 1               |
| pando             | 1            | pandeo           | 1               |
| attono            | 1            | attonitvs        | 1               |
| niceros           | 1            | nicero           | 1               |
| amans             | 1            | amo              | 1               |
| ortvs             | 1            | orior            | 1               |
| mephitis          | 1            | mefitor          | 1               |
| togati            | 1            | togatvs          | 1               |
| eadem             | 1            | idem             | 1               |
| regie             | 1            | regies           | 1               |
| compromissvm      | 1            | compromitto      | 1               |
| canis             | 1            | cano             | 1               |
| agnascor          | 1            | agnatvs          | 1               |
| conicio           | 1            | cono             | 1               |
| caninvs           | 1            | canina           | 1               |
| proiectvs         | 1            | proicio          | 1               |
| pervolo           | 1            | pervellis        | 1               |
| cedrvs            | 1            | cedro            | 1               |
| ceno              | 1            | coenvo           | 1               |
| planvm            | 1            | planvs           | 1               |
| sera              | 1            | servs            | 1               |
| ervditi           | 1            | ervditor         | 1               |
| sallves           | 1            | sallyae          | 1               |
| salvto            | 1            | salvtvs          | 1               |
| ambitiose         | 1            | ambitiosvs       | 1               |
| gorge             | 1            | gorgvs           | 1               |
| ivratvs           | 1            | ivro             | 1               |
| caveo             | 1            | cavtvs           | 1               |
| lepor             | 1            | lepvs            | 1               |
| hac               | 1            | hic              | 1               |
| tifernivm         | 1            | tifernivs        | 1               |
| pascvvm           | 1            | pascvvs          | 1               |
| nvmervs           | 1            | nvmero           | 1               |
| ardvvm            | 1            | ardvvs           | 1               |
| calvvs            | 1            | calve            | 1               |
| tyndaris          | 1            | tyndarvs         | 1               |
| si                | 1            | svm              | 1               |
| avdeo             | 1            | odi              | 1               |
| spartani          | 1            | spartanvs        | 1               |
| ligo              | 1            | liga             | 1               |
| privo             | 1            | privatvs         | 1               |
| rosevs            | 1            | rodea            | 1               |
| impietas          | 1            | impietvs         | 1               |
| gnosivs           | 1            | gnosia           | 1               |
| fvtvrvm           | 1            | fvtvrvs          | 1               |
| pellis            | 1            | pello            | 1               |
| inficio           | 1            | infectvs         | 1               |
| comatvs           | 1            | comatvm          | 1               |
| vtile             | 1            | vtilis           | 1               |
| tapsitani         | 1            | thapsitani       | 1               |
| emvnio            | 1            | emvnitvs         | 1               |
| sphaerita         | 1            | spaeritvs        | 1               |
| sphaera           | 1            | spaera           | 1               |
| simvs             | 1            | sima             | 1               |
| salebra           | 1            | saleber          | 1               |
| raster            | 1            | rastrvm          | 1               |
| seria             | 1            | serivs           | 1               |
| discessvs         | 1            | discedo          | 1               |
| stela             | 1            | stelo            | 1               |
| nvmero            | 1            | nvmervs          | 1               |
| cerno             | 1            | cresco           | 1               |
| inicio            | 1            | iniactvs         | 1               |
| tvmvlo            | 1            | tvmvlabor        | 1               |
| inqvio            | 1            | inqvies          | 1               |
| sciron            | 1            | sciro            | 1               |
| seqvor            | 1            | seqvens          | 1               |
| linqvo            | 1            | linqvor          | 1               |
| cado              | 1            | cadvs            | 1               |
| graviter          | 1            | gravis           | 1               |
| tempestivo        | 1            | tempestivvs      | 1               |
| arelate           | 1            | arelas           | 1               |
| qvamplvres        | 1            | qvamplvs         | 1               |
| infervs           | 1            | imvm             | 1               |
| avlis             | 1            | avlvs            | 1               |
| hasdrvbal         | 1            | hasdrvbalis      | 1               |
| mamertinvs        | 1            | mamertini        | 1               |
| sagvntinvs        | 1            | sagvntini        | 1               |
| consangvinei      | 1            | consangvinevs    | 1               |
| hammon            | 1            | ammo             | 1               |
| tersvs            | 1            | tersa            | 1               |
| distincte         | 1            | distinctvs       | 1               |
| achaias           | 1            | achaeiades       | 1               |
| aegina            | 1            | aeginvs          | 1               |
| prosocer          | 1            | prosocor         | 1               |
| praeteritvs       | 1            | praeteritvm      | 1               |
| dvrvm             | 1            | dvrvs            | 1               |
| angvstvm          | 1            | angvstvs         | 1               |
| laodicia          | 1            | laodicea         | 1               |
| inimice           | 1            | inimicvs         | 1               |
| expensvm          | 1            | expendo          | 1               |
| lanivs            | 1            | laniter          | 1               |
| canterivs         | 1            | canterivm        | 1               |
| aganippis         | 1            | aganippidvs      | 1               |
| habinnas          | 1            | habinna          | 1               |
| svperbvs          | 1            | svperbvm         | 1               |
| flecto            | 1            | flexvra          | 1               |
| echo              | 1            | echvs            | 1               |
| passvm            | 1            | patior           | 1               |
| timor             | 1            | timvs            | 1               |
| reverto           | 1            | revertor         | 1               |
| militia           | 1            | militiae         | 1               |
| integre           | 1            | integro          | 1               |
| sardi             | 1            | sardis           | 1               |
| hispani           | 1            | hispanvs         | 1               |
| olenivs           | 1            | olenia           | 1               |
| statva            | 1            | statvo           | 1               |
| capsella          | 1            | capsela          | 1               |
| angor             | 1            | ango             | 1               |
| venvs             | 1            | venio            | 1               |
| delitesco         | 1            | delitisco        | 1               |
| amomvm            | 1            | amoma            | 1               |
| stemma            | 1            | stemmo           | 1               |
| millesimvs        | 1            | mille            | 1               |
| trabeatvs         | 1            | trabeate         | 1               |
| penso             | 1            | pensatvs         | 1               |
| damnvm            | 1            | damno            | 1               |
| convenio          | 1            | covenio          | 1               |
| pecv              | 1            | pecvvs           | 1               |
| petrevs           | 1            | petreivs         | 1               |
| vsvs              | 1            | vtor             | 1               |
| pythivs           | 1            | pythia           | 1               |
| pernocto          | 1            | pernoctor        | 1               |
| monstrvm          | 1            | monstro          | 1               |
| accommodo         | 1            | accommodatvs     | 1               |
| testificor        | 1            | testificio       | 1               |
| concvbitvs        | 1            | concvmbo         | 1               |
| pachynvm          | 1            | pachynvs         | 1               |
| convivor          | 1            | convivo          | 1               |
| pecto             | 1            | pexvs            | 1               |
| plasma            | 1            | plasmate         | 1               |
| asia              | 1            | asivs            | 1               |
| dindymvs          | 1            | dindymei         | 1               |
| cingvla           | 1            | cingvlvm         | 1               |
| mvtvvs            | 1            | mvtvvm           | 1               |
| ilivs             | 1            | ilia             | 1               |
| versor            | 1            | verso            | 1               |
| praesignis        | 1            | praesigno        | 1               |
| amphitrite        | 1            | amphitrites      | 1               |
| bvllatvs          | 1            | bvlfatvs         | 1               |
| fritillvs         | 1            | fritillvm        | 1               |
| vernacvlvs        | 1            | vernacvlvm       | 1               |
| externi           | 1            | externvs         | 1               |
| hvmo              | 1            | hvmer            | 1               |
| forte             | 1            | fortis           | 1               |
| pan               | 1            | panvs            | 1               |
| pthisicvs         | 1            | tisicvs          | 1               |
| pavxillvs         | 1            | pavxillvm        | 1               |
| edita             | 1            | editvm           | 1               |
| antiqvi           | 1            | antiqvvs         | 1               |
| pylivs            | 1            | pylia            | 1               |
| hyllvs            | 1            | hylle            | 1               |
| interrogativncvla | 1            | interrogatvla    | 1               |
| lvperci           | 1            | lvpercvs         | 1               |
| aptvs             | 1            | apte             | 1               |
| fides             | 1            | fido             | 1               |
| incandeo          | 1            | incandesco       | 1               |
| fretvm            | 1            | fretvs           | 1               |
| nereis            | 1            | nereides         | 1               |
| bias              | 1            | bians            | 1               |
| pvdeo             | 1            | pvdendvs         | 1               |
| cochlea           | 1            | cochea           | 1               |
| chorda            | 1            | cor              | 1               |
| sinape            | 1            | senape           | 1               |
| fortvno           | 1            | fortvnor         | 1               |
| continens         | 1            | contineo         | 1               |
| incipio           | 1            | inceptvm         | 1               |
| tvscvlanvs        | 1            | tvscvlanvm       | 1               |
| ivventivs         | 1            | ivventia         | 1               |
| atinas            | 1            | atinativs        | 1               |
| irreligatvs       | 1            | irreligo         | 1               |
| aeratvs           | 1            | aeratvm          | 1               |
| cavdinvs          | 1            | cavdina          | 1               |
| exercitatvs       | 1            | exercito         | 1               |
| nympha            | 1            | nymphvs          | 1               |
| sepositvs         | 1            | sepono           | 1               |
| qvintilis         | 1            | qvintilivs       | 1               |
| hiempsal          | 1            | hiempsalis       | 1               |
| beo               | 1            | bea              | 1               |
| invivs            | 1            | invia            | 1               |
| cibarivs          | 1            | cibaria          | 1               |
| pvsillvs          | 1            | pvsilla          | 1               |
| oblivivm          | 1            | oblivio          | 1               |
| svbdo             | 1            | svbde            | 1               |
| biceps            | 1            | bicipitvs        | 1               |
| sterto            | 1            | sterno           | 1               |
| recte             | 1            | rectvs           | 1               |
| onero             | 1            | oneror           | 1               |
| torcvlvs          | 1            | torcvlvm         | 1               |
| extentvs          | 1            | extendo          | 1               |
| fvnicvlvs         | 1            | fvnicvlvm        | 1               |
| spvmans           | 1            | spvmo            | 1               |
| charybdis         | 1            | carybdae         | 1               |
| pons              | 1            | pontvs           | 1               |
| tonsvra           | 1            | tondero          | 1               |
| compertvs         | 1            | comperio         | 1               |
| saxvm             | 1            | saxvs            | 1               |
| vectigalis        | 1            | vectigal         | 1               |
| decerno           | 1            | decretvm         | 1               |
| danai             | 1            | danavs           | 1               |
| evctemon          | 1            | evctemvs         | 1               |
| vsvcapio          | 1            | vsvcapivm        | 1               |
| dvctvs            | 1            | dvco             | 1               |
| havstvs           | 1            | havrio           | 1               |
| actvs             | 1            | ago              | 1               |
| dardanivs         | 1            | dardania         | 1               |
| extero            | 1            | extritvo         | 1               |
| angvinvs          | 1            | angvina          | 1               |
| pervigilivm       | 1            | pervigilia       | 1               |
| aegre             | 1            | aeger            | 1               |
| ita               | 1            | itan             | 1               |
| inceptvm          | 1            | incipio          | 1               |
| agna              | 1            | agnvs            | 1               |
| balnearia         | 1            | balinerivm       | 1               |
| commorior         | 1            | commor           | 1               |
| hvmanvm           | 1            | hvmanvs          | 1               |
| conchis           | 1            | conches          | 1               |
| lesbis            | 1            | lesbides         | 1               |
| agamemnonivs      | 1            | agamemmonii      | 1               |
| index             | 1            | indicvs          | 1               |
| peramplvs         | 1            | perampla         | 1               |
| falsvs            | 1            | falsvm           | 1               |
| impero            | 1            | imperatvm        | 1               |
| hermione          | 1            | hermion          | 1               |
| milesivs          | 1            | milesia          | 1               |
| cvcvrbita         | 1            | cvcvrbitvm       | 1               |
| pollicitvm        | 1            | polliceor        | 1               |
| ambactvs          | 1            | ambigo           | 1               |
| abrvmpo           | 1            | abrvptvs         | 1               |
| statvo            | 1            | statva           | 1               |
| enchytvm          | 1            | encytvs          | 1               |
| calidvs           | 1            | caldvs           | 1               |
| coloro            | 1            | coloratvs        | 1               |
| svpremvm          | 1            | svpervs          | 1               |
| viride            | 1            | viridis          | 1               |
| retendo           | 1            | retineo          | 1               |
| arbvscvla         | 1            | arbvscvlvs       | 1               |
| pictor            | 1            | pictvm           | 1               |
| servs             | 1            | sero             | 1               |
| cannae            | 1            | cannas           | 1               |
| circvmsedeo       | 1            | circvmsideo      | 1               |
| lector            | 1            | lectvs           | 1               |
| hvmana            | 1            | hvmanvs          | 1               |
| tibvr             | 1            | tibvrvs          | 1               |
| volcanvs          | 1            | vvlcanvs         | 1               |
| pelopeias         | 1            | pelopeiades      | 1               |
| venerandvs        | 1            | veneror          | 1               |
| istic             | 1            | istvc            | 1               |
| lvno              | 1            | lvnatvs          | 1               |
| exopinissso       | 1            | exopinio         | 1               |
| illino            | 1            | illit            | 1               |
| textvm            | 1            | texo             | 1               |
| eligo             | 1            | electvs          | 1               |
| silvrvs           | 1            | silvro           | 1               |
| percoqvo          | 1            | percoco          | 1               |
| orbita            | 1            | orbitvm          | 1               |
| afflvens          | 1            | afflvo           | 1               |
| aetatvla          | 1            | aetatvlvs        | 1               |
| pvteal            | 1            | pvtealis         | 1               |
| versvtvs          | 1            | versvte          | 1               |
| pascor            | 1            | pasco            | 1               |
| receptvs          | 1            | recipio          | 1               |
| mendax            | 1            | mendaciter       | 1               |
| averni            | 1            | arverni          | 1               |
| insvla            | 1            | insvl            | 1               |
| incitatvs         | 1            | incito           | 1               |
| caervlevs         | 1            | caervlvs         | 1               |
| arte              | 1            | ars              | 1               |
| ovillvs           | 1            | oville           | 1               |
| siccvs            | 1            | siccvm           | 1               |
| casevm            | 1            | casevs           | 1               |
| vasa              | 1            | vas              | 1               |
| primipilvs        | 1            | primipilis       | 1               |
| care              | 1            | careo            | 1               |
| elavo             | 1            | eloveo           | 1               |
| hvmidvs           | 1            | vmidvs           | 1               |
| sceleste          | 1            | scelestvs        | 1               |
| vicesimanvs       | 1            | vicensimanvs     | 1               |
| expressvs         | 1            | exprimo          | 1               |
| exigvvm           | 1            | exigvvs          | 1               |
| qvilibet          | 1            | qvamlibet        | 1               |
| phthioticvs       | 1            | phtioticvs       | 1               |
| crannon           | 1            | cranno           | 1               |
| semiredvctvs      | 1            | semiredvco       | 1               |
| merx              | 1            | merces           | 1               |
| arcanvm           | 1            | arcanvs          | 1               |
| ebvrnvs           | 1            | ebvrnevs         | 1               |
| crocos            | 1            | crocvs           | 1               |
| editvs            | 1            | edo              | 1               |
| tetrarches        | 1            | tetrarchae       | 1               |
| derisvs           | 1            | derideo          | 1               |
| svpervacvvm       | 1            | svpervacvvs      | 1               |
| gaditanvs         | 1            | gaditani         | 1               |
| mas               | 1            | mare             | 1               |
| gradatvs          | 1            | grador           | 1               |
| apte              | 1            | aptvs            | 1               |
| hvmeo             | 1            | hvmer            | 1               |
| profecto          | 1            | proficiscor      | 1               |
| concaleo          | 1            | concalesco       | 1               |
| ignosco           | 1            | ignotvs          | 1               |
| mandatvm          | 1            | mando            | 1               |
| dirce             | 1            | dircvs           | 1               |
| paetvs            | 1            | paeto            | 1               |
| vrgens            | 1            | vrgeo            | 1               |
| lepvs             | 1            | lepor            | 1               |
| senior            | 1            | senex            | 1               |
| effervesco        | 1            | efferveo         | 1               |
| profvndvm         | 1            | profvndvs        | 1               |
| colloqvivm        | 1            | colloqvor        | 1               |
| pelasgias         | 1            | pelasgiades      | 1               |
| improviso         | 1            | improvisvs       | 1               |
| carnifex          | 1            | carnvfex         | 1               |
| anxivs            | 1            | anxio            | 1               |
| ebvllio           | 1            | ebvllivis        | 1               |
| bifvrcvm          | 1            | bifvrcvs         | 1               |
| fvgela            | 1            | fvgella          | 1               |
| arsamosata        | 1            | arsamosatas      | 1               |
| actvarivs         | 1            | actvaria         | 1               |
| remitto           | 1            | remissvs         | 1               |
| aliqvantvs        | 1            | aliqvanto        | 1               |
| praesvm           | 1            | praesens         | 1               |
| leonidas          | 1            | leonides         | 1               |
| prodo             | 1            | prodeo           | 1               |
| nave              | 1            | navis            | 1               |
| epistates         | 1            | episto           | 1               |
| messala           | 1            | messalla         | 1               |
| lippvs            | 1            | lippa            | 1               |
| simpliciter       | 1            | simplex          | 1               |
| motvs             | 1            | moveo            | 1               |
| comminor          | 1            | commino          | 1               |
| vna               | 1            | vnvs             | 1               |
| circvmtero        | 1            | circvmto         | 1               |
| deicio            | 1            | svm              | 1               |
| inaeqvatvs        | 1            | inaeqvo          | 1               |
| adigo             | 1            | adaxco           | 1               |
| media             | 1            | medivs           | 1               |
| cebalinvs         | 1            | cebalinvm        | 1               |
| apocvlo           | 1            | apocvlor         | 1               |
| gallinicivm       | 1            | gallicinivm      | 1               |
| salinae           | 1            | salina           | 1               |
| bes               | 1            | bess             | 1               |
| pvteo             | 1            | pvto             | 1               |
| vmbri             | 1            | vmbra            | 1               |
| cliens            | 1            | clvens           | 1               |
| siphvncvlvs       | 1            | sipvncvlvs       | 1               |
| obses             | 1            | obsidvs          | 1               |
| vanvm             | 1            | vanvs            | 1               |
| pharivs           | 1            | pharia           | 1               |
| instantia         | 1            | instans          | 1               |
| facetvs           | 1            | facetvm          | 1               |
| egressvs          | 1            | egredior         | 1               |
| antitheton        | 1            | antithetvs       | 1               |
| themistocles      | 1            | themistocle      | 1               |
| cincinnatvs       | 1            | cincinno         | 1               |
| stramenticivs     | 1            | stramenticivm    | 1               |
| tvscvs            | 1            | tvsci            | 1               |
| sinistrorsvm      | 1            | sinistrorsvs     | 1               |
| fors              | 1            | forte            | 1               |
| conivrati         | 1            | conivratvs       | 1               |
| arcesilavs        | 1            | arcesilae        | 1               |
| exortvs           | 1            | exorior          | 1               |
| locvples          | 1            | locvplete        | 1               |
| merens            | 1            | mereor           | 1               |
| sororivs          | 1            | sororivm         | 1               |
| reticvlvs         | 1            | reticvlvm        | 1               |
| obrvssa           | 1            | obrvssvs         | 1               |
| praegestio        | 1            | praegesto        | 1               |
| faveo             | 1            | faves            | 1               |
| ivstvm            | 1            | ivstvs           | 1               |
| ivdaea            | 1            | ivdaevs          | 1               |
| taxvs             | 1            | taxo             | 1               |
| medicina          | 1            | medicinvs        | 1               |
| saepta            | 1            | saepio           | 1               |
| circvs            | 1            | circvm           | 1               |
| vicinvm           | 1            | vicinvs          | 1               |
| pirithovs         | 1            | perithovs        | 1               |
| althaea           | 1            | althaevs         | 1               |
| elysivm           | 1            | elysivs          | 1               |
| bithynivs         | 1            | bithynvs         | 1               |
| gaetvli           | 1            | gaetvlvs         | 1               |
| somnvs            | 1            | somnis           | 1               |
| lvscvs            | 1            | lvsce            | 1               |
| arretivm          | 1            | arretivs         | 1               |
| recipio           | 1            | receptvs         | 1               |
| vigiliarivm       | 1            | vigilarivm       | 1               |
| pandvs            | 1            | panda            | 1               |
| ibervs            | 1            | iberi            | 1               |
| dissolvtvs        | 1            | dissolvo         | 1               |
| svperbe           | 1            | svperbvs         | 1               |
| rhodivs           | 1            | rhodii           | 1               |
| electa            | 1            | electvs          | 1               |
| opistographvs     | 1            | opisthographvs   | 1               |
| erigo             | 1            | erectvs          | 1               |
| fingo             | 1            | fictvs           | 1               |
| protervvs         | 1            | protervivs       | 1               |
| perendie          | 1            | perendio         | 1               |
| elementa          | 1            | elementvm        | 1               |
| corolla           | 1            | corollvs         | 1               |
| massiliensis      | 1            | massilienses     | 1               |
| ramale            | 1            | ramalis          | 1               |
| vegrandis         | 1            | vegrandvs        | 1               |
| svber             | 1            | svbsvm           | 1               |
| conciliatricvla   | 1            | conciliatricvlvm | 1               |
| pervetvs          | 1            | perveter         | 1               |
| comptvs           | 1            | como             | 1               |
| qvamlibet         | 1            | qvilibet         | 1               |
| troezen           | 1            | troezenvs        | 1               |
| difficilis        | 1            | difficvlter      | 1               |
| parnethvs         | 1            | parnethon        | 1               |
| riphaevs          | 1            | ripaevs          | 1               |
| aegalevs          | 1            | aegalevm         | 1               |
| pvlcher           | 1            | pvlchre          | 1               |
| directvs          | 1            | dirigo           | 1               |
| tredecim          | 1            | decimvs          | 1               |
| tevcer            | 1            | tevcri           | 1               |
| delvmbis          | 1            | delvmbo          | 1               |
| plvtevs           | 1            | plvtevm          | 1               |
| idrvs             | 1            | ider             | 1               |
| opvlens           | 1            | opvlentvs        | 1               |
| teretina          | 1            | teretinvs        | 1               |
| admissvm          | 1            | admitto          | 1               |
| marita            | 1            | maritvs          | 1               |
| catascopvs        | 1            | catascopes       | 1               |
| congiarivs        | 1            | congiarivm       | 1               |
| disdo             | 1            | disdido          | 1               |
| insipio           | 1            | insipitvs        | 1               |
| servvs            | 1            | servo            | 1               |
| avdiens           | 1            | avdio            | 1               |
| os                | 1            | ora              | 1               |
| lyrici            | 1            | lyricvs          | 1               |
| satvs             | 1            | sero             | 1               |
| lacones           | 1            | lacon            | 1               |
| vacca             | 1            | vaga             | 1               |
| consangvinea      | 1            | consangvinevs    | 1               |
| deperditvs        | 1            | deperdo          | 1               |
| doceo             | 1            | doctvs           | 1               |
| offendo           | 1            | offensvs         | 1               |
| tabae             | 1            | tabas            | 1               |
| paraetacene       | 1            | paraetacenes     | 1               |
| confiteor         | 1            | confessvs        | 1               |
| nimis             | 1            | nimvs            | 1               |
| pvnio             | 1            | pvnior           | 1               |
| vetvs             | 1            | vetervs          | 1               |
| praetereo         | 1            | praeteritvs      | 1               |
| paciscor          | 1            | pactvs           | 1               |
| cvrso             | 1            | intercvrso       | 1               |
| pars              | 1            | pario            | 1               |
| citrevs           | 1            | citrevm          | 1               |
| mixtvs            | 1            | misceo           | 1               |
| elementvm         | 1            | elementa         | 1               |
| svbripio          | 1            | svrripio         | 1               |
| pateo             | 1            | patens           | 1               |
| scribilita        | 1            | sciribilita      | 1               |
| excellentis       | 1            | excellens        | 1               |
| clavvs            | 1            | clavis           | 1               |
| armamenta         | 1            | armamentvm       | 1               |
| silvia            | 1            | silvivs          | 1               |
| transilio         | 1            | transislo        | 1               |
| scriblita         | 1            | sciribilita      | 1               |
| tvte              | 1            | tvtvs            | 1               |
| depvdet           | 1            | depvdo           | 1               |
| hybrida           | 1            | hibridvs         | 1               |
| elephas           | 1            | elephans         | 1               |
| centvm            | 1            | viginti          | 1               |
| chaere            | 1            | chaer            | 1               |
| permagnvm         | 1            | permagnvs        | 1               |
| recenseo          | 1            | recendo          | 1               |
| circvmsisto       | 1            | circvmsto        | 1               |
| cavda             | 1            | cavdvs           | 1               |
| tegeaevs          | 1            | tegeevs          | 1               |
| scripta           | 1            | scriptvm         | 1               |
| pinso             | 1            | pinseo           | 1               |
| albvs             | 1            | alba             | 1               |
| apvlvs            | 1            | apvla            | 1               |
| caro              | 1            | carvs            | 1               |
| ferinvs           | 1            | ferina           | 1               |
| certvm            | 1            | certvs           | 1               |
| emereo            | 1            | emo              | 1               |
| naxvs             | 1            | naxon            | 1               |
| ivnix             | 1            | ivnicvm          | 1               |
| fictile           | 1            | fictilis         | 1               |
| altervter         | 1            | alterivs         | 1               |
| albinvs           | 1            | albinivs         | 1               |
| revs              | 1            | res              | 1               |
| erro              | 1            | errvm            | 1               |
| colo              | 1            | colvs            | 1               |
| obsecro           | 1            | obsecror         | 1               |
| venero            | 1            | veneror          | 1               |
| pelasgis          | 1            | pelasgides       | 1               |
| insvbres          | 1            | insvbrivs        | 1               |
| cvra              | 1            | cvro             | 1               |
| antistes          | 1            | antestitvs       | 1               |
| fvndo             | 1            | svpernvns        | 1               |
| effvndo           | 1            | effvsvs          | 1               |
| obseqvens         | 1            | obseqvor         | 1               |
| svbedo            | 1            | svbsvm           | 1               |
| vereor            | 1            | verens           | 1               |
| etesivs           | 1            | etesiae          | 1               |
| raro              | 1            | rarvs            | 1               |
| amylvm            | 1            | amvlvs           | 1               |
| exvrgeo           | 1            | exsvrgo          | 1               |
| petitor           | 1            | peto             | 1               |
| orichalcvm        | 1            | oricalchvs       | 1               |
| nvmidae           | 1            | nvmidvs          | 1               |
| comitia           | 1            | comitivm         | 1               |
| ambio             | 1            | ambitvs          | 1               |
| observantia       | 1            | observo          | 1               |
| lyrnessis         | 1            | lyrnesis         | 1               |
| elegidion         | 1            | elegidivm        | 1               |
| tribvnicivs       | 1            | tribvnicvs       | 1               |
| rheda             | 1            | raeda            | 1               |
| rebellis          | 1            | rebellvm         | 1               |
| svbtero           | 1            | svbtritvs        | 1               |
| femvr             | 1            | femina           | 1               |
| citatvs           | 1            | cito             | 1               |
| antistivs         | 1            | antistes         | 1               |
| monitvs           | 1            | moneo            | 1               |
| dependeo          | 1            | dependo          | 1               |
| monaeses          | 1            | monaesis         | 1               |
| exspecto          | 1            | exspectatvm      | 1               |
| freqventer        | 1            | freqvens         | 1               |
| semvstvlatvs      | 1            | semivstvlo       | 1               |
| artacana          | 1            | artacan          | 1               |
| pervagatvs        | 1            | pervagor         | 1               |
| athenion          | 1            | athenivs         | 1               |
| octavvs           | 1            | novem            | 1               |
| gaetvlvs          | 1            | gaetvli          | 1               |
| mei               | 1            | mevs             | 1               |
| gallograecia      | 1            | gallograecivs    | 1               |
| perpetve          | 1            | perpetvvs        | 1               |
| pinna             | 1            | penna            | 1               |
| advento           | 1            | advenio          | 1               |
| tvsci             | 1            | tvscivs          | 1               |
| sestertivm        | 1            | sestertivs       | 1               |
| dehavrio          | 1            | deorior          | 1               |
| cerritvs          | 1            | cerrita          | 1               |
| vbivs             | 1            | vbii             | 1               |
| signo             | 1            | signvm           | 1               |
| coeptvm           | 1            | coepio           | 1               |
| elegi             | 1            | eligo            | 1               |
| horridvlvs        | 1            | horridvlvm       | 1               |
| initio            | 1            | initiatvs        | 1               |
| profanvs          | 1            | profani          | 1               |
| commagenvs        | 1            | commagena        | 1               |
| procido           | 1            | procidens        | 1               |
| pvlsvs            | 1            | pello            | 1               |
| perfvga           | 1            | perfvgvs         | 1               |
| defetiscor        | 1            | defessvs         | 1               |
| conivgivm         | 1            | conivx           | 1               |
| penevs            | 1            | penivs           | 1               |
| peneides          | 1            | peneisis         | 1               |
| dorvs             | 1            | doris            | 1               |
| achradina         | 1            | achradon         | 1               |
| prytanevm         | 1            | prytanevs        | 1               |
| siren             | 1            | sirenae          | 1               |
| precarivs         | 1            | precarivm        | 1               |
| patina            | 1            | patinvs          | 1               |
| crassvs           | 1            | crassvm          | 1               |
| occipvt           | 1            | occipio          | 1               |
| svaviter          | 1            | svavis           | 1               |
| melica            | 1            | meliqvs          | 1               |
| vernvm            | 1            | vernvs           | 1               |
| pecvarivs         | 1            | pecvarivm        | 1               |
| rvdo              | 1            | rvdvs            | 1               |
| apocalo           | 1            | apocalvm         | 1               |
| cavpo             | 1            | copvs            | 1               |
| langvens          | 1            | langveo          | 1               |
| lvpvs             | 1            | lvpe             | 1               |
| oppositvs         | 1            | oppono           | 1               |
| midas             | 1            | mida             | 1               |
| paratvs           | 1            | paro             | 1               |
| tacitvm           | 1            | tacitvs          | 1               |
| venditvm          | 1            | vendo            | 1               |
| romvlidae         | 1            | romvlidvs        | 1               |
| carbasvs          | 1            | carbasa          | 1               |
| moneta            | 1            | monetvm          | 1               |
| petavrvm          | 1            | petavro          | 1               |
| egero             | 1            | ago              | 1               |
| continvvs         | 1            | continvo         | 1               |
| pavci             | 1            | pavcvs           | 1               |
| confvndo          | 1            | confvsvs         | 1               |
| repvdio           | 1            | repvdiae         | 1               |
| immerito          | 1            | immeritvs        | 1               |
| svbmitto          | 1            | svbmissvs        | 1               |
| intelligens       | 1            | intelligo        | 1               |
| frico             | 1            | frictvs          | 1               |
| noto              | 1            | nota             | 1               |
| minos             | 1            | minoa            | 1               |
| digressvs         | 1            | digredior        | 1               |
| lycvs             | 1            | lycon            | 1               |
| nvntio            | 1            | nvntiator        | 1               |
| commode           | 1            | commodvs         | 1               |
| triceni           | 1            | tricenvs         | 1               |
| annvvm            | 1            | annvvs           | 1               |
| celer             | 1            | celerivs         | 1               |
| fvlgens           | 1            | fvlgeo           | 1               |
| absolvtvs         | 1            | absolvo          | 1               |
| cvpiens           | 1            | cvpio            | 1               |
| infimvm           | 1            | infervs          | 1               |
| timide            | 1            | timidvs          | 1               |
| salmonis          | 1            | salmon           | 1               |
| mvndities         | 1            | mvnditie         | 1               |
| svccino           | 1            | svccinvs         | 1               |
| mvnitvs           | 1            | mvnite           | 1               |
| prominvlvs        | 1            | prominvla        | 1               |
| intemperans       | 1            | intemperanter    | 1               |
| serpyllvm         | 1            | serpvllvm        | 1               |
| sempiternvm       | 1            | sempiternvs      | 1               |
| evocatvs          | 1            | evoco            | 1               |
| labes             | 1            | labor            | 1               |
| fertvm            | 1            | fertvs           | 1               |
| poetria           | 1            | poetrivm         | 1               |
| caesarianvs       | 1            | caesareanvs      | 1               |
| acceptvs          | 1            | accipio          | 1               |
| fvriosvs          | 1            | fvriose          | 1               |
| designator        | 1            | dissignator      | 1               |
| calidvm           | 1            | calidvs          | 1               |
| frigidvm          | 1            | frigidvs         | 1               |
| magnificvs        | 1            | magnificens      | 1               |
| pvrvs             | 1            | pvra             | 1               |
| amplifice         | 1            | amplificvs       | 1               |
| emo               | 1            | emendo           | 1               |
| graeci            | 1            | graecvs          | 1               |
| baetica           | 1            | baeticvs         | 1               |
| noceo             | 1            | nocens           | 1               |
| scylax            | 1            | scylaces         | 1               |
| taedet            | 1            | taedeo           | 1               |
| sistrvm           | 1            | sistra           | 1               |
| tiridates         | 1            | tiridas          | 1               |
| mando             | 1            | mandatvm         | 1               |
| svbeo             | 1            | svbito           | 1               |
| aprilis           | 1            | aprilivs         | 1               |
| maivs             | 1            | maiivs           | 1               |
| soleo             | 1            | solitvs          | 1               |
| minotavrvs        | 1            | minotavrvm       | 1               |
| decoctior         | 1            | decoctvs         | 1               |
| divvs             | 1            | diva             | 1               |
| sacrarivm         | 1            | sacro            | 1               |
| manlivs           | 1            | manlia           | 1               |
| itonvs            | 1            | iton             | 1               |
| conditvs          | 1            | condo            | 1               |
| svbitvm           | 1            | svbitvs          | 1               |
| evrytis           | 1            | evrytidvs        | 1               |
| neglectvs         | 1            | negligo          | 1               |
| calliopea         | 1            | calliope         | 1               |
| amalthea          | 1            | amalthevs        | 1               |
| pronvba           | 1            | pronvbvs         | 1               |
| propinqvi         | 1            | propinqvvs       | 1               |
| cvtis             | 1            | cvtvs            | 1               |
| qveror            | 1            | qvestvs          | 1               |
| potissimvm        | 1            | potivs           | 1               |
| incvnabvla        | 1            | incvnabvlvm      | 1               |
| venvndo           | 1            | venvmdo          | 1               |
| tvrpiter          | 1            | tvrpis           | 1               |
| militaris         | 1            | milito           | 1               |
| meio              | 1            | meie             | 1               |
| virgatvs          | 1            | virgo            | 1               |
| chivs             | 1            | chia             | 1               |
| margaritvm        | 1            | margaritvs       | 1               |
| distingvo         | 1            | distinctvs       | 1               |
| expiscor          | 1            | expisco          | 1               |
| litvra            | 1            | litvrvs          | 1               |
| pello             | 1            | pvlsvs           | 1               |
| pleione           | 1            | pleiones         | 1               |
| allex             | 1            | hallex           | 1               |
| perpavcvs         | 1            | perpavca         | 1               |
| cvpido            | 1            | cvpidvs          | 1               |
| clivvm            | 1            | clivvs           | 1               |
| depressvs         | 1            | deprimo          | 1               |
| damnas            | 1            | damno            | 1               |
| lex               | 1            | lego             | 1               |
| impar             | 1            | imparo           | 1               |
| decorvs           | 1            | decvs            | 1               |
| haemonia          | 1            | haemonivs        | 1               |
| exasciatvs        | 1            | exasceo          | 1               |
| stativa           | 1            | stativvs         | 1               |
| praevertor        | 1            | praeverto        | 1               |
| naevivs           | 1            | naevia           | 1               |
| opertvm           | 1            | operio           | 1               |
| laqvear           | 1            | laqveo           | 1               |
| sesqvihora        | 1            | sesqvivm         | 1               |
| beneficvs         | 1            | benefico         | 1               |
| mervm             | 1            | mervs            | 1               |
| phalacrvs         | 1            | phalacrvm        | 1               |
| perexcelsvs       | 1            | perexcello       | 1               |
| circvmcisvs       | 1            | circvmcido       | 1               |
| compactvs         | 1            | compaciscor      | 1               |
| loricatvs         | 1            | lorico           | 1               |
| postidea          | 1            | postideo         | 1               |
| cito              | 1            | cite             | 1               |
| minvs             | 1            | parvm            | 1               |
| svsa              | 1            | svsae            | 1               |
| triticevs         | 1            | triticea         | 1               |
| hem               | 1            | em               | 1               |
| vello             | 1            | volo             | 1               |
| illo              | 1            | ille             | 1               |
| svpero            | 1            | svpervs          | 1               |
| labellvm          | 1            | labella          | 1               |
| cvrtvs            | 1            | cvrta            | 1               |
| fvnctvs           | 1            | fvngor           | 1               |
| myrtvs            | 1            | myrti            | 1               |
| consido           | 1            | considero        | 1               |
| dipondivs         | 1            | dvponde          | 1               |
| interiora         | 1            | interior         | 1               |
| fabrico           | 1            | fabricor         | 1               |
| cvbo              | 1            | cvbitvm          | 1               |
| sancte            | 1            | sanctvs          | 1               |
| maternvs          | 1            | materno          | 1               |
| phaethon          | 1            | phaeton          | 1               |
| carvs             | 1            | car              | 1               |
| olens             | 1            | oleo             | 1               |
| rvber             | 1            | rvbeo            | 1               |
| litvs             | 1            | litor            | 1               |
| procervs          | 1            | procer           | 1               |
| tantalis          | 1            | tantalides       | 1               |
| calida            | 1            | calda            | 1               |
| cithara           | 1            | citharae         | 1               |
| fallo             | 1            | falsvs           | 1               |
| necessario        | 1            | necessarivs      | 1               |
| titivs            | 1            | titvs            | 1               |
| falanivs          | 1            | falanivm         | 1               |
| thressvs          | 1            | thraess          | 1               |
| peltatvs          | 1            | pelto            | 1               |
| stvlti            | 1            | stvltvs          | 1               |
| svpplex           | 1            | svpplicivm       | 1               |
| ipse              | 1            | svi              | 1               |
| habitvs           | 1            | habeo            | 1               |
| exiliter          | 1            | exsiliter        | 1               |
| svbmissvs         | 1            | svbmitto         | 1               |
| praetextatvs      | 1            | praetextator     | 1               |
| avdax             | 1            | avdaciter        | 1               |
| prosper           | 1            | prospero         | 1               |
| dominatvs         | 1            | dominor          | 1               |
| linvs             | 1            | linon            | 1               |
| aelinos           | 1            | aelinvs          | 1               |
| orior             | 1            | oriens           | 1               |
| intepesco         | 1            | intepeo          | 1               |
| charites          | 1            | charis           | 1               |
| vigiles           | 1            | vigilvs          | 1               |
| lvgdvnenses       | 1            | lvgdvnensis      | 1               |
| gratia            | 1            | gratis           | 1               |
| tertivs           | 1            | tres             | 1               |
| sacerdos          | 1            | sacerdotivs      | 1               |
| tantalicvs        | 1            | tantalici        | 1               |
| cleomenes         | 1            | cleomene         | 1               |
| bactrianvs        | 1            | bactriani        | 1               |
| despectvs         | 1            | despicio         | 1               |
| evxinvs           | 1            | evxinvm          | 1               |
| fvga              | 1            | fvgo             | 1               |
| tantalvs          | 1            | tantalis         | 1               |
| poetris           | 1            | poetridvs        | 1               |
| pegasevs          | 1            | pegaseivs        | 1               |
| vitis             | 1            | vito             | 1               |
| secretvm          | 1            | secretvs         | 1               |
| perversvs         | 1            | perverto         | 1               |
| nvntivm           | 1            | nvntivs          | 1               |
| dignvs            | 1            | digne            | 1               |
| vita              | 1            | vito             | 1               |
| calvae            | 1            | calva            | 1               |
| imperitia         | 1            | imperitivs       | 1               |
| bellerophontes    | 1            | bellorophanta    | 1               |
| lethe             | 1            | lethvs           | 1               |
| prope             | 1            | propivs          | 1               |
| copvlor           | 1            | copvlo           | 1               |
| lacerta           | 1            | lacertvs         | 1               |
| remigivm          | 1            | remigivs         | 1               |
| seligo            | 1            | selectvm         | 1               |
| vectigal          | 1            | vectigalis       | 1               |
| inibi             | 1            | ineo             | 1               |
| rostratvs         | 1            | rostratvm        | 1               |
| theodorvs         | 1            | theodi           | 1               |
| nicasion          | 1            | nicasio          | 1               |
| distero           | 1            | distrio          | 1               |
| laxatvs           | 1            | laxo             | 1               |
| ferio             | 1            | feries           | 1               |
| advltera          | 1            | advlter          | 1               |
| dvlce             | 1            | dvlcis           | 1               |
| severa            | 1            | severvs          | 1               |
| hilaris           | 1            | hilaria          | 1               |
| qvinqvagenvs      | 1            | qvinqvagenis     | 1               |
| thrace            | 1            | thraca           | 1               |
| paphvs            | 1            | paphon           | 1               |
| millesima         | 1            | millesimvs       | 1               |
| thessala          | 1            | thessalvs        | 1               |
| contemno          | 1            | contemptvs       | 1               |
| titienses         | 1            | titiensis        | 1               |
| ramnes            | 1            | ramnies          | 1               |
| lvceres           | 1            | lvcer            | 1               |
| serenvs           | 1            | serenvm          | 1               |
| fvrens            | 1            | fvro             | 1               |
| clarisonvs        | 1            | clarisona        | 1               |
| providens         | 1            | provideo         | 1               |
| igvvinates        | 1            | igvvinativm      | 1               |
| arsacides         | 1            | arsacidae        | 1               |
| tvrbatvs          | 1            | tvrbo            | 1               |
| ordinatvs         | 1            | ordino           | 1               |
| medvsa            | 1            | medvsvs          | 1               |
| agathocles        | 1            | agathoclvs       | 1               |
| vidva             | 1            | vidvvs           | 1               |
| operatvs          | 1            | operor           | 1               |
| pelasgvs          | 1            | pelasgas         | 1               |
| cymba             | 1            | cymbvs           | 1               |
| derepente         | 1            | derepo           | 1               |
| qvaestvs          | 1            | qvaero           | 1               |
| inaniae           | 1            | inania           | 1               |
| oppleo            | 1            | oppleta          | 1               |
| phoebe            | 1            | phoebvs          | 1               |
| exopto            | 1            | exoptatvs        | 1               |
| acinaces          | 1            | acinace          | 1               |
| pyrene            | 1            | pyrenes          | 1               |
| oxycominvm        | 1            | oxycomen         | 1               |
| colvs             | 1            | colvm            | 1               |
| mordeo            | 1            | morsa            | 1               |

# POS

```
all:
  accuracy: 0.872
  precision: 0.5911
  recall: 0.7965
  support: 146137
ambiguous-tokens:
  accuracy: 0.8364
  precision: 0.5566
  recall: 0.6696
  support: 43026
unknown-tokens:
  accuracy: 0.7162
  precision: 0.1317
  recall: 0.3547
  support: 6114

```

| Expected   | Total Errors | Predictions | Predicted times |
|------------|--------------|-------------|-----------------|
| VER        | 7466         | ADJqua      | 1346            |
|            |              | ADV         | 1263            |
|            |              | NOM         | 1020            |
|            |              | INJ         | 678             |
|            |              | PROind      | 490             |
|            |              | PROdem      | 443             |
|            |              | ADVint      | 363             |
|            |              | ADVint.neg  | 205             |
|            |              | ADJadv.mul  | 198             |
|            |              | ADVrel      | 192             |
|            |              | PROper      | 167             |
|            |              | PROrel      | 116             |
|            |              | PROref      | 114             |
|            |              | ADJcar      | 113             |
|            |              | PRE         | 103             |
|            |              | CONsub      | 96              |
|            |              | CONcoo      | 90              |
|            |              | PROpos.ref  | 82              |
|            |              | PROint      | 79              |
|            |              | PROpos      | 77              |
|            |              | ADVneg      | 51              |
|            |              | ADJord      | 49              |
|            |              | ADJmul      | 36              |
|            |              |             | 31              |
|            |              | ADJadv.ord  | 27              |
|            |              | pos         | 23              |
|            |              | ADJdis      | 8               |
|            |              | VERaux      | 6               |
| NOM        | 4247         | ADJqua      | 1062            |
|            |              | PROind      | 473             |
|            |              | PROper      | 470             |
|            |              | ADV         | 430             |
|            |              | INJ         | 415             |
|            |              | VER         | 381             |
|            |              | PROdem      | 215             |
|            |              | ADJcar      | 192             |
|            |              | ADJadv.mul  | 121             |
|            |              | ADJord      | 114             |
|            |              | PROint      | 71              |
|            |              | PROpos      | 39              |
|            |              | ADJdis      | 37              |
|            |              | ADVrel      | 33              |
|            |              | ADVint      | 31              |
|            |              | PRE         | 30              |
|            |              | PROpos.ref  | 26              |
|            |              | PROrel      | 24              |
|            |              | CONcoo      | 22              |
|            |              | PROref      | 18              |
|            |              | CONsub      | 13              |
|            |              | ADJmul      | 10              |
|            |              | ADJadv.ord  | 6               |
|            |              | ADVint.neg  | 6               |
|            |              | ADVneg      | 5               |
|            |              |             | 2               |
|            |              | pos         | 1               |
| ADJqua     | 2929         | NOM         | 634             |
|            |              | ADV         | 484             |
|            |              | PROind      | 477             |
|            |              | ADJord      | 305             |
|            |              | VER         | 274             |
|            |              | ADJcar      | 159             |
|            |              | PROdem      | 78              |
|            |              | PROpos.ref  | 54              |
|            |              | INJ         | 52              |
|            |              | PROint      | 48              |
|            |              | PROpos      | 44              |
|            |              | PROrel      | 39              |
|            |              | PRE         | 37              |
|            |              | ADJadv.mul  | 36              |
|            |              | ADJdis      | 30              |
|            |              | ADVint.neg  | 30              |
|            |              | PROper      | 29              |
|            |              | ADJmul      | 28              |
|            |              | ADJadv.ord  | 21              |
|            |              | ADVrel      | 19              |
|            |              | CONcoo      | 15              |
|            |              | CONsub      | 14              |
|            |              | PROref      | 10              |
|            |              | ADVint      | 6               |
|            |              | ADVneg      | 4               |
|            |              |             | 1               |
|            |              | pos         | 1               |
| CONsub     | 670          | ADVrel      | 290             |
|            |              | PROrel      | 206             |
|            |              | CONcoo      | 48              |
|            |              | ADVint      | 47              |
|            |              | PROint      | 24              |
|            |              | ADV         | 19              |
|            |              | PRE         | 14              |
|            |              | ADVneg      | 12              |
|            |              | VER         | 6               |
|            |              | ADJord      | 2               |
|            |              | PROind      | 2               |
| PROdem     | 572          | ADJcar      | 246             |
|            |              | ADV         | 171             |
|            |              | PROind      | 64              |
|            |              | PROint      | 51              |
|            |              | PROpos      | 13              |
|            |              | ADVint      | 9               |
|            |              | INJ         | 6               |
|            |              | VER         | 3               |
|            |              | PROrel      | 2               |
|            |              | PROref      | 2               |
|            |              | ADVrel      | 1               |
|            |              | PRE         | 1               |
|            |              | ADJadv.ord  | 1               |
|            |              | PROpos.ref  | 1               |
|            |              | ADVint.neg  | 1               |
| ADV        | 541          | CONcoo      | 113             |
|            |              | PROind      | 85              |
|            |              | PROdem      | 82              |
|            |              | PRE         | 60              |
|            |              | NOM         | 46              |
|            |              | ADJqua      | 34              |
|            |              | CONsub      | 29              |
|            |              | ADJcar      | 26              |
|            |              | ADVint      | 10              |
|            |              | ADJadv.ord  | 10              |
|            |              | ADVrel      | 9               |
|            |              | VER         | 8               |
|            |              | INJ         | 8               |
|            |              | ADVint.neg  | 7               |
|            |              | PROrel      | 4               |
|            |              | PROint      | 3               |
|            |              | PROper      | 2               |
|            |              | ADJord      | 2               |
|            |              | ADVneg      | 2               |
|            |              | ADJmul      | 1               |
| PROrel     | 401          | PROint      | 176             |
|            |              | ADVrel      | 103             |
|            |              | CONsub      | 62              |
|            |              | ADVint      | 29              |
|            |              | PROind      | 23              |
|            |              | ADJcar      | 7               |
|            |              | ADV         | 1               |
| ADVrel     | 354          | CONsub      | 164             |
|            |              | ADVint      | 94              |
|            |              | PROrel      | 72              |
|            |              | PROint      | 18              |
|            |              | ADV         | 2               |
|            |              | INJ         | 1               |
|            |              | ADJadv.mul  | 1               |
|            |              | CONcoo      | 1               |
|            |              | ADVint.neg  | 1               |
| CONcoo     | 322          | ADV         | 123             |
|            |              | ADVint      | 90              |
|            |              | CONsub      | 24              |
|            |              | PROrel      | 20              |
|            |              | INJ         | 15              |
|            |              | ADVint.neg  | 12              |
|            |              | PROdem      | 11              |
|            |              | ADJcar      | 8               |
|            |              | PROind      | 7               |
|            |              | PROint      | 4               |
|            |              | ADVneg      | 3               |
|            |              | ADVrel      | 3               |
|            |              | ADJadv.mul  | 1               |
|            |              | ADJqua      | 1               |
| PRE        | 305          | CONsub      | 148             |
|            |              | INJ         | 49              |
|            |              | ADV         | 47              |
|            |              | PROpos.ref  | 24              |
|            |              | ADVrel      | 15              |
|            |              | ADVint      | 7               |
|            |              | ADJadv.mul  | 4               |
|            |              | ADJdis      | 4               |
|            |              | ADVint.neg  | 3               |
|            |              | CONcoo      | 2               |
|            |              | PROind      | 1               |
|            |              | ADJqua      | 1               |
| PROint     | 217          | PROrel      | 151             |
|            |              | ADVint      | 21              |
|            |              | ADVrel      | 15              |
|            |              | PROind      | 14              |
|            |              | ADJcar      | 13              |
|            |              | ADV         | 2               |
|            |              | CONsub      | 1               |
| ADVint     | 172          | ADVrel      | 86              |
|            |              | PROint      | 35              |
|            |              | CONsub      | 26              |
|            |              | PROrel      | 19              |
|            |              | ADVint.neg  | 4               |
|            |              | CONcoo      | 1               |
|            |              | PROind      | 1               |
| PROind     | 142          | PROint      | 34              |
|            |              | PROrel      | 33              |
|            |              | ADJcar      | 18              |
|            |              | PROdem      | 16              |
|            |              | PROper      | 15              |
|            |              | ADV         | 11              |
|            |              | ADVrel      | 10              |
|            |              | PRE         | 1               |
|            |              | pos         | 1               |
|            |              | ADVint      | 1               |
|            |              | VER         | 1               |
|            |              | NOM         | 1               |
| ADJord     | 119          | ADJcar      | 32              |
|            |              | ADJadv.ord  | 32              |
|            |              | ADJqua      | 15              |
|            |              | PROpos      | 8               |
|            |              | ADJdis      | 7               |
|            |              | PRE         | 4               |
|            |              | ADV         | 3               |
|            |              | PROint      | 3               |
|            |              | ADVrel      | 2               |
|            |              | PROind      | 2               |
|            |              | VER         | 2               |
|            |              | NOM         | 2               |
|            |              | PROpos.ref  | 2               |
|            |              | PROdem      | 2               |
|            |              | ADVint      | 1               |
|            |              | ADVint.neg  | 1               |
|            |              | PROrel      | 1               |
| ADVneg     | 63           | CONsub      | 57              |
|            |              | CONcoo      | 3               |
|            |              | ADVint      | 1               |
|            |              | ADJdis      | 1               |
|            |              | ADVint.neg  | 1               |
| PROpos     | 31           | PROper      | 24              |
|            |              | ADJcar      | 4               |
|            |              | PROint      | 2               |
|            |              | ADJdis      | 1               |
| PROpos.ref | 27           | PROref      | 12              |
|            |              | PROind      | 8               |
|            |              | ADJcar      | 6               |
|            |              | PROpos      | 1               |
| ADJdis     | 23           | ADJcar      | 19              |
|            |              | PROind      | 2               |
|            |              | PROrel      | 1               |
|            |              | PROint      | 1               |
| INJ        | 23           | ADJadv.mul  | 6               |
|            |              | ADVint      | 6               |
|            |              | PROdem      | 4               |
|            |              | NOM         | 3               |
|            |              | PRE         | 3               |
|            |              | PROper      | 1               |
| ADJcar     | 20           | NOM         | 4               |
|            |              | PROdem      | 4               |
|            |              | PROind      | 4               |
|            |              | ADV         | 3               |
|            |              | PROrel      | 2               |
|            |              | PROref      | 1               |
|            |              | CONcoo      | 1               |
|            |              | ADJdis      | 1               |
| PROper     | 20           | PROpos      | 15              |
|            |              | ADVint      | 2               |
|            |              | pos         | 1               |
|            |              | ADJadv.mul  | 1               |
|            |              | NOM         | 1               |
| ADJadv.ord | 19           | ADV         | 17              |
|            |              | ADJord      | 2               |
| PROref     | 10           | PROpos.ref  | 10              |
| ADVint.neg | 5            | ADV         | 5               |
|            | 4            | NOM         | 2               |
|            |              | VER         | 1               |
|            |              | ADVint      | 1               |
| ADJmul     | 3            | ADJqua      | 2               |
|            |              | ADV         | 1               |

# Morph

```
all:
  accuracy: 0.7987
  precision: 0.3918
  recall: 0.2876
  support: 146137
ambiguous-tokens:
  accuracy: 0.7518
  precision: 0.3676
  recall: 0.3089
  support: 73514
unknown-tokens:
  accuracy: 0.5896
  precision: 0.3574
  recall: 0.277
  support: 6114
```

| Expected                                                           | Total Errors | Predictions                                                     | Predicted times |
|--------------------------------------------------------------------|--------------|-----------------------------------------------------------------|-----------------|
| MORPH=EMPTY                                                        | 5107         | Case=Nom|Numb=Sing|Gend=Masc                                    | 1035            |
|                                                                    |              | Case=Abl|Numb=Sing|Gend=MascNeut                                | 866             |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=Com                                     | 357             |
|                                                                    |              | Case=Ind                                                        | 349             |
|                                                                    |              | Deg=Pos                                                         | 280             |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Neut                                    | 191             |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 179             |
|                                                                    |              | Case=Abl|Numb=Plur|Gend=Com                                     | 162             |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=MascNeut                                | 128             |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 122             |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 105             |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=Neut                                    | 95              |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Com                             | 89              |
|                                                                    |              | Case=Abl|Numb=Sing|Gend=Fem                                     | 64              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 63              |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Fem                                     | 62              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 58              |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=Fem                                     | 56              |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 53              |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 52              |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Neut                                    | 42              |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 41              |
|                                                                    |              | Numb=Plur|Mood=Imp|Tense=Fut|Voice=Act|Person=2                 | 39              |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=MascNeut                                | 37              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 34              |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 30              |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Pass                                  | 27              |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 26              |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 23              |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=MascNeut                                | 22              |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 21              |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Neut                            | 20              |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 17              |
|                                                                    |              | Case=Gen|Numb=Sing|Gend=MascNeut                                | 16              |
|                                                                    |              | Deg=Sup                                                         | 16              |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 15              |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 14              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 13              |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Fut|Voice=Act|Person=2                 | 13              |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Masc                                    | 13              |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=Masc                                    | 13              |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 13              |
|                                                                    |              | Numb=Plur|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 10              |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 10              |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 9               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Fem                                     | 9               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 9               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=MascFem                         | 8               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 8               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Neut     | 8               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 8               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 8               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 7               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 7               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=Com                             | 6               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 6               |
|                                                                    |              | Case=Gen|Numb=Plur                                              | 5               |
|                                                                    |              | Deg=Comp                                                        | 5               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 5               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=MascFem                         | 5               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 5               |
|                                                                    |              | Case=Abl|Numb=Sing|Gend=Com                                     | 5               |
|                                                                    |              | Case=Gen|Numb=Sing|Gend=Com                                     | 4               |
|                                                                    |              | Gend=Fem                                                        | 4               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 4               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 4               |
|                                                                    |              | Numb=Plur|Mood=Imp|Tense=Fut|Voice=Act|Person=3                 | 4               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=Neut        | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=3                | 3               |
|                                                                    |              | Case=Gen|Numb=Plur|Deg=Pos|Gend=Com                             | 3               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 3               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 3               |
|                                                                    |              | Case=Voc|Numb=Sing|Gend=Masc                                    | 3               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Pass|Person=3               | 2               |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=Fem                                     | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=MascFem                                 | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Fem                                     | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=Fem       | 2               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=1                | 2               |
|                                                                    |              | Case=Gen|Numb=Plur|Gend=MascNeut                                | 2               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 2               |
|                                                                    |              | Case=Gen|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=MascNeut    | 1               |
|                                                                    |              | Case=Abl|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Com      | 1               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Perf|Voice=Act|Person=1                | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Impa|Voice=Act|Person=3                | 1               |
|                                                                    |              | Case=Voc|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=2                | 1               |
|                                                                    |              | Case=Voc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Case=Abl|Numb=Plur|Deg=Comp|Gend=Com                            | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                   | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Dep|Gend=Masc      | 1               |
|                                                                    |              | Case=Abl|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Impa|Voice=Act|Person=3                | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Fem       | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=MascNeut                                | 1               |
|                                                                    |              | Case=Voc|Numb=Plur                                              | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Neut     | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Case=Voc|Numb=Sing|Deg=Sup|Gend=Masc                            | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=MascFem                                 | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                   | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Case=Dat|Numb=Plur|Gend=Com                                     | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Neut      | 1               |
| Case=Nom|Numb=Sing                                                 | 1274         | Case=Acc|Numb=Sing                                              | 395             |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 202             |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 170             |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 149             |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 57              |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 45              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 44              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 34              |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 31              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 27              |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 13              |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 10              |
|                                                                    |              | Deg=Pos                                                         | 9               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 8               |
|                                                                    |              | Case=Gen|Numb=Plur                                              | 8               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 7               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 7               |
|                                                                    |              | Deg=Comp                                                        | 6               |
|                                                                    |              | MORPH=EMPTY                                                     | 5               |
|                                                                    |              | Deg=Sup                                                         | 5               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 4               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 4               |
|                                                                    |              | Case=Loc|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 2               |
|                                                                    |              | Case=Abl|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 2               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=1                | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 2               |
|                                                                    |              | Case=Dat|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Neut                                    | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Case=Abl|Numb=Plur|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=MascFem                         | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=MascNeut                                | 1               |
|                                                                    |              | Case=Ind                                                        | 1               |
|                                                                    |              | Case=Gen|Numb=Plur|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Fem                                     | 1               |
| Case=Abl|Numb=Sing                                                 | 1238         | Case=Nom|Numb=Sing                                              | 430             |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 238             |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 161             |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 80              |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 39              |
|                                                                    |              | Deg=Pos                                                         | 39              |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 38              |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 31              |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 26              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 25              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 21              |
|                                                                    |              | Case=Abl|Numb=Sing|Gend=MascNeut                                | 13              |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 12              |
|                                                                    |              | Case=Abl|Numb=Sing|Gend=Fem                                     | 11              |
|                                                                    |              | Case=Dat|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 11              |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 8               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Com                             | 5               |
|                                                                    |              | Case=Ind                                                        | 5               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Fut|Voice=Act|Person=2                 | 4               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 3               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 3               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Sup|Gend=MascNeut                        | 3               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 3               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Neut                                    | 2               |
|                                                                    |              | Case=Voc|Numb=Sing|Deg=Pos|Gend=Masc                            | 2               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=Masc                                    | 1               |
|                                                                    |              | Case=Loc|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Voc|Numb=Sing|Gend=Masc                                    | 1               |
|                                                                    |              | Mood=SupUm|Tense=_|Voice=Act                                    | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=MascNeut    | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Dep|Gend=Masc      | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=MascNeut                                | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Pass                                  | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Act|Person=3                | 1               |
|                                                                    |              | Numb=Plur|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Case=Abl|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Masc                            | 1               |
|                                                                    |              | MORPH=EMPTY                                                     | 1               |
|                                                                    |              | Numb=Plur|Mood=Imp|Tense=Fut|Voice=Act|Person=2                 | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Fut|Voice=Pass|Person=2                | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 1               |
| Case=Acc|Numb=Plur                                                 | 1126         | Case=Nom|Numb=Plur                                              | 563             |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 261             |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Masc                            | 44              |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 40              |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 31              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 31              |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 28              |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 20              |
|                                                                    |              | Case=Voc|Numb=Plur                                              | 8               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 8               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Neut     | 7               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 7               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 7               |
|                                                                    |              | Case=Ind                                                        | 7               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 6               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 6               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 5               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 5               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 5               |
|                                                                    |              | Deg=Pos                                                         | 4               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Neut                                    | 4               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=2                 | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 2               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=2                | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Masc                                    | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=MascFem                         | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Sup|Gend=Fem                             | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=MascNeut                                | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | MORPH=EMPTY                                                     | 1               |
|                                                                    |              | Case=Dat|Numb=Plur|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 1               |
|                                                                    |              | Case=Dat|Numb=Plur|Gend=Com                                     | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Abl|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Case=Gen|Numb=Plur                                              | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 1               |
| Case=Dat|Numb=Sing                                                 | 797          | Case=Gen|Numb=Sing                                              | 184             |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 124             |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 122             |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 75              |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 56              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=3                 | 38              |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 26              |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Neut                                    | 23              |
|                                                                    |              | MORPH=EMPTY                                                     | 23              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=1                | 21              |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Pass                                  | 15              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 9               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=2                | 7               |
|                                                                    |              | Case=Dat|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 6               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=MascNeut                                | 6               |
|                                                                    |              | Case=Loc|Numb=Sing                                              | 6               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Fut|Voice=Act|Person=3                 | 5               |
|                                                                    |              | Case=Voc|Numb=Plur                                              | 4               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 4               |
|                                                                    |              | Case=Ind                                                        | 4               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=2                 | 3               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 3               |
|                                                                    |              | Case=Abl|Numb=Plur|Gend=Com                                     | 3               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 2               |
|                                                                    |              | Case=Dat|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 2               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Impa|Voice=Act|Person=3                | 2               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 2               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Dep                                   | 2               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Com                             | 2               |
|                                                                    |              | Case=Voc|Numb=Sing|Gend=Masc                                    | 1               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Deg=Sup                                                         | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=1                 | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Dat|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Neut                                    | 1               |
| Numb=Sing|Mood=Ind|Tense=Impa|Voice=Act|Person=3                   | 646          | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 577             |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Impa|Voice=Act|Person=3                | 29              |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 7               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 6               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 5               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=3                 | 4               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 4               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=3                | 3               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pqp|Voice=Act|Person=3                 | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pqp|Voice=Pass|Person=3|Gend=Fem       | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Fem                                     | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
| Deg=Pos                                                            | 580          | MORPH=EMPTY                                                     | 135             |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 61              |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 40              |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 34              |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 29              |
|                                                                    |              | Case=Abl|Numb=Sing|Gend=MascNeut                                | 25              |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 16              |
|                                                                    |              | Case=Ind                                                        | 15              |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 14              |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 14              |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 10              |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 10              |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=MascNeut                                | 9               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 9               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Fem                                     | 9               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 8               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 8               |
|                                                                    |              | Deg=Comp                                                        | 8               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 7               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 7               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Neut                            | 7               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 7               |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=Com                                     | 6               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 6               |
|                                                                    |              | Deg=Sup                                                         | 5               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 5               |
|                                                                    |              | Case=Abl|Numb=Sing|Gend=Fem                                     | 5               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 4               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=Neut                                    | 4               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 4               |
|                                                                    |              | Case=Abl|Numb=Plur|Gend=Com                                     | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Neut                                    | 3               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 3               |
|                                                                    |              | Case=Voc|Numb=Sing|Deg=Pos|Gend=Masc                            | 3               |
|                                                                    |              | Numb=Plur|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 2               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 2               |
|                                                                    |              | Mood=Inf|Tense=Perf|Voice=Act                                   | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Com                             | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=MascNeut                                | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Case=Dat|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 2               |
|                                                                    |              | Case=Ind|Deg=Pos                                                | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Numb=Plur|Mood=Imp|Tense=Fut|Voice=Act|Person=2                 | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Masc                                    | 1               |
|                                                                    |              | Case=Voc|Numb=Sing|Gend=Masc                                    | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascFem                         | 1               |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=MascNeut                                | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Pass|Person=3               | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=1                | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Impa|Voice=Act|Person=3                | 1               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Fut|Voice=Act|Person=2                 | 1               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Gen|Numb=Plur                                              | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Pass                                  | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
| Case=Gen|Numb=Sing                                                 | 573          | Case=Nom|Numb=Sing                                              | 115             |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 112             |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 110             |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 43              |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 36              |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 20              |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 16              |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=Fem                             | 13              |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Pass                                  | 12              |
|                                                                    |              | Case=Loc|Numb=Sing                                              | 9               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 8               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Masc                            | 7               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=1                | 6               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 6               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 4               |
|                                                                    |              | Case=Abl|Numb=Plur                                              | 4               |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=Com                                     | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 3               |
|                                                                    |              | Case=Ind                                                        | 3               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Masc                            | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=2                | 3               |
|                                                                    |              | Case=Abl|Numb=Plur|Deg=Pos|Gend=Com                             | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 2               |
|                                                                    |              | Case=Voc|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=MascFem                         | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Com                             | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Pass|Person=2               | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=3                | 1               |
|                                                                    |              | Deg=Pos                                                         | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=2                | 1               |
|                                                                    |              | Deg=Sup                                                         | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Comp|Gend=Neut                           | 1               |
|                                                                    |              | Case=Gen|Numb=Plur|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Case=Voc|Numb=Sing|Deg=Sup|Gend=Masc                            | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Sup|Gend=Fem                             | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
|                                                                    |              | Case=Dat|Numb=Plur|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Gend=MascNeut                                | 1               |
|                                                                    |              | Case=Abl|Numb=Plur|Gend=Com                                     | 1               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Fut|Voice=Act|Person=2                 | 1               |
| Case=Nom|Numb=Plur                                                 | 459          | Case=Acc|Numb=Plur                                              | 200             |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 87              |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 65              |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 20              |
|                                                                    |              | Case=Voc|Numb=Plur                                              | 10              |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Pass                                  | 8               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 7               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 5               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 5               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 5               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 4               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 4               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 4               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 4               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Masc                            | 3               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=MascFem                         | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Case=Loc|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=1                | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 2               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pqp|Voice=Pass|Person=3|Gend=Fem       | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Masc      | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Neut     | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 1               |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=Com                                     | 1               |
|                                                                    |              | Deg=Pos                                                         | 1               |
| Case=Nom|Numb=Sing|Gend=Fem                                        | 418          | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 230             |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 134             |
|                                                                    |              | Deg=Pos                                                         | 10              |
|                                                                    |              | Case=Abl|Numb=Sing|Gend=Fem                                     | 8               |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=Com                                     | 7               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Neut                                    | 5               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 4               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 4               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 4               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Case=Voc|Numb=Sing|Deg=Pos|Gend=Masc                            | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=MascFem                                 | 1               |
| Case=Abl|Numb=Plur                                                 | 362          | Case=Dat|Numb=Plur                                              | 171             |
|                                                                    |              | Case=Abl|Numb=Plur|Deg=Pos|Gend=Com                             | 47              |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 33              |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 23              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 21              |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 14              |
|                                                                    |              | Case=Dat|Numb=Plur|Deg=Pos|Gend=Com                             | 11              |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 6               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 5               |
|                                                                    |              | Case=Abl|Numb=Plur|Gend=Com                                     | 5               |
|                                                                    |              | Case=Abl|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Com      | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 2               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Dat|Numb=Plur|Gend=Com                                     | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=SemDep|Person=2             | 1               |
|                                                                    |              | Case=Abl|Numb=Plur|Mood=Adj|Tense=_|Voice=Pass|Gend=Com         | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
|                                                                    |              | Case=Ind                                                        | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=3                | 1               |
|                                                                    |              | Case=Abl|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Deg=Pos                                                         | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 1               |
| Numb=Sing|Mood=Sub|Tense=Impa|Voice=Act|Person=3                   | 358          | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 198             |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 104             |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 19              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=3                 | 18              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 8               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 2               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Impa|Voice=Act|Person=3                | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=Fem       | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=3                | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Impa|Voice=Act|Person=3                | 1               |
| Case=Dat|Numb=Plur                                                 | 358          | Case=Abl|Numb=Plur                                              | 242             |
|                                                                    |              | Case=Dat|Numb=Plur|Deg=Pos|Gend=Com                             | 33              |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 30              |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 20              |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 10              |
|                                                                    |              | Case=Abl|Numb=Plur|Deg=Pos|Gend=Com                             | 6               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 4               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 4               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Case=Dat|Numb=Plur|Gend=Com                                     | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Neut                                    | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 1               |
| Case=Abl|Numb=Sing|Gend=Fem                                        | 332          | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 69              |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Fem                                     | 66              |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 60              |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 51              |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 18              |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Neut                                    | 10              |
|                                                                    |              | Deg=Pos                                                         | 9               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 5               |
|                                                                    |              | MORPH=EMPTY                                                     | 5               |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=Com                                     | 4               |
|                                                                    |              | Case=Abl|Numb=Plur|Gend=Com                                     | 4               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 4               |
|                                                                    |              | Gend=Fem                                                        | 3               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Com                             | 3               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 2               |
|                                                                    |              | Case=Ind                                                        | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 2               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 1               |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=Fem                                     | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=2                | 1               |
| Case=Acc|Numb=Sing|Gend=Fem                                        | 327          | Case=Acc|Numb=Sing|Deg=Pos|Gend=Fem                             | 180             |
|                                                                    |              | MORPH=EMPTY                                                     | 35              |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=Com                                     | 29              |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 21              |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=MascNeut                                | 21              |
|                                                                    |              | Case=Abl|Numb=Sing|Gend=Fem                                     | 7               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=Masc                                    | 7               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Fem                                     | 4               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 3               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 3               |
|                                                                    |              | Deg=Pos                                                         | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascFem                         | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Neut                                    | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Fem                                     | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=Neut                                    | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 1               |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=Fem                                     | 1               |
|                                                                    |              | Gend=Fem                                                        | 1               |
|                                                                    |              | Case=Ind                                                        | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Gend=MascNeut                                | 1               |
| Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                               | 312          | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 144             |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 44              |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 43              |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 24              |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 21              |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 10              |
|                                                                    |              | Deg=Pos                                                         | 7               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 5               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 3               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=Neut      | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascFem                         | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Neut     | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Neut     | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=3                 | 1               |
| Case=Acc|Numb=Sing|Gend=Neut                                       | 311          | Case=Nom|Numb=Sing|Gend=Neut                                    | 186             |
|                                                                    |              | MORPH=EMPTY                                                     | 51              |
|                                                                    |              | Case=Abl|Numb=Sing|Gend=MascNeut                                | 19              |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=MascNeut                                | 16              |
|                                                                    |              | Deg=Pos                                                         | 13              |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 9               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 5               |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=Com                                     | 2               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=MascNeut                                | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=Masc                                    | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=MascFem                                 | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=MascFem                                 | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 1               |
| Case=Acc|Numb=Sing                                                 | 309          | Case=Nom|Numb=Sing                                              | 106             |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 36              |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 19              |
|                                                                    |              | Case=Gen|Numb=Plur                                              | 15              |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 14              |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Fem                             | 12              |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascFem                         | 11              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 8               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 7               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 6               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=MascNeut                                | 5               |
|                                                                    |              | Deg=Sup                                                         | 5               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 5               |
|                                                                    |              | Deg=Pos                                                         | 4               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 4               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Neut                            | 4               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 4               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=MascNeut | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 3               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=MascFem                                 | 2               |
|                                                                    |              | MORPH=EMPTY                                                     | 2               |
|                                                                    |              | Case=Ind                                                        | 2               |
|                                                                    |              | Case=Abl|Numb=Plur                                              | 2               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Fut|Voice=Act|Person=2                 | 2               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 2               |
|                                                                    |              | Deg=Comp                                                        | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=Masc                                    | 2               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 2               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Gend=Fem                                     | 1               |
|                                                                    |              | Case=Voc|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Gend=MascNeut                                | 1               |
|                                                                    |              | Case=Gen|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=1                | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=1                 | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | morph                                                           | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=Neut        | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Neut      | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Neut                                    | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=MascNeut  | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Sup|Gend=MascNeut                        | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Pass|Person=1               | 1               |
| Case=Nom|Numb=Sing|Gend=Neut                                       | 272          | Case=Acc|Numb=Sing|Gend=Neut                                    | 163             |
|                                                                    |              | MORPH=EMPTY                                                     | 33              |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=MascNeut                                | 20              |
|                                                                    |              | Deg=Pos                                                         | 16              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 10              |
|                                                                    |              | Case=Abl|Numb=Sing|Gend=MascNeut                                | 8               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 5               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=MascFem                                 | 3               |
|                                                                    |              | Case=Gen|Numb=Sing|Gend=MascNeut                                | 3               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=Masc                                    | 2               |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=Com                                     | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 1               |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=MascNeut                                | 1               |
|                                                                    |              | Case=Gen|Numb=Plur                                              | 1               |
|                                                                    |              | Deg=Comp                                                        | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
| Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                                | 271          | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 184             |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 20              |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 14              |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 12              |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 9               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 8               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 7               |
|                                                                    |              | Case=Ind                                                        | 5               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 3               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 3               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Com                             | 2               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Fem       | 1               |
| Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=3                   | 261          | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 255             |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 2               |
|                                                                    |              | Case=Abl|Numb=Plur|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 1               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
| Case=Nom|Numb=Plur|Gend=Neut                                       | 259          | Case=Acc|Numb=Plur|Gend=Neut                                    | 138             |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Fem                                     | 41              |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 29              |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 15              |
|                                                                    |              | Case=Ind                                                        | 6               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 5               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Fem                                     | 4               |
|                                                                    |              | Case=Abl|Numb=Sing|Gend=Fem                                     | 4               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 3               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=MascNeut                                | 2               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 2               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 2               |
|                                                                    |              | Deg=Pos                                                         | 2               |
|                                                                    |              | Gend=Fem                                                        | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Neut     | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Gend=MascNeut                                | 1               |
| Case=Abl|Numb=Plur|Deg=Pos|Gend=Com                                | 240          | Case=Dat|Numb=Plur|Deg=Pos|Gend=Com                             | 108             |
|                                                                    |              | Case=Abl|Numb=Plur                                              | 52              |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 12              |
|                                                                    |              | Case=Abl|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Com      | 10              |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 9               |
|                                                                    |              | Case=Dat|Numb=Plur                                              | 9               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 7               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 5               |
|                                                                    |              | Deg=Pos                                                         | 4               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 4               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 3               |
|                                                                    |              | Case=Abl|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 3               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 2               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 2               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Case=Voc|Numb=Plur                                              | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Abl|Numb=Plur|Gend=Com                                     | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Masc                            | 1               |
| Numb=Sing|Mood=Sub|Tense=Pqp|Voice=Act|Person=3                    | 236          | Mood=Inf|Tense=Perf|Voice=Act                                   | 97              |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 48              |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pqp|Voice=Act|Person=3                 | 46              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=3                | 29              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 7               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=3                 | 3               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pqp|Voice=Act|Person=2                 | 2               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 1               |
| Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                           | 208          | Case=Acc|Numb=Sing                                              | 112             |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 62              |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Neut                            | 10              |
|                                                                    |              | Case=Gen|Numb=Plur                                              | 4               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 4               |
|                                                                    |              | Case=Ind                                                        | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 2               |
|                                                                    |              | Deg=Pos                                                         | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=MascNeut                                | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Fem       | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Fut|Voice=Act|Person=2                 | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
| Case=Acc|Numb=Plur|Deg=Pos|Gend=Fem                                | 202          | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 74              |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 68              |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 11              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 11              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 9               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Masc                            | 9               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 2               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 2               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Abl|Numb=Plur|Deg=Pos|Gend=Com                             | 2               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Case=Voc|Numb=Sing|Deg=Pos|Gend=Masc                            | 1               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Dat|Numb=Plur|Deg=Pos|Gend=Com                             | 1               |
| Case=Gen|Numb=Plur|Gend=MascNeut                                   | 200          | Case=Gen|Numb=Plur                                              | 164             |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 17              |
|                                                                    |              | Case=Gen|Numb=Plur|Deg=Pos|Gend=Com                             | 7               |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=Com                                     | 3               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=MascNeut                                | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Gend=MascNeut                                | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Masc                                    | 1               |
|                                                                    |              | Case=Abl|Numb=Plur|Gend=MascNeut                                | 1               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 1               |
|                                                                    |              | Deg=Pos                                                         | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 1               |
|                                                                    |              | Case=Abl|Numb=Plur|Gend=Com                                     | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Neut                                    | 1               |
| Case=Acc|Numb=Plur|Gend=Fem                                        | 194          | Case=Acc|Numb=Plur|Gend=Masc                                    | 42              |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 35              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 25              |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Fem                                     | 19              |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 11              |
|                                                                    |              | Case=Abl|Numb=Plur|Gend=Com                                     | 11              |
|                                                                    |              | Deg=Pos                                                         | 7               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 6               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Fem                                     | 5               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 5               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 5               |
|                                                                    |              | Case=Ind                                                        | 4               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=2                | 4               |
|                                                                    |              | MORPH=EMPTY                                                     | 3               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Fem                             | 3               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Fut|Voice=Act|Person=2                 | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Gend=Fem                                     | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=MascNeut                                | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 1               |
| Numb=Plur|Mood=Sub|Tense=Impa|Voice=Act|Person=3                   | 188          | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 154             |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 21              |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 7               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 3               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Impa|Voice=Act|Person=3                | 2               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
| Case=Acc|Numb=Sing|Gend=MascNeut                                   | 184          | Case=Acc|Numb=Sing                                              | 56              |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 28              |
|                                                                    |              | Deg=Pos                                                         | 24              |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Neut                                    | 23              |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=Com                                     | 10              |
|                                                                    |              | Case=Gen|Numb=Plur                                              | 7               |
|                                                                    |              | Case=Gen|Numb=Sing|Gend=MascNeut                                | 6               |
|                                                                    |              | MORPH=EMPTY                                                     | 6               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=Masc                                    | 6               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 5               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=Neut                                    | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Gend=MascNeut                                | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascFem                         | 1               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Fut|Voice=Act|Person=2                 | 1               |
|                                                                    |              | Case=Ind                                                        | 1               |
| Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                               | 174          | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 70              |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 44              |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 31              |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 7               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Neut     | 6               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 6               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 3               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 1               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 1               |
|                                                                    |              | Deg=Pos                                                         | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
| Case=Nom|Numb=Plur|Deg=Pos|Gend=Masc                               | 171          | Case=Nom|Numb=Plur                                              | 91              |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 15              |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 14              |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Pass                                  | 9               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 6               |
|                                                                    |              | Deg=Pos                                                         | 5               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 3               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 3               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Com                             | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 2               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Dep                                   | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Dep|Gend=Masc      | 2               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Sup|Gend=Masc                            | 1               |
|                                                                    |              | Case=Gen|Numb=Plur|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=MascFem                         | 1               |
|                                                                    |              | Deg=Sup                                                         | 1               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Masc      | 1               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=1                | 1               |
| Case=Voc|Numb=Sing                                                 | 169          | Case=Nom|Numb=Sing                                              | 116             |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 14              |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 10              |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 8               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 6               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 4               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 3               |
|                                                                    |              | Case=Voc|Numb=Sing|Deg=Pos|Gend=Masc                            | 2               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Case=Voc|Numb=Plur                                              | 1               |
|                                                                    |              | Mood=Inf|Tense=Perf|Voice=Act                                   | 1               |
| Case=Acc|Numb=Plur|Gend=Neut                                       | 158          | Case=Nom|Numb=Sing|Gend=Fem                                     | 35              |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Neut                                    | 26              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 19              |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 12              |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 11              |
|                                                                    |              | Case=Ind                                                        | 10              |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 8               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 5               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Masc                                    | 3               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 3               |
|                                                                    |              | Case=Abl|Numb=Sing|Gend=Fem                                     | 3               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Fem                                     | 3               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 3               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=MascNeut                                | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 2               |
|                                                                    |              | Case=Abl|Numb=Plur|Gend=Com                                     | 2               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=Com                                     | 1               |
|                                                                    |              | Deg=Pos                                                         | 1               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Gend=Fem                                                        | 1               |
| Mood=Inf|Tense=Pres|Voice=Dep                                      | 157          | Mood=Inf|Tense=Pres|Voice=Pass                                  | 107             |
|                                                                    |              | Deg=Pos                                                         | 12              |
|                                                                    |              | MORPH=EMPTY                                                     | 5               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 4               |
|                                                                    |              | Case=Abl|Numb=Sing|Gend=Com                                     | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=2                | 3               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 3               |
|                                                                    |              | Case=Abl|Numb=Sing|Gend=Fem                                     | 3               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 3               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=3                 | 2               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=1                | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Dep|Gend=Masc      | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Dep|Person=1                | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Masc      | 1               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Dep|Person=3                 | 1               |
| Numb=Sing|Mood=Ind|Tense=Pqp|Voice=Act|Person=3                    | 147          | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 123             |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 12              |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 5               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 3               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pqp|Voice=Act|Person=3                 | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 1               |
| Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                               | 142          | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 58              |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 20              |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Neut                            | 19              |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 10              |
|                                                                    |              | Deg=Pos                                                         | 8               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 6               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Com                             | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 3               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascFem                         | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=MascFem                         | 1               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 1               |
|                                                                    |              | Deg=Sup                                                         | 1               |
|                                                                    |              | Case=Voc|Numb=Sing|Deg=Pos|Gend=Masc                            | 1               |
|                                                                    |              | MORPH=EMPTY                                                     | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Abl|Numb=Plur|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 1               |
| Case=Nom|Numb=Plur|Gend=Masc                                       | 140          | Case=Nom|Numb=Sing|Gend=Masc                                    | 77              |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=Com                                     | 34              |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 12              |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=MascNeut                                | 7               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 3               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Masc                                    | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=Neut                                    | 2               |
|                                                                    |              | Case=Dat|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Case=Abl|Numb=Plur|Gend=Com                                     | 1               |
|                                                                    |              | Case=Voc|Numb=Plur                                              | 1               |
| Case=Abl|Numb=Sing|Gend=MascNeut                                   | 140          | Deg=Pos                                                         | 39              |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=Neut                                    | 23              |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Neut                                    | 21              |
|                                                                    |              | MORPH=EMPTY                                                     | 15              |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 9               |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=MascNeut                                | 7               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 7               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 7               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 4               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 1               |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=Com                                     | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=Neut        | 1               |
| Case=Abl|Numb=Plur|Gend=Com                                        | 135          | Case=Dat|Numb=Plur|Gend=Com                                     | 94              |
|                                                                    |              | Case=Ind                                                        | 10              |
|                                                                    |              | Case=Abl|Numb=Plur                                              | 5               |
|                                                                    |              | Case=Abl|Numb=Plur|Deg=Pos|Gend=Com                             | 5               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=MascFem                                 | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Masc                                    | 2               |
|                                                                    |              | Case=Dat|Numb=Plur|Deg=Pos|Gend=Com                             | 2               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=MascNeut                                | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Neut                                    | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Case=Dat|Numb=Plur                                              | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Pass                                  | 1               |
| Case=Abl|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Com         | 132          | Case=Abl|Numb=Plur                                              | 22              |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 19              |
|                                                                    |              | Case=Abl|Numb=Plur|Deg=Pos|Gend=Com                             | 18              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 18              |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 10              |
|                                                                    |              | Case=Dat|Numb=Plur|Deg=Pos|Gend=Com                             | 7               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 4               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 4               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 4               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 4               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 3               |
|                                                                    |              | Case=Voc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 2               |
|                                                                    |              | Case=Abl|Numb=Plur|Gend=Com                                     | 2               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=MascNeut | 2               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Case=Dat|Numb=Plur                                              | 1               |
|                                                                    |              | MORPH=EMPTY                                                     | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 1               |
| Case=Dat|Numb=Plur|Gend=Com                                        | 126          | Case=Abl|Numb=Plur|Gend=Com                                     | 99              |
|                                                                    |              | Case=Dat|Numb=Plur|Deg=Pos|Gend=Com                             | 13              |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=MascFem                                 | 7               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Ind                                                        | 1               |
|                                                                    |              | Case=Gen|Numb=Plur|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Gend=MascNeut                                | 1               |
|                                                                    |              | Case=Abl|Numb=Plur|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=MascFem                                 | 1               |
| Case=Nom|Numb=Sing|Deg=Pos|Gend=MascFem                            | 125          | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 41              |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 28              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 14              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 12              |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=MascFem                         | 7               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 3               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Neut                            | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=3                | 2               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=Com                             | 2               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 2               |
|                                                                    |              | Deg=Comp                                                        | 2               |
|                                                                    |              | Deg=Sup                                                         | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Deg=Pos                                                         | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=MascFem                                 | 1               |
|                                                                    |              | Case=Abl|Numb=Plur|Deg=Pos|Gend=Com                             | 1               |
| Numb=Plur|Mood=Ind|Tense=Perf|Voice=Act|Person=3                   | 123          | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 52              |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 25              |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Pass|Person=3               | 16              |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 11              |
|                                                                    |              | Case=Gen|Numb=Plur                                              | 7               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 4               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 2               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Fut|Voice=Act|Person=3                 | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=MascNeut                                | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 1               |
| Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem         | 119          | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 52              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 38              |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 6               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 5               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Neut     | 3               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 3               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 1               |
| Case=Acc|Numb=Plur|Deg=Pos|Gend=Masc                               | 117          | Case=Acc|Numb=Plur                                              | 61              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 16              |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 14              |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 8               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 7               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Masc                                    | 4               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Inf|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem         | 116          | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 42              |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 28              |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 10              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 9               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Neut     | 5               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 4               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 4               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 3               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 3               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Neut     | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 2               |
| Case=Gen|Numb=Sing|Deg=Pos|Gend=MascNeut                           | 116          | Case=Gen|Numb=Sing                                              | 51              |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Masc                            | 16              |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Pass                                  | 9               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 8               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=1                | 5               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=Fem                             | 3               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 2               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 2               |
|                                                                    |              | Case=Loc|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Dat|Numb=Plur|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Voc|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Neut                                    | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=Com                                     | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Loc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
| Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=Masc         | 115          | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Masc      | 28              |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 11              |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 11              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 10              |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 10              |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 7               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 6               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 5               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 5               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 4               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=3                | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=3                | 1               |
|                                                                    |              | Numb=Plur|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=Fem       | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=MascNeut  | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Masc      | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 1               |
|                                                                    |              | Case=Abl|Numb=Plur                                              | 1               |
| Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                           | 111          | Case=Abl|Numb=Sing                                              | 37              |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 14              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 11              |
|                                                                    |              | Case=Dat|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 9               |
|                                                                    |              | Deg=Pos                                                         | 9               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 8               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 7               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 7               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 2               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Ind                                                        | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 1               |
| Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=3                    | 111          | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 61              |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 27              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 21              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Pass|Person=1               | 1               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
| Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc        | 105          | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 73              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 22              |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 7               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
| Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=2                   | 104          | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 41              |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 18              |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 10              |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 8               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=2                 | 7               |
|                                                                    |              | Case=Abl|Numb=Plur                                              | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 2               |
|                                                                    |              | Case=Dat|Numb=Plur                                              | 2               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 2               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=MascFem                         | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=3                 | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=MascFem                         | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
| Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                   | 102          | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=3                | 37              |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 26              |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 20              |
|                                                                    |              | MORPH=EMPTY                                                     | 10              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=3                 | 2               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Comp|Gend=Neut                           | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pqp|Voice=Act|Person=3                 | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 1               |
| Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Neut        | 101          | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 21              |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 18              |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 17              |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Neut     | 9               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 9               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 6               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 5               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 5               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 4               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 3               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Deg=Pos                                                         | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 1               |
| Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                                | 100          | Case=Nom|Numb=Sing                                              | 26              |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 24              |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 9               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 8               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 8               |
|                                                                    |              | Case=Ind                                                        | 5               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 5               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 4               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 3               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 2               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 2               |
|                                                                    |              | Case=Abl|Numb=Plur|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Deg=Sup                                                         | 1               |
| Case=Acc|Numb=Plur|Deg=Pos|Gend=MascFem                            | 98           | Case=Acc|Numb=Plur                                              | 18              |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=MascFem                         | 18              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 12              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=MascFem                         | 10              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 8               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 6               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 6               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 5               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 4               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 4               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=2                | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=2                | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Case=Abl|Numb=Plur|Gend=Com                                     | 1               |
|                                                                    |              | Deg=Pos                                                         | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 1               |
| Case=Acc|Numb=Sing|Deg=Comp|Gend=Neut                              | 97           | Deg=Comp                                                        | 83              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Comp|Gend=Neut                           | 7               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 2               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
| Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                               | 94           | Case=Nom|Numb=Sing                                              | 69              |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 8               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 2               |
|                                                                    |              | Deg=Pos                                                         | 2               |
|                                                                    |              | Deg=Comp                                                        | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Voc|Numb=Sing|Deg=Pos|Gend=Masc                            | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Fut|Voice=Act|Gend=Masc       | 1               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Masc                            | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
| Case=Gen|Numb=Plur                                                 | 93           | Case=Acc|Numb=Sing                                              | 51              |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 5               |
|                                                                    |              | Case=Gen|Numb=Sing|Gend=MascNeut                                | 4               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 3               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 3               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 3               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Ind                                                        | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=MascNeut                                | 2               |
|                                                                    |              | Case=Gen|Numb=Plur|Deg=Pos|Gend=Com                             | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 2               |
|                                                                    |              | Case=Abl|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Neut                                    | 2               |
|                                                                    |              | Deg=Sup                                                         | 2               |
|                                                                    |              | Case=Gen|Numb=Plur|Gend=Fem                                     | 1               |
|                                                                    |              | Case=Gen|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Case=Dat|Numb=Plur|Gend=Com                                     | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Gend=MascNeut                                | 1               |
|                                                                    |              | Case=Gen|Numb=Plur|Deg=Pos|Gend=MascNeut                        | 1               |
| Case=Dat|Numb=Plur|Deg=Pos|Gend=Com                                | 93           | Case=Abl|Numb=Plur|Deg=Pos|Gend=Com                             | 43              |
|                                                                    |              | Case=Abl|Numb=Plur                                              | 9               |
|                                                                    |              | Case=Dat|Numb=Plur                                              | 7               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 5               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 4               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 4               |
|                                                                    |              | Case=Abl|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Com      | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 3               |
|                                                                    |              | Case=Abl|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 2               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=MascFem                         | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Case=Dat|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
| Case=Nom|Numb=Sing|Deg=Comp|Gend=Neut                              | 89           | Deg=Comp                                                        | 65              |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 10              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 7               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 4               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Comp|Gend=Neut                           | 2               |
|                                                                    |              | Deg=Sup                                                         | 1               |
| Case=Nom|Numb=Plur|Gend=Fem                                        | 89           | Case=Nom|Numb=Plur|Gend=Neut                                    | 20              |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 20              |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 13              |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Fem                                     | 8               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 6               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Fem                             | 5               |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=Fem                                     | 4               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 4               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 3               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Fem                                     | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=MascFem                         | 1               |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=Com                                     | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Sup|Gend=Fem                             | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Gend=Fem                                     | 1               |
| Case=Gen|Numb=Sing|Gend=Com                                        | 87           | Case=Dat|Numb=Sing|Gend=Com                                     | 44              |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 21              |
|                                                                    |              | Case=Abl|Numb=Plur|Gend=Com                                     | 5               |
|                                                                    |              | Deg=Comp                                                        | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=MascFem                                 | 2               |
|                                                                    |              | Case=Gen|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Gend=MascNeut                                | 2               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=MascNeut                                | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 1               |
|                                                                    |              | Case=Dat|Numb=Plur|Gend=Com                                     | 1               |
|                                                                    |              | Case=Ind                                                        | 1               |
| Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=MascNeut    | 87           | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 23              |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 21              |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 18              |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 9               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 4               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 2               |
|                                                                    |              | Case=Gen|Numb=Sing|Gend=MascNeut                                | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
|                                                                    |              | Deg=Sup                                                         | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
| Numb=Plur|Mood=Ind|Tense=Impa|Voice=Act|Person=3                   | 86           | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 76              |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 4               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=MascNeut                                | 4               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 2               |
| Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem         | 85           | Case=Acc|Numb=Plur                                              | 29              |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 10              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 10              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 8               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 6               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 5               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 5               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 3               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 2               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Abl|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Com      | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
| Case=Acc|Numb=Sing|Deg=Sup|Gend=MascNeut                           | 85           | Deg=Sup                                                         | 30              |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 22              |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 12              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Sup|Gend=Masc                            | 11              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 6               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Sup|Gend=Fem                             | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Sup|Gend=Fem                             | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascFem                         | 1               |
| Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=1                   | 84           | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=1                 | 39              |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 14              |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 10              |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 4               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Fem                             | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=1                | 3               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=Masc                                    | 2               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Pass                                  | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascFem                         | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Sup|Gend=Masc                            | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
| Case=Acc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut    | 83           | Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=MascNeut | 24              |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 19              |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 18              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 11              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 4               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Neut     | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
| Case=Acc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem         | 81           | Case=Acc|Numb=Sing|Deg=Pos|Gend=Fem                             | 33              |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 24              |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 6               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=Fem      | 4               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 3               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 3               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=MascNeut | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
| Case=Gen|Numb=Sing|Gend=Fem                                        | 78           | Case=Dat|Numb=Sing|Gend=Fem                                     | 31              |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=Fem                             | 28              |
|                                                                    |              | Case=Gen|Numb=Sing|Gend=MascNeut                                | 6               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=Com                                     | 2               |
|                                                                    |              | morph                                                           | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Neut                                    | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Fem                                     | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Case=Nom|Numb=Plur|Deg=Pos|Gend=Fem                                | 77           | Case=Nom|Numb=Plur                                              | 33              |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=Fem                             | 20              |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 14              |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 1               |
| Numb=Sing|Mood=Ind|Tense=Impa|Voice=Pass|Person=3                  | 77           | Case=Nom|Numb=Sing                                              | 27              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Pass|Person=3               | 19              |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 13              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 6               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Impa|Voice=Pass|Person=3               | 6               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 2               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
|                                                                    |              | Deg=Sup                                                         | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 1               |
| Case=Abl|Numb=Sing|Deg=Pos|Gend=Com                                | 74           | Case=Abl|Numb=Sing                                              | 11              |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 10              |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 7               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 7               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 6               |
|                                                                    |              | Case=Dat|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 4               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 3               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Masc                            | 3               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Pass                                  | 3               |
|                                                                    |              | Deg=Pos                                                         | 3               |
|                                                                    |              | Case=Dat|Numb=Sing|Deg=Pos|Gend=Com                             | 3               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=1                | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Sup|Gend=Masc                            | 1               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                   | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascFem                         | 1               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 1               |
| Case=Acc|Numb=Plur|Gend=MascFem                                    | 73           | Case=Nom|Numb=Plur|Gend=MascFem                                 | 20              |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=MascFem                                 | 15              |
|                                                                    |              | Case=Ind                                                        | 8               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 7               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=MascFem                         | 6               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 3               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 3               |
|                                                                    |              | morph                                                           | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Masc                                    | 2               |
|                                                                    |              | Case=Abl|Numb=Plur|Gend=Com                                     | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Fem                                     | 1               |
|                                                                    |              | Case=Dat|Numb=Plur|Gend=Com                                     | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=Masc                                    | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=MascNeut                                | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Neut                                    | 1               |
| Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem         | 73           | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 32              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 22              |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 6               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 2               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 2               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Neut     | 1               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
| Case=Gen|Numb=Sing|Gend=MascNeut                                   | 73           | Case=Gen|Numb=Sing                                              | 60              |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 6               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 3               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Neut                                    | 1               |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=Com                                     | 1               |
| Case=Dat|Numb=Sing|Deg=Pos|Gend=MascNeut                           | 72           | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 46              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 6               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 6               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 5               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 2               |
|                                                                    |              | Deg=Pos                                                         | 1               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
| Case=Gen|Numb=Plur|Deg=Pos|Gend=MascNeut                           | 72           | Case=Gen|Numb=Plur                                              | 66              |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 4               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Case=Gen|Numb=Plur|Deg=Pos|Gend=Fem                             | 1               |
| Case=Gen|Numb=Sing|Deg=Pos|Gend=Com                                | 70           | Case=Acc|Numb=Plur|Deg=Pos|Gend=MascFem                         | 16              |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 13              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 8               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=MascFem                         | 7               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=MascFem                         | 5               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 3               |
|                                                                    |              | Case=Gen|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 2               |
|                                                                    |              | Case=Abl|Numb=Plur|Deg=Pos|Gend=Com                             | 2               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Dat|Numb=Plur|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Comp|Gend=Neut                           | 1               |
|                                                                    |              | Case=Gen|Numb=Plur|Deg=Pos|Gend=Com                             | 1               |
| Case=Voc|Numb=Plur                                                 | 69           | Case=Nom|Numb=Plur                                              | 30              |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 18              |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 9               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 6               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 1               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
| Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut        | 69           | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 36              |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 7               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 6               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 6               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Neut     | 5               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 4               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 2               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
| Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                   | 68           | Case=Nom|Numb=Sing                                              | 20              |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 10              |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=2                | 6               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 5               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 5               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 4               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=2                 | 4               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 2               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 2               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 1               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
| Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc        | 67           | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 29              |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Pass                                  | 9               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 6               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Masc                            | 3               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=1                | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=2                | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Case=Abl|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Com      | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Masc      | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=1|Gend=Masc     | 1               |
| Case=Acc|Numb=Sing|Deg=Pos|Gend=Fem                                | 67           | Case=Acc|Numb=Sing                                              | 47              |
|                                                                    |              | Case=Ind                                                        | 10              |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 4               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 1               |
| Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut        | 67           | Case=Acc|Numb=Sing                                              | 25              |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=MascNeut | 13              |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 8               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 7               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 4               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 2               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 1               |
| Case=Acc|Numb=Sing|Deg=Pos|Gend=MascFem                            | 66           | Case=Acc|Numb=Sing                                              | 53              |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 6               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Par|Tense=Pres|Voice=Dep|Gend=MascFem   | 1               |
| Numb=Sing|Mood=Sub|Tense=Impa|Voice=Pass|Person=3                  | 65           | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Pass|Person=3               | 27              |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 26              |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 6               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 4               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Pass|Person=3               | 1               |
| Case=Abl|Numb=Sing|Deg=Sup|Gend=Fem                                | 64           | Case=Nom|Numb=Sing|Deg=Sup|Gend=Fem                             | 23              |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 20              |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 6               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 5               |
|                                                                    |              | Deg=Sup                                                         | 4               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
| Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                                | 63           | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 29              |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 24              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Neut                            | 2               |
|                                                                    |              | Case=Voc|Numb=Sing|Deg=Pos|Gend=Com                             | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Masc                            | 1               |
| Case=Acc|Numb=Sing|Deg=Comp|Gend=MascFem                           | 62           | Case=Acc|Numb=Sing                                              | 23              |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascFem                         | 16              |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Comp|Gend=Com                            | 11              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Comp|Gend=MascFem                        | 4               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 4               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Dep|Gend=Com       | 1               |
|                                                                    |              | Deg=Sup                                                         | 1               |
| Case=Acc|Numb=Sing|Deg=Pos|Gend=Neut                               | 61           | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 28              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 7               |
|                                                                    |              | Deg=Pos                                                         | 5               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascFem                         | 2               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Deg=Comp                                                        | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
| Case=Nom|Numb=Sing|Deg=Sup|Gend=Neut                               | 57           | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 28              |
|                                                                    |              | Deg=Sup                                                         | 18              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Sup|Gend=Masc                            | 3               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 3               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Sup|Gend=MascNeut                        | 2               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
| Numb=Plur|Mood=Ind|Tense=Pres|Voice=Dep|Person=3                   | 56           | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Pass|Person=3               | 45              |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Dep|Person=3                | 9               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 2               |
| Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=1                    | 55           | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 20              |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 12              |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 11              |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Fem                             | 4               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Pass                                  | 2               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 2               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Act|Person=3                | 1               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 1               |
| Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1                   | 55           | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 12              |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 6               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 6               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 5               |
|                                                                    |              | Deg=Pos                                                         | 4               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 3               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Pass                                  | 3               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 2               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Case=Dat|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | MORPH=EMPTY                                                     | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Fem       | 1               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
|                                                                    |              | Deg=Sup                                                         | 1               |
| Case=Gen|Numb=Sing|Deg=Pos|Gend=Fem                                | 55           | Case=Gen|Numb=Sing                                              | 16              |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 9               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Fem                             | 9               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 8               |
|                                                                    |              | Case=Ind                                                        | 5               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 4               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 3               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                   | 54           | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 49              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=3                 | 3               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
| Case=Ind                                                           | 52           | Case=Acc|Numb=Sing                                              | 11              |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 11              |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 5               |
|                                                                    |              | Case=Abl|Numb=Plur|Gend=Com                                     | 5               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 4               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=MascFem                                 | 4               |
|                                                                    |              | Deg=Pos                                                         | 4               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 3               |
|                                                                    |              | MORPH=EMPTY                                                     | 1               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 1               |
|                                                                    |              | Numb=Plur|Mood=Imp|Tense=Fut|Voice=Act|Person=2                 | 1               |
|                                                                    |              | Case=Gen|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Dat|Numb=Plur                                              | 1               |
| Numb=Sing|Mood=Sub|Tense=Impa|Voice=Dep|Person=3                   | 52           | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Dep|Person=3                | 13              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=3                | 10              |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 9               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 6               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 4               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Com                             | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Dep|Person=3                 | 3               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=Fem       | 1               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Dep|Person=3                | 1               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 1               |
| Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc        | 51           | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 28              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 13              |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 5               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 3               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
| Case=Gen|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com          | 51           | Case=Acc|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 19              |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 16              |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 6               |
|                                                                    |              | Case=Dat|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 3               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Abl|Numb=Plur|Gend=Com                                     | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
| Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=2                    | 49           | Case=Nom|Numb=Sing                                              | 9               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 6               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=2                | 5               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=2                | 5               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 4               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=3                 | 4               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=2                | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 2               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 2               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Pass                                  | 2               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=1                | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 1               |
| Case=Acc|Numb=Sing|Deg=Sup|Gend=Fem                                | 49           | Case=Acc|Numb=Sing|Deg=Pos|Gend=Fem                             | 18              |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 15              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Sup|Gend=Fem                             | 6               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Sup|Gend=MascNeut                        | 3               |
|                                                                    |              | Deg=Sup                                                         | 2               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Sup|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Ind                                                        | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Sup|Gend=MascNeut                        | 1               |
| Numb=Sing|Mood=Ind|Tense=Impa|Voice=Act|Person=1                   | 49           | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=1                 | 31              |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 8               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 7               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Impa|Voice=Act|Person=1                | 2               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pqp|Voice=Act|Person=1                 | 1               |
| Numb=Sing|Mood=Ind|Tense=Impa|Voice=Act|Person=2                   | 49           | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=2                 | 14              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 7               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 6               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 4               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 3               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=2                | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 2               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 2               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pqp|Voice=Act|Person=2                 | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Pass|Person=1                | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pqp|Voice=Act|Person=1                 | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Dep|Person=1                 | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
| Case=Acc|Numb=Plur|Deg=Sup|Gend=Masc                               | 49           | Case=Acc|Numb=Plur|Deg=Pos|Gend=Masc                            | 23              |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Masc                                    | 15              |
|                                                                    |              | Deg=Sup                                                         | 5               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Inf|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Sup|Gend=Fem                             | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Sup|Gend=Masc                            | 1               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
| Case=Dat|Numb=Sing|Gend=MascNeut                                   | 48           | Case=Dat|Numb=Sing                                              | 23              |
|                                                                    |              | Case=Abl|Numb=Sing|Gend=MascNeut                                | 21              |
|                                                                    |              | Case=Gen|Numb=Sing|Gend=MascNeut                                | 1               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Case=Dat|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
| Case=Dat|Numb=Sing|Deg=Pos|Gend=Fem                                | 47           | Case=Gen|Numb=Sing|Deg=Pos|Gend=Fem                             | 24              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 5               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 5               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Case=Gen|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pqp|Voice=Dep|Person=3|Gend=Fem        | 1               |
| Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Neut        | 47           | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 11              |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 9               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 7               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 6               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 4               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Neut     | 4               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
| Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Masc         | 47           | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 10              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 8               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 6               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 6               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=Masc      | 3               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
| Numb=Sing|Mood=Ind|Tense=Pres|Voice=Pass|Person=3                  | 45           | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 15              |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 14              |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Pass|Person=3               | 7               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Pass|Person=3               | 4               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=3                | 1               |
| Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=1                   | 45           | Mood=Inf|Tense=Pres|Voice=Pass                                  | 29              |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 6               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 5               |
|                                                                    |              | Deg=Pos                                                         | 2               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 1               |
| Case=Nom|Numb=Plur|Deg=Pos|Gend=MascFem                            | 44           | Case=Nom|Numb=Plur                                              | 17              |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=MascFem                         | 8               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 7               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 1               |
|                                                                    |              | Case=Voc|Numb=Plur|Deg=Pos|Gend=MascFem                         | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=MascFem                         | 1               |
|                                                                    |              | Deg=Pos                                                         | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascFem                         | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
| Case=Acc|Numb=Plur|Deg=Sup|Gend=Neut                               | 43           | Case=Nom|Numb=Sing|Deg=Sup|Gend=Fem                             | 18              |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 9               |
|                                                                    |              | Deg=Sup                                                         | 8               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Sup|Gend=Masc                            | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Sup|Gend=Neut                            | 1               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Dat|Numb=Sing|Deg=Sup|Gend=Fem                             | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 1               |
| Case=Acc|Numb=Plur|Mood=Adj|Tense=_|Voice=Pass|Gend=Neut           | 43           | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 12              |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                   | 11              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 6               |
|                                                                    |              | Case=Gen|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                   | 3               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=Fem         | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=Fem         | 1               |
|                                                                    |              | Case=Dat|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=Fem         | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=MascNeut    | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
| Numb=Sing|Mood=Sub|Tense=Impa|Voice=Act|Person=2                   | 43           | Mood=Inf|Tense=Pres|Voice=Act                                   | 17              |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=2                | 14              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=2                 | 5               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=3                 | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Fut|Voice=Act|Gend=Masc       | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=MascFem                         | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 1               |
| Numb=Sing|Mood=Ind|Tense=Impa|Voice=Dep|Person=3                   | 42           | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=3                | 20              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 8               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Impa|Voice=Dep|Person=3                | 5               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Dep|Person=3                 | 4               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=Fem       | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Pass|Person=3               | 1               |
| Case=Nom|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=Fem            | 40           | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 26              |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 9               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Adj|Tense=_|Voice=Pass|Gend=Neut        | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
| Numb=Plur|Mood=Ind|Tense=Fut|Voice=Act|Person=3                    | 39           | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 21              |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 13              |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 5               |
| Case=Abl|Numb=Plur|Deg=Sup|Gend=Com                                | 38           | Case=Abl|Numb=Plur|Deg=Pos|Gend=Com                             | 16              |
|                                                                    |              | Deg=Sup                                                         | 8               |
|                                                                    |              | Case=Dat|Numb=Plur|Deg=Sup|Gend=Com                             | 5               |
|                                                                    |              | Case=Dat|Numb=Plur|Deg=Pos|Gend=Com                             | 2               |
|                                                                    |              | Case=Abl|Numb=Plur|Gend=Com                                     | 1               |
|                                                                    |              | Case=Abl|Numb=Plur|Deg=Sup|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Abl|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Sup|Gend=Fem                             | 1               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=MascNeut                                | 1               |
| Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=Fem         | 38           | Case=Acc|Numb=Sing|Deg=Pos|Gend=Fem                             | 15              |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 10              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 4               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 3               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=MascNeut | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=1                 | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
| Numb=Plur|Mood=Sub|Tense=Impa|Voice=Pass|Person=3                  | 38           | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Pass|Person=3               | 22              |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Pass|Person=3               | 8               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 5               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Fut|Voice=Pass|Person=3                | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
| Numb=Plur|Mood=Sub|Tense=Impa|Voice=Dep|Person=3                   | 37           | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Dep|Person=3                | 20              |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Pass|Person=3               | 4               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Dep|Person=3                | 4               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Pres|Voice=Dep|Gend=Com       | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=3                | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
| Case=Dat|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Com         | 37           | Case=Abl|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Com      | 14              |
|                                                                    |              | Case=Dat|Numb=Plur|Deg=Pos|Gend=Com                             | 3               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 2               |
|                                                                    |              | Case=Dat|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=3                | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Neut     | 1               |
|                                                                    |              | Case=Abl|Numb=Plur|Gend=Com                                     | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Deg=Pos                                                         | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
| Case=Ind|Deg=Pos                                                   | 37           | Deg=Pos                                                         | 17              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 5               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 4               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 3               |
|                                                                    |              | MORPH=EMPTY                                                     | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Mood=Inf|Tense=Perf|Voice=Act                                   | 1               |
|                                                                    |              | morph                                                           | 1               |
|                                                                    |              | Case=Dat|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 1               |
| Case=Abl|Numb=Sing|Deg=Sup|Gend=MascNeut                           | 36           | Deg=Sup                                                         | 18              |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 13              |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
| Case=Voc|Numb=Sing|Deg=Pos|Gend=Fem                                | 36           | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 27              |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 4               |
|                                                                    |              | Deg=Pos                                                         | 1               |
|                                                                    |              | Case=Voc|Numb=Sing|Deg=Pos|Gend=Masc                            | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
| Case=Gen|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut    | 35           | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 10              |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 7               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 5               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 4               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Pass                                  | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=1                | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=2                | 1               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=2                | 1               |
| Case=Nom|Numb=Sing|Gend=MascFem                                    | 35           | Case=Nom|Numb=Sing|Gend=Masc                                    | 27              |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Fem                                     | 3               |
|                                                                    |              | Case=Abl|Numb=Plur|Gend=Com                                     | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=MascFem                                 | 1               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 1               |
| Case=Gen|Numb=Plur|Gend=Com                                        | 35           | Case=Gen|Numb=Plur                                              | 28              |
|                                                                    |              | Case=Gen|Numb=Plur|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=MascFem                                 | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Neut                                    | 1               |
|                                                                    |              | Case=Dat|Numb=Sing|Deg=Sup|Gend=Fem                             | 1               |
|                                                                    |              | Case=Ind                                                        | 1               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
| Case=Acc|Numb=Plur|Deg=Comp|Gend=MascFem                           | 34           | Case=Nom|Numb=Plur|Deg=Comp|Gend=MascFem                        | 12              |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 8               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=MascFem                         | 5               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 3               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 2               |
|                                                                    |              | Deg=Comp                                                        | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Comp|Gend=Neut                           | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Masc                            | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Numb=Sing|Mood=Imp|Tense=Fut|Voice=Act|Person=2                    | 34           | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 18              |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Fut|Voice=Act|Person=3                 | 6               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 3               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 3               |
|                                                                    |              | Case=Dat|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
|                                                                    |              | Deg=Pos                                                         | 1               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
| Numb=Plur|Mood=Ind|Tense=Impa|Voice=Pass|Person=3                  | 34           | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Pass|Person=3               | 30              |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Pass|Person=3               | 1               |
| Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut    | 34           | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 25              |
|                                                                    |              | Deg=Pos                                                         | 3               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Fut|Voice=Act|Person=2                 | 2               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
|                                                                    |              | Case=Dat|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
| Case=Loc|Numb=Sing                                                 | 33           | Case=Dat|Numb=Sing                                              | 10              |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 9               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 6               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 5               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 1               |
| Numb=Sing|Mood=Sub|Tense=Impa|Voice=Act|Person=1                   | 33           | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 14              |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 10              |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascFem                         | 3               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Impa|Voice=Act|Person=3                | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=1                | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pqp|Voice=Act|Person=1                 | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
| Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Neut        | 32           | Case=Acc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 7               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 6               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 4               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 4               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=MascNeut | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 2               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 1               |
| Case=Dat|Numb=Sing|Gend=Com                                        | 32           | Case=Nom|Numb=Plur|Gend=Masc                                    | 21              |
|                                                                    |              | Case=Abl|Numb=Plur|Gend=Com                                     | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Deg=Pos                                                         | 2               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Gend=Com                                     | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=MascFem                                 | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 1               |
| Numb=Sing|Mood=Ind|Tense=Fut|Voice=Pass|Person=3                   | 31           | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Pass|Person=3               | 12              |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 5               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 4               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=3                 | 3               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Fut|Voice=Pass|Person=3                | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Dep|Person=3                 | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=3                | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
| Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Dep|Gend=MascNeut     | 31           | Case=Acc|Numb=Sing                                              | 15              |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 7               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=MascNeut | 5               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Fem       | 1               |
|                                                                    |              | Case=Gen|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=MascNeut  | 1               |
| Case=Dat|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=Com          | 31           | Case=Abl|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 21              |
|                                                                    |              | Case=Dat|Numb=Plur                                              | 4               |
|                                                                    |              | Case=Dat|Numb=Plur|Deg=Pos|Gend=Com                             | 3               |
|                                                                    |              | Case=Abl|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Sup|Gend=Neut                            | 1               |
| Case=Acc|Numb=Plur|Mood=Inf|Tense=Perf|Voice=Pass|Gend=Neut        | 30           | Case=Acc|Numb=Plur                                              | 8               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 7               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 3               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 3               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 2               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 1               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Neut     | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Neut     | 1               |
| Case=Abl|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com          | 30           | Case=Abl|Numb=Sing|Deg=Pos|Gend=Com                             | 8               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 7               |
|                                                                    |              | Case=Dat|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 6               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 4               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Pres|Voice=Dep|Gend=Com       | 1               |
|                                                                    |              | Case=Gen|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
| Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=2                   | 30           | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=2                 | 15              |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 8               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 5               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=2                | 1               |
| Numb=Sing|Mood=Sub|Tense=Pqp|Voice=Pass|Person=3|Gend=Neut         | 29           | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 16              |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=MascNeut | 6               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 1               |
| Case=Acc|Numb=Plur|Mood=Inf|Tense=Perf|Voice=Pass|Gend=Masc        | 29           | Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 22              |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 3               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Masc                            | 3               |
|                                                                    |              | Deg=Pos                                                         | 1               |
| Numb=Plur|Mood=Ind|Tense=Fut|Voice=Act|Person=1                    | 29           | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 21              |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 5               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 1               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=2                 | 1               |
| Numb=Sing|Mood=Sub|Tense=Pqp|Voice=Pass|Person=3|Gend=Masc         | 29           | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 20              |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 4               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 3               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 1               |
| Case=Voc|Numb=Sing|Deg=Pos|Gend=Masc                               | 28           | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 6               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 4               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 4               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 4               |
|                                                                    |              | Deg=Pos                                                         | 3               |
|                                                                    |              | Numb=Plur|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 2               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Deg=Sup                                                         | 1               |
| Case=Acc|Numb=Plur|Deg=Comp|Gend=Neut                              | 28           | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 6               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 4               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Comp|Gend=MascFem                        | 3               |
|                                                                    |              | Deg=Comp                                                        | 3               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Com                             | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Comp|Gend=Neut                           | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Deg=Pos                                                         | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=1                | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 1               |
| Numb=Sing|Mood=Sub|Tense=Perf|Voice=Pass|Person=3|Gend=Neut        | 27           | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 16              |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 4               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=MascNeut | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 1               |
| Numb=Sing|Mood=Ind|Tense=Pres|Voice=SemDep|Person=3                | 27           | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 21              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=3                 | 3               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Fem                                     | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Pass|Person=1               | 1               |
| Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                   | 27           | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 7               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 4               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 4               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Pass                                  | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 2               |
|                                                                    |              | Deg=Pos                                                         | 2               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Neut     | 1               |
|                                                                    |              | MORPH=EMPTY                                                     | 1               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
| Numb=Sing|Mood=Sub|Tense=Pres|Voice=Pass|Person=3                  | 27           | Case=Nom|Numb=Sing                                              | 10              |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 9               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Pass|Person=3               | 4               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Pass|Person=3               | 1               |
| Case=Nom|Numb=Plur|Mood=Adj|Tense=_|Voice=Pass|Gend=Neut           | 26           | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 8               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 7               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 4               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                   | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Adj|Tense=_|Voice=Pass|Gend=Neut        | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Pass                                  | 1               |
|                                                                    |              | Deg=Pos                                                         | 1               |
| Case=Acc|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem      | 26           | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 9               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 8               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 4               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Dat|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
| Numb=Plur|Mood=Ind|Tense=Pqp|Voice=Act|Person=3                    | 26           | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 26              |
| Case=Nom|Numb=Sing|Gend=Masc                                       | 26           | Case=Nom|Numb=Sing|Gend=MascFem                                 | 8               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 8               |
|                                                                    |              | Deg=Pos                                                         | 7               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Masc                                    | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Gend=MascNeut                                | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Gend=Com                                     | 1               |
| Case=Nom|Numb=Sing|Mood=Par|Tense=Fut|Voice=Act|Gend=Fem           | 26           | Case=Nom|Numb=Sing                                              | 8               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 4               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 3               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 3               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Fut|Voice=Act|Gend=Masc       | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 1               |
| Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=1|Gend=Masc        | 25           | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 11              |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 8               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 3               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 1               |
| Case=Gen|Numb=Plur|Deg=Pos|Gend=Fem                                | 25           | Case=Gen|Numb=Plur                                              | 19              |
|                                                                    |              | Case=Gen|Numb=Plur|Gend=Fem                                     | 2               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
| Case=Acc|Numb=Plur|Mood=Inf|Tense=Perf|Voice=Pass|Gend=Fem         | 25           | Case=Acc|Numb=Plur                                              | 5               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 4               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 4               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Inf|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
| Case=Nom|Numb=Plur|Deg=Comp|Gend=Neut                              | 25           | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 8               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 7               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Comp|Gend=MascFem                        | 3               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Comp|Gend=Neut                           | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Sup|Gend=Neut                            | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Case=Nom|Numb=Plur|Deg=Sup|Gend=Masc                               | 24           | Deg=Sup                                                         | 16              |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Sup|Gend=MascNeut                        | 3               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Fut|Voice=Pass|Person=2                | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Sup|Gend=Fem                             | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=2                | 1               |
| Mood=Inf|Tense=Pres|Voice=Act                                      | 24           | Mood=Inf|Tense=Pres|Voice=Pass                                  | 15              |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Act|Person=3                | 6               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 2               |
|                                                                    |              | Case=Voc|Numb=Sing|Deg=Pos|Gend=Masc                            | 1               |
| Case=Acc|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem      | 24           | Case=Acc|Numb=Sing                                              | 19              |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascFem                         | 4               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Par|Tense=Pres|Voice=Dep|Gend=MascFem   | 1               |
| Deg=Comp                                                           | 24           | Case=Nom|Numb=Sing                                              | 8               |
|                                                                    |              | Deg=Pos                                                         | 5               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Comp|Gend=Neut                           | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 2               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Pass|Person=3               | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Comp|Gend=MascFem                        | 1               |
|                                                                    |              | Deg=Sup                                                         | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Comp|Gend=Neut                           | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
| Case=Dat|Numb=Sing|Deg=Pos|Gend=Com                                | 23           | Case=Abl|Numb=Sing|Deg=Pos|Gend=Com                             | 14              |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 4               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Deg=Pos                                                         | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
| Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                   | 23           | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=3                 | 19              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 4               |
| Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Fem          | 23           | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 9               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=Fem       | 7               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Gend=Fem                                     | 1               |
| Case=Gen|Numb=Sing|Deg=Sup|Gend=MascNeut                           | 23           | Deg=Sup                                                         | 8               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Sup|Gend=Masc                            | 4               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=2                | 2               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Sup|Gend=Fem                             | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Fut|Voice=Pass|Person=2                | 1               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Abl|Numb=Plur|Deg=Sup|Gend=Com                             | 1               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Sup|Gend=Fem                             | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
| Case=Nom|Numb=Sing|Deg=Sup|Gend=Fem                                | 23           | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 7               |
|                                                                    |              | Deg=Sup                                                         | 6               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 5               |
|                                                                    |              | Case=Ind                                                        | 2               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 1               |
| Numb=Plur|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Masc         | 23           | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Dep|Gend=Masc      | 6               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 4               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=3                | 2               |
|                                                                    |              | Case=Abl|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Com      | 1               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 1               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Perf|Voice=Dep|Person=2|Gend=Masc      | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Dep                                   | 1               |
| Case=Nom|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem      | 23           | Case=Acc|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 14              |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 5               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=MascFem                         | 4               |
| Case=Acc|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=Fem            | 22           | Case=Acc|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=MascNeut    | 9               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                   | 4               |
|                                                                    |              | Case=Gen|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                   | 3               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascFem                         | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=1                 | 1               |
| Numb=Plur|Mood=Sub|Tense=Impa|Voice=Act|Person=1                   | 22           | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 18              |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 2               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 1               |
| Numb=Sing|Mood=Ind|Tense=Pqp|Voice=Pass|Person=3|Gend=Neut         | 22           | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 12              |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 4               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
| Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=Fem          | 22           | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 9               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Fem       | 4               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
| Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Dep|Gend=Masc         | 22           | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Masc      | 9               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 2               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 2               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 2               |
|                                                                    |              | MORPH=EMPTY                                                     | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Pass                                  | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Masc                            | 1               |
| Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem         | 22           | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 18              |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 1               |
| Case=Gen|Numb=Plur|Deg=Sup|Gend=MascNeut                           | 22           | Case=Gen|Numb=Plur                                              | 17              |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Sup|Gend=MascNeut                        | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Sup|Gend=Fem                             | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Sup|Gend=Masc                            | 1               |
| Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=1                   | 21           | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 7               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Act|Person=1                | 5               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 3               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
|                                                                    |              | Deg=Sup                                                         | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
| Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=3                   | 21           | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 19              |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Pass|Person=3               | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
| Numb=Sing|Mood=Ind|Tense=Pqp|Voice=Act|Person=2                    | 21           | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 13              |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 2               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Impa|Voice=Act|Person=1                | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pqp|Voice=Act|Person=1                 | 1               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=2                 | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
| Case=Acc|Numb=Plur|Deg=Sup|Gend=Fem                                | 21           | Case=Nom|Numb=Sing|Deg=Sup|Gend=Masc                            | 7               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 4               |
|                                                                    |              | Mood=Inf|Tense=Perf|Voice=Act                                   | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Sup|Gend=Fem                             | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=MascFem                                 | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=MascFem                         | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Sup|Gend=Fem                             | 1               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 1               |
| Numb=Plur|Mood=Ind|Tense=Impa|Voice=Dep|Person=3                   | 21           | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Dep|Person=3                | 10              |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Dep|Person=3                | 4               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Pass|Person=3               | 4               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 2               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
| Case=Nom|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=Neut           | 21           | Case=Acc|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=MascNeut    | 18              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 2               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 1               |
| Case=Acc|Numb=Plur|Mood=Adj|Tense=_|Voice=Pass|Gend=Fem            | 21           | Case=Acc|Numb=Plur                                              | 7               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 4               |
|                                                                    |              | Case=Gen|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                   | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=Masc        | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=Fem         | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Adj|Tense=_|Voice=Pass|Gend=Masc        | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Masc                            | 1               |
| Mood=Inf|Tense=Pres|Voice=Pass                                     | 20           | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 7               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 5               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=1                | 2               |
|                                                                    |              | Case=Gen|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                   | 1               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
| Numb=Sing|Mood=Ind|Tense=Pqp|Voice=Pass|Person=3|Gend=Masc         | 20           | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 13              |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 6               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 1               |
| Numb=Sing|Mood=Sub|Tense=Pres|Voice=Dep|Person=1                   | 20           | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Dep|Person=1                 | 14              |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=1                | 1               |
| Case=Acc|Numb=Sing|Gend=MascFem                                    | 20           | Case=Acc|Numb=Sing|Gend=Masc                                    | 12              |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascFem                         | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=MascFem                                 | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
| Case=Acc|Numb=Plur|Gend=Masc                                       | 20           | Case=Nom|Numb=Plur|Gend=Masc                                    | 5               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 5               |
|                                                                    |              | Case=Ind                                                        | 4               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Masc                            | 2               |
|                                                                    |              | Case=Abl|Numb=Plur|Gend=Com                                     | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Fem                                     | 1               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 1               |
| Case=Nom|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=Neut        | 20           | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 7               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=MascNeut | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 1               |
| Case=Gen|Numb=Sing|Deg=Comp|Gend=Com                               | 20           | Case=Gen|Numb=Sing                                              | 4               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 2               |
|                                                                    |              | Deg=Sup                                                         | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Comp|Gend=Neut                           | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Comp|Gend=Neut                           | 1               |
|                                                                    |              | Case=Gen|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Deg=Comp                                                        | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Comp|Gend=Com                            | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Dep|Person=2                | 1               |
| Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=2                   | 20           | Mood=Inf|Tense=Pres|Voice=Act                                   | 10              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 3               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 2               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
|                                                                    |              | Mood=Inf|Tense=Perf|Voice=Act                                   | 1               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Gend=MascNeut                                | 1               |
|                                                                    |              | Case=Abl|Numb=Plur|Deg=Pos|Gend=Com                             | 1               |
| Numb=Plur|Mood=Ind|Tense=Perf|Voice=Act|Person=1                   | 19           | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 17              |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
|                                                                    |              | Mood=Inf|Tense=Perf|Voice=Act                                   | 1               |
| Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc        | 19           | Case=Acc|Numb=Plur|Deg=Pos|Gend=Masc                            | 11              |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Inf|Tense=Perf|Voice=Pass|Gend=Masc     | 6               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
| Numb=Plur|Mood=Ind|Tense=Perf|Voice=Act|Person=2                   | 19           | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=2                | 16              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Act|Person=1                | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 1               |
| Case=Gen|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem         | 19           | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 14              |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=Fem                             | 3               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
| Case=Nom|Numb=Plur|Deg=Sup|Gend=Neut                               | 19           | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 4               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Sup|Gend=Fem                             | 4               |
|                                                                    |              | Deg=Sup                                                         | 4               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Sup|Gend=Neut                            | 3               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 2               |
| Case=Acc|Numb=Sing|Mood=Inf|Tense=Fut|Voice=Act|Gend=MascNeut      | 18           | Case=Acc|Numb=Sing                                              | 10              |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 3               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 3               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=MascNeut    | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Fut|Voice=Act|Gend=Masc       | 1               |
| Case=Acc|Numb=Plur|Gend=MascNeut                                   | 18           | Case=Nom|Numb=Plur|Gend=MascNeut                                | 14              |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Fut|Voice=Act|Person=2                 | 2               |
|                                                                    |              | Case=Ind                                                        | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 1               |
| Case=Acc|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=Neut         | 18           | Case=Acc|Numb=Plur                                              | 6               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 5               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Case=Gen|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 1               |
| Numb=Sing|Mood=Sub|Tense=Pres|Voice=Pass|Person=1                  | 18           | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 6               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=3                 | 5               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Pass|Person=1                | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Dep|Person=1                 | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
| Case=Gen|Numb=Plur|Deg=Pos|Gend=Com                                | 17           | Case=Gen|Numb=Plur                                              | 16              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
| Case=Acc|Numb=Plur|Mood=Inf|Tense=Fut|Voice=Act|Gend=Masc          | 17           | Case=Acc|Numb=Plur                                              | 4               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 3               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Masc                            | 2               |
|                                                                    |              | Mood=Inf|Tense=Perf|Voice=Act                                   | 2               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Mood=Inf|Tense=Fut|Voice=Act|Gend=Masc                          | 1               |
|                                                                    |              | Deg=Sup                                                         | 1               |
| Case=Gen|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=MascNeut       | 17           | Case=Gen|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                   | 15              |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=MascNeut    | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                   | 1               |
| Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=3                   | 17           | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 15              |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pqp|Voice=Act|Person=3                 | 1               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Pass|Person=3               | 1               |
| Numb=Sing|Mood=Sub|Tense=Perf|Voice=Pass|Person=3|Gend=Masc        | 17           | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 11              |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 3               |
| Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc        | 17           | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 10              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=3                | 2               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Abl|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Com      | 2               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 1               |
| Case=Dat|Numb=Sing|Deg=Sup|Gend=MascNeut                           | 17           | Deg=Sup                                                         | 7               |
|                                                                    |              | Case=Dat|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 3               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Sup|Gend=MascNeut                        | 3               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascFem                         | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Sup|Gend=Fem                             | 1               |
| Case=Dat|Numb=Plur|Deg=Comp|Gend=Com                               | 16           | Case=Abl|Numb=Plur|Deg=Comp|Gend=Com                            | 5               |
|                                                                    |              | Case=Dat|Numb=Plur|Deg=Pos|Gend=Com                             | 4               |
|                                                                    |              | Case=Dat|Numb=Plur                                              | 2               |
|                                                                    |              | Mood=Inf|Tense=Perf|Voice=Act                                   | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 1               |
|                                                                    |              | Case=Abl|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Comp|Gend=MascFem                        | 1               |
|                                                                    |              | Case=Dat|Numb=Plur|Gend=Com                                     | 1               |
| Numb=Sing|Mood=Ind|Tense=Fut|Voice=Dep|Person=2                    | 16           | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=2                | 5               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Com                             | 2               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Dep|Person=2                | 2               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=2                 | 1               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Dep|Person=2                | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Dep|Person=3                 | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 1               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 1               |
| Numb=Sing|Mood=Ind|Tense=Impa|Voice=SemDep|Person=3                | 16           | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 4               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pqp|Voice=Act|Person=3                 | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Impa|Voice=Act|Person=3                | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Impa|Voice=Pass|Person=3               | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Impa|Voice=SemDep|Person=3             | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=3                | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 1               |
| Numb=Sing|Mood=Ind|Tense=Pres|Voice=Pass|Person=1                  | 16           | Case=Nom|Numb=Sing                                              | 11              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=1                | 2               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Comp|Gend=MascFem                        | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=3                 | 1               |
| Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=1|Gend=Masc         | 16           | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Masc      | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 3               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=Masc      | 1               |
|                                                                    |              | Deg=Pos                                                         | 1               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 1               |
| Case=Acc|Numb=Sing|Mood=Adj|Tense=_|Voice=Dep|Gend=MascNeut        | 15           | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 9               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=MascNeut    | 3               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 3               |
| Case=Acc|Numb=Sing|Gend=Masc                                       | 15           | Case=Acc|Numb=Sing                                              | 11              |
|                                                                    |              | Deg=Pos                                                         | 1               |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=Com                                     | 1               |
|                                                                    |              | Case=Abl|Numb=Plur|Gend=Com                                     | 1               |
|                                                                    |              | MORPH=EMPTY                                                     | 1               |
| Numb=Sing|Mood=Ind|Tense=Pres|Voice=Pass|Person=2                  | 15           | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=2                 | 6               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 5               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 2               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Pass                                  | 1               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 1               |
| Case=Acc|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=MascNeut       | 15           | Case=Nom|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=Neut        | 7               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                   | 3               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 3               |
|                                                                    |              | Deg=Pos                                                         | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
| Mood=SupU|Tense=_|Voice=Act                                        | 15           | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 5               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 4               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 3               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=3                | 1               |
| Numb=Sing|Mood=Sub|Tense=Pqp|Voice=Dep|Person=3|Gend=Masc          | 15           | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Masc      | 4               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 4               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
| Numb=Plur|Mood=Ind|Tense=Pres|Voice=SemDep|Person=3                | 15           | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 12              |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
| Case=Nom|Numb=Plur|Mood=Adj|Tense=_|Voice=Pass|Gend=Masc           | 15           | Case=Gen|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                   | 14              |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
| Case=Nom|Numb=Plur|Deg=Comp|Gend=MascFem                           | 15           | Case=Nom|Numb=Plur                                              | 7               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=MascFem                         | 4               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 3               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Comp|Gend=MascFem                        | 1               |
| Case=Nom|Numb=Sing|Mood=Adj|Tense=_|Voice=Dep|Gend=Neut            | 14           | Case=Nom|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=Neut        | 4               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 3               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Neut                                    | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Adj|Tense=_|Voice=Dep|Gend=MascNeut     | 1               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
| Numb=Sing|Mood=Ind|Tense=Pqp|Voice=Act|Person=1                    | 14           | Case=Acc|Numb=Sing                                              | 8               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Impa|Voice=Act|Person=1                | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pqp|Voice=Act|Person=3                 | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=1                 | 1               |
| Numb=Sing|Mood=Sub|Tense=Pres|Voice=Dep|Person=3                   | 14           | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=3                | 4               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 3               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Dep|Person=3                | 3               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Pass|Person=3               | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Fem       | 2               |
| Case=Acc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=MascNeut     | 14           | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 7               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 5               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Fem       | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
| Numb=Sing|Mood=Sub|Tense=Pres|Voice=Dep|Person=2                   | 14           | Mood=Inf|Tense=Pres|Voice=Act                                   | 11              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=2                | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Dep|Person=1                 | 1               |
| Numb=Sing|Mood=Ind|Tense=Fut|Voice=Pass|Person=3|Gend=Neut         | 14           | Case=Acc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 6               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 4               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
| Numb=Plur|Mood=Ind|Tense=Fut|Voice=Pass|Person=3                   | 14           | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Pass|Person=3               | 10              |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Pass|Person=3               | 4               |
| Case=Gen|Numb=Plur|Deg=Comp|Gend=Com                               | 14           | Case=Gen|Numb=Plur                                              | 13              |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
| Case=Acc|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                      | 14           | Case=Acc|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=MascNeut    | 11              |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=Neut        | 1               |
| Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=3                   | 13           | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 8               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Pass|Person=3               | 2               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Dep|Person=3                | 1               |
| Numb=Sing|Mood=Imp|Tense=Pres|Voice=Dep|Person=2                   | 13           | Mood=Inf|Tense=Pres|Voice=Act                                   | 12              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=2                | 1               |
| Mood=Inf|Tense=Pres|Voice=SemDep                                   | 13           | Mood=Inf|Tense=Pres|Voice=Act                                   | 13              |
| Numb=Plur|Mood=Ind|Tense=Fut|Voice=Act|Person=2                    | 13           | Case=Dat|Numb=Plur|Gend=Com                                     | 2               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=2                 | 2               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 2               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Numb=Plur|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Abl|Numb=Plur                                              | 1               |
| Case=Abl|Numb=Plur|Mood=Adj|Tense=_|Voice=Pass|Gend=Com            | 13           | Case=Gen|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                   | 9               |
|                                                                    |              | Case=Abl|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Case=Abl|Numb=Plur|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Dat|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=Fem         | 1               |
| Case=Nom|Numb=Plur|Mood=Par|Tense=Fut|Voice=Act|Gend=Masc          | 12           | Mood=Inf|Tense=Pres|Voice=Pass                                  | 7               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 4               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 1               |
| Numb=Sing|Mood=Sub|Tense=Perf|Voice=Pass|Person=3|Gend=Fem         | 12           | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 5               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Neut     | 1               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Case=Nom|Numb=Sing|Mood=Par|Tense=Fut|Voice=Act|Gend=Masc          | 12           | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 5               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 2               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
| Numb=Sing|Mood=Ind|Tense=Fut|Voice=Pass|Person=2                   | 12           | Mood=Inf|Tense=Pres|Voice=Act                                   | 7               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=2                 | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Pass|Person=2               | 2               |
| Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=1                   | 12           | Case=Nom|Numb=Sing                                              | 4               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Comp|Gend=MascFem                        | 1               |
|                                                                    |              | MORPH=EMPTY                                                     | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Pass|Person=1               | 1               |
| Numb=Sing|Mood=Ind|Tense=Pqp|Voice=Pass|Person=3|Gend=Fem          | 12           | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 7               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 3               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Case=Abl|Numb=Plur|Deg=Comp|Gend=Com                               | 11           | Case=Abl|Numb=Plur|Deg=Pos|Gend=Com                             | 4               |
|                                                                    |              | Case=Abl|Numb=Plur                                              | 3               |
|                                                                    |              | Deg=Comp                                                        | 2               |
|                                                                    |              | Case=Abl|Numb=Plur|Gend=Com                                     | 1               |
|                                                                    |              | Deg=Sup                                                         | 1               |
| Case=Abl|Numb=Plur|Mood=Par|Tense=Pres|Voice=Dep|Gend=Com          | 11           | Case=Abl|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 6               |
|                                                                    |              | Case=Dat|Numb=Plur|Deg=Pos|Gend=Com                             | 2               |
|                                                                    |              | Case=Dat|Numb=Plur|Gend=Com                                     | 2               |
|                                                                    |              | Case=Abl|Numb=Plur                                              | 1               |
| Case=Gen|Numb=Sing|Mood=Par|Tense=Pres|Voice=Dep|Gend=Com          | 11           | Case=Gen|Numb=Sing                                              | 6               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Dep|Gend=Com       | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Pres|Voice=Dep|Gend=MascFem   | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
| Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=1                   | 11           | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 5               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Pass                                  | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=1                | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
| Case=Dat|Numb=Plur|Deg=Sup|Gend=Com                                | 11           | Case=Dat|Numb=Plur|Deg=Pos|Gend=Com                             | 4               |
|                                                                    |              | Deg=Sup                                                         | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Sup|Gend=Masc                            | 1               |
|                                                                    |              | Case=Abl|Numb=Plur|Deg=Sup|Gend=Com                             | 1               |
|                                                                    |              | Case=Abl|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Neut                                    | 1               |
| Numb=Sing|Mood=Sub|Tense=Pqp|Voice=Pass|Person=3|Gend=Fem          | 11           | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 8               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Case=Nom|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=Neut         | 11           | Case=Nom|Numb=Plur                                              | 3               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=Neut      | 2               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
| Numb=Sing|Mood=Ind|Tense=Impa|Voice=Pass|Person=1                  | 11           | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Pass|Person=1                | 6               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=3                 | 3               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Pass|Person=1               | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Case=Dat|Numb=Sing|Gend=Fem                                        | 11           | Case=Gen|Numb=Sing|Gend=Fem                                     | 4               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Fem                                     | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Dat|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
| Numb=Plur|Mood=Ind|Tense=Pqp|Voice=Pass|Person=3|Gend=Fem          | 11           | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 10              |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
| Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Dep|Gend=Com          | 11           | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 10              |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
| Case=Abl|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=Com          | 10           | Case=Abl|Numb=Plur                                              | 4               |
|                                                                    |              | Case=Dat|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 4               |
|                                                                    |              | Case=Abl|Numb=Plur|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Dat|Numb=Plur|Deg=Pos|Gend=Com                             | 1               |
| Numb=Plur|Mood=Sub|Tense=Pres|Voice=Pass|Person=3                  | 10           | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Pass|Person=3               | 10              |
| Case=Gen|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut    | 10           | Case=Gen|Numb=Plur                                              | 9               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
| Case=Acc|Numb=Sing|Mood=Par|Tense=Fut|Voice=Act|Gend=MascNeut      | 10           | Case=Acc|Numb=Sing|Mood=Inf|Tense=Fut|Voice=Act|Gend=MascNeut   | 4               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 2               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
| Case=Abl|Numb=Sing|Gend=Com                                        | 10           | Case=Nom|Numb=Sing|Gend=Masc                                    | 4               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Com                             | 2               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Abl|Numb=Plur|Gend=Com                                     | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 1               |
| Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem         | 10           | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 4               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 2               |
|                                                                    |              | Case=Gen|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Case=Voc|Numb=Plur                                              | 1               |
| Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=SemDep|Gend=Masc      | 10           | Case=Acc|Numb=Plur|Gend=Neut                                    | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=3                | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=MascNeut                                | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
| Case=Dat|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut    | 10           | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 6               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Case=Dat|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
| Numb=Sing|Mood=Sub|Tense=Impa|Voice=Pass|Person=1                  | 10           | Mood=Inf|Tense=Pres|Voice=Act                                   | 3               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 2               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 2               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Pass|Person=1               | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=3                 | 1               |
| Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=2                   | 10           | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Voc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Abl|Numb=Plur|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 1               |
| Case=Nom|Numb=Plur|Mood=Par|Tense=Pres|Voice=Dep|Gend=MascFem      | 10           | Case=Nom|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 2               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Ind                                                        | 2               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Pres|Voice=Dep|Gend=MascFem   | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
| Case=Abl|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=Fem            | 10           | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 3               |
|                                                                    |              | Case=Gen|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                   | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=MascNeut    | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Adj|Tense=_|Voice=Pass|Gend=Fem         | 1               |
|                                                                    |              | Case=Abl|Numb=Plur|Mood=Adj|Tense=_|Voice=Pass|Gend=Com         | 1               |
| Case=Dat|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=MascNeut     | 10           | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 3               |
|                                                                    |              | Case=Dat|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Masc                            | 1               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
| Case=Dat|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem         | 10           | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 4               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Case=Gen|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 2               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Pass                                  | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
| Case=Gen|Numb=Plur|Mood=Adj|Tense=_|Voice=Pass|Gend=MascNeut       | 10           | Case=Acc|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=MascNeut    | 5               |
|                                                                    |              | Case=Gen|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                   | 1               |
| Case=Nom|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=Masc           | 9            | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 8               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
| Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Dep|Gend=Fem          | 9            | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 5               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 2               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pqp|Voice=Dep|Person=3|Gend=Fem        | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Fem                                     | 1               |
| Case=Abl|Numb=Sing|Deg=Comp|Gend=Com                               | 9            | Case=Abl|Numb=Sing|Deg=Pos|Gend=Com                             | 9               |
| Case=Dat|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com          | 9            | Case=Abl|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 4               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Dat|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Ind                                                        | 1               |
| Case=Abl|Numb=Sing|Mood=Ger|Tense=_|Voice=Dep                      | 9            | Case=Abl|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                   | 5               |
|                                                                    |              | Case=Gen|Numb=Sing|Mood=Ger|Tense=_|Voice=Dep                   | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Dat|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
| Case=Gen|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=Fem            | 9            | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 3               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 2               |
|                                                                    |              | Case=Dat|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=Fem         | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
| Case=Nom|Numb=Plur|Gend=MascFem                                    | 9            | Case=Acc|Numb=Plur|Gend=MascFem                                 | 3               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=MascFem                         | 2               |
|                                                                    |              | Case=Ind                                                        | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=MascNeut                                | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 1               |
| Numb=Plur|Mood=Sub|Tense=Pres|Voice=Pass|Person=1                  | 9            | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 7               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Pass|Person=3               | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Pass|Person=1               | 1               |
| Case=Abl|Numb=Plur|Gend=Fem                                        | 9            | Case=Abl|Numb=Plur|Gend=Com                                     | 3               |
|                                                                    |              | Case=Dat|Numb=Plur|Deg=Pos|Gend=Com                             | 2               |
|                                                                    |              | Case=Ind                                                        | 2               |
|                                                                    |              | Case=Abl|Numb=Plur|Deg=Pos|Gend=Com                             | 2               |
| Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=2|Gend=Masc         | 9            | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 2               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
| Case=Gen|Numb=Plur|Mood=Par|Tense=Pres|Voice=Dep|Gend=Com          | 9            | Case=Gen|Numb=Plur                                              | 6               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Gen|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
| Case=Voc|Numb=Sing|Deg=Pos|Gend=Com                                | 9            | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 8               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
| Numb=Plur|Mood=Ind|Tense=Impa|Voice=SemDep|Person=3                | 9            | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 4               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=MascFem                                 | 1               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Fut|Voice=SemDep|Person=3              | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 1               |
| Numb=Sing|Mood=Sub|Tense=Impa|Voice=Dep|Person=1                   | 9            | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Dep|Person=1                | 5               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Dep|Person=2                | 2               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Dep|Person=2                | 1               |
| Case=Acc|Numb=Sing|Mood=Par|Tense=Pres|Voice=Dep|Gend=MascFem      | 9            | Case=Acc|Numb=Sing                                              | 4               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascFem                         | 4               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 1               |
| Numb=Plur|Mood=Sub|Tense=Pqp|Voice=Pass|Person=3|Gend=Masc         | 9            | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 5               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 2               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Pass                                  | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Masc                            | 1               |
| Numb=Plur|Mood=Ind|Tense=Pqp|Voice=Pass|Person=3|Gend=Masc         | 9            | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 5               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 4               |
| Case=Dat|Numb=Plur|Mood=Adj|Tense=_|Voice=Pass|Gend=Com            | 9            | Case=Gen|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                   | 6               |
|                                                                    |              | Case=Abl|Numb=Plur|Mood=Adj|Tense=_|Voice=Pass|Gend=Com         | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
| Case=Acc|Numb=Plur|Mood=Adj|Tense=_|Voice=Pass|Gend=Masc           | 9            | Case=Acc|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=MascNeut    | 3               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                   | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Masc                            | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=Masc        | 1               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 1               |
| Case=Nom|Numb=Sing|Deg=Comp|Gend=MascFem                           | 8            | Case=Nom|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=1                | 1               |
| Case=Acc|Numb=Sing|Mood=Inf|Tense=Fut|Voice=Act|Gend=Fem           | 8            | Case=Acc|Numb=Sing                                              | 4               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=Fem                             | 3               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 1               |
| Mood=SupUm|Tense=_|Voice=Act                                       | 8            | Case=Abl|Numb=Sing                                              | 7               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 1               |
| Numb=Sing|Mood=Sub|Tense=Perf|Voice=Dep|Person=3|Gend=Masc         | 8            | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Masc      | 2               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 1               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 1               |
| Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=1|Gend=Fem         | 8            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 4               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 1               |
| Numb=Plur|Mood=Ind|Tense=Pqp|Voice=Pass|Person=3|Gend=Neut         | 8            | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
| Numb=Sing|Mood=Sub|Tense=Pres|Voice=SemDep|Person=3                | 8            | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 7               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 1               |
| Case=Voc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem         | 8            | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
| Case=Nom|Numb=Sing|Mood=Par|Tense=Fut|Voice=Dep|Gend=Masc          | 8            | Case=Nom|Numb=Sing|Gend=Masc                                    | 3               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 1               |
| Case=Abl|Numb=Sing|Mood=Par|Tense=Pres|Voice=Dep|Gend=Com          | 8            | Case=Abl|Numb=Sing|Deg=Pos|Gend=Com                             | 3               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 3               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 1               |
|                                                                    |              | Case=Dat|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
| Case=Abl|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=MascNeut       | 8            | Case=Abl|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                   | 8               |
| Numb=Sing|Mood=Sub|Tense=Impa|Voice=SemDep|Person=3                | 8            | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 6               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 2               |
| Numb=Sing|Mood=Ind|Tense=Fut|Voice=Pass|Person=1                   | 8            | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Pass|Person=1               | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
|                                                                    |              | MORPH=EMPTY                                                     | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Pass|Person=1               | 1               |
| Numb=Sing|Mood=Sub|Tense=Pres|Voice=Pass|Person=2                  | 8            | Mood=Inf|Tense=Pres|Voice=Act                                   | 5               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=2                | 1               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=2                 | 1               |
| Case=Abl|Numb=Plur|Gend=MascNeut                                   | 8            | Case=Dat|Numb=Plur|Gend=MascNeut                                | 4               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Masc                                    | 2               |
|                                                                    |              | Case=Ind                                                        | 2               |
| Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=2|Gend=Masc        | 8            | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 3               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 1               |
| Case=Gen|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem         | 7            | Case=Gen|Numb=Plur                                              | 5               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
| Case=Dat|Numb=Sing|Mood=Par|Tense=Pres|Voice=Dep|Gend=Com          | 7            | Case=Abl|Numb=Sing|Mood=Par|Tense=Pres|Voice=Dep|Gend=Com       | 4               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Dat|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
| Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Dep|Gend=Masc         | 7            | Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 3               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Masc                                    | 1               |
| Numb=Plur|Mood=Ind|Tense=Pres|Voice=Pass|Person=1                  | 7            | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 3               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Pass|Person=3               | 3               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 1               |
| Case=Dat|Numb=Sing|Deg=Sup|Gend=Fem                                | 7            | Case=Gen|Numb=Sing|Deg=Sup|Gend=Fem                             | 5               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Sup|Gend=Fem                             | 1               |
| Case=Abl|Numb=Plur|Mood=Par|Tense=Perf|Voice=Dep|Gend=Com          | 7            | Case=Abl|Numb=Plur|Gend=Com                                     | 2               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Dep|Gend=Masc      | 1               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
| Numb=Sing|Mood=Ind|Tense=Fut|Voice=Pass|Person=3|Gend=Masc         | 7            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 4               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 1               |
| Case=Dat|Numb=Plur|Mood=Par|Tense=Perf|Voice=Dep|Gend=Com          | 7            | Case=Abl|Numb=Plur                                              | 3               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Dep|Gend=Masc      | 1               |
|                                                                    |              | Case=Dat|Numb=Plur|Deg=Pos|Gend=Com                             | 1               |
| Case=Voc|Numb=Sing|Deg=Pos|Gend=MascFem                            | 7            | Case=Nom|Numb=Sing|Deg=Pos|Gend=MascFem                         | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=MascFem                         | 1               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Voc|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
| Case=Nom|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=Masc        | 7            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 3               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
| Case=Nom|Numb=Sing|Gend=MascNeut                                   | 7            | Case=Acc|Numb=Sing|Gend=Neut                                    | 3               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Deg=Pos                                                         | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Masc                                    | 1               |
| Case=Abl|Numb=Sing|Deg=Pos|Gend=Masc                               | 7            | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 6               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 1               |
| Numb=Sing|Mood=Ind|Tense=Fut|Voice=Pass|Person=3|Gend=Fem          | 7            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 3               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Case=Nom|Numb=Plur|Mood=Par|Tense=Fut|Voice=Act|Gend=Neut          | 7            | Mood=Inf|Tense=Pres|Voice=Act                                   | 4               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Fut|Voice=Act|Gend=Masc       | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
| Numb=Sing|Mood=Ind|Tense=Impa|Voice=Dep|Person=1                   | 7            | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Dep|Person=1                 | 5               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Fem       | 1               |
| Case=Voc|Numb=Sing|Deg=Sup|Gend=Masc                               | 7            | Deg=Sup                                                         | 6               |
|                                                                    |              | Deg=Pos                                                         | 1               |
| Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Neut         | 7            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Fem       | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Gen|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
| Numb=Plur|Mood=Sub|Tense=Perf|Voice=Act|Person=3                   | 7            | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 4               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Fut|Voice=Act|Person=3                 | 3               |
| Case=Nom|Numb=Sing|Mood=Par|Tense=Fut|Voice=Act|Gend=Neut          | 7            | Case=Acc|Numb=Sing|Mood=Inf|Tense=Fut|Voice=Act|Gend=MascNeut   | 3               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 2               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Fut|Voice=Act|Gend=Masc       | 1               |
| Case=Voc|Numb=Plur|Deg=Pos|Gend=MascFem                            | 7            | Case=Nom|Numb=Plur|Deg=Pos|Gend=MascFem                         | 5               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=MascFem                         | 1               |
| Numb=Plur|Mood=Ind|Tense=Pres|Voice=Dep|Person=1                   | 7            | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Dep|Person=1                | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Pass|Person=3               | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Case=Voc|Numb=Sing                                              | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=3                | 1               |
| Mood=SupU|Tense=_|Voice=Dep                                        | 7            | Case=Acc|Numb=Sing                                              | 4               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
| Numb=Sing|Mood=Ind|Tense=Pqp|Voice=Dep|Person=3|Gend=Masc          | 6            | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Masc      | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 1               |
| Numb=Sing|Mood=Sub|Tense=Perf|Voice=Pass|Person=1|Gend=Masc        | 6            | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 3               |
| Numb=Plur|Mood=Sub|Tense=Impa|Voice=Act|Person=2                   | 6            | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=2                | 1               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 1               |
| Case=Dat|Numb=Plur|Mood=Par|Tense=Pres|Voice=Dep|Gend=Com          | 6            | Case=Abl|Numb=Sing|Mood=Par|Tense=Pres|Voice=Dep|Gend=Com       | 2               |
|                                                                    |              | Case=Abl|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 2               |
|                                                                    |              | Deg=Sup                                                         | 1               |
|                                                                    |              | Case=Dat|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
| Numb=Sing|Mood=Ind|Tense=Fut|Voice=Dep|Person=1                    | 6            | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Dep|Person=1                | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=1                | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=2                | 1               |
| Numb=Plur|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Fem          | 6            | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 2               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Fem       | 1               |
| Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=MascNeut     | 6            | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 3               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Dat|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
| Case=Nom|Numb=Plur|Mood=Adj|Tense=_|Voice=Pass|Gend=Fem            | 6            | Case=Gen|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=Fem         | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 2               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
| Numb=Sing|Mood=Sub|Tense=Pqp|Voice=Pass|Person=1|Gend=Masc         | 6            | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 3               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 2               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
| Numb=Sing|Mood=Ind|Tense=Perf|Voice=SemDep|Person=3|Gend=Masc      | 6            | Case=Acc|Numb=Plur|Gend=Neut                                    | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=MascNeut                                | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=1                | 1               |
| Case=Voc|Numb=Plur|Deg=Pos|Gend=Masc                               | 6            | Case=Gen|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Masc                            | 2               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 2               |
| Numb=Plur|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Neut         | 6            | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Gend=Neut                                    | 1               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Fem       | 1               |
| Case=Voc|Numb=Sing|Gend=Masc                                       | 6            | Case=Dat|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 2               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
|                                                                    |              | MORPH=EMPTY                                                     | 1               |
| Numb=Sing|Mood=Sub|Tense=Impa|Voice=Dep|Person=2                   | 6            | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=2                | 3               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Dep|Person=2                | 2               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
| Numb=Plur|Mood=Sub|Tense=Perf|Voice=Pass|Person=3|Gend=Neut        | 6            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 4               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
| Case=Gen|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                      | 6            | Case=Acc|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=MascNeut    | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                   | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=Fem         | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Pass                                  | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=MascNeut    | 1               |
| Case=Dat|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=Fem            | 6            | Case=Nom|Numb=Plur                                              | 3               |
|                                                                    |              | Case=Gen|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=Fem         | 3               |
| Numb=Plur|Mood=Sub|Tense=Pqp|Voice=Dep|Person=3|Gend=Masc          | 6            | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Masc      | 3               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Dat|Numb=Sing|Gend=Com                                     | 1               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 1               |
| Numb=Plur|Mood=Sub|Tense=Pqp|Voice=Pass|Person=3|Gend=Neut         | 6            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 3               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 1               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
| Case=Nom|Numb=Sing|Deg=Sup|Gend=Masc                               | 5            | Deg=Sup                                                         | 4               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 1               |
| Deg=Sup                                                            | 5            | Deg=Comp                                                        | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Sup|Gend=Fem                             | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Case=Voc|Numb=Sing|Deg=Sup|Gend=Masc                            | 1               |
| Case=Gen|Numb=Sing|Mood=Par|Tense=Fut|Voice=Act|Gend=MascNeut      | 5            | Case=Gen|Numb=Sing                                              | 4               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Pass                                  | 1               |
| Numb=Sing|Mood=Ind|Tense=Impa|Voice=SemDep|Person=2                | 5            | Case=Acc|Numb=Plur|Gend=Neut                                    | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=2                 | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Sup|Gend=Fem                             | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Numb=Plur|Mood=Sub|Tense=Pres|Voice=SemDep|Person=3                | 5            | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 5               |
| Numb=Sing|Mood=Ind|Tense=Fut|Voice=Dep|Person=3                    | 5            | Case=Nom|Numb=Sing                                              | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=3                 | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=Fem       | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Pass|Person=3                | 1               |
| Numb=Plur|Mood=Imp|Tense=Pres|Voice=Act|Person=2                   | 5            | Case=Voc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 2               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Deg=Pos                                                         | 1               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 1               |
| Case=Nom|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=Fem         | 5            | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Numb=Plur|Mood=Sub|Tense=Pres|Voice=Dep|Person=1                   | 5            | Case=Acc|Numb=Sing                                              | 2               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Dep|Person=1                | 1               |
| Case=Voc|Numb=Plur|Deg=Pos|Gend=Fem                                | 5            | Case=Gen|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 1               |
| Case=Acc|Numb=Sing|Mood=Inf|Tense=Fut|Voice=Dep|Gend=MascNeut      | 5            | Case=Acc|Numb=Sing|Mood=Inf|Tense=Fut|Voice=Act|Gend=MascNeut   | 2               |
|                                                                    |              | Case=Gen|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
| Numb=Sing|Mood=Sub|Tense=Perf|Voice=Pass|Person=2|Gend=Masc        | 5            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 3               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 1               |
| Case=Nom|Numb=Plur|Mood=Adj|Tense=_|Voice=Dep|Gend=Neut            | 5            | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Case=Gen|Numb=Sing|Deg=Comp|Gend=Neut                              | 5            | Case=Acc|Numb=Plur|Deg=Comp|Gend=Neut                           | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
|                                                                    |              | Deg=Comp                                                        | 1               |
| Case=Acc|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Neut         | 4            | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 4               |
| Case=Gen|Numb=Sing|Mood=Ger|Tense=_|Voice=Dep                      | 4            | Case=Gen|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                   | 3               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
| Numb=Plur|Mood=Ind|Tense=Pqp|Voice=Dep|Person=3|Gend=Masc          | 4            | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Dep|Gend=Masc      | 2               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Masc      | 1               |
| Numb=Plur|Mood=Ind|Tense=Pres|Voice=SemDep|Person=1                | 4            | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 2               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 1               |
| Numb=Sing|Mood=Ind|Tense=Fut|Voice=Pass|Person=2|Gend=Masc         | 4            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 4               |
| Numb=Plur|Mood=Sub|Tense=Impa|Voice=Dep|Person=1                   | 4            | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Dep|Person=3                | 3               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Dep|Person=1                | 1               |
| Case=Acc|Numb=Plur|Mood=Par|Tense=Pres|Voice=Dep|Gend=Neut         | 4            | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 2               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Pres|Voice=Dep|Gend=Com       | 1               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
| Case=Acc|Numb=Sing|Mood=Par|Tense=Fut|Voice=Act|Gend=Fem           | 4            | Case=Acc|Numb=Sing                                              | 4               |
| Case=Acc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=Fem          | 4            | Case=Acc|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Fem       | 1               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
| Numb=Plur|Mood=Imp|Tense=Pres|Voice=Dep|Person=2                   | 4            | Case=Dat|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Dep                                   | 1               |
| Case=Acc|Numb=Plur|Mood=Inf|Tense=Fut|Voice=Dep|Gend=Masc          | 4            | Case=Acc|Numb=Plur|Mood=Inf|Tense=PeriFut|Voice=Dep|Gend=Masc   | 2               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Masc                            | 1               |
| Case=Abl|Numb=Sing|Mood=Adj|Tense=_|Voice=Dep|Gend=Fem             | 4            | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Mood=Ger|Tense=_|Voice=Dep                   | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=Fem         | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Numb=Sing|Mood=Ind|Tense=Pres|Voice=SemDep|Person=2                | 4            | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 3               |
|                                                                    |              | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=2                | 1               |
| Case=Gen|Numb=Plur|Gend=Fem                                        | 4            | Case=Gen|Numb=Plur                                              | 4               |
| Numb=Sing|Mood=Sub|Tense=Fut|Voice=Dep|Person=3|Gend=Masc          | 4            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Masc      | 2               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 1               |
| Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=1|Gend=Masc        | 4            | Mood=Inf|Tense=Pres|Voice=Pass                                  | 2               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=1                | 1               |
| Case=Abl|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                      | 4            | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=Masc                                    | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=MascNeut    | 1               |
| Case=Gen|Numb=Plur|Mood=Adj|Tense=_|Voice=Pass|Gend=Fem            | 4            | Case=Gen|Numb=Plur                                              | 2               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=MascNeut    | 2               |
| Mood=Inf|Tense=Fut|Voice=Pass                                      | 4            | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 2               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
| Case=Gen|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=Com          | 4            | Case=Gen|Numb=Plur                                              | 3               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
| Numb=Plur|Mood=Ind|Tense=Perf|Voice=SemDep|Person=3|Gend=Masc      | 4            | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Neut     | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Gend=Masc                                    | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Pass                                  | 1               |
| Case=Voc|Numb=Sing|Gend=Fem                                        | 4            | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Fem                                     | 1               |
| Numb=Sing|Mood=Sub|Tense=Fut|Voice=Pass|Person=3|Gend=Neut         | 4            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 3               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
| Numb=Plur|Mood=Sub|Tense=Perf|Voice=Pass|Person=3|Gend=Masc        | 4            | Case=Gen|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
| Case=Nom|Numb=Plur|Mood=Inf|Tense=Perf|Voice=Pass|Gend=Masc        | 4            | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 2               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Masc                            | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
| Case=Voc|Numb=Sing|Deg=Sup|Gend=Fem                                | 4            | Case=Nom|Numb=Sing|Deg=Sup|Gend=Fem                             | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Deg=Sup                                                         | 1               |
| Numb=Plur|Mood=Ind|Tense=Fut|Voice=Dep|Person=3                    | 4            | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Dep|Person=3                | 2               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Fut|Voice=Pass|Person=3                | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Fut|Voice=Act|Person=3                 | 1               |
| Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=SemDep|Gend=MascNeut  | 4            | Case=Acc|Numb=Sing                                              | 3               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
| Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=Fem          | 4            | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Dep|Gend=Masc      | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=Fem       | 1               |
| Case=Voc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc        | 4            | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=1                | 1               |
|                                                                    |              | Case=Dat|Numb=Plur|Deg=Pos|Gend=Com                             | 1               |
| Numb=Plur|Mood=Sub|Tense=Pres|Voice=Dep|Person=3                   | 4            | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Pass|Person=3               | 2               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Pass|Person=3               | 1               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 1               |
| Numb=Plur|Mood=Sub|Tense=Impa|Voice=SemDep|Person=3                | 3            | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Fut|Voice=SemDep|Person=3              | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 1               |
| Case=Acc|Numb=Plur|Mood=Par|Tense=Pres|Voice=Dep|Gend=MascFem      | 3            | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 1               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 1               |
| Case=Dat|Numb=Sing|Deg=Comp|Gend=Com                               | 3            | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Dat|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
| Numb=Plur|Mood=Imp|Tense=Fut|Voice=Act|Person=3                    | 3            | Case=Abl|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Dat|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
| Case=Acc|Numb=Sing|Mood=Inf|Tense=PeriFut|Voice=Act|Gend=MascNeut  | 3            | Case=Gen|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
| Numb=Plur|Mood=Ind|Tense=Fut|Voice=Pass|Person=3|Gend=Neut         | 3            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 2               |
|                                                                    |              | Deg=Pos                                                         | 1               |
| Case=Dat|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=MascNeut       | 3            | Case=Nom|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=Neut        | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                   | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=MascNeut    | 1               |
| Numb=Sing|Mood=Sub|Tense=Pqp|Voice=Dep|Person=3|Gend=Fem           | 3            | Case=Nom|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=Fem       | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Case=Dat|Numb=Sing|Mood=Adj|Tense=_|Voice=Dep|Gend=Fem             | 3            | Case=Dat|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
| Numb=Sing|Mood=Ind|Tense=Pres|Voice=Dep|Person=2                   | 3            | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=2                 | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
| Numb=Sing|Mood=Sub|Tense=Fut|Voice=Pass|Person=3|Gend=Masc         | 3            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
| Case=Abl|Numb=Sing|Mood=Par|Tense=Fut|Voice=Act|Gend=MascNeut      | 3            | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Fut|Voice=Act|Gend=Masc       | 1               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 1               |
| Case=Acc|Numb=Plur|Mood=Adj|Tense=_|Voice=Dep|Gend=Neut            | 3            | Case=Nom|Numb=Plur|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 1               |
| Numb=Sing|Mood=Sub|Tense=Perf|Voice=Dep|Person=3|Gend=Fem          | 3            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Fem       | 2               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 1               |
| Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Dep|Gend=Neut         | 3            | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=Fem       | 3               |
| Case=Gen|Numb=Sing|Deg=Sup|Gend=Fem                                | 3            | Case=Nom|Numb=Plur|Deg=Sup|Gend=Fem                             | 2               |
|                                                                    |              | Case=Gen|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Numb=Plur|Mood=Ind|Tense=Perf|Voice=Dep|Person=1|Gend=Masc         | 3            | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Dep|Gend=Masc      | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Masc      | 1               |
| Case=Acc|Numb=Plur|Mood=Inf|Tense=Fut|Voice=Act|Gend=Fem           | 3            | Mood=Inf|Tense=Pres|Voice=Act                                   | 2               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
| Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Dep|Gend=Fem          | 3            | Case=Acc|Numb=Plur                                              | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
| Numb=Plur|Mood=Sub|Tense=Pqp|Voice=Act|Person=1                    | 3            | Numb=Plur|Mood=Sub|Tense=Pqp|Voice=Act|Person=3                 | 2               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 1               |
| Numb=Sing|Mood=Ind|Tense=Perf|Voice=Act|Person=2                   | 3            | Mood=Inf|Tense=Pres|Voice=Pass                                  | 1               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
| Case=Voc|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com          | 3            | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 3               |
| Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=SemDep|Gend=Com       | 3            | Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 3               |
| Numb=Plur|Mood=Sub|Tense=Perf|Voice=Pass|Person=3|Gend=Fem         | 3            | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 2               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
| Numb=Plur|Mood=Sub|Tense=Perf|Voice=Act|Person=1                   | 3            | Deg=Sup                                                         | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Act|Person=1                | 1               |
| Numb=Sing|Mood=Imp|Tense=Fut|Voice=Act|Person=3                    | 3            | Case=Abl|Numb=Sing                                              | 2               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Fut|Voice=Act|Person=2                 | 1               |
| Case=Voc|Numb=Sing|Deg=Pos|Gend=Neut                               | 3            | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 3               |
| Case=Acc|Numb=Plur|Mood=Inf|Tense=Perf|Voice=Dep|Gend=Masc         | 3            | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Masc                            | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Masc                                    | 1               |
| Mood=Inf|Tense=Fut|Voice=Act                                       | 3            | Mood=Inf|Tense=Pres|Voice=Act                                   | 3               |
| Case=Voc|Numb=Sing|Deg=Comp|Gend=MascFem                           | 3            | Case=Voc|Numb=Sing                                              | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Comp|Gend=MascFem                        | 1               |
| Case=Acc|Numb=Plur|Mood=Inf|Tense=PeriFut|Voice=Act|Gend=Masc      | 3            | Mood=Inf|Tense=Perf|Voice=Act                                   | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Mood=Inf|Tense=Fut|Voice=Act|Gend=Masc       | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Deg=Pos|Gend=Masc                            | 1               |
| Case=Acc|Numb=Sing|Deg=Pos|Gend=Masc                               | 3            | Case=Acc|Numb=Sing                                              | 3               |
| Case=Acc|Numb=Sing|Mood=Inf|Tense=PeriPqp|Voice=Pass|Gend=MascNeut | 3            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 2               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
| Numb=Sing|Mood=Ind|Tense=Impa|Voice=Pass|Person=2                  | 3            | Mood=Inf|Tense=Pres|Voice=Act                                   | 2               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Pass|Person=2                | 1               |
| Case=Dat|Numb=Plur|Gend=Fem                                        | 3            | Case=Abl|Numb=Plur|Gend=Fem                                     | 1               |
|                                                                    |              | Case=Dat|Numb=Plur|Gend=Com                                     | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Numb=Plur|Mood=Sub|Tense=Pqp|Voice=Pass|Person=3|Gend=Fem          | 2            | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 2               |
| Numb=Sing|Mood=Imp|Tense=Pres|Voice=Pass|Person=2                  | 2            | Mood=Inf|Tense=Pres|Voice=Act                                   | 2               |
| Case=Nom|Numb=Plur|Mood=Inf|Tense=Perf|Voice=Pass|Gend=Neut        | 2            | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 1               |
| Case=Dat|Numb=Sing|Mood=Par|Tense=Fut|Voice=Act|Gend=MascNeut      | 2            | Case=Nom|Numb=Sing|Mood=Par|Tense=Fut|Voice=Act|Gend=Masc       | 1               |
|                                                                    |              | Case=Abl|Numb=Sing                                              | 1               |
| Numb=Sing|Mood=Ind|Tense=Impa|Voice=SemDep|Person=1                | 2            | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Deg=Pos                                                         | 1               |
| Numb=Sing|Mood=Ind|Tense=Fut|Voice=SemDep|Person=3                 | 2            | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=3                 | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Fut|Voice=SemDep|Person=3              | 1               |
| Case=Acc|Numb=Plur|Mood=Par|Tense=Fut|Voice=Act|Gend=Fem           | 2            | Case=Nom|Numb=Sing|Mood=Par|Tense=Fut|Voice=Act|Gend=Masc       | 1               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
| Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Dep|Gend=Fem          | 2            | Case=Acc|Numb=Sing                                              | 2               |
| Case=Nom|Numb=Sing|Mood=Adj|Tense=_|Voice=SemDep|Gend=Neut         | 2            | Case=Nom|Numb=Sing|Mood=Adj|Tense=_|Voice=Pass|Gend=Neut        | 2               |
| Numb=Sing|Mood=Ind|Tense=Pres|Voice=SemDep|Person=1                | 2            | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 2               |
| Case=Nom|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Dep|Gend=Masc         | 2            | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
|                                                                    |              | Case=Nom|Numb=Sing|Gend=Masc                                    | 1               |
| Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Com         | 2            | Case=Abl|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 2               |
| Numb=Plur|Mood=Sub|Tense=Perf|Voice=Dep|Person=3|Gend=Masc         | 2            | Deg=Pos                                                         | 1               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Perf|Voice=Dep|Person=2|Gend=Masc      | 1               |
| Numb=Plur|Mood=Ind|Tense=Impa|Voice=Act|Person=1                   | 2            | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 1               |
| Numb=Sing|Mood=Ind|Tense=PeriPqp|Voice=Pass|Person=3|Gend=Masc     | 2            | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
| Numb=Plur|Mood=Sub|Tense=Pres|Voice=SemDep|Person=1                | 2            | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 2               |
| Case=Gen|Numb=Plur|Deg=Sup|Gend=Fem                                | 2            | Case=Nom|Numb=Sing|Deg=Sup|Gend=Fem                             | 1               |
|                                                                    |              | Case=Gen|Numb=Plur|Deg=Pos|Gend=Fem                             | 1               |
| Numb=Sing|Mood=Sub|Tense=Pqp|Voice=SemDep|Person=3|Gend=Masc       | 2            | Case=Acc|Numb=Sing|Gend=MascNeut                                | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=SemDep|Person=3|Gend=Masc   | 1               |
| Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=MascNeut    | 2            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 1               |
|                                                                    |              | Case=Acc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut | 1               |
| Numb=Sing|Mood=Ind|Tense=Perf|Voice=SemDep|Person=3|Gend=Fem       | 2            | Mood=Inf|Tense=Perf|Voice=Act                                   | 2               |
| Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=SemDep|Gend=Masc      | 2            | Case=Nom|Numb=Plur                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Plur|Deg=Pos|Gend=Masc                            | 1               |
| Case=Gen|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=MascNeut     | 2            | Case=Gen|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Gen|Numb=Sing                                              | 1               |
| Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Dep|Gend=Neut         | 2            | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
| Case=Nom|Numb=Sing|Mood=Inf|Tense=Fut|Voice=Act|Gend=Masc          | 2            | Case=Nom|Numb=Sing|Mood=Par|Tense=Fut|Voice=Act|Gend=Masc       | 1               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
| Case=Dat|Numb=Plur|Mood=Adj|Tense=_|Voice=Dep|Gend=Com             | 2            | Case=Gen|Numb=Sing|Mood=Ger|Tense=_|Voice=Dep                   | 1               |
|                                                                    |              | Deg=Comp                                                        | 1               |
| Case=Nom|Numb=Sing|Mood=Par|Tense=Fut|Voice=Dep|Gend=Fem           | 2            | Case=Nom|Numb=Sing                                              | 1               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 1               |
| Case=Abl|Numb=Sing|Deg=Pos|Gend=Neut                               | 2            | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 2               |
| Numb=Plur|Mood=Ind|Tense=Fut|Voice=Dep|Person=1                    | 2            | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Dep|Person=1                | 2               |
| Numb=Sing|Mood=Sub|Tense=Perf|Voice=SemDep|Person=1                | 2            | Case=Acc|Numb=Sing                                              | 1               |
|                                                                    |              | Deg=Pos                                                         | 1               |
| Case=Nom|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Dep|Gend=Neut         | 2            | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 2               |
| Case=Voc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc        | 2            | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Numb=Plur|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 1               |
| Case=Nom|Numb=Plur|Deg=Sup|Gend=Fem                                | 2            | Case=Gen|Numb=Sing|Deg=Sup|Gend=Fem                             | 2               |
| Case=Acc|Numb=Plur|Mood=Adj|Tense=_|Voice=Dep|Gend=Fem             | 2            | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
| Numb=Sing|Mood=Ind|Tense=Fut|Voice=SemDep|Person=2                 | 2            | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Act|Person=2                 | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Dep|Person=2                 | 1               |
| Numb=Plur|Mood=Sub|Tense=Fut|Voice=Act|Person=3                    | 2            | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=3                | 1               |
| Numb=Sing|Mood=Sub|Tense=Impa|Voice=Pass|Person=2                  | 2            | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
| Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=SemDep|Gend=Masc      | 2            | Case=Acc|Numb=Plur|Gend=Masc                                    | 1               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
| Case=Gen|Numb=Sing|Deg=Pos|Gend=Masc                               | 2            | Case=Gen|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Acc|Numb=Sing                                              | 1               |
| Mood=Inf|Tense=Perf|Voice=Pass|Gend=Neut                           | 2            | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
| Numb=Sing|Mood=Ind|Tense=Fut|Voice=Dep|Person=2|Gend=Masc          | 2            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
| Numb=Sing|Mood=Ind|Tense=PeriPerf|Voice=Pass|Person=3|Gend=Neut    | 2            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 1               |
| Case=Nom|Numb=Plur|Mood=Inf|Tense=Perf|Voice=Pass|Gend=Fem         | 2            | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
| Case=Nom|Numb=Plur|Gend=Com                                        | 2            | Case=Nom|Numb=Plur|Gend=MascNeut                                | 2               |
| Numb=Sing|Mood=Sub|Tense=Perf|Voice=Dep|Person=3|Gend=Neut         | 2            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Fem       | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Neut      | 1               |
| Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=SemDep|Gend=Fem       | 2            | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
|                                                                    |              | Case=Nom|Numb=Plur                                              | 1               |
| Case=Dat|Numb=Plur|Gend=MascNeut                                   | 2            | Case=Abl|Numb=Plur|Gend=MascNeut                                | 2               |
| Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=Neut         | 2            | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Fem       | 1               |
| Case=Dat|Numb=Sing|Deg=Pos|Gend=Masc                               | 2            | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
| Case=Abl|Numb=Sing|Mood=Adj|Tense=_|Voice=Dep|Gend=MascNeut        | 2            | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
| Numb=Plur|Mood=Sub|Tense=Perf|Voice=Act|Person=2                   | 2            | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 2               |
| Numb=Sing|Mood=Sub|Tense=Perf|Voice=SemDep|Person=3|Gend=Masc      | 2            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
|                                                                    |              | Case=Acc|Numb=Plur|Gend=Neut                                    | 1               |
| Case=Dat|Numb=Sing|Mood=Par|Tense=Fut|Voice=Dep|Gend=MascNeut      | 2            | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Dep|Person=3                | 1               |
|                                                                    |              | Case=Abl|Numb=Sing|Mood=Par|Tense=Fut|Voice=Dep|Gend=MascNeut   | 1               |
| Numb=Sing|Mood=Sub|Tense=Pqp|Voice=Act|Person=2                    | 2            | Mood=Inf|Tense=Perf|Voice=Act                                   | 2               |
| Case=Loc|Numb=Sing|Gend=Fem                                        | 2            | Case=Dat|Numb=Sing|Gend=Fem                                     | 1               |
|                                                                    |              | Case=Gen|Numb=Sing|Gend=Fem                                     | 1               |
| Numb=Sing|Mood=Imp|Tense=Fut|Voice=Dep|Person=2                    | 2            | Case=Voc|Numb=Sing                                              | 1               |
|                                                                    |              | Case=Nom|Numb=Sing                                              | 1               |
| Case=Abl|Numb=Plur|Deg=Pos|Gend=Neut                               | 2            | Case=Abl|Numb=Plur|Deg=Pos|Gend=Com                             | 2               |
| Case=Voc|Numb=Plur|Gend=MascFem                                    | 2            | Case=Nom|Numb=Plur|Gend=MascFem                                 | 2               |
| Case=Acc|Numb=Sing|Mood=Ger|Tense=_|Voice=Dep                      | 2            | Case=Acc|Numb=Sing                                              | 2               |
| Case=Gen|Numb=Sing|Mood=Adj|Tense=_|Voice=Dep|Gend=MascNeut        | 2            | Case=Gen|Numb=Sing|Mood=Ger|Tense=_|Voice=Dep                   | 2               |
| Case=Nom|Numb=Sing|Mood=Adj|Tense=_|Voice=Dep|Gend=Masc            | 2            | Case=Nom|Numb=Sing|Deg=Pos|Gend=Masc                            | 2               |
| Numb=Plur|Mood=Ind|Tense=Fut|Voice=Pass|Person=1                   | 2            | Numb=Sing|Mood=Ind|Tense=Fut|Voice=Pass|Person=3                | 1               |
|                                                                    |              | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 1               |
| Numb=Plur|Mood=Ind|Tense=Impa|Voice=Pass|Person=1                  | 2            | Numb=Plur|Mood=Ind|Tense=Impa|Voice=Pass|Person=3               | 1               |
|                                                                    |              | Numb=Plur|Mood=Ind|Tense=Impa|Voice=Act|Person=1                | 1               |
| Case=Nom|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com          | 2            | Case=Nom|Numb=Sing|Deg=Pos|Gend=Com                             | 2               |
| Case=Gen|Numb=Plur|Mood=Par|Tense=Perf|Voice=Dep|Gend=MascNeut     | 2            | Case=Gen|Numb=Plur                                              | 2               |
| Numb=Plur|Mood=Sub|Tense=Perf|Voice=Dep|Person=3|Gend=Neut         | 2            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Fem       | 2               |
| Case=Acc|Numb=Plur|Mood=Inf|Tense=Fut|Voice=Act|Gend=Neut          | 2            | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 1               |
|                                                                    |              | Case=Acc|Numb=Plur                                              | 1               |
| Case=Nom|Numb=Sing|Mood=Adj|Tense=_|Voice=Dep|Gend=Fem             | 2            | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 2               |
| Numb=Plur|Mood=Sub|Tense=Pres|Voice=Pass|Person=2                  | 2            | Numb=Plur|Mood=Ind|Tense=Fut|Voice=Pass|Person=2                | 1               |
|                                                                    |              | Case=Dat|Numb=Sing                                              | 1               |
| Numb=Plur|Mood=Ind|Tense=Impa|Voice=Dep|Person=1                   | 2            | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Dep|Person=1                | 2               |
| Numb=Sing|Mood=Sub|Tense=PeriPqp|Voice=Pass|Person=3|Gend=Masc     | 2            | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
| Numb=Sing|Mood=Ind|Tense=Pqp|Voice=SemDep|Person=3|Gend=Masc       | 2            | Case=Dat|Numb=Plur|Deg=Pos|Gend=Com                             | 1               |
|                                                                    |              | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
| Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=MascNeut    | 2            | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
|                                                                    |              | Mood=Inf|Tense=Pres|Voice=Pass                                  | 1               |
| Case=Acc|Numb=Plur|Mood=Par|Tense=Fut|Voice=Act|Gend=Neut          | 2            | Case=Nom|Numb=Sing|Mood=Par|Tense=Fut|Voice=Act|Gend=Fem        | 1               |
|                                                                    |              | Numb=Sing|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 1               |
| Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=1                   | 2            | Numb=Plur|Mood=Ind|Tense=Pres|Voice=Act|Person=1                | 2               |
| Case=Gen|Numb=Plur|Mood=Par|Tense=Pres|Voice=SemDep|Gend=Com       | 1            | Case=Gen|Numb=Plur|Deg=Pos|Gend=Com                             | 1               |
| Numb=Sing|Mood=Ind|Tense=Fut|Voice=SemDep|Person=1                 | 1            | Numb=Plur|Mood=Ind|Tense=Fut|Voice=SemDep|Person=3              | 1               |
| Numb=Sing|Mood=Ind|Tense=PeriPerf|Voice=Pass|Person=3|Gend=Fem     | 1            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
| Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=SemDep|Gend=Neut      | 1            | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
| Case=Voc|Numb=Sing|Gend=MascFem                                    | 1            | Case=Nom|Numb=Sing|Gend=Masc                                    | 1               |
| Case=Abl|Numb=Plur|Mood=Adj|Tense=_|Voice=Dep|Gend=Com             | 1            | Case=Gen|Numb=Sing|Mood=Ger|Tense=_|Voice=Dep                   | 1               |
| Case=Gen|Numb=Plur|Mood=Par|Tense=Perf|Voice=Dep|Gend=Fem          | 1            | Case=Gen|Numb=Plur                                              | 1               |
| Numb=Sing|Mood=Sub|Tense=Pqp|Voice=Dep|Person=3|Gend=Neut          | 1            | Case=Acc|Numb=Sing|Deg=Pos|Gend=MascNeut                        | 1               |
| Case=Abl|Numb=Sing|Mood=Par|Tense=Pres|Voice=SemDep|Gend=Com       | 1            | Case=Abl|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=Com       | 1               |
| Numb=Plur|Mood=Ind|Tense=Pqp|Voice=Act|Person=2                    | 1            | Case=Gen|Numb=Sing                                              | 1               |
| Numb=Sing|Mood=Ind|Tense=Fut|Voice=Pass|Person=1|Gend=Fem          | 1            | Case=Acc|Numb=Plur                                              | 1               |
| Numb=Plur|Mood=Ind|Tense=PeriPqp|Voice=Pass|Person=3|Gend=Masc     | 1            | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
| Case=Nom|Numb=Plur|Mood=Inf|Tense=Perf|Voice=Dep|Gend=Neut         | 1            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Fem       | 1               |
| Numb=Sing|Mood=Imp|Tense=Pres|Voice=SemDep|Person=2                | 1            | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Case=Dat|Numb=Plur|Mood=Par|Tense=Fut|Voice=Act|Gend=Com           | 1            | Numb=Sing|Mood=Ind|Tense=Pres|Voice=Act|Person=2                | 1               |
| Numb=Sing|Mood=Sub|Tense=Fut|Voice=Dep|Person=1|Gend=Fem           | 1            | Case=Abl|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Numb=Plur|Mood=Ind|Tense=Perf|Voice=SemDep|Person=3|Gend=Fem       | 1            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Fem       | 1               |
| Case=Nom|Numb=Plur|Mood=Par|Tense=Pres|Voice=Dep|Gend=Neut         | 1            | Case=Nom|Numb=Plur|Gend=Neut                                    | 1               |
| Numb=Sing|Mood=Sub|Tense=Pqp|Voice=Dep|Person=2|Gend=Masc          | 1            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
| Case=Nom|Numb=Plur|Mood=Adj|Tense=_|Voice=Dep|Gend=Masc            | 1            | Case=Nom|Numb=Plur                                              | 1               |
| Numb=Sing|Mood=Ind|Tense=PeriFut|Voice=Dep|Person=1|Gend=Masc      | 1            | Case=Gen|Numb=Sing                                              | 1               |
| Case=Nom|Numb=Sing|Mood=Inf|Tense=Fut|Voice=Act|Gend=Fem           | 1            | Case=Nom|Numb=Sing                                              | 1               |
| Case=Dat|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=Fem          | 1            | Case=Gen|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
| Case=Acc|Numb=Plur|Mood=Inf|Tense=Perf|Voice=Dep|Gend=Neut         | 1            | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Numb=Sing|Mood=Sub|Tense=Pres|Voice=SemDep|Person=2                | 1            | Numb=Sing|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 1               |
| Case=Acc|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=Com          | 1            | Case=Acc|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 1               |
| Numb=Sing|Mood=Sub|Tense=PeriPerf|Voice=Pass|Person=3|Gend=Masc    | 1            | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
| Case=Abl|Numb=Sing|Deg=Comp|Gend=MascNeut                          | 1            | Case=Abl|Numb=Sing|Deg=Sup|Gend=MascNeut                        | 1               |
| Numb=Sing|Mood=Sub|Tense=PeriPqp|Voice=Dep|Person=3|Gend=Fem       | 1            | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Case=Voc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=Fem          | 1            | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Case=Nom|Numb=Plur|Gend=MascNeut                                   | 1            | Case=Acc|Numb=Plur|Gend=Neut                                    | 1               |
| Case=Nom|Numb=Sing|Mood=Inf|Tense=Perf|Voice=Dep|Gend=Fem          | 1            | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Numb=Plur|Mood=Ind|Tense=PeriPqp|Voice=Pass|Person=3|Gend=Neut     | 1            | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 1               |
| Case=Gen|Numb=Sing|Mood=Par|Tense=Fut|Voice=Dep|Gend=Fem           | 1            | Case=Gen|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Case=Acc|Numb=Plur|Mood=Inf|Tense=Perf|Voice=Dep|Gend=Fem          | 1            | Case=Acc|Numb=Plur                                              | 1               |
| Numb=Plur|Mood=Sub|Tense=Pqp|Voice=Act|Person=3                    | 1            | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=3                | 1               |
| Numb=Plur|Mood=Sub|Tense=PeriPqp|Voice=Dep|Person=3|Gend=Masc      | 1            | Case=Nom|Numb=Plur|Gend=Masc                                    | 1               |
| Numb=Sing|Mood=Sub|Tense=PeriPerf|Voice=Pass|Person=3|Gend=Fem     | 1            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
| Numb=Sing|Mood=Sub|Tense=Fut|Voice=Dep|Person=2|Gend=Fem           | 1            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Fem       | 1               |
| Numb=Plur|Mood=Ind|Tense=Pqp|Voice=Act|Person=1                    | 1            | Numb=Plur|Mood=Sub|Tense=Pres|Voice=Act|Person=1                | 1               |
| Case=Gen|Numb=Sing|Mood=Par|Tense=Fut|Voice=Dep|Gend=MascNeut      | 1            | Case=Abl|Numb=Sing|Mood=Par|Tense=Pres|Voice=Dep|Gend=Com       | 1               |
| Numb=Plur|Mood=Ind|Tense=Impa|Voice=SemDep|Person=2                | 1            | Numb=Sing|Mood=Sub|Tense=Perf|Voice=Act|Person=3                | 1               |
| Numb=Plur|Mood=Sub|Tense=Pres|Voice=Dep|Person=2                   | 1            | Deg=Pos                                                         | 1               |
| Numb=Plur|Mood=Ind|Tense=Fut|Voice=Dep|Person=3|Gend=Masc          | 1            | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
| Case=Gen|Numb=Sing|Mood=Par|Tense=Perf|Voice=SemDep|Gend=MascNeut  | 1            | Case=Nom|Numb=Plur                                              | 1               |
| Case=Voc|Numb=Plur|Deg=Sup|Gend=Masc                               | 1            | Deg=Sup                                                         | 1               |
| Numb=Plur|Mood=Sub|Tense=Perf|Voice=SemDep|Person=3|Gend=Fem       | 1            | Case=Nom|Numb=Plur|Deg=Pos|Gend=Fem                             | 1               |
| Case=Voc|Numb=Plur|Deg=Pos|Gend=Neut                               | 1            | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 1               |
| Numb=Plur|Mood=Sub|Tense=Perf|Voice=Dep|Person=1|Gend=Masc         | 1            | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Dep|Gend=Masc      | 1               |
| Numb=Sing|Mood=Sub|Tense=Impa|Voice=SemDep|Person=2                | 1            | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
| Case=Acc|Numb=Plur|Mood=Par|Tense=Pres|Voice=Dep|Gend=Com          | 1            | Case=Abl|Numb=Plur|Gend=Com                                     | 1               |
| Case=Nom|Numb=Plur|Mood=Par|Tense=Fut|Voice=Act|Gend=Fem           | 1            | Case=Nom|Numb=Plur                                              | 1               |
| Numb=Sing|Mood=Sub|Tense=Perf|Voice=Dep|Person=1|Gend=Masc         | 1            | Case=Nom|Numb=Sing                                              | 1               |
| Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=SemDep|Gend=Fem       | 1            | Case=Acc|Numb=Sing                                              | 1               |
| Case=Acc|Numb=Sing|Mood=Inf|Tense=Fut|Voice=SemDep|Gend=MascNeut   | 1            | Case=Acc|Numb=Sing|Mood=Inf|Tense=Fut|Voice=SemDep|Gend=Fem     | 1               |
| Numb=Plur|Mood=Ind|Tense=Fut|Voice=Pass|Person=3|Gend=Masc         | 1            | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
| Case=Abl|Numb=Plur|Deg=Pos|Gend=Fem                                | 1            | Case=Abl|Numb=Plur|Deg=Pos|Gend=Com                             | 1               |
| Case=Acc|Numb=Sing|Mood=Adj|Tense=_|Voice=Dep|Gend=Fem             | 1            | Case=Acc|Numb=Sing                                              | 1               |
| Case=Abl|Numb=Sing|Gend=Neut                                       | 1            | Case=Nom|Numb=Sing|Gend=Masc                                    | 1               |
| Numb=Sing|Mood=Ind|Tense=Pqp|Voice=Dep|Person=1|Gend=Masc          | 1            | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=Masc      | 1               |
| Case=Nom|Numb=Plur|Deg=Comp|Gend=Fem                               | 1            | Case=Acc|Numb=Plur|Gend=Masc                                    | 1               |
| Numb=Plur|Mood=Ind|Tense=Pres|Voice=Dep|Person=2                   | 1            | Case=Gen|Numb=Sing|Mood=Ger|Tense=_|Voice=Dep                   | 1               |
| Case=Abl|Numb=Plur|Mood=Par|Tense=Fut|Voice=Act|Gend=Com           | 1            | Case=Dat|Numb=Plur                                              | 1               |
| Case=Acc|Numb=Sing|Mood=Inf|Tense=Fut|Voice=Pass                   | 1            | Case=Acc|Numb=Sing                                              | 1               |
| Case=Acc|Numb=Plur|Mood=Inf|Tense=Perf|Voice=SemDep|Gend=Masc      | 1            | Case=Acc|Numb=Plur|Deg=Pos|Gend=Masc                            | 1               |
| Case=Acc|Numb=Plur|Mood=Par|Tense=Fut|Voice=SemDep|Gend=Masc       | 1            | Case=Acc|Numb=Plur                                              | 1               |
| Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=2|Gend=Fem         | 1            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
| Numb=Sing|Mood=Ind|Tense=Perf|Voice=SemDep|Person=2|Gend=Masc      | 1            | Case=Voc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
| Case=Acc|Numb=Plur|Mood=Par|Tense=Pres|Voice=SemDep|Gend=Neut      | 1            | Case=Acc|Numb=Plur|Deg=Pos|Gend=Neut                            | 1               |
| Case=Acc|Numb=Sing|Mood=Inf|Tense=PeriPqp|Voice=Pass|Gend=Fem      | 1            | Case=Acc|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Numb=Plur|Mood=Sub|Tense=Pqp|Voice=Act|Person=2                    | 1            | Numb=Plur|Mood=Sub|Tense=Pqp|Voice=Act|Person=3                 | 1               |
| Case=Dat|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Neut        | 1            | Case=Abl|Numb=Plur                                              | 1               |
| Case=Acc|Numb=Plur|Mood=Par|Tense=Fut|Voice=Dep|Gend=Masc          | 1            | Case=Acc|Numb=Plur                                              | 1               |
| Case=Voc|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=Masc         | 1            | Numb=Plur|Mood=Imp|Tense=Pres|Voice=Act|Person=2                | 1               |
| Case=Acc|Numb=Sing|Mood=Par|Tense=Pres|Voice=SemDep|Gend=MascFem   | 1            | Case=Acc|Numb=Sing|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 1               |
| Numb=Sing|Mood=Sub|Tense=Perf|Voice=Pass|Person=1|Gend=Fem         | 1            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
| Case=Acc|Numb=Plur|Mood=Adj|Tense=_|Voice=Dep|Gend=Masc            | 1            | Deg=Sup                                                         | 1               |
| Numb=Plur|Mood=Sub|Tense=Perf|Voice=Pass|Person=1|Gend=Masc        | 1            | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
| Numb=Plur|Mood=Ind|Tense=Pres|Voice=SemDep|Person=2                | 1            | Case=Dat|Numb=Sing|Gend=Com                                     | 1               |
| Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=MascNeut    | 1            | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
| Case=Dat|Numb=Sing|Mood=Ger|Tense=_|Voice=Dep                      | 1            | Case=Abl|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                   | 1               |
| Numb=Plur|Mood=Sub|Tense=Fut|Voice=Pass|Person=3|Gend=Neut         | 1            | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Neut     | 1               |
| Numb=Sing|Mood=Sub|Tense=Pqp|Voice=Pass|Person=2|Gend=Masc         | 1            | Case=Nom|Numb=Sing|Mood=Par|Tense=Perf|Voice=Pass|Gend=Masc     | 1               |
| Numb=Sing|Mood=Ind|Tense=PeriFut|Voice=Pass|Person=3|Gend=Fem      | 1            | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Case=Gen|Numb=Sing|Deg=Pos|Gend=MascFem                            | 1            | Case=Nom|Numb=Sing|Deg=Comp|Gend=Neut                           | 1               |
| Case=Acc|Numb=Plur|Mood=Par|Tense=Perf|Voice=SemDep|Gend=Neut      | 1            | Case=Acc|Numb=Plur                                              | 1               |
| Numb=Sing|Mood=Ind|Tense=PeriPerf|Voice=Dep|Person=3|Gend=Masc     | 1            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=3|Gend=Masc      | 1               |
| Numb=Sing|Tense=_|Voice=Act                                        | 1            | Mood=Inf|Tense=Pres|Voice=Act                                   | 1               |
| Numb=Plur|Mood=Ind|Tense=Fut|Voice=Dep|Person=2                    | 1            | Case=Acc|Numb=Sing                                              | 1               |
| Numb=Plur|Mood=Ind|Tense=Perf|Voice=Dep|Person=2|Gend=Masc         | 1            | Numb=Plur|Mood=Ind|Tense=Perf|Voice=Dep|Person=1|Gend=Masc      | 1               |
| Case=Voc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem         | 1            | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
| Case=Voc|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem      | 1            | Case=Acc|Numb=Plur|Mood=Par|Tense=Pres|Voice=Act|Gend=MascFem   | 1               |
| Case=Voc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Dep|Gend=Masc         | 1            | Case=Gen|Numb=Sing                                              | 1               |
| Case=Abl|Numb=Sing|Mood=Ger|Tense=_|Voice=SemDep                   | 1            | Case=Abl|Numb=Sing|Mood=Ger|Tense=_|Voice=Act                   | 1               |
| Case=Dat|Numb=Sing|Mood=Par|Tense=Perf|Voice=SemDep|Gend=MascNeut  | 1            | Case=Nom|Numb=Sing|Deg=Pos|Gend=Neut                            | 1               |
| Numb=Plur|Mood=Ind|Tense=Perf|Voice=Pass|Person=3                  | 1            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
| Numb=Sing|Mood=Sub|Tense=Fut|Voice=Act|Person=2                    | 1            | Case=Acc|Numb=Plur                                              | 1               |
| Case=Nom|Numb=Plur|Mood=Par|Tense=Fut|Voice=Dep|Gend=Masc          | 1            | Case=Nom|Numb=Plur                                              | 1               |
| Case=Acc|Numb=Sing|Mood=Inf|Tense=Perf|Voice=SemDep|Gend=Fem       | 1            | Case=Acc|Numb=Sing                                              | 1               |
| Numb=Sing|Mood=Ind|Tense=Perf|Voice=Dep|Person=1                   | 1            | Case=Acc|Numb=Plur                                              | 1               |
| Numb=Plur|Mood=Ind|Tense=Fut|Voice=Pass|Person=1|Gend=Fem          | 1            | Case=Nom|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Fem      | 1               |
| Numb=Sing|Mood=Ind|Tense=Pqp|Voice=Pass|Person=3                   | 1            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Masc     | 1               |
| Case=Nom|Numb=Plur|Deg=Pos|Gend=Com                                | 1            | Case=Nom|Numb=Plur                                              | 1               |
| Case=Voc|Numb=Plur|Mood=Par|Tense=Fut|Voice=Act|Gend=Fem           | 1            | Case=Gen|Numb=Sing                                              | 1               |
| Case=Voc|Numb=Plur|Mood=Par|Tense=Perf|Voice=Pass|Gend=Neut        | 1            | Numb=Sing|Mood=Ind|Tense=Perf|Voice=Pass|Person=3|Gend=Fem      | 1               |
| Case=Gen|Numb=Sing|Mood=Par|Tense=Perf|Voice=Dep|Gend=Fem          | 1            | Case=Gen|Numb=Sing                                              | 1               |
| Numb=Sing|Mood=Ind|Tense=Pqp|Voice=Dep|Person=3|Gend=Fem           | 1            | Case=Nom|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Case=Loc|Numb=Sing|Deg=Pos|Gend=Fem                                | 1            | Case=Gen|Numb=Sing|Deg=Pos|Gend=Fem                             | 1               |
| Numb=Plur|Mood=Ind|Tense=Pres|Voice=Pass|Person=3                  | 1            | Case=Nom|Numb=Plur                                              | 1               |
| Case=Acc|Numb=Plur|Mood=Par|Tense=Fut|Voice=Act|Gend=Masc          | 1            | Case=Acc|Numb=Plur|Deg=Pos|Gend=Masc                            | 1               |
| Case=Voc|Numb=Sing|Deg=Sup|Gend=Neut                               | 1            | Deg=Sup                                                         | 1               |
