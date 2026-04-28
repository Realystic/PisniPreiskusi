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
