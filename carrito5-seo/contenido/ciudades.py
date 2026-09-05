# -*- coding: utf-8 -*-
"""Paginas de ciudad de carrito5.com.

Patron de URL decidido: tpv-<ciudad>.html es la pagina de ciudad. Las URLs
software-tpv-<ciudad>-<barrios>.html que coexisten con una tpv-<ciudad>.html
(Zaragoza y Malaga) se redirigen a la generica; las que son la unica pagina de
su ciudad (Barcelona, Valencia, Bilbao, Sevilla, Sabadell) se quedan.

Madrid es la primera porque es la plaza mas grande del pais y la unica de las
once que anuncia el menu que no tiene pagina (INFORME_CARRITO5.md, punto 7).

Los barrios son secciones dentro de la pagina, no URLs: una pagina por barrio
que no pueda decir nada especifico de ese barrio seria contenido duplicado.

Lo que se afirma del comercio madrileno es de conocimiento general y
comprobable (libertad de horarios en la Comunidad de Madrid desde 2012, ejes
comerciales, ZBE Madrid 360). No se afirma nada sobre distribuidores locales
ni visitas presenciales porque no esta verificado que existan.
"""

CIUDADES = {

"tpv-madrid.html": dict(
  title="Software TPV Gratis para Comercio en Madrid | Carrito5",
  desc="TPV gratuito para tiendas de Madrid: de Salamanca a Vallecas, de Sol a Alcalá de Henares. Se instala en tu PC, funciona sin internet y ya cumple VeriFactu.",
  kw="tpv madrid, software tpv madrid, programa tpv madrid gratis, tpv comercio madrid, tpv tienda madrid, caja registradora madrid software",
  h1="Software TPV gratis para el comercio de Madrid",
  sub="Madrid tiene más tiendas de calle que ninguna otra ciudad de España y horarios que no se parecen a los de ninguna otra. El programa de caja tiene que aguantar los dos.",
  badge="MADRID · COMUNIDAD DE MADRID",
  crumb="TPV en Madrid",
  fecha="2026-09-05",
  trail=[("Inicio", "index.html"), ("TPV en Madrid", "tpv-madrid.html")],
  resumen=[
    "Carrito5 es un programa TPV gratuito para Windows que puedes instalar hoy en cualquier tienda de Madrid, sin tarjeta y sin cuota. El plan Inicio cubre hasta 1.000 artículos, emite tickets con el QR de VeriFactu y sigue cobrando aunque se caiga la conexión.",
    "El soporte se hace por WhatsApp y teléfono desde España, al 611 500 052. Si tu tienda está en Salamanca, Malasaña, Chamberí, Sol, Retiro, Getafe, Leganés o Alcalá de Henares, el programa es el mismo; lo que cambia es cómo lo configuras, y de eso va esta página.",
  ],
  aside=("Tu tienda de Madrid, esta tarde",
         "Descarga, instala en el ordenador del mostrador y saca un ticket de prueba. Si te atascas, te ayudamos por WhatsApp sin cita."),
  cta=("Cobra hoy mismo en tu tienda de Madrid",
       "Instalación directa, sin tarjeta y sin fecha de caducidad. Da de alta lo que más vendes y empieza."),
  bloques=[
    ("Lo que hace distinto vender en Madrid",
     ["La Comunidad de Madrid tiene libertad total de horarios comerciales desde 2012. Eso significa que en Madrid una tienda puede abrir los domingos y festivos que quiera, y muchas lo hacen, sobre todo en el centro y en los ejes turísticos. Un programa de caja que cierre el día a una hora fija o que dependa de que alguien esté en la oficina el domingo por la mañana no sirve aquí.",
      "La segunda diferencia es el volumen de gente de paso. En Sol, Gran Vía, Preciados o Fuencarral una parte de los clientes no va a volver nunca: turistas y madrileños de otro distrito. El ticket tiene que salir rápido y bien, porque no hay segunda oportunidad para arreglarlo. En cambio, en Chamberí, en Prosperidad o en un barrio de Getafe la mayoría de la clientela es de proximidad, y ahí lo que vale es la ficha de cliente: la señora que viene cada semana y el vale de devolución de hace un mes.",
      "Y la tercera es el alquiler. Un local en el barrio de Salamanca o en el centro cuesta lo que cuesta, y eso empuja a locales pequeños con mucha rotación de referencias. El catálogo se llena rápido y hay que saber en cada momento qué se ha vendido y qué no."],
     None),
    ("Qué tienda de Madrid encaja con el plan gratuito",
     ["El plan Inicio de Carrito5 es gratuito de forma indefinida hasta 1.000 artículos en catálogo. Con eso cubre una boutique de Malasaña, una tienda de regalos de Chueca, una papelería de barrio en Carabanchel, una zapatería en Alcalá de Henares o una tienda de complementos en Leganés sin pagar nada.",
      "Donde se queda corto es en el comercio con miles de referencias o con varias cajas cobrando a la vez. En esos casos la salida es la licencia comercial o Caja 5, el producto en propiedad de la misma casa. Preferimos decírtelo antes de que te lo instales que después."],
     ["<strong>Encaja:</strong> moda, calzado, regalo, papelería, juguetería, joyería, herboristería, decoración, mascotas, floristería, óptica.",
      "<strong>No encaja:</strong> hostelería con mesas y comandas, comercio con varias cajas simultáneas, tienda que necesite tablet Android o Mac."]),
    ("Por distritos y zonas: lo que suele pedir cada una",
     ["No hay una tienda de Madrid: hay muchas Madrid, y lo que se pide al programa cambia de una a otra. Esto es lo que más se repite cuando nos escriben desde cada zona.",
      '<div class="c5-tabla-wrap"><table class="c5-tabla"><thead><tr><th>Zona</th><th>Tipo de comercio habitual</th><th>Lo que más se usa del programa</th></tr></thead><tbody>'
      '<tr><td>Salamanca (Serrano, Goya, Velázquez)</td><td>Moda, calzado, joyería, decoración</td><td>Matriz de tallas y colores, ficha de clienta, vales de devolución</td></tr>'
      '<tr><td>Malasaña y Chueca (Fuencarral, Hortaleza)</td><td>Boutiques, vinilos, regalo, cosmética</td><td>Alta rápida de referencias, etiquetas con código de barras</td></tr>'
      '<tr><td>Sol, Gran Vía, Preciados</td><td>Souvenirs, complementos, tiendas de paso</td><td>Cobro rápido con lector, ticket con QR</td></tr>'
      '<tr><td>Chamberí, Retiro, Prosperidad</td><td>Comercio de proximidad: papelería, herboristería, mercería</td><td>Ficha de cliente, devoluciones, stock</td></tr>'
      '<tr><td>Vallecas, Carabanchel, Usera</td><td>Bazar, textil, telefonía, alimentación</td><td>Muchas referencias de bajo importe, códigos de barras, lectura rápida</td></tr>'
      '<tr><td>Getafe, Leganés, Alcalá de Henares, Móstoles</td><td>Comercio de barrio de todo tipo</td><td>Instalación en el PC que ya tienen, funcionamiento sin internet, soporte por WhatsApp</td></tr>'
      '</tbody></table></div>',
      "Si tu tienda está en un barrio que no aparece, el consejo es el mismo: mira el tipo de comercio que más se parece al tuyo, y en la página de tu sector tienes la configuración detallada."],
     None),
    ("Internet en el centro de Madrid: no te fíes",
     ["Parece raro decirlo de la capital, pero en el centro de Madrid la conexión falla más de lo que la gente espera. Locales en planta baja con muros gruesos, edificios antiguos donde la fibra llega a medias, sótanos comerciales sin cobertura móvil. Un TPV que necesite internet para cobrar se queda parado en el peor momento, un sábado de diciembre en Preciados.",
      "Carrito5 guarda los datos en tu ordenador. Cobras e imprimes el ticket con su QR aunque el router esté apagado. Cuando vuelva la conexión, el programa sigue donde lo dejaste. Es la razón por la que muchos comercios de calle prefieren un programa de escritorio a uno de navegador, y en el centro de Madrid se nota más que en ningún sitio."],
     None),
    ("Cómo se instala y quién te atiende",
     ["No hace falta que nadie vaya a tu tienda. Descargas el instalador, lo ejecutas en el ordenador del mostrador y en unos minutos tienes el programa listo para dar de alta artículos. La impresora de tickets que ya tengas suele funcionar sin más; si no, te ayudamos a configurarla.",
      "El soporte es por WhatsApp al 611 500 052 y por teléfono, con atención en España en horario comercial. Si algo se atasca a las nueve de la mañana con la persiana subiendo, escribes y te contesta una persona, no un formulario. Para dudas de instalación y de primeros pasos es donde más se resuelve.",
      "Lo que sí te recomendamos, si estás en Madrid: aprovecha el ordenador que tienes y no compres uno nuevo hasta probar. Lo que más se nota en la velocidad de la caja es el disco, y cambiar a un SSD cuesta mucho menos que un equipo entero."],
     ["Descarga el instalador y ejecútalo en el PC del mostrador.",
      "Configura los datos fiscales de tu negocio y la impresora de tickets.",
      "Da de alta las veinte o treinta referencias que más vendes.",
      "Haz una venta real, imprime el ticket y comprueba el QR.",
      "A partir de ahí, añade el resto del catálogo según entra mercancía."]),
    ("VeriFactu para un comercio de Madrid",
     ["La obligación de VeriFactu es estatal, así que a una tienda de Madrid le aplica el mismo calendario que a una de Sevilla: sociedades desde el 1 de enero de 2027, autónomos desde el 1 de julio de 2027, y 2026 como año de adaptación voluntaria. Carrito5 ya está adaptado y el plan Inicio emite tickets conformes con su QR.",
      "Lo único que cambia respecto a otras regiones es lo que no aplica: Madrid no tiene sistema foral propio, a diferencia de Álava, Bizkaia y Gipuzkoa con ticketBAI. Si te han dicho que en Madrid hay un registro adicional o una tasa autonómica, no es cierto. Esta página es información general y no asesoramiento fiscal: confirma tu fecha con tu asesor."],
     None),
  ],
  faqs=[
    ("¿Carrito5 tiene oficina o distribuidor en Madrid?",
     "La empresa es Ábaco Infoelectrónica S.L., con sede en Jaén, y el soporte a Madrid se hace por WhatsApp, teléfono y acceso remoto. No hace falta visita para instalar el programa: se descarga y se instala en el ordenador de la tienda en unos minutos."),
    ("¿Sirve para una tienda del centro que abre domingos y festivos?",
     "Sí. El programa está en tu ordenador y no depende de ningún servicio externo para cobrar, así que abres cuando quieras. Y como la Comunidad de Madrid tiene libertad de horarios, eso te lo permite la normativa comercial."),
    ("Mi local está en un sótano de Gran Vía y la cobertura es mala. ¿Puedo cobrar?",
     "Sí. Los datos se guardan en tu ordenador y los tickets se emiten sin conexión. Cuando vuelva internet el programa continúa con normalidad. Un TPV de navegador se pararía; este no."),
    ("¿El plan gratuito es suficiente para una boutique de Malasaña o Salamanca?",
     "Casi siempre. Una boutique rara vez pasa de 1.000 referencias en catálogo, y la matriz de tallas y colores permite dar de alta un modelo con todas sus variantes sin multiplicar artículos. Si creces por encima, se amplía con la licencia comercial."),
    ("Tengo un bazar en Vallecas con más de 3.000 referencias. ¿Me vale?",
     "El plan gratuito no, porque el límite es de 1.000 artículos en catálogo. La licencia comercial amplía ese límite, y si tu volumen es alto la opción con licencia en propiedad es Caja 5, de la misma casa. Escríbenos y te decimos cuál te conviene."),
    ("¿Funciona con la impresora de tickets y el cajón que ya tengo?",
     "Con la mayoría de impresoras térmicas de 80 mm sí, y el cajón portamonedas se abre a través de la impresora. Si tienes un modelo raro, mándanos el nombre por WhatsApp antes de descargar y te lo confirmamos."),
    ("¿Hay que pagar algo a la Comunidad de Madrid o al Ayuntamiento por VeriFactu?",
     "No. VeriFactu es una obligación estatal gestionada por la Agencia Tributaria y no lleva tasa ninguna, ni estatal ni autonómica ni municipal. Lo único que puede costarte es el programa, y Carrito5 en su plan Inicio es gratuito."),
    ("¿Puedo usarlo en una tienda de Getafe y otra en Leganés a la vez?",
     "Cada instalación de Carrito5 es independiente y guarda sus datos en su ordenador. Si necesitas ver las dos tiendas desde un mismo sitio con stock compartido, lo que buscas es un producto multitienda, y ahí te orientamos aunque no sea este."),
    ("Vendo a turistas en Sol. ¿El ticket vale como factura simplificada?",
     "Sí. El ticket que emite Carrito5 es una factura simplificada con los datos que exige la norma y el QR de VeriFactu."),
  ],
  satelites=[("Descargar Carrito5 gratis", "descargar-tpv-gratis.html", "Instalador para Windows, sin tarjeta"),
             ("TPV para boutiques", "tpv-boutique.html", "Salamanca, Malasaña, Chueca"),
             ("TPV para tiendas de ropa", "tpv-tienda-ropa.html", "Matriz de tallas y colores"),
             ("TPV en Barcelona", "software-tpv-barcelona.html", "La otra gran plaza"),
             ("TPV en Valencia", "software-tpv-valencia.html", "Ciutat Vella, Ruzafa, Eixample"),
             ("Todos los sectores", "sectores-y-negocios.html", "Elige el tuyo"),
             ("VeriFactu: cuándo entra en vigor", "verifactu-entrada-en-vigor.html", "Las dos fechas de 2027")]),

}
