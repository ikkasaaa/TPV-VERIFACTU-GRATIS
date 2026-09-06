#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pruebas del filtro anti-plantilla."""
import contextlib, io, os, sys, tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gate                                              # noqa: E402
from prueba import Suite, correr                         # noqa: E402

S = Suite("gate")

PROSA_A = "<p>" + " ".join(f"palabra{i}" for i in range(60)) + "</p>"
PROSA_B = "<p>" + " ".join(f"palabra{i}" for i in range(50)) + " otra cosa distinta aqui</p>"
PROSA_C = "<p>" + " ".join(f"termino{i}" for i in range(60)) + "</p>"


def callado(f, *a, **k):
    """Ejecuta f sin su salida por pantalla: aqui interesa lo que devuelve."""
    with contextlib.redirect_stdout(io.StringIO()):
        return f(*a, **k)


def sitio(paginas):
    d = tempfile.mkdtemp(prefix="gate-")
    for n, h in paginas.items():
        open(os.path.join(d, n), "w", encoding="utf-8").write(h)
    return d


@S.caso("dos paginas casi iguales se detectan y dos distintas no")
def _():
    sims = gate.comparar([os.path.join(sitio({"a.html": PROSA_A, "b.html": PROSA_B, "c.html": PROSA_C}), n)
                          for n in ("a.html", "b.html", "c.html")])
    assert sims[0][0] > gate.UMBRAL and sims[0][1:] == tuple(sims[0][1:]), sims[0]
    assert {os.path.basename(x) for x in sims[0][1:]} == {"a.html", "b.html"}
    assert sims[-1][0] == 0.0, "a y c no comparten ni una palabra"


@S.caso("la similitud sale ordenada de mayor a menor")
def _():
    d = sitio({"a.html": PROSA_A, "b.html": PROSA_B, "c.html": PROSA_C})
    js = [j for j, _, _ in gate.comparar(gate.paginas(d))]
    assert js == sorted(js, reverse=True), js


@S.caso("filtrar rechaza la candidata que copia a una pagina ya publicada, no la publicada")
def _():
    d = sitio({"vieja.html": PROSA_A})
    malos = callado(gate.filtrar, {"nueva.html": PROSA_B, "distinta.html": PROSA_C},
                    previas=gate.paginas(d))
    assert malos == {"nueva.html"}, malos


@S.caso("entre dos candidatas que chocan cae la segunda por orden alfabetico")
def _():
    malos = callado(gate.filtrar, {"z.html": PROSA_A, "a.html": PROSA_B})
    assert malos == {"z.html"}, malos


@S.caso("script, style, ASP y comentarios no cuentan como texto visible")
def _():
    a = "<p>hola mundo</p><script>var x = 'relleno comun a todas';</script><% Dim y %><!-- nota -->"
    b = "<p>adios luna</p><script>var x = 'relleno comun a todas';</script><style>p{}</style>"
    d = sitio({"a.html": a, "b.html": b})
    (j, _, _), = gate.comparar(gate.paginas(d))
    assert j == 0.0, f"el andamiaje invisible ha contado: {j}"


@S.caso("cruzado compara pagina de A contra pagina de B y cuenta los pares malos")
def _():
    a = sitio({"x.html": PROSA_A, "y.html": PROSA_C})
    b = sitio({"x.html": PROSA_B, "z.html": "<p>nada que ver con lo anterior</p>"})
    assert callado(gate.cruzado, a, b) == 1


@S.caso("la linea de ordenes sale con 1 si hay pares malos y con 0 si no")
def _():
    d = sitio({"a.html": PROSA_A, "b.html": PROSA_B})
    assert callado(gate.main, ["interno", d]) == 1
    orig = sitio({"a.html": PROSA_A})
    assert callado(gate.main, ["interno", d, "--original", orig]) == 0, "con --original solo queda b.html"


@S.caso("un fichero ilegible se salta en vez de tumbar la comparacion")
def _():
    d = sitio({"a.html": PROSA_A})
    voc = gate.vocabularios(gate.paginas(d) + [os.path.join(d, "no-existe.html")])
    assert len(voc) == 1


if __name__ == "__main__":
    sys.exit(correr(S))
