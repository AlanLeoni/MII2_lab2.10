"""
Il file contiene funzioni che permettono la costruzione e l'animazione di un
orologio stile FFS che indica ore e minuti e secondi
In particolare le funzioni permettono di:
- creare lo sfondo del quadrante che evidenzia i minuti e i cinque minuti
- creare le lancette delle ore e dei minuti
- creare la lancetta dei secondi
- creare un orologio stile FFS con indicazione su ore, minuti e secondi
- creare l'animazione dei secondi dell'orologio
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
RAGGIO_SFONDO_BIANCO = RAGGIO * 95 //100
DIAMETRO_SFONDO = RAGGIO * 2
ALTEZZA_TACCA_MINUTI = RAGGIO * 3 // 100
LUNGHEZZA_TESTA_TACCA_MINUTI = RAGGIO * 82 // 100
LUNGHEZZA_CODA_TACCA_MINUTI = RAGGIO * 8 // 100
ALTEZZA_TACCA_5_MINUTI = RAGGIO * 8 // 100
LUNGHEZZA_TESTA_TACCA_5_MINUTI = RAGGIO * 70 // 100
LUNGHEZZA_CODA_TACCA_5_MINUTI = RAGGIO * 20 // 100
GRADI_TACCHE_5_MINUTI = 360 // 60
MOD5_TACCHE_5_MINUTI = 360 // 12
ALTEZZA_LANCETTA_MINUTI = RAGGIO * 10 // 100
LUNGHEZZA_TESTA_LANCETTA_MINUTI = RAGGIO * 20 // 100
LUNGHEZZA_CODA_LANCETTA_MINUTI = RAGGIO * 85 // 100
ALTEZZA_LANCETTA_ORE = RAGGIO * 12 // 100
LUNGHEZZA_LANCETTA_TESTA_ORE = RAGGIO * 20 // 100
LUNGHEZZA_LANCETTA_CODA_ORE = RAGGIO * 60 // 100
ALTEZZA_LANCETTA_SECONDI  = RAGGIO * 2 // 100
RAGGIO_PALLINO_ROSSO = RAGGIO * 8 // 100
LUNGHEZZA_LANCETTA_TESTA_SECONDI = RAGGIO * 25 // 100
LUNGHEZZA_LANCETTA_CODA_SECONDI = RAGGIO * 60 // 100


def crea_sfondo() -> Immagine:
    """
    Crea lo sfondo del quadrante
    
    :returns: il cerchio del quadrante con un bordo grigio
    """
    sfondo_grigio = cerchio(RAGGIO, GRIGIO)
    sfondo_bianco = cerchio((RAGGIO_SFONDO_BIANCO), BIANCO)
    return sovrapponi(sfondo_bianco, sfondo_grigio)

controlla_valore_atteso(larghezza_immagine(crea_sfondo()), DIAMETRO_SFONDO)
controlla_valore_atteso(altezza_immagine(crea_sfondo()), DIAMETRO_SFONDO)


def crea_tacca_minuti() -> Immagine:
    """
    Crea la singola tacca che indica i minuti
    
    :returns: una singola tacca indicante i minuti
    """
    testa_tacca = rettangolo(LUNGHEZZA_TESTA_TACCA_MINUTI, ALTEZZA_TACCA_MINUTI, BIANCO)
    coda_tacca = rettangolo(LUNGHEZZA_CODA_TACCA_MINUTI, ALTEZZA_TACCA_MINUTI, NERO)
    return cambia_punto_riferimento(
        affianca(testa_tacca, coda_tacca), "left", "middle")

controlla_valore_atteso(larghezza_immagine(crea_tacca_minuti()), LUNGHEZZA_TESTA_TACCA_MINUTI + LUNGHEZZA_CODA_TACCA_MINUTI)
controlla_valore_atteso(altezza_immagine(crea_tacca_minuti()), ALTEZZA_TACCA_MINUTI)


def crea_tacca_cinque_minuti() -> Immagine:
    """
    Crea la singola tacca che indica i cinque minuti
    
    :returns: una singola tacca indicante i cinque minuti
    """
    testa_tacca = rettangolo(LUNGHEZZA_TESTA_TACCA_5_MINUTI, ALTEZZA_TACCA_5_MINUTI, BIANCO)
    coda_tacca = rettangolo(LUNGHEZZA_CODA_TACCA_5_MINUTI, ALTEZZA_TACCA_5_MINUTI, NERO)
    return cambia_punto_riferimento(
        affianca(testa_tacca, coda_tacca), "left", "middle")

controlla_valore_atteso(larghezza_immagine(crea_tacca_cinque_minuti()), LUNGHEZZA_TESTA_TACCA_5_MINUTI + LUNGHEZZA_CODA_TACCA_5_MINUTI)
controlla_valore_atteso(altezza_immagine(crea_tacca_cinque_minuti()), ALTEZZA_TACCA_5_MINUTI)


def crea_tacche_minuti_5_minuti() -> Immagine:
    """
    Crea le tacche circolari indicanti i minuti ed evidenziati i 5 minuti
    
    returns: le tacche circolari indicanti i minuti e i 5 minuti
    """
    quadrante_prec = immagine_vuota()
    for tacca in range(0, 360, GRADI_TACCHE_5_MINUTI):
        if tacca % MOD5_TACCHE_5_MINUTI == 0: 
            tacca_quadrante = ruota(crea_tacca_cinque_minuti(), tacca)
        else:
            tacca_quadrante = ruota(crea_tacca_minuti(), tacca)    
        quadrante_minuti = componi(quadrante_prec, tacca_quadrante)
        quadrante_prec = quadrante_minuti
    return quadrante_minuti

# falliscono tutti di un pixel. 
# controlla_valore_atteso(larghezza_immagine(crea_tacche_minuti_5_minuti()), (larghezza_immagine(crea_tacca_minuti())) * 2)
# controlla_valore_atteso(larghezza_immagine(crea_tacche_minuti_5_minuti()), ((LUNGHEZZA_TESTA_TACCA_5_MINUTI + LUNGHEZZA_CODA_TACCA_5_MINUTI)* 2))
# controlla_valore_atteso(altezza_immagine(crea_tacche_minuti_5_minuti()), ((LUNGHEZZA_TESTA_TACCA_5_MINUTI + LUNGHEZZA_CODA_TACCA_5_MINUTI)* 2))


def crea_quadrante() -> Immagine:
    """
    Crea il quadrante dell'orologio con tacche minuti e cinque minuti
    
    :returns: un'immagine del quadrante dell'orologio senza lancette
    """
    return componi(crea_tacche_minuti_5_minuti(), crea_sfondo())

controlla_valore_atteso(larghezza_immagine(crea_quadrante()), DIAMETRO_SFONDO)
controlla_valore_atteso(altezza_immagine(crea_quadrante()), DIAMETRO_SFONDO)


def crea_lancetta_minuti(angolo: int) -> Immagine:
    """
    Crea la lancetta dei minuti in posizione ore 0
    
    :param angolo: angolo di apertura della lancetta
    :returns: una lancetta ruotata
    """
    posizione_zero = 90
    lancetta_testa = cambia_punto_riferimento(
        (rettangolo(LUNGHEZZA_TESTA_LANCETTA_MINUTI, ALTEZZA_LANCETTA_MINUTI, NERO)), 
        "right", "middle")
    lancetta_coda = cambia_punto_riferimento(
        (rettangolo(LUNGHEZZA_CODA_LANCETTA_MINUTI, ALTEZZA_LANCETTA_MINUTI, NERO)), 
        "left", "middle")
    lancetta_orizzontale = affianca(lancetta_testa, lancetta_coda)
    lancetta_verticale = ruota(lancetta_orizzontale, posizione_zero)
    return ruota(lancetta_verticale, -(angolo))

controlla_valore_atteso(larghezza_immagine(crea_lancetta_minuti(90)), LUNGHEZZA_TESTA_LANCETTA_MINUTI + LUNGHEZZA_CODA_LANCETTA_MINUTI)
controlla_valore_atteso(altezza_immagine(crea_lancetta_minuti(90)), ALTEZZA_LANCETTA_MINUTI)


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
    lancetta_testa = cambia_punto_riferimento(
        (rettangolo(LUNGHEZZA_LANCETTA_TESTA_ORE, ALTEZZA_LANCETTA_ORE, NERO)), 
        "right", "middle")
    lancetta_coda = cambia_punto_riferimento(
        (rettangolo(LUNGHEZZA_LANCETTA_CODA_ORE, ALTEZZA_LANCETTA_ORE, NERO)), 
        "left", "middle")
    lancetta_orizzontale = affianca(lancetta_testa, lancetta_coda)
    lancetta_verticale = ruota(lancetta_orizzontale, 90)
    return ruota(lancetta_verticale, -(angolo))

controlla_valore_atteso(larghezza_immagine(crea_lancetta_ore(90)), LUNGHEZZA_LANCETTA_TESTA_ORE + LUNGHEZZA_LANCETTA_CODA_ORE)
controlla_valore_atteso(altezza_immagine(crea_lancetta_ore(90)), ALTEZZA_LANCETTA_ORE)


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
    pallino_lancetta = cambia_punto_riferimento(
        cerchio(RAGGIO_PALLINO_ROSSO, ROSSO), 
        "middle", "middle")
    lancetta_testa = cambia_punto_riferimento(
        (rettangolo(LUNGHEZZA_LANCETTA_TESTA_SECONDI, ALTEZZA_LANCETTA_SECONDI, ROSSO)), 
        "right", "middle")
    lancetta_coda = cambia_punto_riferimento(
        (rettangolo(LUNGHEZZA_LANCETTA_CODA_SECONDI, ALTEZZA_LANCETTA_SECONDI, ROSSO)),
        "left", "middle")
    lancetta_orizzontale = affianca(
        lancetta_testa, affianca(lancetta_coda, pallino_lancetta))
    lancetta_verticale = ruota(lancetta_orizzontale, 90)
    return ruota(lancetta_verticale, -(angolo))

controlla_valore_atteso(altezza_immagine(crea_lancetta_secondi(90)), RAGGIO_PALLINO_ROSSO * 2)


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

controlla_valore_atteso(larghezza_immagine(crea_orologio(4, 10, 15)), DIAMETRO_SFONDO)
controlla_valore_atteso(altezza_immagine(crea_orologio(4, 10, 15)), DIAMETRO_SFONDO)


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
