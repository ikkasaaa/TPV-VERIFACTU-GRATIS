# -*- coding: utf-8 -*-
"""Base de hechos por sector, lote 7: la unica que sobrevive a las tres pruebas.

De las 14 paginas flojas que quedaban, esta es la unica sin pareja en
carrito5.com bajo ninguno de los dos metodos del motor NI en la pagina de
resultados de Google. Las otras trece estan bloqueadas hasta tener el arbol del
otro dominio.

Su colision es interna, con negocio_segunda_mano.asp, que el informe de FORJA
clasifica como REVISAR. Siguiendo el criterio del cliente (nada de 301 entre
paginas de contenido, la diferenciacion se hace con contenido y enlazado), esta
pagina se escribe hacia lo que la separa: la ropa vintage se compra en balas por
kilo, se data por decada y su talla de epoca no equivale a la de hoy. Un bazar
de segunda mano generalista no hace nada de eso.
"""

SECTORES_7 = {

# ================================================== VINTAGE Y SEGUNDA MANO
"negocio_vintage_segundamano.asp": dict(
  nombre="Tiendas de ropa vintage y segunda mano",
  crumb="Vintage",
  icono="fa-shirt",
  title="Software TPV para Tiendas de Ropa Vintage",
  desc="TPV para ropa vintage: balas compradas por kilo con su coste por prenda, talla de época, estado y taras, depósito de particulares y pieza única sin reposición.",
  kw="tpv tienda vintage, software tienda segunda mano ropa, programa tpv ropa vintage, tpv balas ropa por kilo, gestion tienda vintage",
  h1='Software TPV para Tiendas Vintage. <span>Compras cincuenta kilos y vendes trescientas prendas distintas.</span>',
  sub='Aquí no hay referencia que reponer ni talla que pedir. Entra una bala de ropa por peso, sale prenda a prenda con su década, su estado y una talla que no es la que pone la etiqueta.',
  bloques=[
    ("La bala se compra por kilo y se vende por prenda",
     ["El género entra en fardos: cincuenta kilos de camisería de los ochenta a tanto el kilo. Lo que sale son doscientas o trescientas piezas, cada una con su precio, y ninguna se parece a la anterior.",
      "El coste de cada prenda no está en ninguna factura: hay que repartirlo. Sin ese reparto no sabes si la bala salió a cuenta hasta que la has vendido entera, que es medio año tarde."],
     ["<strong>Compra por peso</strong> con el coste total de la bala y su procedencia.",
      "<strong>Reparto del coste entre las piezas</strong> según se van catalogando.",
      "<strong>Rendimiento por bala</strong>: cuántas piezas salieron vendibles y cuántas se tiraron.",
      "<strong>Merma de clasificado</strong>, que en un fardo puede ser un tercio y nadie la anota."]),
    ("La talla de la etiqueta miente, y el estado es parte del precio",
     ["Un 42 de los años ochenta le vale hoy a quien gasta un 38. La clienta que compra vintage lo sabe y pregunta por medidas reales, no por talla: pecho, cintura, largo de manga.",
      "Y cada pieza tiene su historia: una quemadura de plancha, un descosido, un botón cambiado. Describir la tara en la ficha evita la devolución y, sobre todo, la reseña de alguien que se sintió engañado."],
     ["<strong>Medidas reales en centímetros</strong> además de la talla que trae la etiqueta.",
      "<strong>Década y estilo</strong> como atributos: años 50, 60, 70, 80, 90, Y2K.",
      "<strong>Estado y taras descritas</strong> en la ficha, con su fotografía.",
      "<strong>Composición y etiqueta original</strong>, que en algunas prendas es lo que sube el precio."]),
    ("Cada percha es una unidad, y se vende una vez",
     ["No hay matriz de talla por color porque no hay dos iguales. El catálogo es una lista de piezas únicas con stock uno, cada una con su fotografía, y esa fotografía es la misma que se usa en redes y en la tienda online.",
      "Eso cambia el trabajo diario: dar de alta una prenda es ficharla entera, con su foto y sus medidas, en vez de teclear una referencia. Cuanto más rápido sea ese alta, más piezas llegan al perchero en lugar de quedarse en la trastienda."],
     ["<strong>Artículo único con stock uno</strong>, que desaparece al venderse.",
      "<strong>Alta rápida con fotografía</strong>, pensada para fichar en serie.",
      "<strong>Ubicación en la tienda</strong>: perchero, rack y sección, para encontrarla cuando preguntan.",
      "<strong>Etiqueta con código propio</strong>, porque ninguna prenda trae EAN."]),
    ("El género que no es tuyo, y lo que entra por la puerta",
     ["Muchas tiendas trabajan con depósito: alguien deja diez prendas y cobra cuando se venden. Esa ropa ocupa perchero pero no es stock tuyo, y confundirlas hace que el inventario valga más de lo que tienes. Con el propietario en la ficha, al cerrar el mes sale sola la liquidación de cada uno con su comisión.",
      "Y está la compra directa a particulares que vacían un armario. Es una operación con su documento y sus datos, igual que en cualquier compraventa de bienes usados. El tratamiento que le corresponda en el IVA, incluido el régimen especial de bienes usados si te aplica, confírmalo con tu asesor: depende de tu actividad y no lo decide el programa."]),
  ],
  faqs=[
    ("Compro la ropa en balas por kilo. ¿Puedo saber cuánto me cuesta cada prenda?",
     "Sí. La bala entra como compra por peso con su coste total, y ese coste se reparte entre las piezas según las vas catalogando. Al terminar el fardo tienes su rendimiento real: cuántas salieron vendibles, cuántas se descartaron y qué margen dejó."),
    ("¿Puedo guardar las medidas reales y no solo la talla de la etiqueta?",
     "Sí, en centímetros de pecho, cintura y largo, junto a la talla original. Es lo que pide quien compra vintage, porque un 42 de los años ochenta equivale hoy a un 38 largo."),
    ("Cada prenda es distinta. ¿Cómo se lleva el catálogo?",
     "Como artículos únicos con stock uno, cada uno con su fotografía, su década, su estado y su ubicación en la tienda. Al venderse desaparece del disponible, sin matriz de talla y color que no tendría sentido aquí."),
    ("¿Se pueden describir las taras de una prenda?",
     "Sí, en la ficha, con su fotografía. Dejar escrito el descosido o la mancha antes de vender es lo que evita la devolución y la reseña de quien se sintió engañado."),
    ("Tengo ropa en depósito de particulares. ¿Se distingue de la mía?",
     "Sí, marcando el propietario en la ficha. El inventario separa el género propio del depósito, y al cerrar el mes sale la liquidación de lo vendido de cada depositante con su comisión aplicada."),
    ("Compro armarios enteros a particulares. ¿Queda documentado?",
     "Sí, como compra a particular con sus datos y el importe pagado, y la salida de efectivo reflejada en el arqueo del día. El tratamiento que le corresponda en el IVA depende de tu actividad, así que conviene revisarlo con tu asesor."),
  ],
  rel=[("Cómo hacer el inventario de una tienda","/como-hacer-un-inventario-tienda.asp"),
       ("Etiquetas con código de barras","/etiquetas-codigo-de-barras-tpv.asp"),
       ("TPV para tiendas de vinilos","/negocio_vinilos.asp"),
       ("TPV para tiendas de ropa de tallas grandes","/negocio_tallas_grandes.asp"),
       ("Arqueo de caja y cierre diario","/arqueo-de-caja-cierre-diario.asp"),
       ("Preguntas frecuentes sobre TPV","/preguntas-frecuentes-tpv.asp")]),

}
