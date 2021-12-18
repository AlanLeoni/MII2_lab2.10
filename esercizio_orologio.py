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
    crea_gif,
    larghezza_immagine,
    altezza_immagine,
)

from testing_util import(
    controlla_valore_atteso
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
    raggio_sfondo_bianco = RAGGIO * 95 // 100
    sfondo_grigio = cerchio(RAGGIO, GRIGIO)
    sfondo_bianco = cerchio((raggio_sfondo_bianco), BIANCO)
    return sovrapponi(sfondo_bianco, sfondo_grigio)

controlla_valore_atteso(larghezza_immagine(crea_sfondo()), RAGGIO * 2)
controlla_valore_atteso(altezza_immagine(crea_sfondo()), RAGGIO * 2)

def crea_tacca_minuti() -> Immagine:
    """
    Crea la singola tacca che indica i minuti
    
    :returns: una singola tacca indicante i minuti
    """
    altezza_tacca = RAGGIO * 3 // 100
    lunghezza_testa_tacca= RAGGIO * 82 // 100
    lunghezza_coda_tacca = RAGGIO * 8 // 100
    
    testa_tacca = rettangolo(lunghezza_testa_tacca, altezza_tacca, BIANCO)
    coda_tacca = rettangolo(lunghezza_coda_tacca, altezza_tacca, NERO)
    return cambia_punto_riferimento(
        affianca(testa_tacca, coda_tacca), "left", "middle")

controlla_valore_atteso(larghezza_immagine(crea_tacca_minuti()), (RAGGIO * 82 // 100) + RAGGIO * 8 // 100 )
controlla_valore_atteso(altezza_immagine(crea_tacca_minuti()), RAGGIO * 3 //100)
    
        
def crea_tacca_cinque_minuti() -> Immagine:
    """
    Crea la singola tacca che indica i cinque minuti
    
    :returns: una singola tacca indicante i cinque minuti
    """
    altezza_tacca = RAGGIO * 8 // 100
    lunghezza_testa_tacca = RAGGIO * 70 // 100
    lunghezza_coda_tacca = RAGGIO * 20 // 100
    testa_tacca = rettangolo(lunghezza_testa_tacca, altezza_tacca, BIANCO)
    coda_tacca = rettangolo(lunghezza_coda_tacca, altezza_tacca, NERO)
    return cambia_punto_riferimento(
        affianca(testa_tacca, coda_tacca), "left", "middle")

controlla_valore_atteso(larghezza_immagine(crea_tacca_cinque_minuti()), (RAGGIO * 70 // 100) + RAGGIO * 20 // 100 )
controlla_valore_atteso(altezza_immagine(crea_tacca_cinque_minuti()), RAGGIO * 8 //100)

def crea_tacche_minuti_5_minuti() -> Immagine:
    """
    Crea le tacche circolari indicanti i minuti ed evidenziati i 5 minuti
    
    returns: le tacche circolari indicanti i minuti e i 5 minuti
    """
    gradi  = 360 // 60
    mod5 = 360 // 12
    quadrante_prec = immagine_vuota()
    for tacca in range(0, 360, gradi):
        if tacca % mod5 == 0: 
            tacca_quadrante = ruota(crea_tacca_cinque_minuti(), tacca)
        else:
            tacca_quadrante = ruota(crea_tacca_minuti(), tacca)    
        quadrante_minuti = componi(quadrante_prec, tacca_quadrante)
        quadrante_prec = quadrante_minuti
    return quadrante_minuti
controlla_valore_atteso(larghezza_immagine(crea_tacche_minuti_5_minuti()), ((RAGGIO * 82 // 100) + (RAGGIO * 8 // 100 )) * 2 + 0)

def crea_quadrante() -> Immagine:
    """
    Crea il quadrante dell'orologio con tacche minuti e cinque minuti
    
    :returns: un'immagine del quadrante dell'orologio senza lancette
    """
    return componi(crea_tacche_minuti_5_minuti(), crea_sfondo())


def crea_lancetta_minuti(angolo: int) -> Immagine:
    """
    Crea la lancetta dei minuti in posizione ore 0
    
    :param angolo: angolo di apertura della lancetta
    :returns: una lancetta ruotata
    """
    altezza_lancetta = RAGGIO * 10 // 100
    lunghezza_testa_lancetta = RAGGIO * 20 // 100
    lunghezza_coda_lancetta = RAGGIO * 85 // 100
    posizione_zero = 90
    lancetta_testa = cambia_punto_riferimento(
        (rettangolo(lunghezza_testa_lancetta, altezza_lancetta, NERO)), 
        "right", "middle")
    lancetta_coda = cambia_punto_riferimento(
        (rettangolo(lunghezza_coda_lancetta, altezza_lancetta, NERO)), 
        "left", "middle")
    lancetta_orizzontale = affianca(lancetta_testa, lancetta_coda)
    lancetta_verticale = ruota(lancetta_orizzontale, posizione_zero)
    return ruota(lancetta_verticale, -(angolo))


def angolo_minuti(minuti: int) -> int:
    """
    Definisce il grado di rotazione rispetto ai minuti
    
    :param minuti: la posizione della lancetta
    :returns: l'angolo di apertura della lancetta rispetto alla posizione 0
    """
    grado_rotazione_minuto = 360 // 60
    return minuti * grado_rotazione_minuto


def crea_lancetta_ore(angolo: int) -> Immagine:
    """
    Crea l'immagine di una lancetta in posizione 0
    
    :params angolo: angolo di rotazione rispetto alla posizione 0
    :returns: una lancetta ruotata
    """
    altezza_lancetta = RAGGIO * 12 // 100
    lunghezza_lancetta_testa = RAGGIO * 20 // 100
    lunghezza_lancetta_coda = RAGGIO * 60 // 100
    lancetta_testa = cambia_punto_riferimento(
        (rettangolo(lunghezza_lancetta_testa, altezza_lancetta, NERO)), 
        "right", "middle")
    lancetta_coda = cambia_punto_riferimento(
        (rettangolo(lunghezza_lancetta_coda, altezza_lancetta, NERO)), 
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
    grado_rotazione_ore = 360 // 12
    return ((ore * grado_rotazione_ore) % 360) + (angolo_minuti(minuti))//12


def crea_lancetta_secondi(angolo: int) -> Immagine:
    """
    Crea la lancetta dei secondi in posizione ore 0
    
    :param angolo: angolo di apertura della lancetta
    :returns: una lancetta ruotata
    """
    altezza_lancetta = RAGGIO * 2 // 100
    raggio_pallino_rosso = RAGGIO * 8 // 100
    lunghezza_lancetta_testa = RAGGIO * 25 // 100
    lunghezza_lancetta_coda = RAGGIO * 60 // 100
    pallino_lancetta = cambia_punto_riferimento(
        cerchio(raggio_pallino_rosso, ROSSO), 
        "middle", "middle")
    lancetta_testa = cambia_punto_riferimento(
        (rettangolo(lunghezza_lancetta_testa, altezza_lancetta, ROSSO)), 
        "right", "middle")
    lancetta_coda = cambia_punto_riferimento(
        (rettangolo(lunghezza_lancetta_coda, altezza_lancetta, ROSSO)),
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


def crea_animazione_orologio(ore: int, minuti: int, secondi: int):
    """
    Crea l'animazione di un orologio con la lancetta dei secondi che si muove 
    da 0 a secondi
    
    param ore: la posizione della lancetta delle ore
    param minuti: la posizione della lancetta dei minuti
    param minuti: la posizione della lancetta dei secondi
    returns: la gif animata di un orologio con i secondi che avanzano
    """
    lista_orologi = [
        crea_orologio(ore, minuti, passo)
        for passo in range(0, secondi)
    ]
    velocita = (40 * 1000 //40)
    return crea_gif("animazione_orologio",lista_orologi, velocita)


# crea_animazione_orologio(11, 15, 59)
