"""Contenido fijo parte 4: Plan de evacuación, conclusiones y recuperación."""


def write_cap6_evacuacion(doc, h1, p, bullet, data):
    h1(doc, "CAPITULO N°6: PLAN DE EVACUACIÓN")
    p(doc, "El Plan de Evacuación es el conjunto de procedimientos organizados y seguros destinados a conservar la vida y la integridad física de las personas, mediante su desplazamiento ordenado desde una zona de riesgo hacia una Zona de Seguridad previamente establecida.")

    p(doc, "Principios Fundamentales de la Evacuación:", bold=True)
    bullet(doc, "Calma: Mantener la calma es fundamental para pensar con claridad y evitar el pánico colectivo.")
    bullet(doc, "Orden: Seguir las vías de evacuación señalizadas y las instrucciones de los líderes.")
    bullet(doc, "Rapidez (Sin Precipitación): El movimiento debe ser ágil y constante, pero sin correr.")

    p(doc, "¿Cuándo se debe Evacuar?", bold=True)
    bullet(doc, "Incendio declarado que no pudo ser controlado en su fase inicial.")
    bullet(doc, "Aviso o amenaza creíble de un artefacto explosivo.")
    bullet(doc, "Después de un sismo de gran magnitud, si se observan daños estructurales evidentes.")
    bullet(doc, "Orden directa de una autoridad competente (Bomberos o Carabineros).")
    bullet(doc, "Durante simulacros de evacuación programados.")

    p(doc, "¿Quién Ordena la Evacuación?", bold=True)
    bullet(doc, "Autoridades de emergencia presentes (Bomberos, Carabineros).")
    bullet(doc, "El Administrador o el Comité de Administración del edificio.")
    bullet(doc, "El Jefe o Líder de Emergencia designado en el plan.")

    h1(doc, "TIPOS DE EVACUACIÓN")
    p(doc, "Evacuación Parcial:", bold=True)
    p(doc, "Corresponde a la evacuación organizada de una parte específica del edificio, como un solo piso o sector, mientras el resto permanece seguro en sus dependencias. Se aplica cuando la emergencia está contenida.")
    p(doc, "Evacuación Total:", bold=True)
    p(doc, "Implica la desocupación completa y ordenada de todo el edificio. Se ordena cuando la permanencia en cualquier parte del edificio representa un peligro inminente para la vida.")

    h1(doc, "VIAS PRINCIPALES")
    p(doc, "Siga estos pasos de manera ordenada:")
    bullet(doc, "Salga de su departamento y diríjase a la puerta de acceso a la escalera (SALIDA DE EMERGENCIA).")
    bullet(doc, "Ingrese a la caja de escaleras (Zona Vertical de Seguridad).")
    bullet(doc, "Descienda en calma y en orden, utilizando siempre el pasamanos.")
    bullet(doc, "Continúe bajando hasta llegar al primer piso, saliendo por el hall principal.")
    bullet(doc, "Diríjase de inmediato hacia la Zona de Seguridad exterior.")

    h1(doc, "ZONAS DE SEGURIDAD")
    zona = data.get("zona_seguridad", "")
    if zona:
        p(doc, zona)
    else:
        p(doc, "Se define como Zona de Seguridad Principal el área exterior del edificio designada para este fin. Estos lugares han sido seleccionados por ser espacios abiertos que cumplen con una distancia prudente respecto a la fachada del edificio.")


def write_protocolos_evacuacion(doc, h1, p, bullet):
    h1(doc, "PROTOCOLOS DE EVACUACIÓN")
    bullet(doc, "Liderazgo de la Emergencia: El Administrador o Jefe de Emergencia dirigirá las operaciones desde un puesto de mando.")
    bullet(doc, "Evacuación Escalonada: Se realizará de forma ordenada y por etapas, primero el piso del siniestro y pisos adyacentes.")

    p(doc, "Instrucciones para TODOS los Residentes:", bold=True)
    bullet(doc, "Mantenga la Calma y Siga las Instrucciones.")
    bullet(doc, "NO UTILICE LOS ASCENSORES.")
    bullet(doc, "Diríjase a la Vía de Evacuación Señalizada.")
    bullet(doc, "Descienda en Orden usando el pasamanos.")
    bullet(doc, "Ayude a Quienes lo Necesiten: niños, adultos mayores o personas con dificultades.")
    bullet(doc, "No se Devuelva: Por ningún motivo regrese a buscar objetos personales.")
    bullet(doc, "Vaya a la Zona de Seguridad y permanezca allí.")

    p(doc, "Responsabilidades de los Líderes de Evacuación:", bold=True)
    bullet(doc, "Identificación: Usarán chaleco reflectante y portarán letrero con el número de piso.")
    bullet(doc, "Verificar que no quede nadie en su piso.")
    bullet(doc, "Guiar al grupo hasta la Zona de Seguridad.")
    bullet(doc, "Realizar un conteo y reportar ausentes al Jefe de Emergencia.")

    p(doc, "Asistencia a Personas con Movilidad Reducida:", bold=True)
    bullet(doc, "Cada piso deberá tener personas designadas para asistir en el traslado de quienes lo necesiten.")
    bullet(doc, "Si la evacuación por escaleras no es posible, trasladar a un área de refugio seguro.")


def write_recomendaciones(doc, h1, p, bullet):
    h1(doc, "RECOMENDACIONES GENERALES")
    bullet(doc, "Mantenga la Calma: El pánico es el mayor riesgo.")
    bullet(doc, "No Corra, Camine Rápido.")
    bullet(doc, "¡No Regrese por Ningún Motivo!")
    bullet(doc, "Si Hay Humo, Agáchese: El aire más limpio está cerca del suelo.")
    bullet(doc, "Siga Siempre las Instrucciones.")
    bullet(doc, "Circule por su Derecha en las Escaleras: Deje el lado izquierdo libre para Bomberos.")
    bullet(doc, "Facilite su Desplazamiento: Si usa zapatos con taco alto, quíteselos.")
    bullet(doc, "Diríjase a la Zona de Seguridad y permanezca con su grupo.")


def write_conclusiones(doc, h1, p, bullet):
    h1(doc, "CONCLUSIONES")
    p(doc, "Un plan de emergencia es una herramienta vital, pero su verdadero éxito reside en el compromiso, el conocimiento y la preparación de cada persona que forma parte de la comunidad.")
    bullet(doc, "El Conocimiento Individual es la Base de la Prevención: Cada ocupante tiene la responsabilidad de saber dónde se encuentran los equipos de seguridad, vías de evacuación y Zonas de Seguridad.")
    bullet(doc, "La Cooperación Colectiva es la Clave del Éxito: La evacuación siempre se debe realizar hacia la planta baja y a la Zona de Seguridad designada.")
    bullet(doc, "El Liderazgo Efectivo Salva Vidas: Los Líderes de Evacuación son el pilar de la operación en terreno.")
    bullet(doc, "La Mejora Continua Fortalece Nuestra Seguridad: Este plan es un documento vivo que debe ser repasado y practicado constantemente.")


def write_cap7_recuperacion(doc, h1, p, bullet):
    h1(doc, "CAPITULO N°7: RECUPERACIÓN")
    p(doc, "Una vez que la emergencia ha sido controlada, comienza la fase de recuperación.")
    p(doc, "Paso 1: Control y Aseguramiento del Edificio", bold=True)
    p(doc, "El personal de emergencia determinará cuándo la amenaza inmediata ha cesado. Solo entonces se podrá iniciar la evaluación.")
    p(doc, "Paso 2: Inspección Técnica de Seguridad", bold=True)
    p(doc, "Antes de autorizar el reingreso, se deberá revisar: sistemas eléctricos, de agua potable y de gas; estructura general del edificio; ascensores y bombas de agua; sistemas de seguridad y comunicaciones.")
    p(doc, "Paso 3: Autorización y Retorno Seguro", bold=True)
    bullet(doc, "El reingreso solo se permitirá cuando las autoridades o técnicos certifiquen que es seguro.")
    bullet(doc, "El retorno se realizará de forma ordenada con el apoyo de los Líderes de Evacuación.")
    p(doc, "Paso 4: Evaluación de la Emergencia y Mejora del Plan", bold=True)
    p(doc, "El Comité de Administración y el equipo de emergencia se reunirán para analizar el manejo de la situación e identificar mejoras.")
    p(doc, "Paso 5: Activación de Seguros y Reparaciones", bold=True)
    p(doc, "La Administración se encargará de la evaluación de daños materiales y la activación de los seguros comprometidos.")
