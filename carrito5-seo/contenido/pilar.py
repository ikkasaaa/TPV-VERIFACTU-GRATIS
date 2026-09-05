# -*- coding: utf-8 -*-
"""Paginas pilar de carrito5.com: las que capturan la intencion comercial
amplia («mejor tpv gratis», «tpv para autonomos gratis», «programa caja
registradora gratis») y la pagina de entidad que necesita la busqueda
generativa para saber quien es Carrito5.

Reparto con abacosoftware.com (mismo dueño): la intencion «gratis» entera
es de carrito5. abacosoftware tiene tpv-gratis-para-comercio.asp como
editorial de «letra pequeña» y debe enlazar aqui como la opcion gratuita de
la casa, no competir. Detalle en PLAN_MAESTRO_SEO_GEO.md.

Sobre competidores: se describen categorias de producto, no se atribuyen
precios ni funciones concretas a marcas que no se hayan verificado. Cuando
se nombra una marca es como ejemplo de la categoria y con lo que esa marca
publica de forma general (modelo de comision por cobro, app movil, software
libre). La regla del skill schema-verifactu-tpv: sobre terceros, solo lo
verificable, y siempre «pide la declaracion responsable por escrito».
"""

AVISO = ("Esta página es información general, no asesoramiento fiscal. Los plazos de "
         "VeriFactu se han movido dos veces y pueden volver a cambiar: confirma tu caso "
         "con tu asesor o en la sede electrónica de la Agencia Tributaria.")

PILAR = {

# ============================================================ comparativa
"mejor-tpv-gratis-2026.html": dict(
  title="Mejor TPV Gratis 2026: Comparativa Honesta para Comercio",
  desc="Qué programas TPV gratis existen de verdad en España en 2026, por dónde cobra cada uno y cuál encaja con una tienda física. Con VeriFactu y sin comisión.",
  kw="mejor tpv gratis, tpv gratis 2026, comparativa tpv gratis, software tpv gratuito, programa tpv gratis españa, mejor programa tpv gratis, tpv gratis windows",
  h1="Mejor TPV gratis en 2026: qué hay y por dónde cobra cada uno",
  sub="Ningún software se regala. Los gratuitos cobran por otro sitio: comisión, módulos, límite de tiempo o tu paciencia. Esta página dice dónde está el cobro en cada caso, incluido el nuestro.",
  badge="COMPARATIVA 2026",
  crumb="Mejor TPV gratis",
  fecha="2026-09-05",
  soft=True,
  trail=[("Inicio", "index.html"), ("Mejor TPV gratis 2026", "mejor-tpv-gratis-2026.html")],
  resumen=[
    "En España hay cinco tipos de TPV gratuito en 2026: la aplicación de facturación de la AEAT, los programas de escritorio con plan gratuito por tamaño de catálogo (como Carrito5, gratis hasta 1.000 artículos), las apps de TPV atadas a una pasarela de cobro que cobran comisión por cada venta, los TPV en la nube con plan gratuito que cobran por módulos, y el software libre que cuesta tiempo de instalación.",
    "Para una tienda física con mostrador y stock, el que menos cuesta a cinco años es el de escritorio con plan gratuito, siempre que el catálogo quepa. Para quien solo emite facturas, la herramienta de la AEAT. Para quien cobra poco y quiere empezar con el móvil, la app con comisión, sabiendo lo que se paga.",
  ],
  aside=("Dónde cobra Carrito5, sin rodeos",
         "Gratis hasta 1.000 artículos en catálogo. Por encima, licencia comercial. Sin comisión por venta, sin hardware obligatorio y sin caducidad."),
  cta=("Comprueba la letra pequeña con tu catálogo",
       "Descarga Carrito5, da de alta tus artículos y mira si cabes en el plan gratuito. Es la comparativa que de verdad cuenta."),
  bloques=[
    ("Los cinco tipos de TPV gratis que existen, y dónde está el cobro",
     ["Antes de comparar marcas conviene comparar modelos de negocio, porque es lo que decide cuánto pagas a cinco años. Estos son los cinco que hay en el mercado español.",
      '<div class="c5-tabla-wrap"><table class="c5-tabla"><thead><tr><th>Tipo</th><th>Ejemplo</th><th>Por dónde cobra</th><th>Funciona sin internet</th><th>Para quién</th></tr></thead><tbody>'
      '<tr><td>Aplicación oficial de la AEAT</td><td>Herramienta de facturación de la Agencia Tributaria</td><td>No cobra. Tampoco lleva catálogo, stock ni caja.</td><td>No</td><td>Profesional que emite pocas facturas y no tiene mostrador.</td></tr>'
      '<tr><td>Escritorio con plan gratuito por catálogo</td><td>Carrito5 (plan Inicio)</td><td>Licencia comercial cuando el catálogo pasa de 1.000 artículos.</td><td>Sí</td><td>Tienda física con stock, una caja y catálogo contenido.</td></tr>'
      '<tr><td>App atada a pasarela de cobro</td><td>TPV de las plataformas de datáfono (Square, SumUp y similares)</td><td>Comisión sobre cada cobro con tarjeta, todos los meses, para siempre.</td><td>Parcial: la app sí, el cobro no.</td><td>Quien empieza con el móvil y factura poco con tarjeta.</td></tr>'
      '<tr><td>Nube con plan gratuito por módulos</td><td>Loyverse y similares</td><td>Cuota mensual por los módulos que necesitas (inventario avanzado, empleados).</td><td>Limitado</td><td>Quien quiere tablet y acepta cuota al crecer.</td></tr>'
      '<tr><td>Software libre</td><td>Odoo Community, uniCenta</td><td>Tu tiempo, o el de un informático que lo instale y lo mantenga.</td><td>Sí, si lo instalas en local</td><td>Quien tiene perfil técnico o presupuesto para consultoría.</td></tr>'
      '</tbody></table></div>',
      "La fila que más engaña es la tercera. Un 1,5 o un 2 por ciento sobre cada cobro con tarjeta parece poco hasta que lo multiplicas por toda la facturación con tarjeta de cinco años. En una tienda que cobra 100.000 euros al año con tarjeta son entre 7.500 y 10.000 euros por un programa «gratis». Comprueba la tarifa exacta de cada plataforma, que cambia; el orden de magnitud no."],
     None),
    ("Cómo se calcula el coste real a cinco años",
     ["Una tienda no cambia de programa cada año, así que el coste que importa es el acumulado. La cuenta es sencilla y conviene hacerla con tus propios números antes de instalar nada.",
      "Suma tres cosas: lo que pagas de cuota o licencia, lo que pagas de comisión sobre tus cobros con tarjeta, y lo que pagas de hardware obligatorio si el programa solo funciona con su terminal o su tablet. Réstale lo que ya tienes: el ordenador del mostrador, la impresora de tickets, el datáfono de tu banco.",
      "Con esa cuenta, el programa de escritorio con plan gratuito gana casi siempre en comercio físico, porque las tres partidas son cero mientras el catálogo quepa. La app con comisión gana si cobras muy poco con tarjeta. Y la nube gana si necesitas varias tiendas o trabajar desde fuera, cosa que en una tienda de barrio con una caja rara vez ocurre."],
     ["<strong>Cuota o licencia</strong>: de 0 a 40 euros al mes según el producto. A cinco años, hasta 2.400 euros.",
      "<strong>Comisión por cobro</strong>: de 0 a un 2 por ciento de lo que cobres con tarjeta. La partida que más crece con el negocio.",
      "<strong>Hardware obligatorio</strong>: de 0 a varios cientos de euros si el programa exige su terminal.",
      "<strong>Lo que ya tienes</strong>: PC, impresora y datáfono de tu banco. Un programa que los aprovecha ahorra todo eso."]),
    ("Qué tiene que cumplir cualquiera de ellos en 2026",
     [AVISO,
      "Sea cual sea el que elijas, en 2027 tiene que ser un sistema de facturación conforme a VeriFactu: sociedades desde el 1 de enero y autónomos desde el 1 de julio. Eso descarta las hojas de cálculo, los programas abandonados y las apps que no publiquen su adaptación.",
      "La comprobación es una sola: pide al fabricante la declaración responsable de su software por escrito. Es el documento que acredita que el programa cumple, y si no te lo dan, no lo instales. Vale para Carrito5 y vale para cualquier otro."],
     None),
    ("Carrito5 dentro de esta comparativa: lo bueno y lo que no hace",
     ["Sería raro que una comparativa en nuestra web no nos saliera bien, así que vamos a decir también lo que no hacemos. Carrito5 es un programa de escritorio para Windows con plan gratuito hasta 1.000 artículos. Lo bueno: sin comisión, sin cuota, sin hardware obligatorio, funciona sin internet, lleva tallas y colores, clientes con devoluciones y códigos de barras con etiquetas, y ya está adaptado a VeriFactu. Lo hace la misma empresa que desarrolla Caja 5 desde hace más de 28 años.",
      "Lo que no hace: no funciona en Mac ni en tablet Android, no lleva varias cajas a la vez sobre el mismo stock, no tiene comandas de hostelería y no conecta con balanza. Si tu negocio necesita alguna de esas cosas, en esta misma tabla tienes las alternativas, y te lo decimos antes de que pierdas una tarde."],
     None),
    ("Cómo elegir en diez minutos",
     ['<ol class="c5-pasos">'
      '<li><strong>¿Tienes mostrador y stock?</strong> Si no, la aplicación de la AEAT te vale y ahórrate el resto.</li>'
      '<li><strong>¿Cuántos artículos distintos vendes?</strong> Menos de 1.000, plan gratuito de escritorio. Más, licencia o nube.</li>'
      '<li><strong>¿Cuánto cobras con tarjeta al año?</strong> Multiplica por 0,02 y por cinco. Es lo que cuesta la app «gratis» con comisión.</li>'
      '<li><strong>¿Se te cae internet?</strong> Si la respuesta es «a veces», descarta lo que no funcione en local.</li>'
      '<li><strong>¿Tienes ya PC, impresora y datáfono?</strong> Elige lo que los aproveche.</li>'
      '<li><strong>Pide la declaración responsable</strong> al fabricante que te quede. Sin ella, siguiente.</li>'
      '</ol>'],
     None),
  ],
  faqs=[
    ("¿Cuál es el mejor TPV gratis para una tienda pequeña en 2026?",
     "Para una tienda física con una caja y catálogo contenido, un programa de escritorio con plan gratuito por tamaño de catálogo, como Carrito5, es el que menos cuesta a cinco años: sin cuota, sin comisión y sin hardware obligatorio. Si cobras poco con tarjeta y quieres empezar con el móvil, una app con comisión puede valer al principio."),
    ("¿Existe algún TPV gratis de verdad, sin ningún cobro?",
     "La aplicación de la AEAT no cobra nada, pero no es un TPV: no lleva catálogo, stock ni caja. Todo lo demás cobra por algún sitio: catálogo, comisión, módulos o tiempo de instalación. Lo importante es saber por cuál."),
    ("¿Los TPV gratis cumplen con VeriFactu?",
     "Algunos sí y otros no. Pide al fabricante la declaración responsable por escrito: es el único documento que lo acredita. Carrito5 la entrega y su plan gratuito emite tickets conformes."),
    ("¿Cuánto cuesta de verdad un TPV con comisión por venta?",
     "Depende de lo que cobres con tarjeta. Con un 1,5 o un 2 por ciento, una tienda que cobra 100.000 euros al año con tarjeta paga entre 1.500 y 2.000 euros anuales. A cinco años, entre 7.500 y 10.000. Comprueba la tarifa exacta de cada plataforma."),
    ("¿Qué límite tiene el plan gratuito de Carrito5?",
     "1.000 artículos en catálogo. Por encima se amplía con la licencia comercial. No hay límite de tickets, de tiempo ni de funciones dentro de ese catálogo."),
    ("¿Es mejor un TPV en la nube o uno instalado en el PC?",
     "Para una tienda con una caja, el instalado en el PC funciona sin internet y no lleva cuota. La nube compensa cuando hay varias tiendas o hace falta trabajar desde fuera del local."),
    ("¿Puedo empezar con uno gratis y cambiar después?",
     "Sí, pero pregunta antes a cada fabricante cómo se sacan el catálogo y los clientes si un día quieres cambiar. Es la pregunta que casi nadie hace al instalar un programa gratuito y la que más cara sale al querer irse."),
    ("¿Sirve un TPV gratis para un bar o restaurante?",
     "Los de esta comparativa están pensados para comercio. La hostelería necesita mesas y comandas, que es otro tipo de producto. Carrito5 no lo cubre."),
  ],
  satelites=[("Descargar Carrito5 gratis", "descargar-tpv-gratis.html", "Plan Inicio, sin tarjeta"),
             ("VeriFactu gratis: opciones reales", "verifactu-gratis.html", "La AEAT y los TPV gratuitos"),
             ("La aplicación de la AEAT", "verifactu-aeat-descargar.html", "Para quién sirve y para quién no"),
             ("TPV gratis para autónomos", "tpv-gratis-autonomos.html", "Tu caso concreto"),
             ("Programa de caja registradora gratis", "programa-caja-registradora-gratis.html", "Si vienes de una caja de toda la vida"),
             ("Quién está detrás de Carrito5", "sobre-carrito5.html", "Empresa, sede y modelo")]),

# ============================================================ autonomos
"tpv-gratis-autonomos.html": dict(
  title="TPV Gratis para Autónomos con Tienda | Sin Cuota ni Comisión",
  desc="TPV gratuito para autónomo con comercio: se instala en tu PC, no pide tarjeta, no cobra comisión y cumple VeriFactu antes de tu fecha de julio de 2027.",
  kw="tpv gratis autonomos, tpv para autonomos gratis, programa tpv autonomo, software tpv autonomos, tpv autonomo sin cuota, caja registradora autonomo gratis",
  h1="TPV gratis para autónomos con tienda",
  sub="Si eres autónomo con un local, cada gasto fijo sale de tu bolsillo. Un programa de caja que cobra cuota es un gasto fijo más. Este no la tiene.",
  badge="AUTÓNOMOS Y PEQUEÑO COMERCIO",
  crumb="TPV para autónomos",
  fecha="2026-09-05",
  soft=True,
  trail=[("Inicio", "index.html"), ("TPV gratis para autónomos", "tpv-gratis-autonomos.html")],
  resumen=[
    "Carrito5 es un TPV gratuito para autónomos con comercio físico: plan Inicio sin cuota y sin caducidad hasta 1.000 artículos en catálogo, sin comisión por venta y sin hardware obligatorio. Se instala en el ordenador que tengas con Windows y funciona sin internet.",
    "Para un autónomo la obligación de VeriFactu llega el 1 de julio de 2027. Carrito5 ya está adaptado, así que empezar con él ahora evita cambiar de programa dos veces.",
  ],
  aside=("Gasto fijo: cero",
         "Sin cuota, sin comisión y sin caducidad. Lo único que pones es el ordenador que ya tienes en el mostrador."),
  cta=("Instálalo hoy y quita un gasto fijo de la lista",
       "Descarga, da de alta lo que más vendes y cobra esta misma tarde. Si te atascas, WhatsApp."),
  bloques=[
    ("Lo que cambia cuando el negocio es tuyo",
     ["Un autónomo con una tienda mira las cuentas de otra manera. Una cuota de 30 euros al mes por el programa de caja es un gasto pequeño para una cadena y 360 euros al año que salen de tu nómina si eres tú. Y una comisión del 2 por ciento sobre lo que cobras con tarjeta es dinero que no ves salir, pero sale todos los meses.",
      "Por eso para un autónomo el orden de las preguntas es distinto. Primero cuánto cuesta de verdad a lo largo del tiempo. Después si aguanta un sábado sin internet. Y después qué funciones tiene, porque las que hacen falta en una tienda de una persona son pocas: cobrar, ticket, stock y clientes."],
     None),
    ("Qué te da el plan gratuito y qué no",
     ["El plan Inicio de Carrito5 es el programa completo para lo esencial, gratuito de forma indefinida mientras tu catálogo no pase de 1.000 artículos. Sin tarjeta, sin fecha de caducidad, sin versión de prueba que se apaga a los 30 días.",
      "Lo que no da: no hay versión para Mac ni para tablet, no lleva varias cajas y no tiene comandas de hostelería. Si tu actividad es un bar, un taller con órdenes de trabajo complejas o una tienda con dos mostradores, te lo decimos ahora para que no pierdas la tarde."],
     ["<strong>Catálogo</strong> con códigos de barras, lector y etiquetas, y matriz de tallas y colores.",
      "<strong>Stock</strong> por artículo y por variante.",
      "<strong>Ticket</strong> con QR de VeriFactu.",
      "<strong>Clientes</strong> con historial, devoluciones sobre el ticket original y vales.",
      "<strong>Sin internet</strong>: los datos están en tu ordenador."]),
    ("VeriFactu si eres autónomo: tu fecha y lo que necesitas",
     [AVISO,
      "El calendario vigente tras el Real Decreto-ley 15/2025 pone a los autónomos el 1 de julio de 2027. Hasta entonces la adaptación es voluntaria. No hay que pagar nada a Hacienda, no hay que contratar nada con nadie, y no hace falta gestor para el hecho de facturar con un programa adaptado.",
      "Lo que sí necesitas es que el programa con el que emites tickets esté adaptado y que su fabricante te dé la declaración responsable. Carrito5 la entrega. Si hoy facturas con una libreta, con una hoja de cálculo o con una caja registradora antigua, eso es lo que tiene que cambiar antes de julio de 2027."],
     None),
    ("Cuánto ahorras a cinco años, con números",
     ["Un autónomo con una tienda que cobra 60.000 euros al año con tarjeta y usa un programa por suscripción de 25 euros al mes con un 1,75 por ciento de comisión paga cada año 300 euros de cuota y 1.050 de comisión. A cinco años, 6.750 euros. Con Carrito5 en el plan Inicio, cero, y el datáfono sigue siendo el de tu banco con la comisión que tengas negociada.",
      "Si tu catálogo pasa de 1.000 artículos y necesitas la licencia comercial, sigue siendo un pago acotado y sin comisión. Y si prefieres tener el programa en propiedad, Caja 5, de la misma casa, se compra una vez. Haz la cuenta con tus números: la hoja está en la comparativa de TPV gratis."],
     None),
    ("Empezar en una tarde, sin ayuda técnica",
     ['<ol class="c5-pasos">'
      '<li>Descarga el instalador en el ordenador del mostrador y ejecútalo.</li>'
      '<li>Pon tus datos fiscales: nombre, NIF, dirección. Salen en el ticket.</li>'
      '<li>Elige la impresora de tickets que tengas y saca uno de prueba.</li>'
      '<li>Da de alta las veinte o treinta referencias que más vendes. No el catálogo entero.</li>'
      '<li>Haz una venta real y comprueba el ticket con su QR.</li>'
      '</ol>',
      "Si algo no arranca, WhatsApp al 611 500 052. Te contesta una persona en España, en horario comercial."],
     None),
  ],
  faqs=[
    ("¿Hay un TPV gratis para autónomos sin cuota mensual?",
     "Sí. El plan Inicio de Carrito5 no tiene cuota, no pide tarjeta y no caduca. El límite es de 1.000 artículos en catálogo, no de tiempo ni de tickets."),
    ("¿Cuándo me obliga VeriFactu si soy autónomo?",
     "Desde el 1 de julio de 2027, según el calendario vigente tras el RD-ley 15/2025. Durante 2026 y el primer semestre de 2027 la adaptación es voluntaria. Confirma tu fecha con tu asesor."),
    ("¿Tengo que pagar algo a Hacienda por VeriFactu?",
     "No. No hay tasa ni cuota. Lo único que puede costarte es el programa, y Carrito5 en su plan Inicio es gratuito."),
    ("¿Puedo seguir cobrando con la libreta hasta 2027?",
     "Hasta tu fecha, sí. Pero empezar antes con un programa adaptado te ahorra el cambio con prisa y te da el stock y la ficha de clientes desde ya."),
    ("¿Me sirve para llevar a los clientes que repiten?",
     "Sí. La ficha de cliente guarda el historial de compras y sirve para hacer devoluciones sobre el ticket original y vales de devolución."),
    ("¿Necesito comprar un ordenador o una impresora?",
     "Casi nunca. Vale el ordenador con Windows que ya tengas y la mayoría de impresoras de tickets de 80 mm. Prueba antes de comprar nada."),
    ("¿Cobráis comisión por lo que cobro con tarjeta?",
     "No. Cobras con el datáfono de tu banco y la comisión es la que tengas negociada con él. Carrito5 no participa."),
    ("Soy autónomo y trabajo en un mercadillo, sin local. ¿Me sirve?",
     "Si cobras desde un portátil con Windows, sí, y funciona sin internet. Si cobras desde el móvil, no: Carrito5 es un programa de escritorio."),
  ],
  satelites=[("VeriFactu para autónomos", "verifactu-autonomos.html", "Tu fecha y tus obligaciones"),
             ("Mejor TPV gratis 2026", "mejor-tpv-gratis-2026.html", "Comparativa con números"),
             ("Descargar Carrito5 gratis", "descargar-tpv-gratis.html", "Instalador para Windows"),
             ("TPV para comercio local", "software-tpv-comercio-local.html", "La tienda de barrio"),
             ("Subvenciones por adaptarse a VeriFactu", "blog-subvenciones-verifactu-autonomos-2026.html", "Lo que hay y lo que no")]),

# ============================================================ caja registradora
"programa-caja-registradora-gratis.html": dict(
  title="Programa de Caja Registradora Gratis para PC | Carrito5",
  desc="Convierte el ordenador de tu tienda en una caja registradora: programa gratuito para Windows con tickets con QR, stock y clientes. Sin cuota ni comisión.",
  kw="programa caja registradora gratis, software caja registradora, caja registradora pc gratis, programa caja registradora windows, caja registradora virtual gratis, sustituir caja registradora",
  h1="Programa de caja registradora gratis: tu PC como caja",
  sub="Una caja registradora es un ordenador con pocas teclas. Si ya tienes el ordenador, lo que te falta es el programa, y ese es gratis.",
  badge="DE LA CAJA REGISTRADORA AL TPV",
  crumb="Programa de caja registradora",
  fecha="2026-09-05",
  soft=True,
  trail=[("Inicio", "index.html"), ("Programa de caja registradora gratis", "programa-caja-registradora-gratis.html")],
  resumen=[
    "Carrito5 es un programa gratuito que convierte un ordenador con Windows en una caja registradora completa: cobro, ticket impreso con QR, catálogo con códigos de barras y lector, stock de artículos y ficha de clientes. El plan Inicio no tiene cuota ni caducidad hasta 1.000 artículos.",
    "A diferencia de una caja registradora tradicional, lleva el QR de VeriFactu en cada ticket, guarda cada venta con su artículo y su cliente, y se actualiza sin cambiar de aparato.",
  ],
  aside=("Lo que necesitas, probablemente ya lo tienes",
         "Un PC con Windows, una impresora de tickets y un cajón que se abre desde la impresora. Descarga el programa y prueba."),
  cta=("Jubila la caja registradora esta semana",
       "Instala Carrito5 en el ordenador, conecta la impresora y saca el primer ticket con QR."),
  bloques=[
    ("Caja registradora o programa de caja: la diferencia que importa en 2027",
     [AVISO,
      "Una caja registradora de toda la vida suma, imprime un ticket y abre el cajón. Guarda un total del día en su memoria y poco más. Un programa de caja en un ordenador hace eso y además guarda cada venta con su artículo, lleva el stock y conoce a los clientes.",
      "Hasta ahora esa diferencia era de comodidad. Con VeriFactu pasa a ser de cumplimiento: los sistemas informáticos de facturación tienen que generar registros encadenados y el QR en cada ticket, y una caja registradora antigua no lo hace. Si tu caja registradora emite tickets a clientes, pregunta al fabricante si la ha adaptado y si te entrega la declaración responsable. Si no, antes de tu fecha tendrás que sustituirla, y un programa gratuito en el ordenador que ya tienes es la salida más barata."],
     None),
    ("Qué hace falta para montar la caja con el ordenador",
     ["Menos de lo que parece, y casi todo lo tiene ya una tienda que lleva años abierta.",
      '<div class="c5-tabla-wrap"><table class="c5-tabla"><thead><tr><th>Pieza</th><th>Qué vale</th><th>Coste si no lo tienes</th></tr></thead><tbody>'
      '<tr><td>Ordenador</td><td>Cualquiera con Windows 7, 8, 10 u 11. Con disco SSD va más ágil.</td><td>De 0 (el que tienes) a unos 300 euros de segunda mano.</td></tr>'
      '<tr><td>Programa</td><td>Carrito5, plan Inicio.</td><td>0 euros hasta 1.000 artículos.</td></tr>'
      '<tr><td>Impresora de tickets</td><td>Térmica de 80 mm, USB o red. La mayoría de marcas valen.</td><td>De 0 (la que tienes) a unos 100 euros.</td></tr>'
      '<tr><td>Cajón portamonedas</td><td>Se conecta a la impresora de tickets. Consúltanos tu modelo.</td><td>De 0 a unos 50 euros.</td></tr>'
      '<tr><td>Lector de códigos de barras</td><td>Opcional. USB, funciona como un teclado.</td><td>Unos 30 o 40 euros.</td></tr>'
      '<tr><td>Datáfono</td><td>El de tu banco, como hasta ahora.</td><td>Sin cambio.</td></tr>'
      '</tbody></table></div>',
      "El cajón es la duda más frecuente. Los cajones portamonedas se conectan a la impresora de tickets con un cable RJ11. Mándanos el modelo de tu impresora y de tu cajón por WhatsApp y te confirmamos si te valen."],
     None),
    ("Qué gana la tienda al pasar del aparato al programa",
     ["Lo primero que se nota es el stock: cada venta descuenta el artículo, así que sabes qué queda sin contar. Lo segundo, los clientes: cada venta queda en la ficha de quien la hizo, y una devolución se hace sobre el ticket original y no sobre un papel firmado. Lo tercero, las etiquetas: lo que llega sin código de barras recibe uno propio y el programa imprime la etiqueta.",
      "Y lo que no cambia: la velocidad. Con un lector de códigos de barras la caja va igual de rápida que el aparato, y con los artículos sin código se teclea un código corto, como se tecleaba el departamento en la caja de antes."],
     ["<strong>Stock al día</strong> sin recuentos.",
      "<strong>Ficha de cliente</strong> con historial, devoluciones y vales sobre el ticket original.",
      "<strong>Etiquetas con código de barras</strong> para lo que llega sin él.",
      "<strong>Ticket con QR</strong> de VeriFactu.",
      "<strong>Los datos en tu ordenador</strong>, no en un servidor ajeno."]),
    ("Lo que una caja registradora hace y este programa no",
     ["Honestidad: hay dos cosas que la caja de toda la vida hace mejor. Arranca en dos segundos al enchufarla, mientras que un ordenador tarda lo que tarde Windows. Y no se actualiza sola en el peor momento. Contra lo primero, dejar el ordenador encendido; contra lo segundo, configurar Windows para que actualice fuera de horario.",
      "Y hay una cosa que este programa no hace: no funciona en tablet ni en móvil. Si quieres cobrar con una tablet Android, este no es tu producto y hay otros en la comparativa de TPV gratis."],
     None),
  ],
  faqs=[
    ("¿Puedo usar mi ordenador como caja registradora gratis?",
     "Sí. Carrito5 se instala en cualquier PC con Windows y hace de caja: cobro, ticket con QR, códigos de barras, stock y clientes. El plan Inicio es gratuito hasta 1.000 artículos."),
    ("¿Mi caja registradora antigua cumple con VeriFactu?",
     "Depende de si el fabricante la ha adaptado. Pídele la declaración responsable. Si no te la da, antes de tu fecha de 2027 tendrás que sustituirla por un sistema adaptado."),
    ("¿Y el cajón portamonedas?",
     "Los cajones se conectan a la impresora de tickets con un cable RJ11. Mándanos por WhatsApp el modelo de tu impresora y de tu cajón y te confirmamos si te valen."),
    ("¿Qué impresora de tickets necesito?",
     "Una térmica de 80 mm, USB o de red. La mayoría de marcas del mercado funcionan. Si ya tienes una, casi seguro que vale."),
    ("¿Es tan rápido como la caja registradora?",
     "Con un lector de códigos de barras, sí. Para los artículos sin código se teclea un código corto, igual que se tecleaba el departamento en la caja de antes."),
    ("¿Qué pasa si se va la luz o internet?",
     "Sin internet sigues cobrando: los datos están en tu ordenador. Sin luz, como con cualquier caja: conviene un pequeño SAI si en tu zona hay cortes."),
    ("¿Sirve para cobrar con una tablet?",
     "No. Carrito5 es un programa de escritorio para Windows. Para tablet o móvil hay otros productos en la comparativa de TPV gratis."),
    ("¿Cuánto cuesta cuando paso de 1.000 artículos?",
     "Se amplía con la licencia comercial, un pago acotado y sin comisión. Y si prefieres el programa en propiedad, Caja 5, de la misma casa, se compra una vez."),
  ],
  satelites=[("Descargar Carrito5 gratis", "descargar-tpv-gratis.html", "Instalador para Windows"),
             ("Mejor TPV gratis 2026", "mejor-tpv-gratis-2026.html", "Todas las opciones comparadas"),
             ("Hardware TPV para calzado", "tpv-zapateria-hardware.html", "Impresoras, lectores y cajones"),
             ("Cómo hacer el arqueo de caja", "blog/como-hacer-arqueo-de-caja-cierre-z.html", "El cierre Z, explicado"),
             ("Factura simplificada y ticket", "factura-simplificada-ticket.html", "Lo que tiene que llevar el ticket"),
             ("VeriFactu gratis", "verifactu-gratis.html", "Opciones sin coste")]),

# ============================================================ entidad
"sobre-carrito5.html": dict(
  title="Quién está detrás de Carrito5 | Ábaco Infoelectrónica, Jaén",
  desc="Carrito5 es el TPV gratuito de Ábaco Infoelectrónica S.L., fabricante español de software de punto de venta desde hace más de 28 años. Sede, modelo y contacto.",
  kw="carrito5, carrito5 tpv, carrito 5 opiniones, quien es carrito5, abaco infoelectronica, carrito5 empresa, carrito5 jaen",
  h1="Quién está detrás de Carrito5",
  sub="Antes de instalar un programa gratuito en la caja de tu tienda tienes derecho a saber quién lo hace, dónde está y por dónde cobra. Aquí está todo.",
  badge="LA EMPRESA",
  crumb="Sobre Carrito5",
  fecha="2026-09-05",
  soft=True,
  trail=[("Inicio", "index.html"), ("Sobre Carrito5", "sobre-carrito5.html")],
  resumen=[
    "Carrito5 es un programa TPV gratuito para Windows desarrollado por Ábaco Infoelectrónica S.L., empresa española con sede en Jaén que fabrica software de punto de venta para el comercio minorista desde hace más de 28 años y que también desarrolla Caja 5, su TPV con licencia en propiedad.",
    "El modelo es público: Carrito5 es gratuito hasta 1.000 artículos en catálogo, se amplía con licencia comercial, y no cobra comisión por venta ni obliga a comprar hardware. Atención por WhatsApp y teléfono en el 611 500 052.",
  ],
  aside=("Habla con una persona",
         "WhatsApp o teléfono al 611 500 052, en horario comercial y desde España. Sin bot y sin cola de tickets."),
  cta=("Ahora que sabes quién somos, pruébalo",
       "Descarga Carrito5, instálalo en el ordenador de tu tienda y comprueba si te encaja. Sin tarjeta."),
  bloques=[
    ("Ficha de la empresa",
     ["Estos son los datos que identifican a Carrito5 y a la empresa que lo desarrolla. Son los mismos que aparecen en abacosoftware.com, la web del producto principal de la casa, porque es la misma empresa.",
      '<div class="c5-tabla-wrap"><table class="c5-tabla"><tbody>'
      '<tr><th>Producto</th><td>Carrito5, software TPV para Windows con plan gratuito</td></tr>'
      '<tr><th>Empresa</th><td>Ábaco Infoelectrónica S.L. (Ábaco Software)</td></tr>'
      '<tr><th>Sede</th><td>Jaén, España</td></tr>'
      '<tr><th>Actividad</th><td>Desarrollo de software de punto de venta y gestión para comercio minorista, desde hace más de 28 años</td></tr>'
      '<tr><th>Otros productos</th><td>Caja 5 (TPV con licencia en propiedad para PC), Caja 5 Nube (multitienda), app de etiquetas QL5</td></tr>'
      '<tr><th>Sistema operativo</th><td>Windows 7, 8, 10 y 11. Sin versión para Mac, Android ni iOS</td></tr>'
      '<tr><th>Plan gratuito</th><td>Plan Inicio: hasta 1.000 artículos en catálogo, sin cuota, sin tarjeta y sin caducidad</td></tr>'
      '<tr><th>VeriFactu</th><td>Adaptado: el ticket sale con el QR y los datos que exige el reglamento</td></tr>'
      '<tr><th>Atención</th><td>WhatsApp y teléfono 611 500 052, horario comercial, desde España</td></tr>'
      '<tr><th>Web del grupo</th><td><a href="https://www.abacosoftware.com/" rel="noopener">abacosoftware.com</a></td></tr>'
      '</tbody></table></div>'],
     None),
    ("De dónde viene Carrito5",
     ["Ábaco Software lleva más de 28 años haciendo programas de caja para tiendas en España. Su producto principal es Caja 5, un TPV que se compra una vez y es del comerciante, con versión para PC y versión en la nube para varias tiendas. Con esa base salió Carrito5: un programa más ligero, pensado para el autónomo y la tienda pequeña que están empezando o que tienen un catálogo contenido, y que no quieren pagar por lo que no van a usar.",
      "Por eso Carrito5 no es un producto de una empresa nueva que aún no sabe cómo va a ganar dinero. Es la puerta de entrada de una casa que ya vive de vender Caja 5. Cuando una tienda con Carrito5 crece por encima de los 1.000 artículos o necesita varias cajas, la salida natural es Caja 5, y ese es el negocio."],
     None),
    ("Por dónde cobra y por dónde no",
     ["Preferimos decirlo en una lista corta antes de que lo busques en la letra pequeña."],
     ["<strong>Cobra</strong> por la licencia comercial cuando el catálogo pasa de 1.000 artículos.",
      "<strong>Cobra</strong> por Caja 5 si la tienda necesita un programa en propiedad o varias cajas.",
      "<strong>No cobra</strong> comisión por venta: el datáfono es el de tu banco.",
      "<strong>No cobra</strong> por hardware: usas tu ordenador y tu impresora.",
      "<strong>No vende</strong> los datos de tu negocio: viven en tu ordenador, no en un servidor ajeno.",
      "<strong>No caduca</strong>: el plan Inicio no es una prueba de 30 días."]),
    ("Cómo se da soporte",
     ["No hay departamento de informática en una tienda pequeña, así que el soporte tiene que ser una persona al otro lado. El canal principal es WhatsApp al 611 500 052, y el teléfono, en horario comercial y con atención en España. Para las dudas de instalación, impresora y primeros pasos es donde más se resuelve, normalmente en la misma conversación.",
      "Lo que no hacemos: visitas presenciales para instalar. No hacen falta. El programa se descarga, se instala en unos minutos y, si algo se atasca, se ve por acceso remoto o se resuelve por WhatsApp."],
     None),
    ("Sobre las opiniones y valoraciones",
     ["Si buscas «Carrito5 opiniones» encontrarás poco, y no queremos rellenarlo con estrellas inventadas. No publicamos valoraciones que no podamos mostrar con nombre y comercio. Lo que sí puedes hacer es probarlo: es gratis, se instala en media hora y una tarde cobrando con tu propio catálogo te dice más que cualquier reseña."],
     None),
  ],
  faqs=[
    ("¿Quién desarrolla Carrito5?",
     "Ábaco Infoelectrónica S.L., conocida como Ábaco Software, empresa española con sede en Jaén que desarrolla software TPV para comercio desde hace más de 28 años. Es la misma empresa que hace Caja 5."),
    ("¿Carrito5 y Caja 5 son lo mismo?",
     "No. Carrito5 es el programa gratuito para tiendas pequeñas, con límite de 1.000 artículos. Caja 5 es el TPV con licencia en propiedad, para comercios que necesitan más catálogo, varias cajas o versión en la nube. Los dos son de la misma casa."),
    ("¿Cómo gana dinero Carrito5 si es gratis?",
     "Con la licencia comercial cuando el catálogo pasa de 1.000 artículos, y con Caja 5 cuando la tienda necesita un producto mayor. No cobra comisión por venta ni por hardware."),
    ("¿Dónde está la empresa?",
     "En Jaén, España. El soporte se hace por WhatsApp, teléfono y acceso remoto para toda España; no hacen falta visitas para instalar."),
    ("¿Es seguro instalar un programa gratuito en la caja de mi tienda?",
     "Carrito5 lo hace una empresa con más de 28 años vendiendo software de caja, con un modelo de negocio público y sin acceso a tus cobros ni a tus datos, que se guardan en tu ordenador."),
    ("¿Hay opiniones de Carrito5?",
     "No publicamos valoraciones que no podamos mostrar con nombre y comercio. La forma de saber si te vale es probarlo: es gratis y se instala en media hora."),
    ("¿Cómo contacto con Carrito5?",
     "Por WhatsApp o teléfono en el 611 500 052, en horario comercial. Te atiende una persona en España."),
    ("¿Qué funciones tiene Carrito5?",
     "Catálogo con códigos de barras, lector y etiquetas; control de stock; matriz de tallas y colores; ficha de clientes con historial, devoluciones y vales; tickets con QR de VeriFactu. Funciona sin internet, en Windows."),
  ],
  satelites=[("Descargar Carrito5 gratis", "descargar-tpv-gratis.html", "Plan Inicio, sin tarjeta"),
             ("Mejor TPV gratis 2026", "mejor-tpv-gratis-2026.html", "Carrito5 comparado con el resto"),
             ("TPV para comercio local", "software-tpv-comercio-local.html", "Para quién está pensado"),
             ("VeriFactu gratis", "verifactu-gratis.html", "Lo que cumple el plan Inicio"),
             ("Caja 5, el TPV en propiedad", "https://www.abacosoftware.com/caja5_pc.asp", "Cuando la tienda crece")]),

}
