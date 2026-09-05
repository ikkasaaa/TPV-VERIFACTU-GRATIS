# -*- coding: utf-8 -*-
"""Blog de carrito5.com: tercera capa, posts de pregunta y respuesta.

Cada post contesta una pregunta completa, tal como la escribe alguien en
Google o se la hace a ChatGPT, con la respuesta corta arriba y el desarrollo
debajo. Son atemporales; la fecha de publicacion los reparte por el
calendario para que el blog no se quede sin novedad entre campañas.

Reparto con abacosoftware.com: se evitan las preguntas que ya contesta ese
dominio (que es un TPV, TPV o datafono, tactil o teclado, como hacer una
devolucion, declaracion responsable). Las de aqui van de coste, hardware
concreto, sin internet, codigos propios, tallas, portatil, limites del plan
gratuito, obligatoriedad, como elegir, mantenimiento y tablet.

Mismas reglas de funciones confirmadas que blog_2026_09.py. Los precios de
hardware son orientativos del mercado español y se dicen como tales.
"""

BLOG_PREGUNTAS_1 = {

# ------------------------------------------------------------------ 17 sep
"cuanto-cuesta-un-tpv-para-una-tienda-pequena": dict(
  title="¿Cuánto Cuesta un TPV para una Tienda Pequeña? Cuentas Reales",
  desc="Un TPV para una tienda pequeña cuesta entre 0 y 600 euros de una vez si aprovechas el ordenador que tienes y usas un programa gratuito, y entre 1.500 y 4.000 a cinco años si pagas cuota. Las cuentas, partida por partida.",
  kw="cuanto cuesta un tpv, precio tpv tienda pequeña, cuanto cuesta un tpv para comercio, precio software tpv, tpv barato tienda, coste tpv completo",
  h1="¿Cuánto cuesta un TPV para una tienda pequeña?",
  sub="Depende de una sola decisión: si pagas el programa cada mes o no. El hardware cuesta lo mismo en los dos casos y casi siempre menos de lo que la gente cree.",
  publicado="2026-09-17",
  para="Quien va a montar o renovar la caja de una tienda",
  resumen=[
    "Un TPV completo para una tienda pequeña en España cuesta entre 0 y 600 euros de una sola vez si se usa un programa gratuito y se aprovecha el ordenador que ya hay: impresora de tickets de 60 a 150 euros, lector de códigos de 20 a 40, cajón portamonedas de 30 a 60, y un PC de segunda mano de 150 a 300 si no se tiene. Con un programa por suscripción, hay que sumar entre 20 y 40 euros al mes, que a cinco años son de 1.200 a 2.400 euros, más la comisión por cobro si el programa la lleva.",
    "El datáfono no forma parte del TPV: es el de tu banco, con la comisión que negocies con él, y no cambia con el programa que uses.",
  ],
  cuerpo=[
    ("Las cinco partidas",
     ['<div class="c5-tabla-wrap"><table class="c5-tabla"><thead><tr><th>Partida</th><th>Coste orientativo</th><th>Se puede evitar si</th></tr></thead><tbody>'
      '<tr><td>Ordenador</td><td>0 a 300 euros (segunda mano o reacondicionado)</td><td>Ya tienes uno con Windows en la tienda o en casa</td></tr>'
      '<tr><td>Programa de caja</td><td>0 euros con plan gratuito; 20 a 40 al mes por suscripción; 300 a 600 en licencia de pago único</td><td>Usas un programa gratuito y tu catálogo cabe en su límite</td></tr>'
      '<tr><td>Impresora de tickets</td><td>60 a 150 euros (térmica de 80 mm)</td><td>Ya tienes una de la caja registradora anterior</td></tr>'
      '<tr><td>Lector de códigos de barras</td><td>20 a 40 euros (USB de mano)</td><td>Tu género no lleva códigos y tecleas referencias</td></tr>'
      '<tr><td>Cajón portamonedas</td><td>30 a 60 euros</td><td>Reutilizas el de la caja anterior si es compatible</td></tr>'
      '<tr><td>Pantalla táctil</td><td>150 a 300 euros</td><td>No hace falta: teclado y ratón funcionan igual</td></tr>'
      '</tbody></table></div>',
      "Sumando el caso más habitual, ordenador ya existente, programa gratuito, impresora y lector nuevos y cajón nuevo, salen entre 110 y 250 euros. El caso caro, todo nuevo y programa por suscripción, ronda los 600 euros de entrada más 30 euros al mes."],
     None),
    ("La cuenta que importa: cinco años",
     ["Una tienda no cambia de programa cada año, así que lo que cuenta es el acumulado. Un TPV con programa gratuito cuesta lo mismo el primer año que el quinto: el hardware inicial y nada más. Un TPV con suscripción de 30 euros al mes cuesta 1.800 euros en cinco años solo de programa, y si el programa lleva comisión por cobro con tarjeta, un 1,5 o 2 por ciento de toda la facturación con tarjeta se suma cada año.",
      "Para una tienda que cobra 80.000 euros al año con tarjeta, esa comisión son entre 1.200 y 1.600 euros anuales. A cinco años, con la cuota, entre 7.800 y 9.800 euros. Frente a 250 de hardware con un programa gratuito y el datáfono del banco de siempre."],
     ["<strong>Programa gratuito</strong>: coste de hardware el primer año, cero después.",
      "<strong>Suscripción</strong>: 1.200 a 2.400 euros a cinco años, solo de programa.",
      "<strong>Comisión por cobro</strong>: la partida que más crece si el programa la lleva."]),
    ("Lo que no hay que comprar",
     ["Pantalla táctil: en una tienda de comercio con lector de códigos, el teclado y el ratón van igual de rápido y cuestan diez veces menos. Impresora de etiquetas dedicada: para empezar, hojas adhesivas en la impresora normal. Ordenador nuevo: uno de segunda mano con Windows 10 y disco SSD por 200 euros cobra durante años. Y el «pack TPV» cerrado con hardware obligatorio de una marca: casi siempre es lo mismo más caro."],
     None),
    ("Dónde está el coste real: el tiempo",
     ["El coste que casi nadie calcula es la tarde de dar de alta el catálogo y los días de acostumbrarse. Es el mismo con cualquier programa, gratuito o de pago, y es la razón para elegir bien la primera vez. Un programa que se prueba gratis con el catálogo real antes de decidir ahorra esa tarde repetida."],
     None),
  ],
  cierre=("La partida de programa, a cero",
          ["Carrito5 es gratuito hasta 1.000 artículos, sin cuota, sin comisión por cobro y sin hardware obligatorio: funciona con el ordenador, la impresora de tickets y el lector que ya tengas o que compres por menos de 200 euros. Se instala en Windows en unos minutos. Descárgalo, da de alta tus artículos y haz la cuenta con tus números."],
          "Descargar Carrito5 gratis", "/descargar-tpv-gratis.html"),
  faqs=[
    ("¿Cuánto cuesta montar un TPV desde cero?",
     "Entre 110 y 250 euros si ya tienes ordenador y usas un programa gratuito: impresora de tickets, lector y cajón. Todo nuevo y con suscripción, unos 600 euros de entrada más 20 a 40 al mes."),
    ("¿Cuánto cuesta el programa de TPV?",
     "De 0 euros con plan gratuito a 20 o 40 al mes por suscripción, o 300 a 600 en licencia de pago único. A cinco años la suscripción son 1.200 a 2.400 euros."),
    ("¿Necesito pantalla táctil?",
     "No. En comercio, con lector de códigos, teclado y ratón van igual de rápido y cuestan mucho menos."),
    ("¿El datáfono forma parte del TPV?",
     "No. El datáfono es el de tu banco, con su comisión, y no cambia con el programa. Cuidado con los programas «gratis» que cobran comisión por cada cobro con tarjeta."),
    ("¿Vale mi ordenador viejo?",
     "Si tiene Windows 7, 8, 10 u 11 y arranca, casi seguro. Un disco SSD de 40 euros lo hace ir más ágil que uno nuevo con disco mecánico."),
  ],
  relacionadas=[("Mejor TPV gratis 2026", "mejor-tpv-gratis-2026.html", "Por dónde cobra cada uno"),
                ("Programa de caja registradora gratis", "programa-caja-registradora-gratis.html", "Tu PC como caja"),
                ("¿Qué impresora de tickets comprar?", "blog/que-impresora-de-tickets-comprar-para-un-tpv.html", "La partida más cara del hardware"),
                ("TPV gratis para autónomos", "tpv-gratis-autonomos.html", "Gasto fijo: cero")]),

# ------------------------------------------------------------------ 1 oct
"que-impresora-de-tickets-comprar-para-un-tpv": dict(
  title="¿Qué Impresora de Tickets Comprar para un TPV? Lo que Importa",
  desc="Para un TPV de tienda, una impresora térmica de 80 mm con conexión USB o de red, corte automático y salida para cajón. Entre 60 y 150 euros. Lo que hay que mirar, lo que no, y por qué el QR de VeriFactu decide la calidad.",
  kw="que impresora de tickets comprar, impresora tickets tpv, impresora termica 80mm tienda, impresora tickets usb tpv, impresora tickets qr verifactu, mejor impresora tickets comercio",
  h1="¿Qué impresora de tickets comprar para un TPV?",
  sub="Casi todas valen y casi todas se parecen. Las diferencias que importan son cuatro, y desde 2027 una de ellas es que imprima un QR que se pueda leer.",
  publicado="2026-10-01",
  para="Quien va a comprar o cambiar la impresora de tickets",
  resumen=[
    "Para una tienda, la impresora de tickets adecuada es térmica, de 80 milímetros de ancho de papel, con conexión USB (o de red si el ordenador está lejos), corte automático y conector RJ11 para abrir el cajón portamonedas. Cuesta entre 60 y 150 euros. Las de 58 milímetros son para móviles y datáfonos; las de impacto ya no tienen sentido en comercio.",
    "Desde 2027 hay un criterio nuevo: el QR de VeriFactu tiene que leerse con un móvil. Eso pide 203 puntos por pulgada como mínimo, cabezal limpio y papel térmico decente. Antes de comprar, pregunta al fabricante de tu programa por los modelos que ha probado.",
  ],
  cuerpo=[
    ("Los cuatro criterios que importan",
     ['<div class="c5-tabla-wrap"><table class="c5-tabla"><thead><tr><th>Criterio</th><th>Qué elegir</th><th>Por qué</th></tr></thead><tbody>'
      '<tr><td>Tecnología</td><td>Térmica directa</td><td>Sin tinta ni cinta; solo papel. Silenciosa y rápida.</td></tr>'
      '<tr><td>Ancho de papel</td><td>80 mm</td><td>El estándar de comercio. 58 mm es para datáfonos y móviles y el ticket sale estrecho y largo.</td></tr>'
      '<tr><td>Conexión</td><td>USB; red (Ethernet) si el PC está lejos; Bluetooth solo para portátil en la calle</td><td>USB es lo más simple y lo que cualquier programa de Windows reconoce.</td></tr>'
      '<tr><td>Cajón</td><td>Conector RJ11 en la parte trasera</td><td>El cajón portamonedas se abre por la impresora, no por el ordenador.</td></tr>'
      '</tbody></table></div>',
      "Corte automático y 203 puntos por pulgada son habituales en cualquier modelo de 80 mm de más de 60 euros. Lo que no hace falta: pantalla, wifi, colores, ni velocidades por encima de 200 mm por segundo, que en una tienda no se notan."],
     None),
    ("El QR de VeriFactu: el criterio nuevo",
     ["Desde el 1 de enero de 2027 para sociedades y el 1 de julio para autónomos, cada ticket lleva un código QR que el cliente puede escanear. Un QR mal impreso, borroso o con líneas blancas, es un ticket que no cumple. Tres cosas lo garantizan: resolución de 203 puntos por pulgada o más, cabezal limpio (se limpia con alcohol isopropílico cada pocas semanas) y papel térmico de calidad, que no es el más barato del paquete de cien.",
      "Antes de comprar, escanea con el móvil el QR de un ticket de prueba de ese modelo. Si no lo has podido probar, pregunta al fabricante del programa qué modelos ha visto imprimir bien el QR."],
     ["<strong>203 ppp</strong> o más.",
      "<strong>Cabezal limpio</strong> cada pocas semanas.",
      "<strong>Papel térmico decente</strong>, no el más barato.",
      "<strong>Prueba con el móvil</strong> antes de dar la impresora por buena."]),
    ("Marcas y precios, sin nombres",
     ["El mercado español de impresoras de tickets tiene tres franjas. De 60 a 90 euros, marcas asiáticas genéricas que funcionan bien con USB y ESC/POS, que es el lenguaje estándar que entienden los programas de caja; duran varios años en una tienda pequeña. De 90 a 150, las marcas clásicas del sector, con mejor mecánica de corte y repuestos fáciles. Por encima de 150, modelos con red, pantalla o formatos especiales que una tienda no necesita.",
      "Para la mayoría de tiendas, la franja media es la compra sensata. La barata vale si el volumen es bajo y se acepta cambiarla antes."],
     None),
    ("Lo que se olvida al comprar",
     ["El rollo de papel: de 80 mm de ancho y, según la impresora, 60 u 80 mm de diámetro; comprar el que no cabe es un clásico. El cable USB, que a veces no viene. La fuente de alimentación externa, que es donde fallan las baratas. Y el cajón: si ya tienes uno, mira que el conector sea RJ11 y pregunta si el voltaje coincide, que suele ser de 24 voltios en las dos."],
     None),
  ],
  cierre=("La impresora que tengas, probablemente vale",
          ["Carrito5 imprime en impresoras térmicas de 80 mm por USB y saca el ticket con su QR de VeriFactu. Si ya tienes una, casi seguro que sirve; si dudas, mándanos el modelo por WhatsApp antes de comprar otra. Y el programa es gratuito hasta 1.000 artículos, para Windows, así que la impresora es la única partida del hardware que de verdad tienes que decidir."],
          "Descargar Carrito5 gratis", "/descargar-tpv-gratis.html"),
  faqs=[
    ("¿Qué impresora de tickets necesito para una tienda?",
     "Térmica, de 80 mm, USB, con corte automático y conector RJ11 para el cajón. Entre 60 y 150 euros."),
    ("¿58 mm u 80 mm?",
     "80 mm para comercio. 58 mm es para datáfonos e impresoras de bolsillo; el ticket sale estrecho y el QR más pequeño."),
    ("¿Cómo sé si imprime bien el QR de VeriFactu?",
     "Escanea con el móvil el QR de un ticket de prueba: tiene que abrir la comprobación de la Agencia Tributaria. Resolución de 203 ppp, cabezal limpio y papel decente."),
    ("¿El cajón se conecta al ordenador o a la impresora?",
     "A la impresora, con un cable RJ11. La impresora manda el pulso que abre el cajón cuando imprime el ticket."),
    ("¿Vale la impresora de mi caja registradora antigua?",
     "Si es térmica de 80 mm con USB o red, probablemente. Si es de impacto o solo tiene puerto serie, mejor cambiarla. Consulta el modelo con el fabricante de tu programa."),
  ],
  relacionadas=[("¿Cuánto cuesta un TPV?", "blog/cuanto-cuesta-un-tpv-para-una-tienda-pequena.html", "Todas las partidas"),
                ("¿Qué lector de códigos de barras necesito?", "blog/que-lector-de-codigos-de-barras-necesito-para-mi-tienda.html", "La otra pieza del hardware"),
                ("Hardware TPV para calzado", "tpv-zapateria-hardware.html", "Un ejemplo de equipamiento"),
                ("VeriFactu: lo que cambia en la caja", "blog/verifactu-1-enero-2027-que-cambia-en-la-caja.html", "El QR en el ticket")]),

# ------------------------------------------------------------------ 15 oct
"se-puede-cobrar-sin-internet-con-un-tpv": dict(
  title="¿Se Puede Cobrar sin Internet con un TPV? Sí, si el Programa es Local",
  desc="Un TPV cobra sin internet si el programa y los datos están en el propio ordenador; si el programa vive en la nube, se para. El datáfono es aparte y depende del banco. Cómo saber cuál tienes y qué hacer el día que se cae la línea.",
  kw="cobrar sin internet tpv, tpv sin conexion, tpv offline tienda, tpv funciona sin internet, se cae internet tienda cobrar, tpv local o nube",
  h1="¿Se puede cobrar sin internet con un TPV?",
  sub="Sí, con un programa que guarde los datos en tu ordenador. No, con uno que viva en el navegador. La diferencia se nota un sábado a las doce con la línea caída y la tienda llena.",
  publicado="2026-10-15",
  para="Quien ha sufrido un corte de línea con la tienda llena",
  resumen=[
    "Un TPV puede cobrar sin internet si el programa está instalado en el ordenador de la tienda y guarda ahí los datos: catálogo, stock, clientes y ventas. Cobra, imprime el ticket con su QR, descuenta el stock y sigue igual cuando vuelve la conexión. Un TPV en la nube, que funciona en el navegador, se para o queda en un modo limitado en cuanto se cae la línea.",
    "El datáfono es otra historia: el de tu banco necesita línea, fija o móvil, y falla independientemente del programa. Con VeriFactu, un programa local sigue cumpliendo sin conexión: los registros se generan en el ordenador y se remiten cuando hay línea.",
  ],
  cuerpo=[
    ("Dos tipos de programa, dos comportamientos",
     ["Un programa de escritorio se instala en el ordenador y trabaja con los datos que están en ese ordenador. Internet le sirve para actualizarse y, con VeriFactu, para remitir los registros, pero no para cobrar. Si la línea se cae, no se entera.",
      "Un programa en la nube se abre en el navegador y los datos están en un servidor de la empresa que lo vende. Sin internet, el navegador no llega al servidor y no hay caja. Algunos tienen un modo sin conexión que guarda unas pocas ventas y las sincroniza después; suele ser limitado y conviene probarlo antes de fiarse."],
     ["<strong>Escritorio</strong>: los datos en tu ordenador; cobra sin línea.",
      "<strong>Nube</strong>: los datos en un servidor ajeno; sin línea, se para o queda limitado.",
      "<strong>Híbrido</strong>: pregunta cuántas ventas guarda sin conexión y qué pasa si se apaga el equipo."]),
    ("Dónde se cae internet más de lo que parece",
     ["No es un problema de pueblos. Se cae en el centro de Madrid y de Barcelona en locales de planta baja con muros gruesos, en sótanos comerciales, en calles con procesión o fiesta donde cien mil móviles saturan las antenas, en el paseo marítimo en agosto, y en cualquier tienda cuyo router lleve tres años sin reiniciarse. Y siempre pasa en el momento de más venta, porque es cuando más gente hay usando la red.",
      "Una tienda que dependa de la línea para cobrar tiene que preguntarse cuántas horas al año no la tiene, y qué facturan esas horas."],
     None),
    ("VeriFactu sin conexión",
     ["Es la duda nueva: si VeriFactu remite registros a Hacienda, ¿hace falta internet para cobrar? No. El programa genera el registro de cada venta en el ordenador, con su huella y su QR, y lo remite cuando hay conexión. Sin línea, se sigue cobrando y los registros se encadenan igual; al volver la línea, se envían. Lo que exige la norma es que el sistema los genere y conserve, y eso un programa local lo hace sin red. Información general; el detalle, con tu asesor."],
     None),
    ("El datáfono: el que sí se para",
     ["El datáfono del banco necesita línea, fija o móvil, y cuando se cae, se cae. Un programa local no lo arregla, pero permite seguir cobrando en efectivo con el ticket correcto, y apuntar la venta con tarjeta pendiente si el cliente vuelve. Muchas tiendas tienen un segundo datáfono con tarjeta SIM de otro operador para esos ratos, y un cartel de «solo efectivo» para la media hora que dure."],
     None),
    ("Cómo saber cuál tienes",
     ["Apaga el router y haz una venta. Si el programa cobra, imprime y descuenta el stock, es local. Si aparece un aviso de sin conexión, un modo limitado o una pantalla en blanco, es de nube. Es una prueba de un minuto que conviene hacer antes de que la haga un sábado el proveedor de internet."],
     None),
  ],
  cierre=("Los datos en tu ordenador, la caja siempre abierta",
          ["Carrito5 es un programa de escritorio para Windows: el catálogo, el stock, los clientes y las ventas están en tu ordenador, y cobra e imprime el ticket con su QR de VeriFactu aunque no haya internet. Es gratuito hasta 1.000 artículos. Descárgalo, apaga el router y haz una venta de prueba."],
          "Descargar Carrito5 gratis", "/descargar-tpv-gratis.html"),
  faqs=[
    ("¿Un TPV funciona sin internet?",
     "Si es un programa instalado en el ordenador con los datos en local, sí: cobra, imprime y descuenta stock sin línea. Si es un programa en el navegador, no, o solo en un modo limitado."),
    ("¿Y VeriFactu sin conexión?",
     "El programa genera los registros y el QR en el ordenador y los remite cuando hay línea. Cobrar no necesita conexión. Confírmalo con tu asesor para tu caso."),
    ("¿El datáfono cobra sin internet?",
     "No. Depende de la línea fija o móvil del banco. Un segundo datáfono con SIM de otro operador y un cartel de «solo efectivo» resuelven la media hora."),
    ("¿Cómo sé si mi programa es local o de nube?",
     "Apaga el router y haz una venta. Si cobra e imprime, es local. Si avisa de sin conexión o se queda en blanco, es de nube."),
    ("¿Dónde se cae internet en una tienda?",
     "En locales con muros gruesos, sótanos, calles con fiesta o procesión, paseos marítimos en verano y routers viejos. Siempre en el momento de más venta."),
  ],
  relacionadas=[("VeriFactu sin conexión", "verifactu-sin-conexion-internet-offline.html", "La página de referencia"),
                ("Semana Santa en zona turística", "blog/semana-santa-2027-comercio-zonas-turisticas.html", "Cuando la calle se llena"),
                ("TPV en Madrid", "tpv-madrid.html", "Sótanos de Gran Vía"),
                ("Verano en la tienda de costa", "blog/verano-2027-tienda-de-costa-preparar-temporada.html", "El paseo marítimo en agosto")]),

# ------------------------------------------------------------------ 29 oct
"que-lector-de-codigos-de-barras-necesito-para-mi-tienda": dict(
  title="¿Qué Lector de Códigos de Barras Necesito para mi Tienda?",
  desc="Para una tienda, un lector USB de mano que funcione como teclado, de 20 a 40 euros, lee cualquier código de barras de producto. Solo hace falta uno 2D, algo más caro, si vas a leer códigos QR o etiquetas muy pequeñas. Cómo elegirlo y conectarlo.",
  kw="que lector de codigos de barras comprar, lector codigo barras tienda, lector codigos usb tpv, lector 1d o 2d tienda, lector codigo barras precio, escaner codigo barras comercio",
  h1="¿Qué lector de códigos de barras necesito para mi tienda?",
  sub="Uno USB, de mano, de los de 30 euros. Se enchufa, funciona como un teclado y lee cualquier código de producto. El resto de opciones son para casos concretos.",
  publicado="2026-10-29",
  para="Quien va a poner lector por primera vez o cambiarlo",
  resumen=[
    "El lector de códigos de barras adecuado para una tienda es uno USB de mano que funciona en modo teclado: se conecta, no necesita instalar nada, y cuando lee un código escribe el número donde esté el cursor, como si lo tecleara alguien. Cuesta entre 20 y 40 euros y lee todos los códigos de barras de producto (EAN-13, EAN-8, Code 128) y los que imprime tu programa.",
    "Un lector 2D, de 40 a 90 euros, lee además códigos QR y códigos muy pequeños o arrugados, y lee desde pantallas de móvil. Solo hace falta si vas a escanear QR o si tu género tiene etiquetas diminutas, como en joyería. Los lectores de mostrador fijos y los inalámbricos son para alimentación con mucho volumen y para almacenes.",
  ],
  cuerpo=[
    ("Cómo funciona y por qué no hay que instalar nada",
     ["Un lector USB en modo teclado (HID, en la jerga) es, para el ordenador, un teclado más. Cuando lee un código, escribe los dígitos y pulsa Intro. El programa de caja recibe esa entrada como si la hubiera tecleado el cajero, busca el artículo y lo añade al ticket. No hay controlador ni configuración: se enchufa y lee.",
      "Es también la razón por la que vale para cualquier programa de Windows, gratuito o de pago, y por la que si mañana cambias de programa, el lector sigue sirviendo."],
     None),
    ("1D o 2D: la única decisión",
     ['<div class="c5-tabla-wrap"><table class="c5-tabla"><thead><tr><th></th><th>Lector 1D (láser o CCD)</th><th>Lector 2D (imagen)</th></tr></thead><tbody>'
      '<tr><td>Lee</td><td>Códigos de barras lineales: EAN, Code 128, los de tus etiquetas</td><td>Lo mismo, más QR, Data Matrix y códigos desde pantallas de móvil</td></tr>'
      '<tr><td>Precio</td><td>20 a 40 euros</td><td>40 a 90 euros</td></tr>'
      '<tr><td>Códigos pequeños o arrugados</td><td>Regular</td><td>Mejor</td></tr>'
      '<tr><td>Para quién</td><td>La mayoría de tiendas</td><td>Joyería, cosmética con etiquetas diminutas, quien lea QR o cupones en el móvil</td></tr>'
      '</tbody></table></div>',
      "Si dudas, el 2D de 50 euros vale para todo y la diferencia de precio se olvida en una semana. Pero el 1D de 25 es suficiente en una tienda de ropa, de regalo o de papelería."],
     None),
    ("Con cable, inalámbrico o de mostrador",
     ["Con cable USB: el normal, para un mostrador donde el lector está junto a la caja. Inalámbrico (base USB o Bluetooth): para leer en el almacén, en la mesa de la calle de Sant Jordi o en una tienda grande; cuesta el doble y hay que cargarlo. De mostrador fijo, el de los supermercados: para alimentación con cientos de tickets al día donde el cajero pasa el producto por delante; en una tienda de comercio no compensa.",
      "Y el lector del móvil con una aplicación: sirve para inventarios ocasionales, no para cobrar en caja, porque es lento y hay que desbloquear el teléfono cada vez."],
     ["<strong>Cable USB</strong>: el habitual, 20 a 40 euros.",
      "<strong>Inalámbrico</strong>: almacén y calle, el doble de precio.",
      "<strong>Mostrador fijo</strong>: solo alimentación de mucho volumen."]),
    ("Lo que lee y lo que no",
     ["Un lector lee cualquier código de barras impreso con contraste: los EAN de los productos de marca, los códigos que imprime tu programa en etiquetas propias, los ISBN de los libros. No lee códigos borrosos, tapados por plástico brillante con reflejo, o impresos en rojo sobre blanco, que para el láser es invisible. Si tus etiquetas propias no se leen, casi siempre es la impresión: más contraste, más tamaño, papel mate."],
     None),
  ],
  cierre=("Un lector de 30 euros y un programa gratuito",
          ["Carrito5 lee con cualquier lector USB en modo teclado, da de alta los artículos pasando su código de barras, asigna código propio a los que no lo traen e imprime sus etiquetas para leerlas igual. Es gratuito hasta 1.000 artículos, para Windows. Compra el lector, descarga el programa y esta tarde cobras pasando códigos."],
          "Descargar Carrito5 gratis", "/descargar-tpv-gratis.html"),
  faqs=[
    ("¿Qué lector de códigos de barras comprar para una tienda?",
     "Uno USB de mano en modo teclado, de 20 a 40 euros. Se enchufa y lee cualquier código de producto sin instalar nada."),
    ("¿Necesito un lector 2D?",
     "Solo si vas a leer códigos QR, códigos desde la pantalla de un móvil o etiquetas muy pequeñas como en joyería. Cuesta de 40 a 90 euros."),
    ("¿Hay que instalar algo para que funcione?",
     "No. En modo teclado, el ordenador lo ve como un teclado y el programa de caja recibe el código como si se hubiera tecleado."),
    ("¿Sirve para leer las etiquetas que imprime mi programa?",
     "Sí, si están impresas con contraste y tamaño suficiente, en papel mate. Si no se leen, el problema suele ser la impresión."),
    ("¿Lector con cable o inalámbrico?",
     "Con cable para el mostrador. Inalámbrico solo si lees en el almacén o fuera de la tienda; cuesta el doble y hay que cargarlo."),
  ],
  relacionadas=[("Etiquetar antes de la campaña", "blog/etiquetar-genero-antes-de-campana.html", "Códigos y etiquetas en la práctica"),
                ("¿Cómo pongo código de barras a mis productos?", "blog/como-poner-codigo-de-barras-a-mis-productos.html", "Códigos propios sin GS1"),
                ("¿Qué impresora de tickets comprar?", "blog/que-impresora-de-tickets-comprar-para-un-tpv.html", "La otra pieza"),
                ("¿Cuánto cuesta un TPV?", "blog/cuanto-cuesta-un-tpv-para-una-tienda-pequena.html", "Todas las partidas")]),

# ------------------------------------------------------------------ 12 nov
"como-poner-codigo-de-barras-a-mis-productos": dict(
  title="¿Cómo Poner Código de Barras a mis Productos si No lo Traen?",
  desc="Para vender en tu propia tienda no necesitas comprar códigos EAN: el programa de caja asigna un código interno a cada artículo y lo imprime en una etiqueta que el lector lee igual. Solo hace falta un EAN oficial si vas a vender a otras tiendas o en marketplaces.",
  kw="como poner codigo de barras a mis productos, crear codigo de barras propio tienda, codigo de barras interno tpv, necesito ean para vender en mi tienda, generar codigos de barras productos sin codigo, etiquetas codigo barras tienda",
  h1="¿Cómo pongo código de barras a productos que no lo traen?",
  sub="Con un código interno que asigna el programa y una etiqueta impresa. No hace falta comprar códigos EAN ni darse de alta en ningún sitio, salvo que vayas a vender fuera de tu tienda.",
  publicado="2026-11-12",
  para="Tiendas con género sin código: artesanía, granel, proveedor pequeño, producto propio",
  resumen=[
    "Para cobrar en tu propia tienda con lector, cada artículo necesita un código de barras que el programa reconozca, y ese código puede ser interno: el programa lo asigna al dar de alta el artículo y lo imprime en una etiqueta adhesiva. El lector lo lee exactamente igual que un EAN de fábrica. No hay que comprar nada ni registrarse en ningún organismo.",
    "El código EAN oficial, que se obtiene a través de la organización GS1 y tiene un coste anual, solo hace falta si vas a vender tus productos a otros comercios, a distribuidores o en marketplaces que lo exijan. Para vender en tu mostrador, el código interno es suficiente y es lo que usan la mayoría de tiendas pequeñas.",
  ],
  cuerpo=[
    ("Dos tipos de código, dos usos",
     ['<div class="c5-tabla-wrap"><table class="c5-tabla"><thead><tr><th></th><th>Código interno</th><th>EAN oficial (GS1)</th></tr></thead><tbody>'
      '<tr><td>Quién lo asigna</td><td>Tu programa de caja, al dar de alta el artículo</td><td>GS1 España, con una cuota anual según facturación</td></tr>'
      '<tr><td>Dónde vale</td><td>En tu tienda</td><td>En cualquier comercio del mundo</td></tr>'
      '<tr><td>Coste</td><td>Cero</td><td>Cuota anual más el alta</td></tr>'
      '<tr><td>Para quién</td><td>Quien vende en su mostrador producto propio, artesanía, granel o de proveedor pequeño</td><td>Quien fabrica y vende a otras tiendas, distribuidores o marketplaces</td></tr>'
      '</tbody></table></div>',
      "Una tienda puede usar los dos a la vez: EAN de fábrica para el género de marca, leído con el lector al darlo de alta, y código interno para todo lo demás."],
     None),
    ("Cómo se hace, en cinco pasos",
     ['<ol class="c5-pasos">'
      '<li><strong>Da de alta el artículo</strong> en el programa con su nombre y su precio. Si trae código de fábrica, pásalo por el lector y queda como su código. Si no lo trae, el programa le asigna uno interno.</li>'
      '<li><strong>En moda</strong>, da de alta el modelo con su matriz de tallas y colores: cada variante recibe su código.</li>'
      '<li><strong>Imprime la etiqueta</strong>, sola o en lote, en hojas adhesivas con la impresora normal o en una impresora de etiquetas.</li>'
      '<li><strong>Pégala</strong> en el producto, en la percha, en el pincho de la maceta o en el estante si el producto es a granel.</li>'
      '<li><strong>Cobra pasando el lector</strong>. El programa reconoce el código interno igual que un EAN.</li>'
      '</ol>'],
     None),
    ("Dónde poner la etiqueta según lo que vendas",
     ["En ropa, en la etiqueta colgante de la prenda o en la percha. En joyería, en la etiqueta de joya, con un código corto. En artesanía y regalo, en la base del objeto o en su caja. En granel y a peso, en el estante o en un tablón junto a la caja con los códigos de lo más vendido, que el cajero pasa con el lector sin tocar el producto. En plantas, en el pincho. En libros no hace falta: el ISBN ya es el código.",
      "La regla: la etiqueta tiene que estar donde el cajero la vea sin buscar, con contraste y tamaño suficiente para que el lector la lea a la primera."],
     ["<strong>Ropa</strong>: etiqueta colgante o percha.",
      "<strong>Joyería</strong>: etiqueta de joya, código corto.",
      "<strong>Granel</strong>: tablón de códigos junto a la caja.",
      "<strong>Plantas</strong>: en el pincho."]),
    ("Cuándo sí hace falta el EAN oficial",
     ["Si fabricas velas, cosmética, alimentación o cualquier producto y quieres que lo vendan otras tiendas, ellas necesitan un código que no choque con los suyos ni con los de nadie: ese es el EAN de GS1, único en el mundo. Lo mismo si vas a vender en marketplaces que lo exigen. En ese caso el EAN se imprime en el envase y tu tienda lo lee como cualquier otro. Para el resto, código interno y a vender."],
     None),
  ],
  cierre=("Código interno, etiqueta impresa, lector",
          ["Carrito5 asigna un código interno a cada artículo que no trae código de barras, da de alta cada modelo con sus tallas y colores con un código por variante, imprime las etiquetas y las lee con cualquier lector USB. Es gratuito hasta 1.000 artículos, para Windows. Descárgalo, da de alta diez artículos sin código e imprime sus etiquetas esta tarde."],
          "Descargar Carrito5 gratis", "/descargar-tpv-gratis.html"),
  faqs=[
    ("¿Necesito comprar códigos EAN para vender en mi tienda?",
     "No. Para vender en tu mostrador basta un código interno que asigna el programa de caja y se imprime en una etiqueta. El EAN oficial solo hace falta para vender a otros comercios o en marketplaces."),
    ("¿Cómo genero un código de barras para un producto?",
     "Dando de alta el artículo en el programa: si no trae código, se le asigna uno interno. Después se imprime la etiqueta y se pega."),
    ("¿El lector lee un código interno igual que uno de fábrica?",
     "Sí. Es un código de barras normal; el programa sabe que corresponde a ese artículo."),
    ("¿Con qué imprimo las etiquetas?",
     "Con hojas adhesivas en la impresora normal para empezar, o con una impresora de etiquetas si etiquetas cientos al mes."),
    ("¿Y la ropa con tallas y colores?",
     "El modelo se da de alta con su matriz de tallas y colores y cada variante recibe su código. La etiqueta de la prenda lleva el de su talla y color."),
  ],
  relacionadas=[("¿Qué lector de códigos de barras necesito?", "blog/que-lector-de-codigos-de-barras-necesito-para-mi-tienda.html", "El que los lee"),
                ("Etiquetar antes de la campaña", "blog/etiquetar-genero-antes-de-campana.html", "La tarde de etiquetado"),
                ("Matriz de tallas y colores", "tallas-y-colores.html", "Un código por variante"),
                ("TPV para tiendas de artesanía", "tpv-tienda-artesania.html", "Piezas únicas sin código")]),

# ------------------------------------------------------------------ 10 dic
"sirve-un-tpv-gratis-para-una-tienda-de-ropa": dict(
  title="¿Sirve un TPV Gratis para una Tienda de Ropa? Depende de Tres Cosas",
  desc="Un TPV gratuito sirve para una tienda de ropa si lleva matriz de tallas y colores, si su límite de artículos cabe con las variantes contadas, y si hace devoluciones y vales sobre el ticket. Cómo comprobar las tres antes de instalar nada.",
  kw="tpv gratis tienda de ropa, tpv gratuito moda tallas, software gratis tienda ropa, programa tpv ropa gratis sirve, tpv gratis boutique, tpv ropa sin cuota",
  h1="¿Sirve un TPV gratis para una tienda de ropa?",
  sub="Muchos TPV gratuitos son para bares o para cualquier cosa, y en una tienda de ropa se rompen en la primera camiseta con seis tallas. Tres comprobaciones lo dicen en diez minutos.",
  publicado="2026-12-10",
  para="Tiendas de ropa, boutiques, calzado y complementos",
  resumen=[
    "Un TPV gratis sirve para una tienda de ropa si cumple tres cosas: tiene matriz de tallas y colores, para dar de alta un modelo con todas sus variantes de una vez y ver el stock por talla; su límite de artículos, si lo tiene, cabe con las variantes contadas, no solo con los modelos; y hace devoluciones y cambios sobre el ticket original con vale de devolución, que en moda son diarios.",
    "Si falla la primera, no vale para ropa por muy gratis que sea. Carrito5 cumple las tres: matriz de tallas y colores, ficha de cliente con devoluciones y vales, y plan gratuito hasta 1.000 artículos, para Windows.",
  ],
  cuerpo=[
    ("Comprobación uno: la matriz de tallas y colores",
     ["Es la que separa un TPV de moda de un TPV cualquiera. Sin matriz, una camiseta en seis tallas y cuatro colores son veinticuatro artículos que hay que crear uno a uno, y una colección de doscientos modelos son miles. Con matriz, el modelo se da de alta una vez, se marcan tallas y colores, y el programa crea las variantes con su stock por separado. Al vender, se elige talla y color o se pasa la etiqueta, y se descuenta la variante exacta.",
      "Cómo comprobarlo: da de alta una camiseta con cinco tallas y tres colores. Si tardas más de dos minutos o tienes que crear quince artículos, ese programa no es para ropa."],
     None),
    ("Comprobación dos: el límite, contado por variantes",
     ["Los TPV gratuitos suelen tener un límite: de artículos, de tickets, de tiempo o de funciones. En ropa el límite de artículos hay que leerlo con cuidado, porque cada variante de talla y color suele contar como un artículo. Doscientos modelos con seis tallas y dos colores son 2.400 variantes. Antes de instalar, pregunta al fabricante cómo cuenta las variantes en su límite y haz la cuenta con tu colección.",
      "Y desconfía del límite de tiempo: una prueba de 30 días en ropa se acaba antes de haber entrado la segunda temporada."],
     ["<strong>Límite de artículos</strong>: pregunta si cuenta variantes o modelos.",
      "<strong>Límite de tickets</strong>: en rebajas se pasa en una semana.",
      "<strong>Límite de tiempo</strong>: no sirve para una tienda que va a durar.",
      "<strong>Funciones capadas</strong>: si las devoluciones o las etiquetas son de pago, es de pago."]),
    ("Comprobación tres: devoluciones, cambios y vales",
     ["En una tienda de ropa se cambia a diario: la talla, el color, el regalo. El programa tiene que localizar la venta original por ticket o por la ficha de la clienta, devolver la prenda a su talla en el stock y emitir un vale de devolución que quede registrado. Si el cambio se hace «a mano» porque el programa gratuito no lo lleva, el stock deja de ser real la primera semana."],
     None),
    ("Lo que además conviene, y lo que no hace falta",
     ["Conviene: etiquetas con código de barras por variante, para cobrar pasando el lector; ficha de clienta con historial, para saber su talla al año siguiente; y que funcione sin internet, porque las boutiques de centro pierden la línea. No hace falta: pantalla táctil, integración con marketplaces, comandas ni módulos de hostelería. Un TPV «para todo» suele ser un TPV para bares con las tallas puestas encima."],
     None),
  ],
  cierre=("Las tres comprobaciones, en diez minutos con tu colección",
          ["Carrito5 tiene matriz de tallas y colores, hace devoluciones y cambios sobre el ticket original con vale registrado en la ficha de la clienta, imprime etiquetas por variante y funciona sin internet. El plan Inicio es gratuito hasta 1.000 artículos; pregúntanos por WhatsApp cómo cuentan las variantes para tu colección antes de instalar. Descárgalo y da de alta una camiseta con sus tallas."],
          "Descargar Carrito5 gratis", "/descargar-tpv-gratis.html"),
  faqs=[
    ("¿Qué tiene que tener un TPV para una tienda de ropa?",
     "Matriz de tallas y colores, devoluciones y cambios sobre el ticket con vale, etiquetas por variante y ficha de clienta. Lo demás es secundario."),
    ("¿Los TPV gratis llevan tallas y colores?",
     "Algunos sí y muchos no, porque están pensados para bares o para cualquier tienda. Compruébalo dando de alta una camiseta con cinco tallas y tres colores."),
    ("¿Cómo cuenta el límite de artículos con las variantes?",
     "Depende del programa. Pregunta al fabricante si cuenta modelos o variantes y haz la cuenta con tu colección antes de instalar."),
    ("¿Y las devoluciones?",
     "Tienen que hacerse sobre el ticket original, con la prenda de vuelta a su talla en el stock y el vale registrado. Si se hacen a mano, el stock deja de ser real."),
    ("¿Carrito5 sirve para ropa?",
     "Sí: matriz de tallas y colores, ficha de clienta con devoluciones y vales, etiquetas por variante, sin internet. Plan gratuito hasta 1.000 artículos."),
  ],
  relacionadas=[("TPV para tiendas de ropa", "tpv-tienda-ropa.html", "El sector"),
                ("Matriz de tallas y colores", "tallas-y-colores.html", "Cómo funciona"),
                ("TPV para boutiques", "tpv-boutique.html", "Pocas prendas, cada una importa"),
                ("Mejor TPV gratis 2026", "mejor-tpv-gratis-2026.html", "Por dónde cobra cada uno")]),

}
