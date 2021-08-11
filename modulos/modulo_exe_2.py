from os.path import getsize, getmtime
from time import localtime, asctime
import modulo_2

modulos = modulo_2.find('xml')

for modulo in modulos:
    tm = asctime(localtime(getmtime(modulo)))
    kb = getsize(modulo)/1024
    print('%s: (%d kbytes, %s)' %(modulo, kb,tm))