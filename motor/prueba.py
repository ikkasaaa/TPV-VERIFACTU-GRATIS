# -*- coding: utf-8 -*-
"""Harness de pruebas minimo. Sin dependencias, un fallo no para el resto.

    S = Suite("nombre")

    @S.caso("lo que tiene que pasar, en una frase")
    def _():
        assert ..., "que ha fallado"

    if __name__ == "__main__":
        sys.exit(correr(S))

Cada caso lleva como titulo el comportamiento que protege, no el nombre de la
funcion: cuando falla, la linea que sale ya dice que se ha roto.
"""
import sys, traceback


class Suite:
    def __init__(self, nombre):
        self.nombre, self.casos = nombre, []

    def caso(self, titulo):
        def deco(f):
            self.casos.append((titulo, f))
            return f
        return deco

    def correr(self):
        fallos = 0
        print(f"  {self.nombre}")
        for titulo, f in self.casos:
            try:
                f()
                print(f"   ok  {titulo}")
            except AssertionError as e:
                fallos += 1
                print(f"   !!  {titulo}\n         {e}")
            except Exception:                      # un reventon tambien es un fallo
                fallos += 1
                print(f"   !!  {titulo}\n" + "".join(
                    "         " + l for l in traceback.format_exc().splitlines(True)[-3:]))
        return fallos


def correr(*suites):
    """Ejecuta las suites y devuelve el codigo de salida (0 si todo pasa)."""
    total = fallos = 0
    for s in suites:
        fallos += s.correr()
        total += len(s.casos)
        print()
    print(f"  {total - fallos} / {total} pasan")
    return 1 if fallos else 0
