# -*- coding: utf-8 -*-
"""Paginas que carrito5.com enlaza desde su hub y su menu pero que no existen
en el sitio vivo (devuelven 404):

    tpv-boutique.html      enlazada desde sectores-y-negocios.html
    tallas-y-colores.html  enlazada desde el MENU de todas las paginas

Ferreteria y supermercado de barrio se escribieron y se RETIRARON el 5-9-2026:
el cliente confirmo que el TPV no cubre esos modelos de negocio. No se publican
y los enlaces del hub hacia ellas se han quitado.

FUNCIONES CONFIRMADAS POR EL CLIENTE (5-9-2026), las unicas que se afirman:
  - matriz de tallas y colores
  - ficha de clientes con historial, devoluciones sobre el ticket y vales
  - codigos de barras con lector, codigo interno para articulos sin EAN,
    impresion de etiquetas
Ademas de lo que ya publica la web viva: catalogo, stock, tickets con QR de
VeriFactu, funcionamiento sin internet, Windows.

NO se afirma: cierre o arqueo de caja, turnos, avisos de stock minimo, ticket
regalo, rebajas por familia, factura completa, exportacion de datos, balanza,
varias cajas. Si el cliente confirma alguna, se añade; mientras, no.
"""

SECTORES_HUECO = {

# ================================================================== boutique
"tpv-boutique.html": dict(
  title="TPV para Boutiques | Tallas, Colores y Clienta que Vuelve",
  desc="TPV gratuito para boutique de moda: matriz de tallas y colores, ficha de clienta con historial y devoluciones sobre el ticket. Windows, sin cuota ni comisión.",
  kw="tpv boutique, software boutique moda, programa tpv boutique gratis, tpv tienda ropa exclusiva, caja boutique ropa",
  h1="TPV para boutiques: pocas prendas, cada una importa",
  sub="En una boutique no se vende volumen, se vende criterio. El programa de caja tiene que ser rápido, discreto y acordarse de cada clienta mejor que tú.",
  badge="BOUTIQUE Y MODA DE AUTOR",
  crumb="Boutiques",
  fecha="2026-09-05",
  trail=[("Inicio", "index.html"), ("Sectores", "sectores-y-negocios.html"), ("Boutiques", "tpv-boutique.html")],
  resumen=[
    "Carrito5 encaja en una boutique por tres cosas: la matriz de tallas y colores para dar de alta un modelo con todas sus variantes de una vez, la ficha de clienta con su historial para devoluciones y vales, y los códigos de barras con lector para que la caja vaya rápida. El plan Inicio es gratuito hasta 1.000 artículos en catálogo.",
    "Se instala en el ordenador de la tienda, no necesita internet para cobrar y no cobra comisión por venta.",
  ],
  aside=("Instálalo entre dos clientas",
         "El instalador tarda unos minutos y no pide tarjeta. Da de alta la colección de esta temporada y ya estás cobrando."),
  cta=("Tu colección, dada de alta esta tarde",
       "Con la matriz de tallas y colores, un modelo con sus variantes se da de alta en un minuto. Descarga y compruébalo."),
  bloques=[
    ("Lo que una boutique necesita y una cadena no",
     ["El software de caja se diseña para cadenas y luego se vende a boutiques. Por eso viene con cosas que sobran: informes de cien tiendas, permisos por empleado, integración con marketplaces. Y le falta lo que sí hace falta en una tienda de treinta metros con una persona detrás del mostrador: que sea rápido, que no interrumpa la conversación con la clienta y que recuerde lo que compró la última vez.",
      "En una boutique el ticket medio es alto y el número de tickets es bajo. Eso cambia las prioridades. Un error en un ticket de cuatro euros se olvida; uno en un vestido de doscientos hay que arreglarlo delante de la clienta, con calma. Lo que importa es la devolución limpia, el vale bien hecho y el cambio de talla sin drama."],
     None),
    ("La ficha de clienta es el activo de la tienda",
     ["Una boutique vive de que la gente vuelva. La clienta que compró el abrigo en octubre es la que va a comprar el vestido en mayo, si te acuerdas de ella. Carrito5 guarda la ficha de cliente con su historial de compras, así que cuando entra sabes qué talla usa, qué colores se lleva y qué le devolviste hace dos meses.",
      "Eso sirve para dos cosas concretas. Para la devolución: se localiza el ticket original en su historial y se hace el vale o el cambio sin discutir. Y para el regalo: cuando viene alguien en diciembre sin saber la talla, la tienes en la ficha."],
     ["<strong>Historial de compras</strong> por clienta, con la prenda, la talla y el color de cada compra.",
      "<strong>Devolución sobre el ticket original</strong>, con vale de devolución o cambio de prenda.",
      "<strong>Vale de devolución</strong> con su importe, guardado en la ficha de la clienta."]),
    ("Tallas y colores sin dar de alta treinta artículos",
     ["Un modelo en cinco tallas y tres colores son quince artículos distintos si los das de alta uno a uno. En una boutique con doscientos modelos por temporada eso son tres mil líneas, y nadie las mantiene. La matriz de tallas y colores de Carrito5 resuelve eso: das de alta el modelo una vez, indicas las tallas y colores que tienes, y el programa crea las combinaciones con su stock por separado.",
      "Al final de temporada ves qué tallas se han quedado y qué colores han volado, que es la información que decide la compra de la siguiente. En la página de tallas y colores está explicado paso a paso."],
     None),
    ("Etiquetas y lector: la caja va sola",
     ["Muchas prendas llegan del proveedor con su código de barras; se dan de alta leyéndolo con el lector y se cobran pasándolo. Las que llegan sin código, o las de proveedores pequeños, reciben un código propio y Carrito5 imprime la etiqueta para colgarla de la prenda. Con eso el cobro es pasar el lector, elegir talla y color si el código no lo lleva, y cobrar. Sin buscar en listas mientras la clienta espera."],
     None),
    ("Cuánto cuesta y qué no cobra",
     ["El plan Inicio es gratuito hasta 1.000 artículos en catálogo, sin caducidad y sin tarjeta. No cobramos comisión por venta ni obligamos a comprar hardware; cobras con el datáfono de tu banco y usas el ordenador y la impresora que tengas.",
      "Si en algún momento el catálogo pasa de 1.000 artículos, se amplía con la licencia comercial, y si quieres un programa en propiedad, Caja 5, de la misma casa. Pero eso viene después, si viene."],
     None),
  ],
  faqs=[
    ("¿Es gratis para una boutique pequeña?",
     "Sí. El plan Inicio es gratuito hasta 1.000 artículos en catálogo, sin tarjeta y sin caducidad. Pregúntanos por WhatsApp cómo cuentan las tallas y colores dentro de ese límite para tu caso."),
    ("¿Cómo doy de alta un vestido en cinco tallas y tres colores?",
     "Una sola vez, con la matriz de tallas y colores. Indicas las tallas y colores que tienes y el programa crea las variantes con su stock por separado."),
    ("¿Guarda qué compró cada clienta?",
     "Sí, en su ficha de cliente, con la prenda, la talla y el color de cada compra. Sirve para devoluciones, vales y para el regalo de alguien que no sabe la talla."),
    ("¿Cómo hago una devolución si la clienta no trae el ticket?",
     "Se busca la venta en su historial de cliente y se hace la devolución sobre esa venta, con vale o con cambio."),
    ("¿Imprime etiquetas para las prendas que vienen sin código?",
     "Sí. El programa asigna un código propio a la prenda e imprime la etiqueta con su código de barras."),
    ("¿Funciona con el ordenador que tengo detrás del mostrador?",
     "Si tiene Windows, casi seguro. Pruébalo antes de comprar nada."),
    ("¿Cobráis algo por cada venta con tarjeta?",
     "No. Cobras con el datáfono de tu banco, con la comisión que tengas con él. Carrito5 no participa en el cobro."),
  ],
  satelites=[("TPV para tiendas de ropa", "tpv-tienda-ropa.html", "Si tu volumen es mayor"),
             ("Matriz de tallas y colores", "tallas-y-colores.html", "Cómo funciona paso a paso"),
             ("TPV para lencería y mercería", "tpv-lenceria-merceria.html", "Tallas, copas y colores"),
             ("TPV para joyerías", "tpv-joyeria-relojeria.html", "Piezas de valor"),
             ("TPV en Madrid", "tpv-madrid.html", "Salamanca, Malasaña, Chueca"),
             ("Descargar Carrito5 gratis", "descargar-tpv-gratis.html", "Sin tarjeta")]),

# ============================================================ tallas y colores
"tallas-y-colores.html": dict(
  title="Matriz de Tallas y Colores en el TPV | Carrito5",
  desc="Cómo dar de alta un modelo con todas sus tallas y colores de una vez y ver el stock por variante. La función que separa un TPV de moda del resto. Gratis.",
  kw="tpv tallas y colores, matriz tallas colores, programa tpv tallas, software tienda ropa tallas colores, control stock tallas, tpv textil tallas",
  h1="Tallas y colores: un modelo, todas sus variantes",
  sub="Es la función que separa un TPV de moda de un TPV cualquiera. Sin ella, cada camiseta en seis tallas y cuatro colores son veinticuatro artículos que nadie mantiene.",
  badge="FUNCIÓN · MODA Y CALZADO",
  crumb="Tallas y colores",
  fecha="2026-09-05",
  trail=[("Inicio", "index.html"), ("Tallas y colores", "tallas-y-colores.html")],
  resumen=[
    "La matriz de tallas y colores de Carrito5 permite dar de alta un modelo una sola vez, indicar las tallas y los colores que tienes, y que el programa cree cada combinación con su stock propio. Al vender, eliges talla y color y se descuenta la variante exacta.",
    "Está incluida en el plan gratuito y se usa igual en ropa, calzado, lencería y textil hogar: solo cambia qué llamas talla.",
  ],
  aside=("Pruébala con un modelo real",
         "Descarga, da de alta una camiseta con sus tallas y colores y haz una venta. Verás el stock por variante en el momento."),
  cta=("Da de alta tu colección en una tarde",
       "Con la matriz, doscientos modelos con sus variantes se dan de alta en el tiempo que antes te llevaban veinte."),
  bloques=[
    ("El problema que resuelve",
     ["Una tienda de ropa que no tiene matriz de tallas y colores hace una de dos cosas, y las dos son malas. O da de alta cada combinación como un artículo separado, con lo que una colección de doscientos modelos son tres o cuatro mil líneas que hay que crear, etiquetar y mantener. O da de alta solo el modelo y lleva las tallas de cabeza, con lo que el stock del programa no dice qué talla queda y a final de temporada no se sabe qué se ha quedado sin vender.",
      "La matriz es la tercera vía: el modelo se crea una vez, con su nombre, su precio y su código. Después se indican las tallas (de XS a XXL, o números de calzado, o medidas de cama en textil hogar) y los colores. El programa genera cada combinación de talla y color como una variante con stock independiente, sin que tengas que crearlas a mano."],
     None),
    ("Cómo se usa, paso a paso",
     ["El flujo en Carrito5 es el mismo para una camiseta, un zapato o un juego de sábanas: lo único que cambia es qué llamas talla.",
      '<ol class="c5-pasos">'
      '<li><strong>Crea el modelo</strong> con su nombre y su precio de venta.</li>'
      '<li><strong>Indica las tallas</strong> que existen para ese modelo. En calzado, los números; en textil hogar, las medidas.</li>'
      '<li><strong>Indica los colores</strong> del modelo.</li>'
      '<li><strong>Introduce el stock</strong> por variante cuando llega la mercancía.</li>'
      '<li><strong>Vende</strong> eligiendo talla y color en la caja, o pasando el código de barras de la prenda. Se descuenta la variante exacta.</li>'
      '<li><strong>Consulta</strong> el stock del modelo por talla y color, para saber qué queda de cada una.</li>'
      '</ol>',
      "Si la prenda llega del proveedor con código de barras, se da de alta leyéndolo con el lector. Si llega sin código, el programa le asigna uno propio e imprime la etiqueta."],
     None),
    ("Lo que cambia a final de temporada",
     ["El valor real de la matriz se ve en febrero y en agosto. El stock por talla y color de un modelo te dice, sin contar nada, que la talla M en negro ha volado y que la XL en azul no se ha tocado. Multiplica eso por toda la colección y tienes la información que decide la compra de la siguiente temporada, que es donde una tienda de ropa gana o pierde el año."],
     None),
    ("Dónde se usa además de en ropa",
     ["El nombre engaña: la matriz sirve para cualquier artículo que tenga dos dimensiones de variante. En zapatería es número y color. En lencería es talla y copa. En textil hogar es medida de cama y color. En complementos, tamaño y color de un bolso. En deportes, talla técnica y color de una zapatilla.",
      "Lo que no cubre es la tercera dimensión: talla, color y además largo de pernera, por ejemplo. Ahí lo habitual es dar de alta el largo como modelo distinto («vaquero recto 32» y «vaquero recto 34») y usar la matriz para talla y color dentro de cada uno."],
     None),
  ],
  faqs=[
    ("¿La matriz de tallas y colores está en el plan gratuito?",
     "Sí. El plan Inicio es gratuito hasta 1.000 artículos en catálogo. Pregúntanos por WhatsApp cómo cuentan las variantes dentro de ese límite para tu colección."),
    ("¿Cómo doy de alta un modelo con cinco tallas y tres colores?",
     "Una sola vez: creas el modelo, indicas sus tallas y sus colores, y el programa genera las quince combinaciones con su stock por separado."),
    ("¿Puedo leer el código de barras que trae la prenda del proveedor?",
     "Sí. Se da de alta leyéndolo con el lector y después se cobra pasándolo. Para prendas sin código, el programa asigna uno propio e imprime la etiqueta."),
    ("¿Sirve para calzado con numeración?",
     "Sí. En zapatería la «talla» es el número (del 35 al 46, por ejemplo) y el color sigue siendo el color."),
    ("¿Y para sábanas por medida de cama?",
     "Sí. La medida (90, 105, 135, 150, 180) hace de talla y el color de segunda dimensión."),
    ("¿Puedo ver de un vistazo qué tallas quedan de un modelo?",
     "Sí, el stock se consulta por modelo, con lo que queda de cada talla y color."),
    ("Tengo tres variantes: talla, color y largo. ¿Cómo lo hago?",
     "La matriz cubre dos dimensiones. Da de alta cada largo como un modelo distinto y usa la matriz para talla y color dentro de cada uno."),
  ],
  satelites=[("TPV para tiendas de ropa", "tpv-tienda-ropa.html", "Donde más se usa"),
             ("TPV para zapaterías", "tpv-zapateria.html", "Números y pares"),
             ("TPV para lencería y mercería", "tpv-lenceria-merceria.html", "Talla y copa"),
             ("TPV para textil hogar", "tpv-textil-hogar.html", "Medidas de cama"),
             ("TPV para boutiques", "tpv-boutique.html", "Pocas prendas, cada una importa"),
             ("Descargar Carrito5 gratis", "descargar-tpv-gratis.html", "Y pruébala hoy")]),

}
