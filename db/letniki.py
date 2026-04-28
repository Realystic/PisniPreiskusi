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