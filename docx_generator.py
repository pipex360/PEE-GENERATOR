"""Generador principal del documento PEE."""
from doc_styles import (
    create_doc, add_title, add_h1, add_h2, add_paragraph,
    add_bullet, add_table_2col, add_table_3col, add_table_4col, add_spacer,
)
from plan_content import (
    write_marco_legal, write_cap1_objetivos, write_conceptos, write_cap2_organizacion,
)
from plan_content2 import (
    write_cap3_recursos, write_sistemas_edificio, write_cap4_preventivas,
    write_capacitacion, write_simulacros,
)
from plan_content3 import (
    write_proc_incendio, write_proc_sismo, write_proc_bomba, write_proc_asalto,
    write_proc_electrica, write_proc_agua, write_proc_gas, write_proc_inundacion,
)
from plan_content4 import (
    write_cap6_evacuacion, write_protocolos_evacuacion, write_recomendaciones,
    write_conclusiones, write_cap7_recuperacion,
)

p = add_paragraph
bullet = add_bullet
h1 = add_h1


def _write_cover(doc, data):
    add_title(doc, "PLAN DE EMERGENCIA Y EVACUACIÓN")
    add_title(doc, data.get("nombre_edificio", ""))
    add_spacer(doc)
    add_table_2col(doc, [
        ("Realizado por:", data.get("realizado_por", "")),
        ("Aprobado por:", data.get("aprobado_por", "")),
        ("Fecha de actualización:", data.get("fecha_actualizacion", "")),
    ])
    doc.add_page_break()


def _write_ficha_tecnica(doc, data):
    h1(doc, "FICHA TECNICA DEL EDIFICIO")
    p(doc, "La presente ficha técnica consolida los datos esenciales del inmueble, abarcando sus especificaciones constructivas, elementos estructurales y los equipos de seguridad con los que cuenta.")
    if data.get("coordenadas"):
        p(doc, f"Coordenadas de Google maps: {data['coordenadas']}")
    add_spacer(doc)

    # Tabla 1: Identificación
    add_table_2col(doc, [
        ("1. IDENTIFICACIÓN DEL EDIFICIO", ""),
        ("Nombre del edificio", data.get("nombre_edificio", "")),
        ("Dirección", data.get("direccion", "")),
        ("Entre Calles", f"{data.get('entre_calle_1', '')} / {data.get('entre_calle_2', '')}"),
        ("Acceso al edificio", data.get("acceso_edificio", "")),
        ("Permiso municipal N°", data.get("permiso_municipal", "Pendiente")),
        ("Rol de avalúos del SII", data.get("rol_avaluos", "Pendiente")),
        ("Comuna", data.get("comuna", "")),
    ])
    add_spacer(doc)

    # Tabla 2: Características
    add_table_2col(doc, [
        ("2. CARACTERÍSTICAS DEL EDIFICIO", ""),
        ("Pisos sobre nivel de la calle", data.get("pisos_sobre", "")),
        ("Pisos bajo nivel (subterráneos)", data.get("pisos_bajo", "")),
        ("Superficie edificada (m2)", data.get("superficie", "")),
        ("Carga de ocupación (Art.4.2.4 OGUC)", data.get("carga_ocupacion", "")),
        ("Acceso a carro bomba", data.get("acceso_carro_bomba", "NO")),
        ("Calle acceso carro bomba", data.get("calle_carro_bomba", "")),
        ("Aperturas hacia el exterior", data.get("aperturas_exterior", "Móviles")),
        ("N.º de unidades", data.get("num_unidades", "")),
        ("N.º de estacionamientos", data.get("num_estacionamientos", "")),
        ("Destino de la edificación", data.get("destino_edificacion", "")),
    ])
    add_spacer(doc)

    # Destinos por piso
    destinos = data.get("destinos_pisos", "")
    if destinos:
        p(doc, "Destinos o actividades principales por pisos:", bold=True)
        for line in destinos.strip().split("\n"):
            if line.strip():
                bullet(doc, line.strip())
    add_spacer(doc)

    # Tabla 3: Estructura
    add_table_2col(doc, [
        ("3. ESTRUCTURA Y MATERIAL PREDOMINANTE", ""),
        ("Estructura Principal (Art. 5.3.1 OGUC)", f"{data.get('clase_estructura', 'CLASE B')}\n{data.get('descripcion_estructura', '')}"),
        ("Tabiques interiores", data.get("tabiques_interiores", "")),
        ("Características de las fachadas exteriores", data.get("fachadas_exteriores", "")),
    ])
    add_spacer(doc)

    # Tabla 4: Alarmas
    add_table_2col(doc, [
        ("4. ALARMAS Y DETECCIÓN DE INCENDIO", ""),
        ("Bocinas de alarma de incendio", data.get("bocinas_alarma", "No")),
        ("Detectores de humo", data.get("detectores_humo", "No")),
        ("Detectores de calor", data.get("detectores_calor", "No aplica")),
        ("Palancas de alarma de incendio", data.get("palancas_alarma", "No")),
    ])
    add_spacer(doc)

    # Tabla 5: Comunicación
    add_table_2col(doc, [
        ("5. SISTEMAS DE COMUNICACIÓN", ""),
        ("Teléfonos", data.get("telefonos", "")),
        ("Citófonos", data.get("citofonos", "")),
        ("Sistema altavoces", data.get("altavoces", "No")),
        ("Otros", data.get("otros_comunicacion", "No")),
    ])
    add_spacer(doc)

    # Tabla 6: Incendios
    add_table_2col(doc, [
        ("6. SISTEMA DE COMBATE DE INCENDIOS", ""),
        ("Red seca", data.get("red_seca", "No")),
        ("Red húmeda", data.get("red_humeda", "")),
        ("Estanque de Almacenamiento de Agua", data.get("estanque_agua", "No")),
        ("Extintores Portátiles", data.get("extintores", "No")),
        ("Red Inerte de electricidad (Art. 4.3.11 OGUC)", data.get("red_inerte", "No")),
    ])
    add_spacer(doc)

    # Tabla 7: Vías de evacuación
    add_table_2col(doc, [
        ("7. VÍAS DE EVACUACIÓN", ""),
        ("Vías de Evacuación", data.get("vias_evacuacion", "")),
        ("Punto de Reunión", data.get("punto_reunion", "")),
        ("Zona de Seguridad", data.get("zona_seguridad", "")),
    ])
    add_spacer(doc)

    # Tabla 8: Electricidad
    add_table_2col(doc, [
        ("8. ELECTRICIDAD", ""),
        ("Tablero eléctrico general", data.get("tablero_general", "SI")),
        ("Tableros de unidades", data.get("tableros_unidades", "")),
        ("Grupo electrógeno", data.get("grupo_electrogeno", "No")),
        ("Iluminación de emergencia", data.get("iluminacion_emergencia", "")),
    ])
    add_spacer(doc)

    # Tabla 9: Combustible
    add_table_2col(doc, [
        ("9. COMBUSTIBLE", ""),
        ("Gas", data.get("gas", "No")),
        ("Medidores", data.get("medidores_gas", "No")),
    ])
    add_spacer(doc)

    # Tabla 10: Almacenamiento combustible
    add_table_2col(doc, [
        ("10. ALMACENAMIENTO DE COMBUSTIBLE", ""),
        ("Tanque de gas", data.get("tanque_gas", "No aplica")),
        ("Tanque de petróleo", data.get("tanque_petroleo", "No")),
    ])
    add_spacer(doc)

    # Tabla 11: Ventilación
    add_table_2col(doc, [
        ("11. SISTEMA CENTRALIZADO DE VENTILACIÓN", ""),
        ("Sistema centralizado", data.get("ventilacion_centralizada", "No")),
        ("Tablero comando", data.get("tablero_comando_vent", "No")),
        ("Toma de aire", data.get("toma_aire", "No")),
    ])
    add_spacer(doc)

    # Tabla 12: Ascensores
    add_table_2col(doc, [
        ("12. ASCENSORES", ""),
        ("Número de ascensores", data.get("num_ascensores", "")),
        ("Capacidad máxima de personas", data.get("capacidad_personas", "")),
        ("Capacidad máxima en kilos", data.get("capacidad_kilos", "")),
        ("Sistema del ascensor", data.get("sistema_ascensor", "Eléctrico")),
        ("Llave para Bomberos", data.get("llave_bomberos", "Conserjería")),
    ])
    add_spacer(doc)
    doc.add_page_break()


def _write_guia_practica(doc, data):
    h1(doc, "GUIA PRACTICA DE EMERGENCIA Y EVACUACIÓN")
    p(doc, "La presente guía práctica entrega a todos los ocupantes y usuarios del edificio las instrucciones precisas sobre cómo actuar de manera segura y eficiente ante una situación de emergencia.")


def _write_mercalli(doc):
    h1(doc, "ESQUEMA DE PERCEPCIÓN SÍSMICA SEGÚN ESCALA DE MERCALLI")
    rows = [
        ("Grado Mercalli", "Percepción", "Efectos observables"),
        ("I - Instrumental", "No se percibe.", "Detectado solo por sismógrafos."),
        ("II - Muy débil", "Percibido solo por personas en reposo.", "Objetos colgantes pueden oscilar."),
        ("III - Débil", "Percibido en interiores.", "Vibraciones similares al paso de vehículos."),
        ("IV - Moderado", "Sentido por muchas personas.", "Ventanas, puertas y platos vibran."),
        ("V - Algo fuerte", "Sentido por casi todos.", "Objetos pequeños se desplazan."),
        ("VI - Fuerte", "Sentido por todos.", "Caída de objetos, grietas menores en muros."),
        ("VII - Muy fuerte", "Personas corren al exterior.", "Daños moderados en construcciones mal diseñadas."),
        ("VIII - Destructivo", "Pánico generalizado.", "Daños severos en estructuras comunes."),
        ("IX - Ruinoso", "Difícil mantenerse en pie.", "Edificios se dañan seriamente o colapsan."),
        ("X - Desastroso", "Pérdida total del control.", "Colapso de muchas construcciones."),
        ("XI - Catastrófico", "Devastación general.", "Puentes destruidos, grietas en el suelo."),
        ("XII - Totalmente catastrófico", "Destrucción total.", "Cambios en el paisaje."),
    ]
    add_table_3col(doc, rows)
    add_spacer(doc)


def _write_anexo_telefonos(doc, data):
    h1(doc, "ANEXO N.º 1: NÚMEROS TELEFÓNICOS DE EMERGENCIA")
    nombre = data.get("nombre_edificio", "EDIFICIO")
    rows = [
        ("EDIFICIO", nombre),
        ("SEGURIDAD", ""),
        ("ADMINISTRACIÓN", ""),
        ("CONSERJERÍA", ""),
        ("", ""),
        ("EMERGENCIAS", ""),
        ("SAMU", "131"),
    ]
    if data.get("cesfam_nombre"):
        rows.append((data["cesfam_nombre"], data.get("cesfam_telefono", "")))
    if data.get("sapu_nombre"):
        rows.append((data["sapu_nombre"], data.get("sapu_telefono", "")))
    if data.get("hospital_nombre"):
        rows.append((data["hospital_nombre"], data.get("hospital_telefono", "")))
    if data.get("hospital_urgencia_nombre"):
        rows.append((data["hospital_urgencia_nombre"], data.get("hospital_urgencia_telefono", "")))

    rows.extend([
        ("", ""),
        ("BOMBEROS", ""),
        ("EMERGENCIAS", "132"),
    ])
    if data.get("bomberos_cuartel"):
        rows.append((data["bomberos_cuartel"], data.get("bomberos_telefono", "")))

    rows.extend([
        ("", ""),
        ("CARABINEROS", ""),
        ("EMERGENCIAS", "133"),
    ])
    if data.get("comisaria_nombre"):
        rows.append((data["comisaria_nombre"], data.get("comisaria_telefono", "")))
    if data.get("plan_cuadrante"):
        rows.append(("PLAN CUADRANTE", data["plan_cuadrante"]))
    if data.get("seguridad_ciudadana"):
        rows.append(("SEGURIDAD CIUDADANA", data["seguridad_ciudadana"]))

    rows.extend([
        ("", ""),
        ("POLICÍA DE INVESTIGACIONES", ""),
        ("EMERGENCIAS", "134"),
        ("CUARTEL GENERAL PDI", "(+56) 227080000"),
        ("", ""),
        ("MUTUALIDADES DE TRABAJADORES", ""),
        ("ACHS (emergencias)", "1404"),
        ("Hospital del Trabajador", "600 301 2222"),
        ("MUTUAL DE SEGURIDAD CCHC", "600 200 555"),
        ("IST", "800 204 000"),
        ("ISL", "600 586 9090"),
        ("", ""),
        ("ENEL", ""),
        ("EMERGENCIAS (CELULARES)", "(+56) 226960000"),
        ("EMERGENCIAS (FIJO)", "600 696 0000"),
        ("", ""),
        ("AGUAS ANDINAS", ""),
        ("EMERGENCIAS", "(+56) 227312400"),
        ("", ""),
        ("METROGAS", ""),
        ("EMERGENCIAS (FIJO)", "600 337 8000"),
        ("EMERGENCIAS (CELULARES)", "(+56) 223378000"),
        ("", ""),
        ("SERVICIOS DE EDIFICIO", ""),
        ("BOMBAS DE AGUA", data.get("empresa_bombas_agua", "")),
        ("GRUPO ELECTRÓGENO", data.get("empresa_electrogeno", "")),
        ("ASCENSORES", data.get("empresa_ascensores", "")),
        ("SISTEMA DE INCENDIOS", data.get("empresa_incendios", "")),
        ("EXTINTORES", data.get("empresa_extintores", "")),
    ])

    add_table_2col(doc, rows)
    add_spacer(doc)


def _write_anexo_registro(doc):
    h1(doc, "ANEXO N.º 2: REGISTRO DE DIFUSIÓN DE PLAN DE EMERGENCIA Y EVACUACIÓN")
    rows = [("NOMBRE", "DEPARTAMENTO", "RUT", "FIRMA")]
    for _ in range(25):
        rows.append(("", "", "", ""))
    add_table_4col(doc, rows)
    add_spacer(doc)


def _write_anexo_planos(doc):
    h1(doc, "ANEXO N.º 3: PLANOS DE EVACUACIÓN")
    p(doc, "(Insertar planos de evacuación del edificio aquí)")
    add_spacer(doc)


def generate_pee(data, output_path):
    """Genera el documento PEE completo y lo guarda en output_path."""
    doc = create_doc()

    # Portada
    _write_cover(doc, data)

    # Ficha Técnica
    _write_ficha_tecnica(doc, data)

    # Guía Práctica
    _write_guia_practica(doc, data)

    # Marco Legal
    write_marco_legal(doc, h1, p, bullet)

    # Capítulo 1: Objetivos
    write_cap1_objetivos(doc, h1, p, bullet)
    write_conceptos(doc, h1, bullet)

    # Capítulo 2: Organización
    write_cap2_organizacion(doc, h1, p, bullet)

    # Capítulo 3: Recursos Técnicos
    write_cap3_recursos(doc, h1, p, bullet)
    write_sistemas_edificio(doc, h1, p, bullet)

    # Capítulo 4: Medidas Preventivas
    write_cap4_preventivas(doc, h1, p, bullet)
    write_capacitacion(doc, h1, p, bullet)
    write_simulacros(doc, h1, p, bullet)

    # Capítulo 5: Procedimientos
    write_proc_incendio(doc, h1, p, bullet)
    write_proc_sismo(doc, h1, p, bullet)
    _write_mercalli(doc)
    write_proc_bomba(doc, h1, p, bullet)
    write_proc_asalto(doc, h1, p, bullet)
    write_proc_electrica(doc, h1, p, bullet)
    write_proc_agua(doc, h1, p, bullet)
    write_proc_gas(doc, h1, p, bullet)
    write_proc_inundacion(doc, h1, p, bullet)

    # Capítulo 6: Plan de Evacuación
    write_cap6_evacuacion(doc, h1, p, bullet, data)
    write_protocolos_evacuacion(doc, h1, p, bullet)
    write_recomendaciones(doc, h1, p, bullet)

    # Conclusiones
    write_conclusiones(doc, h1, p, bullet)

    # Capítulo 7: Recuperación
    write_cap7_recuperacion(doc, h1, p, bullet)

    # Anexos
    doc.add_page_break()
    _write_anexo_telefonos(doc, data)
    doc.add_page_break()
    _write_anexo_registro(doc)
    doc.add_page_break()
    _write_anexo_planos(doc)

    doc.save(output_path)
    return output_path
