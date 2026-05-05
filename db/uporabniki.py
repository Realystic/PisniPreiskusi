from db.geslo import sifriraj_geslo

class Uporabnik:
    """Razred, ki predstavlja tabelo uporabniki in omogoča dodajanje, spreminjanje,
    brisanje ter pridobivanje (posameznega ali vseh) uporabnikov iz baze."""

    def __init__(self, ime, email, geslo_hash, sol, vloga="student", id=None):
        self.id = id
        self.ime = ime
        self.email = email
        self.geslo_hash = geslo_hash
        self.sol = sol
        self.vloga = vloga

    def __str__(self):
        return f"{self.id}: {self.ime} ({self.email}, vloga: {self.vloga})"

    def shrani(self, pov):
        """Ustvari novega uporabnika ali posodobi obstoječega v bazi."""
        kaz = pov.cursor()

        if self.id is None:
            kaz.execute("""
                INSERT INTO uporabniki (ime, email, geslo_hash, sol, vloga)
                VALUES (?, ?, ?, ?, ?)
            """, (self.ime, self.email, self.geslo_hash, self.sol, self.vloga))
            self.id = kaz.lastrowid
        else:
            kaz.execute("""
                UPDATE uporabniki
                SET ime = ?, email = ?, geslo_hash = ?, sol = ?, vloga = ?
                WHERE id = ?
            """, (self.ime, self.email, self.geslo_hash, self.sol, self.vloga, self.id))

        pov.commit()
    
    @classmethod
    def ustvari(cls, pov, ime, email, geslo, vloga="student"):
        """Ustvari novega uporabnika s podanimi podatki, zgoščenim geslom in ga shrani v bazo."""
        geslo_hash, sol = sifriraj_geslo(geslo)

        u = cls(
            ime=ime,
            email=email,
            geslo_hash=geslo_hash,
            sol=sol,
            vloga=vloga
        )
        u.shrani(pov)
        return u


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
            SELECT id, ime, email, geslo_hash, sol,vloga
            FROM uporabniki
            WHERE id = ?
        """, (id,))
        vrstica = kaz.fetchone()

        if vrstica:
            return Uporabnik(
                    vrstica[1],  # ime
                    vrstica[2],  # email
                    vrstica[3],  # geslo_hash
                    vrstica[4],  # sol
                    vrstica[5],  # vloga
                    id=vrstica[0]
                )
        return None

    @staticmethod
    def najdi_po_emailu(pov, email):
        """Najde uporabnika po emailu (uporablja se pri prijavi)."""
        kaz = pov.cursor()
        kaz.execute("""
            SELECT id, ime, email, geslo_hash, sol, vloga
            FROM uporabniki
            WHERE email = ?
        """, (email,))
        vrstica = kaz.fetchone()

        if vrstica:
            return Uporabnik(
                    vrstica[1],  # ime
                    vrstica[2],  # email
                    vrstica[3],  # geslo_hash
                    vrstica[4],  # sol
                    vrstica[5],  # vloga
                    id=vrstica[0]
                )
        
        return None

@staticmethod
def vsi(pov):
    kaz = pov.cursor()
    kaz.execute("""
        SELECT id, ime, email, vloga
        FROM uporabniki
        ORDER BY ime ASC
    """)
    vrstice = kaz.fetchall()

    return [
        Uporabnik(
            ime=v[1],
            email=v[2],
            geslo_hash=None,
            sol=None,
            vloga=v[3],
            id=v[0]
        )
        for v in vrstice
    ]
