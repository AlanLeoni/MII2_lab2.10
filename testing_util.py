import sys
from PIL.Image import Image


def controlla_valore_atteso(valore, valore_atteso):
    if valore != valore_atteso:
        print("Test fallito! Il valore attuale", valore, "differisce dal valore atteso", valore_atteso,
              file=sys.stderr)
    # else:
    #     print("Test passato")
