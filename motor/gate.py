#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Filtro anti-plantilla, compartido por todos los sitios.

Mide la similitud de Jaccard sobre el vocabulario visible de cada pagina.
Sirve para cualquier web: solo necesita saber que extensiones son paginas.

Uso desde la linea de ordenes:

  python3 motor/gate.py interno <dir> [--original <dir-sin-tocar>] [--umbral 0.45]
  python3 motor/gate.py cruzado <dir-sitio-a> <dir-sitio-b> [--umbral 0.45]

Sale con 1 si algun par supera el umbral. `--original` limita la comparacion a
las paginas que no existian en la web entregada por el cliente.

Aprendizaje que justifica que esto exista: generar paginas desde una base de
hechos con andamiaje comun da 0,75-0,91 de similitud, porque el texto propio
del tema apenas pesa un 23 %. Escritas a mano se quedan en 0,24-0,41.
"""
import argparse, glob, itertools, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from marcado import jaccard, leer, vocabulario          # noqa: E402

UMBRAL = 0.45
EXTS = ("*.asp", "*.html")


def paginas(base, exts=EXTS, excluir=()):
    """Rutas de las paginas de un directorio (sin recursion: los sitios que se
    tratan aqui son planos y lo que cuelga de subcarpetas son recursos)."""
    fs = (f for e in exts for f in glob.glob(os.path.join(base, e)))
    return sorted(f for f in fs if os.path.basename(f) not in excluir)


def vocabularios(ficheros):
    """{ruta: vocabulario}. Lo ilegible se salta: no se puede comparar."""
    out = {}
    for f in ficheros:
        try:
            out[f] = vocabulario(leer(f))
        except OSError:
            continue
    return out


def pares(voc, candidatas=None):
    """[(similitud, a, b)] de mas a menos parecido.

    Con `candidatas`, solo los pares donde al menos una es candidata: lo ya
    publicado no se compara consigo mismo, que ni se puede cambiar ni interesa.
    """
    sims = ((jaccard(voc[a], voc[b]), a, b)
            for a, b in itertools.combinations(sorted(voc), 2)
            if candidatas is None or a in candidatas or b in candidatas)
    return sorted(sims, reverse=True)


def comparar(ficheros):
    return pares(vocabularios(ficheros))


def _imprimir(sims, umbral, muestra):
    for j, x, y in sims[:muestra]:
        marca = "!!" if j > umbral else "  "
        print(f"   {marca} {j:.2f}  {os.path.basename(x)} <-> {os.path.basename(y)}")


def informe(ficheros, umbral=UMBRAL, muestra=5):
    """Imprime el resultado y devuelve el numero de pares que superan el umbral."""
    sims = comparar(ficheros)
    if not sims:
        print("  nada que comparar")
        return 0
    malos = [s for s in sims if s[0] > umbral]
    media = sum(s[0] for s in sims) / len(sims)
    print(f"  paginas comparadas: {len(ficheros)}")
    print(f"  similitud media {media:.2f}   maxima {sims[0][0]:.2f}   umbral {umbral}")
    print(f"  pares por encima del umbral: {len(malos)}")
    _imprimir(sims, umbral, muestra)
    return len(malos)


def filtrar(candidatas, previas=(), umbral=UMBRAL):
    """candidatas: {nombre: html} nuevo. previas: rutas ya publicadas.

    Devuelve el conjunto de candidatas que NO deben publicarse por parecerse
    demasiado a otra candidata o a algo ya publicado. Cuando dos candidatas
    chocan entre si, cae la segunda por orden alfabetico: la regla es
    arbitraria pero estable, y asi el mismo lote da el mismo resultado siempre.
    """
    voc = {f: vocabulario(h) for f, h in candidatas.items()}
    for p in previas:
        b = os.path.basename(p)
        if b not in voc:
            try:
                voc[b] = vocabulario(leer(p))
            except OSError:
                pass
    malos = set()
    for j, a, b in pares(voc, candidatas):
        if j <= umbral:
            break
        malo = b if b in candidatas else a
        malos.add(malo)
        print(f"   !! {j:.2f}  {a} <-> {b}  -> no se publica {malo}")
    return malos


def cruzado(base_a, base_b, umbral=UMBRAL, muestra=8):
    """Compara dos sitios distintos entre si, pagina de A contra pagina de B.

    Cuando dos dominios pertenecen al mismo dueño (aqui abacosoftware.com y
    carrito5.com), reutilizar texto entre ellos crea contenido duplicado que
    perjudica a los dos. Esta comprobacion lo detecta antes de publicar.
    """
    va, vb = vocabularios(paginas(base_a)), vocabularios(paginas(base_b))
    sims = sorted(((jaccard(sa, sb), x, y) for x, sa in va.items() for y, sb in vb.items()),
                  reverse=True)
    malos = [s for s in sims if s[0] > umbral]
    print(f"  {len(va)} paginas x {len(vb)} paginas = {len(sims)} comparaciones")
    print(f"  similitud maxima entre sitios: {sims[0][0]:.2f}" if sims else "  sin datos")
    print(f"  pares por encima de {umbral}: {len(malos)}")
    _imprimir(sims, umbral, muestra)
    return len(malos)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("modo", choices=("interno", "cruzado"))
    ap.add_argument("dirs", nargs="+", help="un directorio (interno) o dos (cruzado)")
    ap.add_argument("--original", help="web sin tocar: solo se comparan las paginas nuevas")
    ap.add_argument("--umbral", type=float, default=UMBRAL)
    ap.add_argument("--muestra", type=int, default=8, help="pares que se listan")
    a = ap.parse_args(argv)
    for d in a.dirs + ([a.original] if a.original else []):
        if not os.path.isdir(d):
            print("  !! no es un directorio:", d)
            return 2
    if a.modo == "cruzado":
        if len(a.dirs) != 2:
            print("  cruzado necesita exactamente dos directorios")
            return 2
        return 1 if cruzado(*a.dirs, umbral=a.umbral, muestra=a.muestra) else 0
    fs = paginas(a.dirs[0])
    if a.original:
        viejas = {os.path.basename(f) for f in paginas(a.original)}
        fs = [f for f in fs if os.path.basename(f) not in viejas]
    return 1 if informe(fs, a.umbral, a.muestra) else 0


if __name__ == "__main__":
    sys.exit(main())
