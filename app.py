from flask import Flask, render_template, request, send_file
from docx_generator import generate_pee
import tempfile
import os

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/generar", methods=["POST"])
def generar():
    data = {
        # Identificación
        "nombre_edificio": request.form.get("nombre_edificio", ""),
        "direccion": request.form.get("direccion", ""),
        "entre_calle_1": request.form.get("entre_calle_1", ""),
        "entre_calle_2": request.form.get("entre_calle_2", ""),
        "acceso_edificio": request.form.get("acceso_edificio", ""),
        "permiso_municipal": request.form.get("permiso_municipal", "Pendiente"),
        "rol_avaluos": request.form.get("rol_avaluos", "Pendiente"),
        "comuna": request.form.get("comuna", ""),
        "coordenadas": request.form.get("coordenadas", ""),
        # Características
        "pisos_sobre": request.form.get("pisos_sobre", ""),
        "pisos_bajo": request.form.get("pisos_bajo", ""),
        "superficie": request.form.get("superficie", ""),
        "carga_ocupacion": request.form.get("carga_ocupacion", ""),
        "acceso_carro_bomba": request.form.get("acceso_carro_bomba", "NO"),
        "calle_carro_bomba": request.form.get("calle_carro_bomba", ""),
        "aperturas_exterior": request.form.get("aperturas_exterior", "Móviles"),
        "num_unidades": request.form.get("num_unidades", ""),
        "num_estacionamientos": request.form.get("num_estacionamientos", "No"),
        "destino_edificacion": request.form.get("destino_edificacion", ""),
        # Pisos y destinos
        "destinos_pisos": request.form.get("destinos_pisos", ""),
        # Estructura
        "clase_estructura": request.form.get("clase_estructura", ""),
        "descripcion_estructura": request.form.get("descripcion_estructura", ""),
        "tabiques_interiores": request.form.get("tabiques_interiores", ""),
        "fachadas_exteriores": request.form.get("fachadas_exteriores", ""),
        # Alarmas
        "bocinas_alarma": request.form.get("bocinas_alarma", "No"),
        "detectores_humo": request.form.get("detectores_humo", "No"),
        "detectores_calor": request.form.get("detectores_calor", "No aplica"),
        "palancas_alarma": request.form.get("palancas_alarma", "No"),
        # Comunicación
        "telefonos": request.form.get("telefonos", ""),
        "citofonos": request.form.get("citofonos", ""),
        "altavoces": request.form.get("altavoces", "No"),
        "otros_comunicacion": request.form.get("otros_comunicacion", "No"),
        # Incendios
        "red_seca": request.form.get("red_seca", "No"),
        "red_humeda": request.form.get("red_humeda", ""),
        "estanque_agua": request.form.get("estanque_agua", "No"),
        "extintores": request.form.get("extintores", "No"),
        "red_inerte": request.form.get("red_inerte", "No"),
        # Evacuación
        "vias_evacuacion": request.form.get("vias_evacuacion", ""),
        "punto_reunion": request.form.get("punto_reunion", ""),
        "zona_seguridad": request.form.get("zona_seguridad", ""),
        # Electricidad
        "tablero_general": request.form.get("tablero_general", "SI"),
        "tableros_unidades": request.form.get("tableros_unidades", ""),
        "grupo_electrogeno": request.form.get("grupo_electrogeno", "No"),
        "iluminacion_emergencia": request.form.get("iluminacion_emergencia", ""),
        # Gas
        "gas": request.form.get("gas", "No"),
        "medidores_gas": request.form.get("medidores_gas", "No"),
        "tanque_gas": request.form.get("tanque_gas", "No aplica"),
        "tanque_petroleo": request.form.get("tanque_petroleo", "No"),
        # Ventilación
        "ventilacion_centralizada": request.form.get("ventilacion_centralizada", "No"),
        "tablero_comando_vent": request.form.get("tablero_comando_vent", "No"),
        "toma_aire": request.form.get("toma_aire", "No"),
        # Ascensores
        "num_ascensores": request.form.get("num_ascensores", ""),
        "capacidad_personas": request.form.get("capacidad_personas", ""),
        "capacidad_kilos": request.form.get("capacidad_kilos", ""),
        "sistema_ascensor": request.form.get("sistema_ascensor", "Eléctrico"),
        "llave_bomberos": request.form.get("llave_bomberos", "Conserjería"),
        # Teléfonos emergencia locales
        "cesfam_nombre": request.form.get("cesfam_nombre", ""),
        "cesfam_telefono": request.form.get("cesfam_telefono", ""),
        "sapu_nombre": request.form.get("sapu_nombre", ""),
        "sapu_telefono": request.form.get("sapu_telefono", ""),
        "hospital_nombre": request.form.get("hospital_nombre", ""),
        "hospital_telefono": request.form.get("hospital_telefono", ""),
        "hospital_urgencia_nombre": request.form.get("hospital_urgencia_nombre", ""),
        "hospital_urgencia_telefono": request.form.get("hospital_urgencia_telefono", ""),
        "bomberos_cuartel": request.form.get("bomberos_cuartel", ""),
        "bomberos_telefono": request.form.get("bomberos_telefono", ""),
        "comisaria_nombre": request.form.get("comisaria_nombre", ""),
        "comisaria_telefono": request.form.get("comisaria_telefono", ""),
        "plan_cuadrante": request.form.get("plan_cuadrante", ""),
        "seguridad_ciudadana": request.form.get("seguridad_ciudadana", ""),
        # Servicios edificio
        "empresa_bombas_agua": request.form.get("empresa_bombas_agua", ""),
        "empresa_electrogeno": request.form.get("empresa_electrogeno", ""),
        "empresa_ascensores": request.form.get("empresa_ascensores", ""),
        "empresa_incendios": request.form.get("empresa_incendios", ""),
        "empresa_extintores": request.form.get("empresa_extintores", ""),
        # Realizado/Aprobado
        "realizado_por": request.form.get("realizado_por", ""),
        "aprobado_por": request.form.get("aprobado_por", ""),
        "fecha_actualizacion": request.form.get("fecha_actualizacion", ""),
    }

    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".docx")
    tmp.close()
    generate_pee(data, tmp.name)

    nombre_archivo = f"PEE - {data['nombre_edificio'] or 'Condominio'}.docx"
    return send_file(
        tmp.name,
        as_attachment=True,
        download_name=nombre_archivo,
        mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=5000)
