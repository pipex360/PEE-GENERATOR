"""Contenido fijo parte 2: Recursos técnicos, medidas preventivas y procedimientos."""


def write_cap3_recursos(doc, h1, p, bullet):
    h1(doc, "CAPITULO N°3: RECURSOS TÉCNICOS")
    p(doc, "Luces de emergencia: para garantizar una evacuación segura, el edificio está equipado con un sistema de alumbrado de emergencia autónomo en pasillos, vías de evacuación y escaleras. Estas luces se activan automáticamente ante un corte de energía.")

    h1(doc, "SISTEMA DE COMBATE DE INCENDIOS")
    p(doc, "El sistema de combate de incendios del edificio se compone de dos redes de agua principales e independientes: la Red Húmeda y la Red Seca.")

    p(doc, "Red húmeda:", bold=True)
    bullet(doc, "Propósito y Uso: La Red Húmeda es el sistema de primera intervención para el control de fuegos incipientes (amagos). Está diseñada para ser utilizada exclusivamente por residentes y personal previamente capacitado.")
    bullet(doc, "Ubicación y Componentes: Los gabinetes de la Red Húmeda se encuentran en los pasillos de cada piso. Cada uno está equipado con una manguera semirrígida de 30 metros y un pitón (boquilla).")
    bullet(doc, "Funcionamiento: El sistema se mantiene siempre presurizado y es abastecido por la bomba de incendios y los estanques de reserva de agua del edificio.")
    p(doc, "Instrucciones de Uso Básico:", bold=True)
    bullet(doc, "Abra el gabinete.")
    bullet(doc, "Extienda completamente la manguera hacia el lugar del amago.")
    bullet(doc, "Una vez extendida, abra la llave de paso para permitir el flujo de agua.")
    bullet(doc, "Sujete firmemente el pitón y dirija el chorro a la base del fuego.")

    p(doc, "Extintores portátiles:", bold=True)
    p(doc, "Tipos y Ubicación: El edificio está equipado con extintores portátiles. Se encuentran debidamente señalizados y montados en los muros de todas las áreas comunes, pasillos y recintos técnicos.")
    p(doc, "Polvo Químico Seco (PQS 10A-60BC, de 10 kilos): Para fuegos de Clase A, B y C.")
    p(doc, "Dióxido de Carbono (CO2): Ubicados cerca de salas eléctricas y tableros.")
    p(doc, "Instrucciones de Uso Básico:", bold=True)
    bullet(doc, "Retire el extintor de su soporte y quite el pasador de seguridad.")
    bullet(doc, "Ubíquese a una distancia segura y apunte la boquilla hacia la base del fuego.")
    bullet(doc, "Apriete la manilla superior para descargar el agente extintor.")
    bullet(doc, "Mueva la boquilla de lado a lado (en forma de abanico) hasta apagar las llamas.")


def write_sistemas_edificio(doc, h1, p, bullet):
    h1(doc, "SISTEMA DE EDIFICIO")
    p(doc, "Remarcadores Eléctricos:", bold=True)
    p(doc, "De acuerdo con la legislación vigente, art. 73, DS MOP 121/91, todos los edificios deberán incluir la instalación de remarcadores por cada unidad del edificio o conjunto habitacional.")
    p(doc, "Citofonía:", bold=True)
    p(doc, "El sistema de citofonía proporciona una comunicación directa entre cada departamento y la conserjería. En una emergencia se convierte en el canal principal para reportar un siniestro de manera inmediata.")
    p(doc, "Teléfono:", bold=True)
    p(doc, "El edificio cuenta con un teléfono de red fija en la conserjería, destinado exclusivamente a ser el vínculo de comunicación con los organismos de apoyo externo (Bomberos, Ambulancia, Carabineros, etc.).")
    p(doc, "Señalización de Seguridad:", bold=True)
    bullet(doc, "Vías de Evacuación y Salidas de Emergencia: Flechas y pictogramas que indican la ruta de escape correcta.")
    bullet(doc, "Equipos de Emergencia: Ubicación de extintores, Red Húmeda y Red Seca.")
    bullet(doc, "Zonas de Seguridad: Identificación de los puntos de encuentro seguros.")
    bullet(doc, "Advertencia de Riesgos: Señales de riesgo eléctrico en tableros y salas técnicas.")
    p(doc, "Normativa y Mantenimiento: Toda la señalización se rige por los colores, formas y símbolos establecidos en la Norma Chilena NCh 2111.")
    p(doc, "Las Vías de Evacuación:", bold=True)
    p(doc, "Las vías de evacuación son los caminos designados y señalizados para un desalojo seguro del edificio, siendo las cajas de escaleras las rutas principales. Es una obligación crítica de todos los residentes el mantener estos pasillos y escaleras completamente despejados en todo momento.")


def write_cap4_preventivas(doc, h1, p, bullet):
    h1(doc, "CAPITULO N°4: MEDIDAS PREVENTIVAS")
    p(doc, "Este plan establece un método de respuesta organizado para que toda la comunidad actúe de forma segura y coordinada ante una emergencia.")
    bullet(doc, "Propósito y Responsabilidad de la Administración: Para garantizar la operatividad de todos los equipos de seguridad, la Administración gestiona un programa de mantenimiento preventivo.")
    bullet(doc, "Sistemas Críticos Bajo Mantenimiento:")
    bullet(doc, "Sistemas de Incendio: Detección y Alarma, Red Húmeda, Red Seca y Extintores.", level=1)
    bullet(doc, "Sistemas de Evacuación y Seguridad: Iluminación de Emergencia, Puertas de Escape, Señalización.", level=1)
    bullet(doc, "Sistemas Generales: Tableros Eléctricos, CCTV y Controles de Acceso, Suministro de Agua Potable y Comunicaciones.", level=1)
    bullet(doc, "Pruebas y Certificaciones: Las rutinas de mantenimiento incluyen pruebas operativas periódicas de los sistemas de emergencia.")
    bullet(doc, "Responsabilidad de los Residentes: Cada residente debe mantener en buen estado las instalaciones interiores de su propio departamento.")


def write_capacitacion(doc, h1, p, bullet):
    h1(doc, "CAPACITACIÓN")
    bullet(doc, "Principio Fundamental de Actuación: La primera prioridad es la vida. Ninguna persona deberá intentar controlar una emergencia si esto pone en riesgo su integridad física.")
    bullet(doc, "Programa de Capacitación por Niveles:")
    bullet(doc, "Capacitación para el Personal del Condominio: Prevención de Riesgos, Uso de extintores y Red Húmeda, Primeros Auxilios básicos, Protocolos de comunicación y corte de suministros.", level=1)
    bullet(doc, "Formación para Líderes de Evacuación: Liderazgo y comunicación en crisis, Procedimientos de evacuación, Reconocimiento de Zonas de Seguridad.", level=1)
    bullet(doc, "Información para Todos los Residentes: Las vías de evacuación, el significado de las alarmas, la importancia de participar en los simulacros anuales (Ley 21.442).", level=1)


def write_simulacros(doc, h1, p, bullet):
    h1(doc, "PROGRAMA DE ENTRENAMIENTO Y SIMULACROS")
    bullet(doc, "Propósito y Obligatoriedad Legal: Conforme a la Ley de Copropiedad N° 21.442, la comunidad debe realizar simulacros de evacuación al menos una vez al año.")
    p(doc, "Tipos de Ejercicios Prácticos:", bold=True)
    bullet(doc, "Ejercicios de Simulación (Para el Equipo de Gestión): Ejercicios teóricos dirigidos por la Administración para probar la toma de decisiones.")
    bullet(doc, "Simulacros de Evacuación (Para la Comunidad): Ejercicios prácticos que implican la movilización de personas hacia las Zonas de Seguridad.")
    bullet(doc, "Objetivos del Simulacro Anual: Evaluar el desempeño del Plan, comprobar el funcionamiento de equipos, medir tiempos de evacuación, identificar mejoras, fomentar la participación.")

    p(doc, "Kit de Elementos Auxiliares para Emergencias:", bold=True)
    p(doc, "Equipamiento Mínimo Recomendado:")
    bullet(doc, "Botiquín de Primeros Auxilios (sin medicamentos ni fármacos)")
    bullet(doc, "Megáfono para dirigir la evacuación")
    bullet(doc, "Linternas potentes con baterías cargadas")
    bullet(doc, "Chalecos Reflectantes para identificar al personal y Líderes de Evacuación")
    bullet(doc, "Cinta de Demarcación para aislar zonas de peligro")
    bullet(doc, "Frazadas o mantas térmicas")
    p(doc, "Contenido Recomendado del Botiquín:")
    bullet(doc, "Suero fisiológico, gasas y apósitos estériles, vendas elásticas, tela adhesiva hipoalergénica, guantes de procedimiento, tijeras.")
