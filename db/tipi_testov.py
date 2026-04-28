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