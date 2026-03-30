"""
Generador de PEE basado en plantilla.
Copia el documento plantilla y reemplaza los placeholders con los datos del formulario.
"""
import os
import shutil
from docx import Document


TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "plantilla_pee.docx")

# Mapeo: campo del formulario -> placeholder(s) en la plantilla
FIELD_MAP = {
    "nombre_edificio": ["{{DIRECCION_UPPER}}", "{{DIRECCION}}"],
    "direccion": ["{{DIRECCION_UPPER}}", "{{DIRECCION}}"],
    "coordenadas": ["{{COORDENADAS}}"],
    "entre_calle_1": ["{{ENTRE_CALLE_1}}"],
    "entre_calle_2": ["{{ENTRE_CALLE_2}}"],
    "acceso_edificio": ["{{ACCESO_EDIFICIO}}"],
    "comuna": ["{{COMUNA}}"],
    "permiso_municipal": ["{{PERMISO_MUNICIPAL}}"],
    "rol_avaluos": ["{{ROL_AVALUOS}}"],
    "realizado_por": ["{{REALIZADO_POR}}"],
    "aprobado_por": ["{{APROBADO_POR}}"],
    "fecha_actualizacion": ["{{FECHA_ACTUALIZACION}}"],
    "pisos_sobre": ["{{PISOS_SOBRE}}"],
    "pisos_bajo": ["{{PISOS_BAJO}}"],
    "superficie": ["{{SUPERFICIE}}"],
    "carga_ocupacion": ["{{CARGA_OCUPACION}}"],
    "acceso_carro_bomba": ["{{ACCESO_CARRO_BOMBA}}", "{{CARRO_BOMBA_SI_NO}}"],
    "aperturas_exterior": ["{{APERTURAS_EXTERIOR}}"],
    "num_unidades": ["{{NUM_UNIDADES}}"],
    "num_estacionamientos": ["{{NUM_ESTACIONAMIENTOS}}"],
    "destino_edificacion": ["{{DESTINO_EDIFICACION}}"],
    "destino_piso_sub": ["{{DESTINO_PISO_SUB}}"],
    "destino_piso_sub_desc": ["{{DESTINO_PISO_SUB_DESC}}"],
    "destino_piso_1": ["{{DESTINO_PISO_1}}"],
    "destino_piso_1_desc": ["{{DESTINO_PISO_1_DESC}}"],
    "destino_pisos_sup": ["{{DESTINO_PISOS_SUP}}"],
    "destino_pisos_sup_desc": ["{{DESTINO_PISOS_SUP_DESC}}"],
    "clase_estructura": ["{{CLASE_ESTRUCTURA}}"],
    "descripcion_estructura": ["{{DESCRIPCION_ESTRUCTURA}}"],
    "tabiques_interiores": ["{{TABIQUES_INTERIORES}}"],
    "fachadas_exteriores": ["{{FACHADAS_EXTERIORES}}"],
    "red_humeda": ["{{RED_HUMEDA}}"],
    "vias_evacuacion": ["{{VIAS_EVACUACION}}"],
    "punto_reunion": ["{{PUNTO_REUNION}}"],
    "zona_seguridad": ["{{ZONA_SEGURIDAD}}"],
    "tableros_unidades": ["{{TABLEROS_UNIDADES}}"],
    "iluminacion_emergencia": ["{{ILUMINACION_EMERGENCIA}}"],
    "num_ascensores": ["{{NUM_ASCENSORES}}"],
    "capacidad_personas": ["{{CAPACIDAD_PERSONAS}}"],
    "capacidad_kilos": ["{{CAPACIDAD_KILOS}}"],
    "sistema_ascensor": ["{{SISTEMA_ASCENSOR}}"],
    "llave_bomberos": ["{{LLAVE_BOMBEROS}}"],
    "cesfam_nombre": ["{{CESFAM_NOMBRE}}"],
    "cesfam_telefono": ["{{CESFAM_TELEFONO}}"],
    "sapu_nombre": ["{{SAPU_NOMBRE}}"],
    "sapu_telefono": ["{{SAPU_TELEFONO}}"],
    "hospital_nombre": ["{{HOSPITAL_NOMBRE}}"],
    "hospital_telefono": ["{{HOSPITAL_TELEFONO}}"],
    "hospital_urgencia_nombre": ["{{HOSPITAL_URGENCIA_NOMBRE}}"],
    "hospital_urgencia_telefono": ["{{HOSPITAL_URGENCIA_TELEFONO}}"],
    "bomberos_cuartel": ["{{BOMBEROS_CUARTEL}}"],
    "bomberos_telefono": ["{{BOMBEROS_TELEFONO}}"],
    "comisaria_nombre": ["{{COMISARIA_NOMBRE}}"],
    "comisaria_telefono": ["{{COMISARIA_TELEFONO}}"],
    "plan_cuadrante": ["{{PLAN_CUADRANTE}}"],
    "seguridad_ciudadana": ["{{SEGURIDAD_CIUDADANA}}"],
}


def _build_replacements(data):
    """Construye el diccionario de reemplazos placeholder -> valor."""
    replacements = {}
    for field, placeholders in FIELD_MAP.items():
        value = data.get(field, "")
        for ph in placeholders:
            # Para DIRECCION_UPPER usar mayúsculas
            if ph == "{{DIRECCION_UPPER}}":
                val = data.get("direccion", data.get("nombre_edificio", "")).upper()
                replacements[ph] = val
            # Para CARRO_BOMBA_SI_NO formatear como SI/NO
            elif ph == "{{CARRO_BOMBA_SI_NO}}":
                cb = data.get("acceso_carro_bomba", "NO")
                replacements[ph] = f"SI" if cb == "SI" else f"NO"
            else:
                replacements[ph] = value
    return replacements


def _replace_in_runs(runs, replacements):
    """Reemplaza placeholders en los runs de un párrafo."""
    for run in runs:
        for placeholder, value in replacements.items():
            if placeholder in run.text:
                run.text = run.text.replace(placeholder, value)


def generate_pee(data, output_path):
    """Genera el documento PEE copiando la plantilla y reemplazando los datos."""
    # Copiar plantilla al destino
    shutil.copy2(TEMPLATE_PATH, output_path)

    # Abrir la copia y reemplazar
    doc = Document(output_path)
    replacements = _build_replacements(data)

    # Reemplazar en párrafos del cuerpo
    for paragraph in doc.paragraphs:
        _replace_in_runs(paragraph.runs, replacements)

    # Reemplazar en tablas
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    _replace_in_runs(paragraph.runs, replacements)

    # Reemplazar en headers y footers
    for section in doc.sections:
        for header in [section.header, section.first_page_header]:
            if header:
                for paragraph in header.paragraphs:
                    _replace_in_runs(paragraph.runs, replacements)
        for footer in [section.footer, section.first_page_footer]:
            if footer:
                for paragraph in footer.paragraphs:
                    _replace_in_runs(paragraph.runs, replacements)

    doc.save(output_path)
    return output_path
