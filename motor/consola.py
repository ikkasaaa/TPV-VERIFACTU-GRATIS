# -*- coding: utf-8 -*-
"""Detalles de comportarse como una orden de Unix.

Sin esto, cerrar la salida antes de tiempo (`... | head`) revienta con
BrokenPipeError en vez de terminar en silencio. Se arreglo tres veces en tres
scripts distintos antes de tener un sitio donde ponerlo.
"""
import signal


def tuberias():
    """Restaura el SIGPIPE por defecto. En Windows no existe: no pasa nada."""
    try:
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    except (AttributeError, ValueError):
        pass
