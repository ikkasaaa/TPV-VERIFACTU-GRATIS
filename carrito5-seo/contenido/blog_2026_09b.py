# -*- coding: utf-8 -*-
"""Blog de carrito5.com: segunda capa de septiembre de 2026.

Posts de sector con fecha, intercalados con los generales del mes para tener
dos publicaciones por semana. Mismas reglas de funciones confirmadas que
blog_2026_09.py: tallas y colores; clientes con historial, devoluciones y
vales; codigos de barras con lector, codigo propio y etiquetas; catalogo,
stock, ticket con QR, sin internet, Windows. Nada mas.
"""

BLOG_2026_09B = {

# ------------------------------------------------------------------ 10 sep
"vuelta-al-cole-zapateria-infantil-numeros": dict(
  title="Vuelta al Cole en la Zapatería Infantil: un Número Más",
  desc="En septiembre la zapatería infantil vende el colegial a niños que han crecido un número. Ficha del niño con su último número y stock por número.",
  kw="zapateria infantil vuelta al cole, zapato colegial septiembre, calzado infantil campaña escolar, tpv zapateria infantil, numeros calzado niños stock",
  h1="Zapatería infantil en septiembre: el mismo niño, un número más",
  sub="El zapato de colegio se compra la primera semana de septiembre, con prisa, y el niño ha crecido desde junio. La tienda que sabe qué número llevaba en marzo vende en dos minutos.",
  publicado="2026-09-10",
  para="Zapaterías y calzado infantil",
  resumen=[
    "La campaña del calzado escolar se concentra en las dos primeras semanas de septiembre: zapato colegial, deportiva de educación física y bota de agua para octubre. El problema es el número: cada niño ha crecido desde la última compra y los padres no saben cuál lleva ahora. Una ficha de cliente con el número de la última compra resuelve la venta en dos minutos.",
    "Y como el colegial se vende por número y el stock se agota por números sueltos, el pedido de reposición de mitad de septiembre se hace número a número, con lo que dice el stock del programa.",
  ],
  cuerpo=[
    ("La compra que se hace con prisa y sin saber el número",
     ["La primera semana de septiembre entran en la zapatería familias con dos o tres niños, una lista del colegio y media hora. Quieren el colegial azul o negro, la deportiva blanca para gimnasia, y salir. Lo que frena la venta es siempre lo mismo: «¿qué número lleva ahora?». Se prueba el 30, aprieta; el 31, bien; se busca el 31 en el almacén y no queda en negro.",
      "Dos cosas quitan la mitad de ese tiempo. La ficha del niño, con el número de la última compra en marzo: si llevaba un 30, se empieza por el 31. Y el stock por número en pantalla: antes de ir al almacén, saber si queda el 31 en negro o hay que ofrecer el azul."],
     None),
    ("La ficha del niño, no la del padre",
     ["En calzado infantil el cliente es el niño, aunque pague el padre. La ficha de cliente lleva el nombre de la familia y, en cada compra, el modelo y el número; con tres niños son tres líneas distintas y hay que distinguirlas. Lo práctico es anotar el nombre del niño en cada venta, para que en marzo, con el cambio de temporada, se sepa que Lucía llevaba un 31 en septiembre y que ahora tocará un 32.",
      "En Carrito5 cada venta queda en la ficha del cliente con el modelo, el número y el color. La nota del nombre del niño la pone la tienda. Con eso, la familia que vuelve en marzo, en junio y en septiembre se atiende con la ficha delante."],
     ["<strong>Cada venta con número y color</strong> en la ficha de la familia.",
      "<strong>Nombre del niño</strong> anotado en la venta, si hay varios hermanos.",
      "<strong>Al volver</strong>: empezar por un número más que la última compra."]),
    ("Stock por número: reponer los sueltos",
     ["El colegial se agota por números, no por modelos. En una campaña normal el 31 y el 32 se van la primera semana y el 27 y el 36 sobran. Si el pedido de reposición se hace «diez pares más del colegial negro», llegan diez pares repartidos y siguen faltando el 31 y el 32.",
      "Con el modelo dado de alta con su matriz de números y colores, el stock dice qué números quedan de cada modelo, y el pedido del 10 de septiembre al proveedor es una lista de números sueltos. Muchos proveedores de calzado infantil sirven pares sueltos en campaña; hay que pedirlos así."],
     None),
    ("Deportiva, bota de agua y lo que viene en octubre",
     ["La segunda ola de la campaña es la deportiva de educación física, que suele llegar cuando el colegio da el horario, y la bota de agua y el chubasquero con las primeras lluvias de octubre. Las dos se venden a familias que ya han pasado por la tienda en septiembre y tienen ficha. Avisarlas por WhatsApp cuando entra la bota de agua vende más que el escaparate."],
     None),
  ],
  cierre=("El número de cada niño, en la ficha",
          ["Carrito5 da de alta cada modelo con su matriz de números y colores, guarda cada venta en la ficha de la familia con el número y el color, y lleva el stock por número para reponer los sueltos. Es gratuito hasta 1.000 artículos, para Windows. Instalado hoy, la campaña de este septiembre queda apuntada y la de marzo empieza sabiendo qué número lleva cada niño."],
          "Descargar Carrito5 gratis", "/descargar-tpv-gratis.html"),
  faqs=[
    ("¿Cuándo se vende el calzado escolar?",
     "Las dos primeras semanas de septiembre el colegial; la deportiva cuando el colegio da el horario; la bota de agua con las primeras lluvias de octubre."),
    ("¿Cómo sé qué número lleva un niño que compró en marzo?",
     "Con la ficha de cliente de la familia: cada venta lleva el modelo, el número y el color. Se empieza a probar un número más."),
    ("¿Cómo repongo si se agotan el 31 y el 32?",
     "Número a número, con lo que dice el stock por número del programa. Muchos proveedores de infantil sirven pares sueltos en campaña."),
    ("Tengo familias con tres niños. ¿Cómo distingo las compras?",
     "Anotando el nombre del niño en cada venta de la ficha de la familia. La ficha es de quien paga; la nota dice para quién."),
    ("¿Sirve Carrito5 para una zapatería infantil?",
     "Sí: modelo con matriz de números y colores, stock por variante, ficha de cliente con historial y etiquetas con código de barras. Plan gratuito hasta 1.000 artículos."),
  ],
  relacionadas=[("TPV para zapaterías", "tpv-zapateria.html", "Números, pares y stock"),
                ("Vuelta al cole en la papelería", "blog/vuelta-al-cole-papeleria-ultimas-semanas.html", "La otra campaña escolar"),
                ("Matriz de tallas y colores", "tallas-y-colores.html", "Números como tallas"),
                ("Calendario comercial 2026-2027", "blog/calendario-comercial-2026-2027-fechas-clave.html", "Todas las campañas")]),

# ------------------------------------------------------------------ 24 sep
"otono-boutique-cambio-de-armario-nueva-temporada": dict(
  title="Otoño en la Boutique: la Nueva Temporada Entra en Septiembre",
  desc="La colección de otoño llega en septiembre y la clienta la quiere el día que refresca. Entrar cada modelo con tallas y colores y avisar a quien compró.",
  kw="boutique otoño nueva temporada, cambio de armario tienda ropa, coleccion otoño boutique septiembre, tpv boutique tallas colores, avisar clientas nueva coleccion",
  h1="Otoño en la boutique: entrar la colección y avisar a quien la espera",
  sub="La primera semana fresca de septiembre la clienta abre el armario, ve que no tiene nada y viene a la tienda. Si la colección aún está en cajas, vuelve otro día o no vuelve.",
  publicado="2026-09-24",
  para="Boutiques y tiendas de moda",
  resumen=[
    "La colección de otoño entra en la boutique en varias entregas entre finales de agosto y principios de octubre, y la clienta la busca el primer día que refresca. Cada entrega se da de alta al llegar, modelo por modelo con su matriz de tallas y colores y su etiqueta, para que esté en tienda esa misma tarde.",
    "Y la venta de otoño empieza con la ficha de cliente: quien compró la primavera pasada es quien va a comprar el otoño, y un aviso por WhatsApp con la colección ya colgada vende más que el escaparate.",
  ],
  cuerpo=[
    ("El día que refresca",
     ["Cada año hay un día, entre el 10 y el 25 de septiembre, en que baja la temperatura de golpe y las clientas de la boutique aparecen el mismo sábado. No lo decide la tienda; lo decide el tiempo. Lo que sí decide la tienda es si ese sábado la colección está colgada, con talla y precio, o sigue en cajas en la trastienda porque no ha dado tiempo.",
      "Por eso la entrada de género en septiembre no se deja para «cuando haya un rato». Cada caja se abre el día que llega y se da de alta esa tarde."],
     None),
    ("Entrar la colección: modelo, tallas, colores, etiqueta",
     ["Una entrega de otoño de una boutique son veinte o treinta modelos con sus tallas y sus colores. Dados de alta uno a uno como artículos serían trescientas líneas; dados de alta como modelo con su matriz, son treinta altas. Cada una con su precio, sus tallas y colores marcados, y el stock por variante según el albarán.",
      "Las prendas que llegan con código de barras del proveedor se leen con el lector; las de proveedor pequeño reciben código propio y etiqueta impresa. Al terminar, la caja está colgada y la caja cobra pasando la etiqueta."],
     ["<strong>Un alta por modelo</strong>, no por talla.",
      "<strong>Stock por variante</strong> desde el albarán.",
      "<strong>Etiqueta propia</strong> para lo que no trae código.",
      "<strong>Esa misma tarde</strong>, colgado."]),
    ("Avisar a quien compró la primavera",
     ["La clienta de boutique repite. La que compró dos blusas y un pantalón en abril es la que va a comprar el abrigo en octubre, si sabe que ha llegado. Con las ventas de primavera en la ficha de cliente, la lista de a quién avisar sale del programa: quien compró en marzo, abril y mayo, con su talla.",
      "El aviso es una foto de tres prendas por WhatsApp y una frase. No hace falta más, y funciona mejor cuando se sabe la talla de quien lo recibe: «ha llegado en tu 40»."],
     None),
    ("Lo que queda de verano",
     ["La colección de verano que no se ha vendido no se guarda entera. Los básicos sí, con su código y su stock para el año que viene. Lo de tendencia va a la última rebaja de septiembre, con etiqueta nueva, antes de que el otoño lo tape. La decisión se toma con la lista del stock de verano por modelo y talla, que a estas alturas ya dice qué se ha movido y qué no."],
     None),
  ],
  cierre=("Treinta altas y la lista de a quién avisar",
          ["Carrito5 da de alta cada modelo con su matriz de tallas y colores, imprime etiquetas para lo que llega sin código y guarda cada venta en la ficha de la clienta con su talla. Es gratuito hasta 1.000 artículos, para Windows. Instalado esta semana, la próxima entrega de otoño entra en una tarde y el aviso a las clientas de primavera sale del programa."],
          "Descargar Carrito5 gratis", "/descargar-tpv-gratis.html"),
  faqs=[
    ("¿Cuándo llega la colección de otoño a la boutique?",
     "En varias entregas entre finales de agosto y principios de octubre. Cada una se da de alta el día que llega."),
    ("¿Cómo doy de alta treinta modelos con sus tallas sin pasarme la semana?",
     "Con la matriz de tallas y colores: un alta por modelo, marcando tallas y colores, y el stock por variante desde el albarán. Una tarde."),
    ("¿A quién aviso de la nueva colección?",
     "A quien compró la primavera pasada, que está en la ficha de cliente con su talla. Una foto por WhatsApp y una frase."),
    ("¿Qué hago con el verano que no se ha vendido?",
     "Los básicos se guardan con su código y su stock. Lo de tendencia, a la última rebaja de septiembre con etiqueta nueva."),
    ("¿Carrito5 sirve para una boutique?",
     "Sí: tallas y colores, ficha de clienta con historial y devoluciones, códigos de barras y etiquetas. Plan gratuito hasta 1.000 artículos."),
  ],
  relacionadas=[("TPV para boutiques", "tpv-boutique.html", "Pocas prendas, cada una importa"),
                ("Matriz de tallas y colores", "tallas-y-colores.html", "Un alta por modelo"),
                ("La Navidad se prepara en septiembre", "blog/campana-navidad-tienda-preparar-en-septiembre.html", "El pedido de diciembre"),
                ("Cambio de temporada", "blog/cambio-de-temporada-primavera-stock-invierno.html", "Lo mismo, en febrero")]),

}
