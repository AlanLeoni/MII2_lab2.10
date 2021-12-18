"""
Il file contiene funzioni che permettono la costruzione di un orologio stile 
FFS che indica ore e minuti e secondi
In particolare le funzioni permettono di:
- creare lo sfondo del quadrante che evidenzia i minuti e i cinque minuti
- creare le lancette delle ore e dei minuti
- creare la lancetta dei secondi
- creare un orologio stile FFS con indicazione su ore, minuti e secondi
"""
from img_lib_v0_6 import(
    Immagine, 
    affianca, 
    cerchio, 
    immagine_vuota, 
    rettangolo, 
    ruota, 
    sovrapponi, 
    cambia_punto_riferimento, 
    componi, 
    salva_immagine,
    visualizza_immagine
)

RAGGIO = 300
NERO = (0, 0, 0)
BIANCO = (255, 255, 255)
GRIGIO = (84, 84, 84)
ROSSO = (255, 0, 0)



def crea_sfondo() -> Immagine:
    """
    Crea lo sfondo del quadrante
    
    :returns: il cerchio del quadrante con un bordo grigio
    """
    sfondo_grigio = cerchio(RAGGIO, GRIGIO)
    sfondo_bianco = cerchio((RAGGIO * 95 // 100), BIANCO)
    return sovrapponi(sfondo_bianco, sfondo_grigio)


def crea_lancetta_minuti(angolo: int) -> Immagine:
    """
    Crea la lancetta dei minuti in posizione ore 0
    
    :param angolo: angolo di apertura della lancetta
    :returns: una lancetta ruotata
    """
    altezza_lancetta = RAGGIO * 10 // 100
    lancetta_testa = cambia_punto_riferimento(
        (rettangolo(RAGGIO * 20 // 100, altezza_lancetta, NERO)), 
        "right", "middle")
    lancetta_coda = cambia_punto_riferimento(
        (rettangolo(RAGGIO * 85 // 100, altezza_lancetta, NERO)), 
        "left", "middle")
    lancetta_orizzontale = affianca(lancetta_testa, lancetta_coda)
    lancetta_verticale = ruota(lancetta_orizzontale, 90)
    return ruota(lancetta_verticale, -(angolo))


def angolo_minuti(minuti: int) -> int:
    """
    Definisce il grado di rotazione rispetto ai minuti
    
    :param minuti: la posizione della lancetta
    :returns: l'angolo di apertura della lancetta rispetto alla posizione 0
    """
    return minuti * 6


def crea_lancetta_ore(angolo: int) -> Immagine:
    """
    Crea l'immagine di una lancetta in posizione 0
    
    :params angolo: angolo di rotazione rispetto alla posizione 0
    :returns: una lancetta ruotata
    """
    altezza_lancetta = RAGGIO * 12 // 100
    lancetta_testa = cambia_punto_riferimento(
        (rettangolo(RAGGIO * 20 // 100, altezza_lancetta, NERO)), 
        "right", "middle")
    lancetta_coda = cambia_punto_riferimento(
        (rettangolo(RAGGIO * 60 // 100, altezza_lancetta, NERO)), 
        "left", "middle")
    lancetta_orizzontale = affianca(lancetta_testa, lancetta_coda)
    lancetta_verticale = ruota(lancetta_orizzontale, 90)
    return ruota(lancetta_verticale, -(angolo))


def angolo_ore(ore: int, minuti: int) -> int:
    """
    Definisce il grado di rotazione della lancetta delle ore rispetto alle ore
    e ai minuti
    
    :param ore: l'ora desiderata. Accetta input a 12 o 24 h
    :param minuti: i minuti desiderati
    :returns: l'angolo di apertura della lancetta rispetto alla posizione 0
    """
    return ((ore * 30) % 360) + (angolo_minuti(minuti))//12


def crea_tacca_minuti() -> Immagine:
    """
    Crea la singola tacca che indica i minuti
    
    :returns: una singola tacca indicante i minuti
    """
    altezza_tacca = RAGGIO * 3 // 100
    testa_tacca = rettangolo(RAGGIO * 82 // 100, altezza_tacca, BIANCO)
    coda_tacca = rettangolo(RAGGIO * 8 // 100, altezza_tacca, NERO)
    return cambia_punto_riferimento(
        affianca(testa_tacca, coda_tacca), "left", "middle")


def crea_tacche_minuti() -> Immagine:
    """
    Crea le tacche circolari indicanti i minuti
    
    :returns: le tacche circolari indicanti i minuti
    """
    gradi = 6
    quadrante_prec = immagine_vuota()
    for tacca in range(0, 360, gradi):
        tacca_quadrante = ruota(crea_tacca_minuti(), tacca)
        quadrante_minuti = componi(quadrante_prec, tacca_quadrante)
        quadrante_prec = quadrante_minuti
    return quadrante_minuti


def crea_tacca_cinque_minuti() -> Immagine:
    """
    Crea la singola tacca che indica i cinque minuti
    
    :returns: una singola tacca indicante i cinque minuti
    """
    altezza_tacca = RAGGIO * 8 // 100
    testa_tacca = rettangolo(RAGGIO * 70 // 100, altezza_tacca, BIANCO)
    coda_tacca = rettangolo(RAGGIO * 20 // 100, altezza_tacca, NERO)
    return cambia_punto_riferimento(
        affianca(testa_tacca, coda_tacca), "left", "middle")


def crea_tacche_cinque_minuti() -> Immagine:
    """
    Crea le tacche circolari indicanti i cinque minuti
    
    :returns: le tacche circolari indicanti i cinque minuti
    """
    gradi = 30
    quadrante_prec = immagine_vuota()
    for tacca in range(0, 360, gradi):
        tacca_quadrante = ruota(crea_tacca_cinque_minuti(), tacca)
        quadrante_cinque_minuti = componi(quadrante_prec, tacca_quadrante)
        quadrante_prec = quadrante_cinque_minuti
    return quadrante_cinque_minuti


def crea_quadrante() -> Immagine:
    """
    Crea il quadrante dell'orologio con tacche minuti e cinque minuti
    
    :returns: un'immagine del quadrante dell'orologio senza lancette
    """
    return componi(
        componi(crea_tacche_cinque_minuti(), crea_tacche_minuti()), 
        crea_sfondo())


def crea_lancetta_secondi(angolo: int) -> Immagine:
    """
    Crea la lancetta dei secondi in posizione ore 0
    
    :param angolo: angolo di apertura della lancetta
    :returns: una lancetta ruotata
    """
    altezza_lancetta = RAGGIO * 2 // 100
    pallino_lancetta = cambia_punto_riferimento(
        cerchio(RAGGIO *8 // 100, ROSSO), 
        "middle", "middle")
    lancetta_testa = cambia_punto_riferimento(
        (rettangolo(RAGGIO * 25 // 100, altezza_lancetta, ROSSO)), 
        "right", "middle")
    lancetta_coda = cambia_punto_riferimento(
        (rettangolo(RAGGIO * 60 // 100, altezza_lancetta, ROSSO)),
        "left", "middle")
    lancetta_orizzontale = affianca(
        lancetta_testa, affianca(lancetta_coda, pallino_lancetta))
    lancetta_verticale = ruota(lancetta_orizzontale, 90)
    return ruota(lancetta_verticale, -(angolo))


def angolo_secondi(secondi: int) -> int:
    """
    Definisce il grado di rotazione rispetto ai secondi
    
    :param secondi: la posizione della lancetta
    :returns: l'angolo di apertura della lancetta rispetto alla posizione 0
    """
    angolo = secondi * 6
    return angolo


def crea_orologio(ore: int, minuti: int, secondi: int) -> Immagine:
    ore_minuti = componi(crea_lancetta_ore(angolo_ore(ore, minuti)), 
                         crea_lancetta_minuti(angolo_minuti(minuti)))
    lancette = componi(crea_lancetta_secondi(angolo_secondi(secondi)),
                       ore_minuti)
    return componi(lancette, crea_quadrante())

salva_immagine("orologio_ore_minuti_secondi", crea_orologio(4, 10, 45))