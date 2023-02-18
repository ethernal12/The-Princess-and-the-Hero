# The Princess and the Hero

### Konfiguracije igre:

* Demo GIF igre:

<img src="https://github.com/ethernal12/The-Princess-and-the-Hero)GIF_game_demo.gif" width="500" height="400">

* Kloniraj REPO in v root direktoriju zaženi \__main__.py z ukazom:

* inštaliraj zunanje knjižnice z ukazom:

~~~
pip install -r requirements.txt

~~~

* Poženi igro z ukazom:

~~~
python src
~~~

### Kako igrati igro:

* Igra se začne z začetno postavitvijo heroja, princeske in barab na igrišču.
* Igralec mora vtipkati željeno pozicijo dx in dy za premik heroja. Premik je omejen na razpon +2 , -2 koraka.
* Če hočete končati igro in terminal, kadarkoli kot input podajte črko q.

### Cilj, nasveti in konec igre:

* Cilj igre je priti do princese, ki je označena z ♀ simbolom, jo tako rešiti pred barabami, ki jo hočejo uloviti in
  tako napreduješ v drugi nivo.

* Če se ti med potjo približa baraba na en korak razdalje zgubiš življenje, na voljo imaš 3 življena.
* Če barabe ulovijo princesko je igre konec.
* Če ti uspe priti do princese, preden presežeš število 5 korakov, greš v naslednji nivo, kjer se polje igrišča zoži in
  število barab podvoji.
* Igro končaš, če prideš v 8 Nivo.

***Nasvet: Manj korakov porabiš, da prideš po princese, večji je tvoj Score***
