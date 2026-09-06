# carrito5-seo

Pipeline de contenido para carrito5.com (TPV gratuito para Windows).

Sitio estático, distinto de abacosoftware (ASP). Comparte con él el motor de
`../motor/`, que incluye el filtro anti-plantilla y la **comprobación cruzada
entre sitios**: los dos dominios son del mismo dueño, así que reutilizar texto
entre ellos crea contenido duplicado que perjudica a ambos.

    python3 pipeline/generar.py <dir-salida> nucleo verifactu

Lo que ya existe en la web viva no se sobrescribe: va a `_propuestas/`. La lista
de páginas vivas sale de `inventario/urls_descubiertas.txt` (más las siete de
constancia directa en `generar.py`); si descubres una página viva nueva, añádela
al inventario y el generador la respeta.

Comprobar duplicación, dentro del sitio y contra abacosoftware:

    python3 ../motor/gate.py interno <dir-salida>
    python3 ../motor/gate.py cruzado <dir-salida> <dir-abacosoftware>

Herramientas de inventario (`pipeline/`): `analizar_inventario.py` agrupa las
URLs vivas por intención, `calidad_titulos.py` revisa los `<title>` observados y
`cobertura_geografica.py` cruza las ciudades del menú con las que tienen página.
Todas leen de `inventario/` por defecto.

La web base del cliente no está en el repo. Las tres páginas originales
(index, tpv-tienda-ropa, tpv-zapateria) se extraen del fichero de auditoría
que entregó el cliente.
