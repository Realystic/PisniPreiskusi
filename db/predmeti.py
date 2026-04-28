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