# -*- coding: utf-8 -*-
"""Lo que comparten todos los scripts de abacosoftware-seo.

Importar este modulo deja `motor/` en sys.path, asi que despues de `import
sitio` se puede hacer `import gate, marcado`. Funciona igual desde el directorio
temporal de enlaces simbolicos que monta el driver, porque la ruta se calcula
sobre el fichero real (realpath), no sobre el enlace.
"""
import glob, os, sys

RAIZ = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))     # abacosoftware-seo/
MOTOR = os.path.join(os.path.dirname(RAIZ), "motor")
for p in (MOTOR, os.path.dirname(os.path.realpath(__file__))):
    if p not in sys.path:
        sys.path.insert(0, p)

BASE = "https://www.abacosoftware.com"
OG_IMAGE = BASE + "/img/og-caja5-tpv.png"
TEL = "953 050 112"
TEL_HREF = "tel:953050112"
WA = "https://wa.me/34611500052"
DEMO = "descargar.asp?origen=descargas&amp;link=www.abacosoftware.com/eutpv.exe"
PRECIO = "333 €"

# Ficheros .asp/.html que no son paginas: includes, conexiones y copias que el
# cliente dejo en el servidor. Ninguna herramienta debe tratarlos como contenido.
NO_PAGINA = {
    "conexion.asp", "conexion_visitas.asp", "menu_nav.asp", "footer_comun.asp",
    "tpv_consultas_desde_web_med.asp", "tpv_consultas_desde_web_medNO.asp",
    "tpv_consultas_desde_web_med -09-10-2023.asp",
    "contenido_copyr-footer.html", "info_asp.aspx", "ventas.aspx",
}


def salida():
    """Directorio de la web sobre el que trabaja un script: primer argumento o ./site."""
    return sys.argv[1] if len(sys.argv) > 1 else "site"


def paginas(base, exts=("*.asp",)):
    """Rutas ordenadas de las paginas reales de la web."""
    fs = (f for e in exts for f in glob.glob(os.path.join(base, e)))
    return sorted(f for f in fs if os.path.basename(f) not in NO_PAGINA
                  and not os.path.basename(f).endswith("_"))
