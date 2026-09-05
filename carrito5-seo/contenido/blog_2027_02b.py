# -*- coding: utf-8 -*-
"""Blog de carrito5.com: segunda capa de febrero de 2027.

La tienda de bicicletas antes de la primavera y las Fallas de Valencia
(15 al 19 de marzo). Mismas reglas de funciones confirmadas que
blog_2026_09.py. Sobre bicicletas no se afirma gestion de taller ni numero
de cuadro en ficha: solo catalogo, stock, clientes y etiquetas.
"""

BLOG_2027_02B = {

# ------------------------------------------------------------------ 11 feb
"tienda-bicicletas-primavera-preparar-marzo": dict(
  title="Tienda de Bicicletas: la Temporada Arranca en Marzo",
  desc="El primer sábado de sol de marzo la tienda de bicicletas se llena. Recambios etiquetados, cascos y textil por talla y la ficha del cliente con su bici.",
  kw="tienda bicicletas primavera, temporada bicicletas marzo, recambios bicicleta tienda stock, tienda ciclismo preparar temporada, tpv tienda bicicletas",
  h1="Tienda de bicicletas: la temporada arranca el primer sábado de sol",
  sub="En febrero la tienda está tranquila y en marzo, el primer fin de semana que hace bueno, entran veinte personas con la bici del año pasado. Lo que se prepare ahora es lo que se vende entonces.",
  publicado="2027-02-11",
  para="Tiendas de bicicletas y ciclismo",
  resumen=[
    "La temporada de la tienda de bicicletas empieza el primer fin de semana de sol de marzo y dura hasta octubre, con el pico en abril y mayo. Febrero es el mes de preparar: recambios de consumo (cámaras, cubiertas, pastillas, cadenas) dados de alta y etiquetados, cascos, guantes y luces con su matriz de tallas y colores, y la ficha de cada cliente con la bici que tiene, para venderle lo que le corresponde sin preguntar.",
    "El pedido de febrero se hace con lo vendido en marzo y abril del año pasado por referencia, que es lo que se va a repetir.",
  ],
  cuerpo=[
    ("El primer sábado de sol",
     ["Cada año pasa igual: un sábado de marzo amanece con sol y quince grados y la tienda se llena de gente que ha sacado la bici del trastero, tiene las ruedas desinfladas, la cadena seca y las pastillas gastadas, y quiere salir mañana. Todos a la vez. Lo que se vende ese día son cámaras, cubiertas, pastillas, cadenas, lubricante, un casco nuevo porque el viejo se rompió, y luces.",
      "La tienda que tiene eso en stock, etiquetado y a mano, vende veinte tickets de cuarenta euros. La que tiene que pedirlo pierde el sábado y quizá el cliente."],
     None),
    ("Recambios de consumo: muchas referencias, pocas ventas cada una",
     ["El problema del recambio de bici es el mismo que el de cualquier tienda técnica: cientos de referencias parecidas, cámara de 26, de 27,5, de 29, de 700 con válvula fina o gorda, pastillas para diez marcas de freno. Casi todo trae código de barras del fabricante; lo que no, recibe código propio. Cada referencia en el programa con su stock, y el sábado de marzo la caja va a golpe de lector.",
      "El pedido de febrero es lo vendido en marzo y abril del año pasado por referencia, más lo que está a cero y se sabe que se pide. En recambio no se acierta a ojo: se acierta con la lista."],
     ["<strong>Cámaras, cubiertas, pastillas y cadenas</strong> por medida y tipo, con su código.",
      "<strong>Lubricantes y limpieza</strong> junto a la caja, para el ticket de impulso.",
      "<strong>Pedido de febrero</strong> con lo vendido en marzo y abril del año pasado."]),
    ("Cascos, guantes y textil: talla y color",
     ["El casco va por talla (S, M, L) y color; los guantes, por talla; el maillot y el culotte, por talla y color. Cada modelo con su matriz de tallas y colores, y el stock por variante en pantalla, para contestar «¿lo tienes en M en negro?» sin ir al almacén. En abril, cuando el que compró la bici en marzo vuelve a por la ropa, es la pregunta más repetida."],
     None),
    ("La ficha del cliente: qué bici tiene",
     ["Un cliente con una bici de montaña de 29 pulgadas y frenos de una marca concreta va a necesitar cámaras de 29 y pastillas de esa marca cada temporada. Si su ficha lleva anotada la bici (modelo, medida de rueda, tipo de freno) y las compras anteriores, la venta de marzo es «te toca cadena, la última fue hace un año». Carrito5 guarda las ventas en la ficha; la nota de la bici la escribe la tienda, y vale por todas las temporadas que vengan.",
      "Lo que Carrito5 no hace: gestionar el taller ni las órdenes de reparación. Eso se lleva aparte; la tienda y la caja, en el programa."],
     None),
  ],
  cierre=("Recambios etiquetados y la bici de cada cliente en su ficha",
          ["Carrito5 da de alta cada recambio con su código de barras o con código propio, lleva cascos y textil por talla y color, y guarda cada venta en la ficha del cliente con la nota de su bici. Es gratuito hasta 1.000 artículos, para Windows. Instalado en febrero, el primer sábado de sol la caja va a golpe de lector."],
          "Descargar Carrito5 gratis", "/descargar-tpv-gratis.html"),
  faqs=[
    ("¿Cuándo empieza la temporada en una tienda de bicicletas?",
     "El primer fin de semana de sol de marzo, de golpe, y dura hasta octubre con el pico en abril y mayo."),
    ("¿Qué se vende ese primer sábado?",
     "Cámaras, cubiertas, pastillas, cadenas, lubricante, cascos y luces: lo que la bici del trastero necesita para salir mañana."),
    ("¿Cómo llevo cientos de referencias de recambio?",
     "Cada una con su código de barras del fabricante o código propio, y su stock en el programa. El pedido se hace con lo vendido el año pasado por referencia."),
    ("¿Cómo llevo cascos y ropa por talla?",
     "Con la matriz de tallas y colores: cada modelo es un alta y el stock se ve por variante."),
    ("¿Carrito5 gestiona el taller?",
     "No. Lleva la tienda: catálogo, stock, códigos, tallas y ficha de cliente con sus compras y la nota de su bici. El taller se lleva aparte."),
  ],
  relacionadas=[("TPV para tiendas de bicicletas", "tpv-tienda-bicicletas.html", "El sector"),
                ("TPV para tiendas de deportes", "tpv-tienda-deportes.html", "Tallas técnicas"),
                ("Etiquetar antes de la campaña", "blog/etiquetar-genero-antes-de-campana.html", "Códigos y etiquetas"),
                ("Cambio de temporada", "blog/cambio-de-temporada-primavera-stock-invierno.html", "La primavera en moda")]),

# ------------------------------------------------------------------ 25 feb
"fallas-2027-valencia-comercio-15-19-marzo": dict(
  title="Fallas 2027: el Comercio del Centro de Valencia, 15 al 19",
  desc="Del 15 al 19 de marzo de 2027 el centro de Valencia se llena y se corta. Para el comercio de Ciutat Vella y Ruzafa: horarios, red saturada y ticket rápido.",
  kw="fallas 2027 comercio valencia, fallas tienda centro valencia, abrir tienda fallas, comercio ruzafa fallas, vender turistas fallas valencia, tpv valencia",
  h1="Fallas 2027: la semana del comercio del centro de Valencia",
  sub="Del lunes 15 al viernes 19 de marzo las calles se cortan, las mascletàs paran la ciudad a las dos y la gente de paso compra entre una y otra. Es la primera gran campaña de turismo del año en Valencia.",
  publicado="2027-02-25",
  para="Comercio del centro de Valencia y su área",
  resumen=[
    "Las Fallas de 2027 van del 15 al 19 de marzo, con el 19, San José, festivo en la Comunidad Valenciana y la cremà esa noche. Para el comercio de Ciutat Vella, Ruzafa, el Eixample y las zonas de monumentos es una semana con la calle llena de visitantes, calles cortadas, horarios marcados por las mascletàs y una red móvil que se cae cuando la plaza del Ayuntamiento se llena.",
    "Lo que la decide para una tienda: saber qué días puede abrir y con qué horario, tener el género de temporada y souvenir etiquetado, y un programa de caja que cobre e imprima el ticket con QR aunque no haya conexión, para un cliente que no va a volver.",
  ],
  cuerpo=[
    ("Una semana con horario propio",
     ["Las Fallas no son una campaña de compras como Navidad: son una semana en que la ciudad cambia de ritmo. A las dos, mascletà, y media hora antes y después la plaza del Ayuntamiento y sus calles son intransitables. Por la tarde, visitas a los monumentos; por la noche, verbenas y castillos. El comercio del centro vende en los huecos: por la mañana hasta la una, y por la tarde de cinco a ocho, a gente de paso.",
      "El 19 es festivo en la Comunidad Valenciana, y la apertura ese día depende del calendario de aperturas de la Generalitat; en el centro de Valencia, declarado zona de gran afluencia turística, se puede abrir. La tienda comprueba su caso y decide el horario de la semana con la mascletà delante."],
     None),
    ("El cliente de paso y el ticket",
     ["Quien entra en Fallas es un visitante: del resto de España, de Europa, de la propia Comunidad. Compra rápido, entre acto y acto, y no vuelve. La ficha de cliente no sirve aquí; sirve la velocidad y el ticket bien hecho: todo etiquetado, pasar el lector, factura simplificada con su QR de VeriFactu y siguiente.",
      "Y para el visitante extranjero que pide factura completa para su empresa, se hace con sus datos, pero fuera del pico, con calma."],
     ["<strong>Souvenirs y regalo</strong>: etiqueta propia, porque casi nada trae código.",
      "<strong>Moda de primavera</strong>: modelo con tallas y colores, que la temporada ya ha entrado.",
      "<strong>Horario en el escaparate</strong> con la mascletà marcada, para que la gente sepa cuándo estás."]),
    ("La red se cae en la plaza",
     ["Con cien mil personas en la plaza del Ayuntamiento a las dos, la red móvil de todo el centro se satura, y con ella los datáfonos que van por móvil y los programas de caja que viven en internet. Un programa que guarda los datos en el propio ordenador cobra e imprime el ticket igual. El datáfono es otra cosa: conviene tener plan B en efectivo esa media hora y decirlo en un cartel."],
     None),
    ("Después del 19: Semana Santa a la vuelta de la esquina",
     ["Las Fallas terminan el 19 y la Semana Santa de 2027 empieza el 21 de marzo, dos días después. En Valencia eso encadena dos semanas de turismo seguidas, con la Semana Santa Marinera en el Cabanyal. Lo vendido en Fallas por referencia, apuntado en el programa, es la reposición urgente del sábado 20 para llegar a la segunda semana con género."],
     None),
  ],
  cierre=("Cobrar entre mascletà y mascletà, con o sin red",
          ["Carrito5 guarda los datos en tu ordenador y cobra e imprime tickets con QR sin conexión, lee códigos de barras, imprime etiquetas para el souvenir sin código y lleva la moda de primavera por talla y color. Es gratuito hasta 1.000 artículos, para Windows. Instalado antes del 10 de marzo, la semana de Fallas se cobra pasando el lector."],
          "Descargar Carrito5 gratis", "/descargar-tpv-gratis.html"),
  faqs=[
    ("¿Cuándo son las Fallas de 2027?",
     "Del 15 al 19 de marzo de 2027, con la cremà la noche del 19, que es San José y festivo en la Comunidad Valenciana."),
    ("¿Puedo abrir la tienda el 19 de marzo en Valencia?",
     "Depende del calendario de aperturas en festivo de la Generalitat. El centro de Valencia está declarado zona de gran afluencia turística y ahí la apertura es libre; comprueba tu zona."),
    ("¿Qué horario conviene en Fallas?",
     "Por la mañana hasta la una y por la tarde de cinco a ocho, evitando la mascletà de las dos. Y ponerlo en el escaparate."),
    ("¿Qué pasa con el datáfono si se cae la red en la plaza?",
     "El datáfono por móvil puede fallar esa media hora. Un programa de caja que guarda los datos en el ordenador sigue cobrando e imprimiendo; para el cobro, plan B en efectivo."),
    ("¿Y después de Fallas?",
     "La Semana Santa empieza el 21 de marzo, dos días después. Lo vendido en Fallas por referencia es la reposición urgente del sábado 20."),
  ],
  relacionadas=[("Software TPV en Valencia", "software-tpv-valencia.html", "Ciutat Vella, Ruzafa, Eixample"),
                ("Semana Santa 2027 en zona turística", "blog/semana-santa-2027-comercio-zonas-turisticas.html", "La semana siguiente"),
                ("Funciona sin internet", "verifactu-sin-conexion-internet-offline.html", "Cobrar con la red caída"),
                ("Factura simplificada y ticket", "factura-simplificada-ticket.html", "El ticket al cliente de paso")]),

}
