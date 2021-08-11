import os.path
import sys
import glob

def find(txt):
    resp = []
    for path in sys.path:
        modulos = glob.glob('%s/*.py'%path)
        for modulo in modulos:
            if txt in os.path.basename(modulo):
                resp.append(modulo)
    return resp