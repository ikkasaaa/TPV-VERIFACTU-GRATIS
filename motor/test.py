#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lanza todas las suites de motor/. Uso: python3 motor/test.py"""
import importlib, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from prueba import correr                                # noqa: E402

SUITES = ("test_clusters", "test_marcado", "test_gate", "test_analizar")

if __name__ == "__main__":
    sys.exit(correr(*(importlib.import_module(m).S for m in SUITES)))
