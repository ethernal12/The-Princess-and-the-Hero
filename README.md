# The Princess and the Hero
### Konfiguracije igre:

* Demo GIF igre: ![Demo of Princess and the Hero](https://github.com/ethernal12/The-Princess-and-the-Hero/blob/implement_end_game_logic/game_demo.gif){:width="50px"}

* Kloniraj REPO in v root direktoriju zaženi \__main__.py z ukazom: 
~~~
python src
~~~
* Igra ne vsebuje zunanjih knjižnic
### Kako igrati igro:
* Igra se začne z začetno postavitvijo heroja, princeske in barab na igrišču.
* Igralec mora vtipkati željeno pozicijo dx in dy za premik heroja. Premik je omejen na razpon +2 , -2 koraka.
* Če hočete končati igro in terminal, kadarkoli kot input podajte črko q.
### Cilj, nasveti in konec igre:
* Cilj igre je priti do princese, ki je označena s srcem, jo tako rešiti pred barabami, ki jo hočejo uloviti in tako napreduješ v drugi nivo.

* Če se ti med potjo približa baraba na en korak razdalje je igre konec, prav tako, če medtem barabe ulovijo princeso je igre konec.
* Če ti uspe priti do princese, preden presežeš število 5 korakov, greš v naslednji nivo, kjer se polje igrišča zoži in število barab podvoji.
* Igro končaš, če prideš v 8 Nivo.

***Nasvet: Manj korakov porabiš, da prideš po princese, večji je Score***
