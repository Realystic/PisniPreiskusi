import sqlite3

def ustvari_povezavo():
    """Ustvari povezavo z bazo podatkov in omogoči uporabo tujih ključev."""
    pov = sqlite3.connect("izpiti.sqlite")
    pov.execute("PRAGMA foreign_keys = ON;")
    return pov

class Letnik:
    """Razred, ki predstavlja tabelo letniki in omogoča dodajanje, spreminjanje, brisanje in izpisovanje (enega ali vseh) letnikov."""

    def __init__(self, letnik, id=None):
        self.id = id
        self.letnik = letnik

    def __str__(self):
        return f"{self.id}: {self.letnik}"


    def shrani(self, pov):
        """Ustvari ali posodobi letnik v bazi."""
        kaz = pov.cursor()

        if self.id is None:
            # INSERT
            kaz.execute("""
                INSERT INTO letniki (letnik)
                VALUES (?)
            """, (self.letnik,))
            self.id = kaz.lastrowid
        else:
            # UPDATE
            kaz.execute("""
                UPDATE letniki
                SET letnik = ?
                WHERE id = ?
            """, (self.letnik, self.id))

        pov.commit()

    def izbrisi(self, pov):
        """Izbriše letnik iz baze."""
        if self.id is None:
            return

        kaz = pov.cursor()
        kaz.execute("DELETE FROM letniki WHERE id = ?", (self.id,))
        pov.commit()
        self.id = None

    @staticmethod
    def najdi(pov, id):
        """Najde letnik po ID-ju in vrne objekt Letnik."""
        kaz = pov.cursor()
        kaz.execute("SELECT id, letnik FROM letniki WHERE id = ?", (id,))
        vrstica = kaz.fetchone()

        if vrstica:
            return Letnik(vrstica[1], id=vrstica[0])
        return None

    @staticmethod
    def vsi(pov):
        """Vrne seznam vseh letnikov kot objektov."""
        kaz = pov.cursor()
        kaz.execute("SELECT id, letnik FROM letniki ORDER BY letnik ASC")
        vrstice = kaz.fetchall()

        return [Letnik(v[1], id=v[0]) for v in vrstice]


class Predmet:
    """Razred, ki predstavlja tabelo predmeti in omogoča dodajanje, spreminjanje, brisanje in izpisovanje (enega ali vseh) predmetov."""

    def __init__(self, ime, id_letnik, id=None):
        self.id = id
        self.ime = ime
        self.id_letnik = id_letnik
    
    def __str__(self):
        return f"{self.id}: {self.ime} (letnik {self.id_letnik})"

    def shrani(self, pov):
        """Ustvari ali posodobi predmet v bazi."""
        kaz = pov.cursor()

        if self.id is None:
            # INSERT
            kaz.execute("""
                INSERT INTO predmeti (ime, id_letnik)
                VALUES (?, ?)
            """, (self.ime, self.id_letnik))
            self.id = kaz.lastrowid
        else:
            # UPDATE
            kaz.execute("""
                UPDATE predmeti
                SET ime = ?, id_letnik = ?
                WHERE id = ?
            """, (self.ime, self.id_letnik, self.id))

        pov.commit()

    def izbrisi(self, pov):
        """Izbriše predmet iz baze."""
        if self.id is None:
            return

        kaz = pov.cursor()
        kaz.execute("DELETE FROM predmeti WHERE id = ?", (self.id,))
        pov.commit()
        self.id = None

    @staticmethod
    def najdi(pov, id):
        """Najde predmet po ID-ju in vrne objekt Predmet."""
        kaz = pov.cursor()
        kaz.execute("""
            SELECT id, ime, id_letnik
            FROM predmeti
            WHERE id = ?
        """, (id,))
        vrstica = kaz.fetchone()

        if vrstica:
            return Predmet(vrstica[1], vrstica[2], id=vrstica[0])
        return None

    @staticmethod
    def vsi(pov):
        """Vrne seznam vseh predmetov."""
        kaz = pov.cursor()
        kaz.execute("SELECT id, ime, id_letnik FROM predmeti ORDER BY ime ASC")
        vrstice = kaz.fetchall()

        return [Predmet(v[1], v[2], id=v[0]) for v in vrstice]

    @staticmethod
    def za_letnik(pov, id_letnik):
        """Vrne seznam predmetov za določen letnik."""
        kaz = pov.cursor()
        kaz.execute("""
            SELECT id, ime, id_letnik
            FROM predmeti
            WHERE id_letnik = ?
            ORDER BY ime ASC
        """, (id_letnik,))
        vrstice = kaz.fetchall()
        return [Predmet(v[1], v[2], id=v[0]) for v in vrstice]


class Tema:
    """Razred, ki predstavlja tabelo teme in omogoča dodajanje, spreminjanje,
    brisanje ter pridobivanje (posamezne ali vseh) tem iz baze."""

    def __init__(self, tema, id_predmet, id=None):
        self.id = id
        self.tema = tema
        self.id_predmet = id_predmet

    
    def __str__(self):
        return f"{self.id}: {self.tema} (predmet {self.id_predmet})"

    def shrani(self, pov):
        """Ustvari novo temo ali posodobi obstoječo v bazi."""
        kaz = pov.cursor()

        if self.id is None:
            # INSERT
            kaz.execute("""
                INSERT INTO teme (tema, id_predmet)
                VALUES (?, ?)
            """, (self.tema, self.id_predmet))
            self.id = kaz.lastrowid
        else:
            # UPDATE
            kaz.execute("""
                UPDATE teme
                SET tema = ?, id_predmet = ?
                WHERE id = ?
            """, (self.tema, self.id_predmet, self.id))

        pov.commit()

    def izbrisi(self, pov):
        """Izbriše temo iz baze."""
        if self.id is None:
            return

        kaz = pov.cursor()
        kaz.execute("DELETE FROM teme WHERE id = ?", (self.id,))
        pov.commit()
        self.id = None

    @staticmethod
    def najdi(pov, id):
        """Najde temo po ID-ju in vrne objekt Tema."""
        kaz = pov.cursor()
        kaz.execute("""
            SELECT id, tema, id_predmet
            FROM teme
            WHERE id = ?
        """, (id,))
        vrstica = kaz.fetchone()

        if vrstica:
            return Tema(vrstica[1], vrstica[2], id=vrstica[0])
        return None

    @staticmethod
    def vse(pov):
        """Vrne seznam vseh tem kot objektov."""
        kaz = pov.cursor()
        kaz.execute("SELECT id, tema, id_predmet FROM teme ORDER BY tema ASC")
        vrstice = kaz.fetchall()

        return [Tema(v[1], v[2], id=v[0]) for v in vrstice]
    
    @staticmethod
    def za_predmet(pov, id_predmet):
        """Vrne seznam tem za določen predmet."""
        kaz = pov.cursor()
        kaz.execute("""
            SELECT id, tema, id_predmet
            FROM teme
            WHERE id_predmet = ?
            ORDER BY tema ASC
        """, (id_predmet,))
        vrstice = kaz.fetchall()
        return [Tema(v[1], v[2], id=v[0]) for v in vrstice]
    
    @staticmethod
    def za_preizkus(pov, id_preizkus):
        """Vrne seznam tem, ki pripadajo določenemu pisnemu preizkusu."""
        kaz = pov.cursor()
        kaz.execute("""
            SELECT t.id, t.tema, t.id_predmet
            FROM teme t
            JOIN povezovalna_teme_testi ptt ON t.id = ptt.id_teme
            WHERE ptt.id_test = ?
            ORDER BY t.tema ASC
        """, (id_preizkus,))
        vrstice = kaz.fetchall()

        return [Tema(v[1], v[2], id=v[0]) for v in vrstice]

class Predavalnica:
    """Razred, ki predstavlja tabelo predavalnice in omogoča dodajanje,
    spreminjanje, brisanje ter pridobivanje (posamezne ali vseh) predavalnic."""

    def __init__(self, ime, id=None):
        self.id = id
        self.ime = ime
    
    def __str__(self):
        return f"{self.id}: {self.ime}"

    def shrani(self, pov):
        """Ustvari novo predavalnico ali posodobi obstoječo v bazi."""
        kaz = pov.cursor()

        if self.id is None:
            # INSERT
            kaz.execute("""
                INSERT INTO predavalnice (ime)
                VALUES (?)
            """, (self.ime,))
            self.id = kaz.lastrowid
        else:
            # UPDATE
            kaz.execute("""
                UPDATE predavalnice
                SET ime = ?
                WHERE id = ?
            """, (self.ime, self.id))

        pov.commit()

    def izbrisi(self, pov):
        """Izbriše predavalnico iz baze."""
        if self.id is None:
            return

        kaz = pov.cursor()
        kaz.execute("DELETE FROM predavalnice WHERE id = ?", (self.id,))
        pov.commit()
        self.id = None

    @staticmethod
    def najdi(pov, id):
        """Najde predavalnico po ID-ju in vrne objekt Predavalnica."""
        kaz = pov.cursor()
        kaz.execute("""
            SELECT id, ime
            FROM predavalnice
            WHERE id = ?
        """, (id,))
        vrstica = kaz.fetchone()

        if vrstica:
            return Predavalnica(vrstica[1], id=vrstica[0])
        return None

    @staticmethod
    def vse(pov):
        """Vrne seznam vseh predavalnic kot objektov."""
        kaz = pov.cursor()
        kaz.execute("SELECT id, ime FROM predavalnice ORDER BY ime ASC")
        vrstice = kaz.fetchall()

        return [Predavalnica(v[1], id=v[0]) for v in vrstice]


class TipTesta:
    """Razred, ki predstavlja tabelo tipi_testov in omogoča dodajanje,
    spreminjanje, brisanje ter pridobivanje (posameznega ali vseh) tipov testov."""

    def __init__(self, tip, id=None):
        self.id = id
        self.tip = tip

    def __str__(self):
        return f"{self.id}: {self.tip}"

    def shrani(self, pov):
        """Ustvari nov tip testa ali posodobi obstoječega v bazi."""
        kaz = pov.cursor()

        if self.id is None:
            kaz.execute("""
                INSERT INTO tipi_testov (tip)
                VALUES (?)
            """, (self.tip,))
            self.id = kaz.lastrowid
        else:
            kaz.execute("""
                UPDATE tipi_testov
                SET tip = ?
                WHERE id = ?
            """, (self.tip, self.id))

        pov.commit()

    def izbrisi(self, pov):
        """Izbriše tip testa iz baze."""
        if self.id is None:
            return

        kaz = pov.cursor()
        kaz.execute("DELETE FROM tipi_testov WHERE id = ?", (self.id,))
        pov.commit()
        self.id = None

    @staticmethod
    def najdi(pov, id):
        """Najde tip testa po ID-ju in vrne objekt TipTesta."""
        kaz = pov.cursor()
        kaz.execute("""
            SELECT id, tip
            FROM tipi_testov
            WHERE id = ?
        """, (id,))
        vrstica = kaz.fetchone()

        if vrstica:
            return TipTesta(vrstica[1], id=vrstica[0])
        return None

    @staticmethod
    def vsi(pov):
        """Vrne seznam vseh tipov testov kot objektov."""
        kaz = pov.cursor()
        kaz.execute("SELECT id, tip FROM tipi_testov ORDER BY tip ASC")
        vrstice = kaz.fetchall()

        return [TipTesta(v[1], id=v[0]) for v in vrstice]


class PisniPreizkus:
    """Razred, ki predstavlja tabelo pisni_preizkusi in omogoča dodajanje,
    spreminjanje, brisanje ter pridobivanje (posameznega ali vseh) pisnih preizkusov."""

    def __init__(self, datum, ura, id_predavalnica, id_letnik, id_predmet, id_tip, id=None):
        self.id = id
        self.datum = datum
        self.ura = ura
        self.id_predavalnica = id_predavalnica
        self.id_letnik = id_letnik
        self.id_predmet = id_predmet
        self.id_tip = id_tip

    def __str__(self):
        return (
            f"{self.id}: {self.datum} ob {self.ura} "
            f"(letnik {self.id_letnik}, predmet {self.id_predmet}, "
            f"predavalnica {self.id_predavalnica}, tip {self.id_tip})"
        )

    def shrani(self, pov):
        """Ustvari nov pisni preizkus ali posodobi obstoječega v bazi."""
        kaz = pov.cursor()

        if self.id is None:
            kaz.execute("""
                INSERT INTO pisni_preizkusi (datum, ura, id_predavalnica, id_letnik, id_predmet, id_tip)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (self.datum, self.ura, self.id_predavalnica, self.id_letnik, self.id_predmet, self.id_tip))
            self.id = kaz.lastrowid
        else:
            kaz.execute("""
                UPDATE pisni_preizkusi
                SET datum = ?, ura = ?, id_predavalnica = ?, id_letnik = ?, id_predmet = ?, id_tip = ?
                WHERE id = ?
            """, (self.datum, self.ura, self.id_predavalnica, self.id_letnik, self.id_predmet, self.id_tip, self.id))

        pov.commit()

    def izbrisi(self, pov):
        """Izbriše pisni preizkus iz baze."""
        if self.id is None:
            return

        kaz = pov.cursor()
        kaz.execute("DELETE FROM pisni_preizkusi WHERE id = ?", (self.id,))
        pov.commit()
        self.id = None

    @staticmethod
    def najdi(pov, id):
        """Najde pisni preizkus po ID-ju in vrne objekt PisniPreizkus."""
        kaz = pov.cursor()
        kaz.execute("""
            SELECT id, datum, ura, id_predavalnica, id_letnik, id_predmet, id_tip
            FROM pisni_preizkusi
            WHERE id = ?
        """, (id,))
        vrstica = kaz.fetchone()

        if vrstica:
            return PisniPreizkus(
                vrstica[1], vrstica[2], vrstica[3],
                vrstica[4], vrstica[5], vrstica[6],
                id=vrstica[0]
            )
        return None

    @staticmethod
    def vsi(pov):
        """Vrne seznam vseh pisnih preizkusov kot objektov."""
        kaz = pov.cursor()
        kaz.execute("""
            SELECT id, datum, ura, id_predavalnica, id_letnik, id_predmet, id_tip
            FROM pisni_preizkusi
            ORDER BY datum ASC, ura ASC
        """)
        vrstice = kaz.fetchall()

        return [
            PisniPreizkus(v[1], v[2], v[3], v[4], v[5], v[6], id=v[0])
            for v in vrstice
        ]

    @staticmethod
    def na_dan(pov, datum):
        """Vrne vse pisne preizkuse na določen datum (YYYY-MM-DD)."""
        kaz = pov.cursor()
        kaz.execute("""
            SELECT id, datum, ura, id_predavalnica, id_letnik, id_predmet, id_tip
            FROM pisni_preizkusi
            WHERE datum = ?
            ORDER BY ura ASC
        """, (datum,))
        vrstice = kaz.fetchall()

        return [
            PisniPreizkus(v[1], v[2], v[3], v[4], v[5], v[6], id=v[0])
            for v in vrstice
        ]

    @staticmethod
    def za_predmet(pov, id_predmet):
        """Vrne vse pisne preizkuse za določen predmet."""
        kaz = pov.cursor()
        kaz.execute("""
            SELECT id, datum, ura, id_predavalnica, id_letnik, id_predmet, id_tip
            FROM pisni_preizkusi
            WHERE id_predmet = ?
            ORDER BY datum ASC, ura ASC
        """, (id_predmet,))
        vrstice = kaz.fetchall()

        return [
            PisniPreizkus(v[1], v[2], v[3], v[4], v[5], v[6], id=v[0])
            for v in vrstice
        ]

    @staticmethod
    def za_letnik(pov, id_letnik):
        """Vrne vse pisne preizkuse za določen letnik."""
        kaz = pov.cursor()
        kaz.execute("""
            SELECT id, datum, ura, id_predavalnica, id_letnik, id_predmet, id_tip
            FROM pisni_preizkusi
            WHERE id_letnik = ?
            ORDER BY datum ASC, ura ASC
        """, (id_letnik,))
        vrstice = kaz.fetchall()

        return [
            PisniPreizkus(v[1], v[2], v[3], v[4], v[5], v[6], id=v[0])
            for v in vrstice
        ]

    @staticmethod
    def za_predavalnico(pov, id_predavalnica):
        """Vrne vse pisne preizkuse v določeni predavalnici."""
        kaz = pov.cursor()
        kaz.execute("""
            SELECT id, datum, ura, id_predavalnica, id_letnik, id_predmet, id_tip
            FROM pisni_preizkusi
            WHERE id_predavalnica = ?
            ORDER BY datum ASC, ura ASC
        """, (id_predavalnica,))
        vrstice = kaz.fetchall()

        return [
            PisniPreizkus(v[1], v[2], v[3], v[4], v[5], v[6], id=v[0])
            for v in vrstice
        ]

    @staticmethod
    def v_obdobju(pov, datum_od, datum_do):
        """Vrne vse pisne preizkuse v določenem časovnem obdobju."""
        kaz = pov.cursor()
        kaz.execute("""
            SELECT id, datum, ura, id_predavalnica, id_letnik, id_predmet, id_tip
            FROM pisni_preizkusi
            WHERE datum BETWEEN ? AND ?
            ORDER BY datum ASC, ura ASC
        """, (datum_od, datum_do))
        vrstice = kaz.fetchall()

        return [
            PisniPreizkus(v[1], v[2], v[3], v[4], v[5], v[6], id=v[0])
            for v in vrstice
        ]



def dodaj_temo_preizkusu(pov, id_teme, id_test):
    """Poveže temo s pisnim preizkusom v tabeli povezovalna_teme_testi."""
    kaz = pov.cursor()
    kaz.execute("""
        INSERT INTO povezovalna_teme_testi (id_teme, id_test)
        VALUES (?, ?)
    """, (id_teme, id_test))
    pov.commit()


def ustvari_preizkus(pov, datum, ura, id_predavalnica, id_letnik, id_predmet, id_tip, seznam_tem):
    """Ustvari nov pisni preizkus in ga poveže z izbranimi temami."""
    # 1) ustvari preizkus
    preizkus = PisniPreizkus(datum, ura, id_predavalnica, id_letnik, id_predmet, id_tip)
    preizkus.shrani(pov)

    # 2) poveže izbrane teme
    for id_teme in seznam_tem:
        dodaj_temo_preizkusu(pov, id_teme, preizkus.id)

    return preizkus

def opis_preizkusa(pov, preizkus):
    """Vrne lep opis pisnega preizkusa z imeni namesto ID-jev."""

    predmet = Predmet.najdi(pov, preizkus.id_predmet)
    letnik = Letnik.najdi(pov, preizkus.id_letnik)
    predavalnica = Predavalnica.najdi(pov, preizkus.id_predavalnica)
    tip = TipTesta.najdi(pov, preizkus.id_tip)
    teme = Tema.za_preizkus(pov, preizkus.id)

    seznam_tem = ", ".join(t.tema for t in teme)

    return (
        f"  ID: {preizkus.id}\n"
        f"  Termin: {preizkus.datum} ob {preizkus.ura}\n"
        f"  Letnik: {letnik.letnik}\n"
        f"  Predmet: {predmet.ime}\n"
        f"  Predavalnica: {predavalnica.ime}\n"
        f"  Tip testa: {tip.tip}\n"
        f"  Teme: {seznam_tem}\n"
    )