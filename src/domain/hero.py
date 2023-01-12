from dataclasses import dataclass


@dataclass
class Hero:
    x: int
    y: int
    tocke: int = 0
    st_zivljenj: int = 3
    # če uporabim post init za generiranje življenj heroju se mi pri vsaki new_game usvari ponovno 3 življenja,
    # hočem pa da ima heroj na celotno igro 3 življenja
    zivljenja_list = ['\u2665 ' for _ in range(st_zivljenj)]

    def premik(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def odtrani_zivljenje(self):
        self.zivljenja_list.remove('\u2665 ')

    def dodaj_zivljenje(self):
        self.zivljenja_list.append('\u2665 ')

    def st_ostalih_zivljenj(self):
        return ' '.join(self.zivljenja_list)
