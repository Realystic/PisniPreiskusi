class Uporabnik:
    """Razred, ki predstavlja tabelo uporabniki in omogoča dodajanje, spreminjanje,
    brisanje ter pridobivanje (posameznega ali vseh) uporabnikov iz baze."""

    def __init__(self, ime, email, geslo_hash, vloga="student", id=None):
        self.id = id
        self.ime = ime
        self.email = email
        self.geslo_hash = geslo_hash
        self.vloga = vloga

    def __str__(self):
        return f"{self.id}: {self.ime} ({self.email}, vloga: {self.vloga})"

    def shrani(self, pov):
        """Ustvari novega uporabnika ali posodobi obstoječega v bazi."""
        kaz = pov.cursor()

        if self.id is None:
            # INSERT
            kaz.execute("""
                INSERT INTO uporabniki (ime, email, geslo_hash, vloga)
                VALUES (?, ?, ?, ?)
            """, (self.ime, self.email, self.geslo_hash, self.vloga))
            self.id = kaz.lastrowid
        else:
            # UPDATE
            kaz.execute("""
                UPDATE uporabniki
                SET ime = ?, email = ?, geslo_hash = ?, vloga = ?
                WHERE id = ?
            """, (self.ime, self.email, self.geslo_hash, self.vloga, self.id))

        pov.commit()

    def izbrisi(self, pov):
        """Izbriše uporabnika iz baze."""
        if self.id is None:
            return

        kaz = pov.cursor()
        kaz.execute("DELETE FROM uporabniki WHERE id = ?", (self.id,))
        pov.commit()
        self.id = None

    @staticmethod
    def najdi(pov, id):
        """Najde uporabnika po ID-ju in vrne objekt Uporabnik."""
        kaz = pov.cursor()
        kaz.execute("""
            SELECT id, ime, email, geslo_hash, vloga
            FROM uporabniki
            WHERE id = ?
        """, (id,))
        vrstica = kaz.fetchone()

        if vrstica:
            return Uporabnik(vrstica[1], vrstica[2], vrstica[3], vrstica[4], id=vrstica[0])
        return None

    @staticmethod
    def najdi_po_emailu(pov, email):
        """Najde uporabnika po emailu (uporablja se pri prijavi)."""
        kaz = pov.cursor()
        kaz.execute("""
            SELECT id, ime, email, geslo_hash, vloga
            FROM uporabniki
            WHERE email = ?
        """, (email,))
        vrstica = kaz.fetchone()

        if vrstica:
            return Uporabnik(vrstica[1], vrstica[2], vrstica[3], vrstica[4], id=vrstica[0])
        return None

    @staticmethod
    def vsi(pov):
        """Vrne seznam vseh uporabnikov kot objektov."""
        kaz = pov.cursor()
        kaz.execute("""
            SELECT id, ime, email, geslo_hash, vloga
            FROM uporabniki
            ORDER BY ime ASC
        """)
        vrstice = kaz.fetchall()

        return [Uporabnik(v[1], v[2], v[3], v[4], id=v[0]) for v in vrstice]