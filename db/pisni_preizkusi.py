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