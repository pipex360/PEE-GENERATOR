"""
Contenido de texto fijo del Plan de Emergencia y Evacuación.
Cada sección es una función que recibe el doc y los helpers para escribirse.
"""


def write_marco_legal(doc, h1, p, bullet):
    h1(doc, "MARCO LEGAL")
    p(doc, "El marco legal que rige la elaboración de un Plan de Emergencia y Evacuación se basa en las siguientes normativas:")
    bullet(doc, "Ley N° 21.442 sobre Copropiedad Inmobiliaria: En su Artículo 40°, esta ley establece la obligatoriedad para todo condominio de contar con un plan de emergencia ante siniestros como incendios, terremotos, tsunamis, entre otros. Dicho plan debe detallar las acciones a seguir antes, durante y después de una emergencia, poniendo especial énfasis en la alerta temprana y los procedimientos de evacuación. Además, la ley mandata que el plan de evacuación sea actualizado al menos una vez al año.")
    bullet(doc, "Directrices del Servicio Nacional de Prevención y Respuesta ante Desastres (SENAPRED): El Plan se alinea con las guías de la autoridad técnica en gestión de riesgos, como la \"Guía para la Implementación de Planes para la Reducción de Riesgos de Desastres en los Centros de Trabajo\".")


def write_cap1_objetivos(doc, h1, p, bullet):
    h1(doc, "CAPITULO N°1: OBJETIVOS Y CONCEPTOS")
    p(doc, "Objetivo General", bold=True)
    p(doc, "Establecer un marco de actuación organizado y eficaz que permita a la comunidad responder de manera segura ante una emergencia. El fin principal es salvaguardar la integridad física y la vida de todas las personas, minimizar las pérdidas materiales en bienes comunes y privados, y facilitar una pronta recuperación de la normalidad en las operaciones del edificio.")
    p(doc, "Objetivos Específicos", bold=True)
    p(doc, "Para cumplir con el objetivo general, este plan se enfoca en las siguientes metas:")
    bullet(doc, "Identificar y Evaluar Riesgos: Analizar y definir las principales amenazas de origen natural, técnico o social que puedan afectar a la comunidad.")
    bullet(doc, "Definir Procedimientos de Evacuación: Establecer y comunicar claramente las vías de evacuación, las zonas de seguridad y los puntos de encuentro.")
    bullet(doc, "Asignar Roles y Responsabilidades: Organizar y designar formalmente a los responsables de liderar y coordinar las acciones durante una emergencia.")
    bullet(doc, "Fomentar una Cultura Preventiva: Capacitar e informar permanentemente a los residentes y usuarios del edificio sobre los procedimientos de este plan.")
    bullet(doc, "Coordinar con Entidades Externas: Establecer canales de comunicación y coordinación con los organismos de respuesta a emergencias.")
    bullet(doc, "Servir como Marco General: Actuar como el plan maestro del condominio.")


def write_conceptos(doc, h1, bullet):
    h1(doc, "CONCEPTOS")
    bullet(doc, "Prevención: Conjunto de acciones cuyo objeto es impedir o evitar que fenómenos naturales o provocados por la actividad humana, causen emergencias o desastres.")
    bullet(doc, "Emergencia: Alteraciones en las personas, los bienes, los servicios y el medio ambiente, causadas por un fenómeno natural o generado por la actividad humana, que puede resolverse con los recursos de la comunidad afectada.")
    bullet(doc, "Evacuación: Abandono masivo de un local o edificio frente a una emergencia.")
    bullet(doc, "Evacuación Parcial: Se realizará cuando la emergencia sea detectada a tiempo y solo requiera la evacuación del nivel afectado.", level=1)
    bullet(doc, "Evacuación total: Se llevará a cabo en aquellos casos en los que la naturaleza de la emergencia sea de gran envergadura.", level=1)
    bullet(doc, "Líder: Persona que posee la habilidad para inducir a los seguidores a trabajar con responsabilidad en tareas conducidas por él o ella.")
    bullet(doc, "Plan de Emergencia: Conjunto de actividades y procedimientos destinados a controlar una situación de emergencia en el menor tiempo posible.")
    bullet(doc, "Plan de evacuación: Conjunto de actividades y procedimientos tendientes a conservar la vida y la integridad física de las personas.")
    bullet(doc, "Ejercicio de Simulación: Actuación en grupo en un espacio cerrado, en la que se representan varios roles para la toma de decisiones ante una situación imitada de la realidad.")
    bullet(doc, "Ejercicio de Simulacro: Ejercicio práctico en terreno a gran escala, en el cual los participantes se acercan lo más posible a un escenario de desastre real.")
    bullet(doc, "Desastre: Alteraciones intensas en las personas, los bienes, los servicios y el medio ambiente, que excede la capacidad de respuesta de la comunidad afectada.")


def write_cap2_organizacion(doc, h1, p, bullet):
    h1(doc, "CAPITULO N°2: ORGANIZACIÓN DE LA EMERGENCIA")
    h1(doc, "ORGANIGRAMA")
    h1(doc, "DESCRIPCIÓN DE ROLES Y FUNCIONES")
    p(doc, "Director(a) de la Emergencia:", bold=True)
    bullet(doc, "Quién: Es la máxima autoridad durante la crisis. Este rol lo asume el Administrador(a) del condominio. En su ausencia, el presidente del Comité de Administración debe tomar el mando.")
    bullet(doc, "Función: Dirige desde un punto estratégico. Es el único interlocutor válido con las autoridades (Bomberos, Carabineros) y los medios de comunicación. Toma las decisiones críticas, como ordenar la evacuación total.")
    p(doc, "Jefe de Emergencia:", bold=True)
    bullet(doc, "Quién: Es el comandante en terreno. Este rol es ideal para el Mayordomo o el conserje con más experiencia.")
    bullet(doc, "Función: Dirige a los equipos de apoyo interno. Supervisa que los procedimientos del plan se ejecuten correctamente.")
    p(doc, "Apoyo Interno:", bold=True)
    bullet(doc, "Líderes de Evacuación (o Líderes de Piso): Son residentes voluntarios y capacitados, idealmente uno por cada piso o sector. Su misión es guiar a sus vecinos de manera ordenada por las vías de evacuación hacia las zonas de seguridad.")
    bullet(doc, "Personal del Condominio (Conserjes): Son el principal apoyo operativo del Jefe de Emergencia. Sus tareas incluyen: dar la alarma, llamar a los servicios de emergencia externos, cortar suministros básicos.")
    p(doc, "Apoyo Externo:", bold=True)
    p(doc, "Son las instituciones y servicios profesionales que se harán cargo de controlar la emergencia. El rol de la comunidad es llamarlos a tiempo y facilitarle toda la información y el acceso necesario a su llegada.")
