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