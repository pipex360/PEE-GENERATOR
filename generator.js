const {
  Document, Packer, Paragraph, TextRun, HeadingLevel,
  AlignmentType, TabStopPosition, TabStopType,
  Table, TableRow, TableCell, WidthType, BorderStyle,
  PageBreak
} = require('docx');

function title(text) {
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 200 },
    children: [new TextRun({ text, bold: true, size: 36, font: 'Calibri' })],
  });
}

function heading(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_1,
    spacing: { before: 400, after: 200 },
    children: [new TextRun({ text: text.toUpperCase(), bold: true, size: 28, font: 'Calibri' })],
  });
}

function heading2(text) {
  return new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 300, after: 150 },
    children: [new TextRun({ text, bold: true, size: 24, font: 'Calibri' })],
  });
}

function para(text) {
  return new Paragraph({
    spacing: { after: 120 },
    children: [new TextRun({ text, size: 22, font: 'Calibri' })],
  });
}

function boldPara(label, value) {
  return new Paragraph({
    spacing: { after: 100 },
    children: [
      new TextRun({ text: `${label}: `, bold: true, size: 22, font: 'Calibri' }),
      new TextRun({ text: value || 'N/A', size: 22, font: 'Calibri' }),
    ],
  });
}

function bullet(text) {
  return new Paragraph({
    bullet: { level: 0 },
    spacing: { after: 80 },
    children: [new TextRun({ text, size: 22, font: 'Calibri' })],
  });
}

function pageBreak() {
  return new Paragraph({ children: [new PageBreak()] });
}

function emptyLine() {
  return new Paragraph({ spacing: { after: 100 }, children: [] });
}

async function generatePEE(data) {
  const d = {
    nombreEdificio: data.nombreEdificio || 'Condominio',
    direccion: data.direccion || '',
    coordenadas: data.coordenadas || '',
    pisos: data.pisos || '',
    subterraneos: data.subterraneos || '0',
    departamentos: data.departamentos || '',
    estacionamientos: data.estacionamientos || '',
    bodegas: data.bodegas || '',
    anoConstruccion: data.anoConstruccion || '',
    administrador: data.administrador || '',
    telefonoAdmin: data.telefonoAdmin || '',
    emailAdmin: data.emailAdmin || '',
    tipoEstructura: data.tipoEstructura || 'Hormigón armado',
    redHumeda: data.redHumeda !== false,
    redSeca: data.redSeca !== false,
    extintores: data.extintores !== false,
    lucesEmergencia: data.lucesEmergencia !== false,
    citofonia: data.citofonia !== false,
    ascensores: data.ascensores || '0',
    zonaSeguridad: data.zonaSeguridad || '',
    rutaEvacuacion: data.rutaEvacuacion || 'Escaleras principales hacia hall de acceso y zona de seguridad exterior',
    observaciones: data.observaciones || '',
  };

  const sections = [];

  // --- PORTADA ---
  sections.push(
    emptyLine(), emptyLine(), emptyLine(), emptyLine(),
    title('PLAN DE EMERGENCIA Y EVACUACIÓN'),
    emptyLine(),
    title(d.nombreEdificio.toUpperCase()),
    emptyLine(),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: d.direccion, size: 28, font: 'Calibri' })],
    }),
    emptyLine(), emptyLine(),
    new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [new TextRun({ text: `Documento generado automáticamente`, size: 20, font: 'Calibri', italics: true })],
    }),
    pageBreak(),
  );

  // --- FICHA TÉCNICA ---
  sections.push(
    heading('FICHA TÉCNICA DEL EDIFICIO'),
    para('La presente ficha técnica consolida los datos esenciales del inmueble, abarcando sus especificaciones constructivas, elementos estructurales y los equipos de seguridad disponibles para la respuesta ante emergencias.'),
    emptyLine(),
    boldPara('Nombre del edificio', d.nombreEdificio),
    boldPara('Dirección', d.direccion),
    boldPara('Coordenadas Google Maps', d.coordenadas),
    boldPara('Número de pisos', d.pisos),
    boldPara('Subterráneos', d.subterraneos),
    boldPara('Departamentos / Unidades', d.departamentos),
    boldPara('Estacionamientos', d.estacionamientos),
    boldPara('Bodegas', d.bodegas),
    boldPara('Año de construcción', d.anoConstruccion),
    boldPara('Tipo de estructura', d.tipoEstructura),
    boldPara('Ascensores', d.ascensores),
    emptyLine(),
    heading2('Datos del Administrador'),
    boldPara('Nombre', d.administrador),
    boldPara('Teléfono', d.telefonoAdmin),
    boldPara('Email', d.emailAdmin),
    pageBreak(),
  );

  // --- GUÍA PRÁCTICA ---
  sections.push(
    heading('GUÍA PRÁCTICA DE EMERGENCIA Y EVACUACIÓN'),
    para('La presente guía práctica entrega a todos los ocupantes y usuarios del edificio las instrucciones precisas sobre cómo actuar de manera segura y eficiente ante cualquier tipo de emergencia que pueda presentarse en las instalaciones.'),
    pageBreak(),
  );

  // --- MARCO LEGAL ---
  sections.push(
    heading('MARCO LEGAL'),
    para('El marco legal que rige la elaboración de un Plan de Emergencia y Evacuación se basa en las siguientes normativas:'),
    bullet('Ley N° 21.442 sobre Copropiedad Inmobiliaria: En su Artículo 40°, esta ley establece la obligatoriedad para todo condominio de contar con un plan de emergencia y evacuación actualizado.'),
    bullet('Directrices del Servicio Nacional de Prevención y Respuesta ante Desastres (SENAPRED): El Plan se alinea con las guías de la autoridad técnica en gestión de riesgos y emergencias del país.'),
    bullet('D.S. N° 594 del Ministerio de Salud: Reglamento sobre condiciones sanitarias y ambientales básicas en los lugares de trabajo, que establece requisitos de seguridad.'),
    bullet('Ordenanza General de Urbanismo y Construcciones (OGUC): Normativa que regula las condiciones de seguridad constructiva de los edificios.'),
    pageBreak(),
  );

  // --- CAPÍTULO 1: OBJETIVOS ---
  sections.push(
    heading('CAPÍTULO N°1: OBJETIVOS Y CONCEPTOS'),
    heading2('Objetivo General'),
    para(`Establecer un marco de actuación organizado y eficaz que permita a la comunidad de ${d.nombreEdificio} responder de manera segura ante una emergencia. El fin principal es salvaguardar la vida e integridad física de todas las personas.`),
    heading2('Objetivos Específicos'),
    bullet('Identificar y Evaluar Riesgos: Analizar y definir las principales amenazas de origen natural, técnico o social que puedan afectar a la comunidad.'),
    bullet('Definir Procedimientos de Evacuación: Establecer y comunicar claramente las vías de evacuación, las zonas de seguridad y los puntos de encuentro.'),
    bullet('Asignar Roles y Responsabilidades: Organizar y designar formalmente a los responsables de liderar y coordinar las acciones durante una emergencia.'),
    bullet('Fomentar una Cultura Preventiva: Capacitar e informar permanentemente a los residentes y usuarios del edificio sobre los procedimientos de este plan.'),
    bullet('Coordinar con Entidades Externas: Establecer canales de comunicación y coordinación con Bomberos, Carabineros, SAMU y otras entidades de emergencia.'),
    pageBreak(),
  );

  // --- CONCEPTOS ---
  sections.push(
    heading('CONCEPTOS'),
    bullet('Prevención: Conjunto de acciones cuyo objeto es impedir o evitar que fenómenos naturales o provocados por la actividad humana causen emergencias o desastres.'),
    bullet('Emergencia: Alteraciones en las personas, los bienes, los servicios y el medio ambiente, causadas por un fenómeno natural o generado por la actividad humana.'),
    bullet('Evacuación: Abandono masivo de un local o edificio frente a una emergencia. El entrenamiento previo permite hacerlo rápida y ordenadamente.'),
    bullet('Evacuación Parcial: Se realizará cuando la emergencia solo requiera la evacuación del nivel afectado y los niveles inmediatamente superiores e inferiores.'),
    bullet('Evacuación Total: Se llevará a cabo cuando la emergencia sea de gran envergadura y suponga un riesgo importante para la integridad del edificio.'),
    bullet('Plan de Emergencia: Conjunto de actividades y procedimientos destinados a controlar una situación de emergencia en el menor tiempo posible.'),
    bullet('Plan de Evacuación: Conjunto de actividades y procedimientos tendientes a conservar la vida y la integridad física de las personas.'),
    bullet('Ejercicio de Simulación: Actuación en grupo en un espacio cerrado, en la que se representan varios roles para la toma de decisiones ante una emergencia simulada.'),
    bullet('Ejercicio de Simulacro: Ejercicio práctico en terreno a gran escala, en el cual los participantes se acercan lo más posible a un escenario real de emergencia.'),
    pageBreak(),
  );

  // --- CAPÍTULO 2: ORGANIZACIÓN ---
  sections.push(
    heading('CAPÍTULO N°2: ORGANIZACIÓN DE LA EMERGENCIA'),
    heading2('Organigrama'),
    para('La estructura de mando durante una emergencia se organiza de la siguiente manera:'),
    bullet('Director(a) de la Emergencia → Jefe de Emergencia → Apoyo Interno (Líderes + Conserjes) → Apoyo Externo (Bomberos, Carabineros, SAMU)'),
    emptyLine(),
    heading2('Descripción de Roles y Funciones'),
    emptyLine(),
    para('Director(a) de la Emergencia:'),
    bullet(`Quién: Es la máxima autoridad durante la crisis. Este rol lo asume el Administrador(a) del condominio (${d.administrador || 'por designar'}). En su ausencia, el presidente del Comité de Administración.`),
    bullet('Función: No participa directamente en las acciones de control, sino que dirige desde un punto estratégico. Es el único interlocutor oficial ante los medios y autoridades.'),
    emptyLine(),
    para('Jefe de Emergencia:'),
    bullet('Quién: Es el comandante en terreno. Este rol es ideal para el Mayordomo o el conserje con más experiencia, por su conocimiento práctico del edificio.'),
    bullet('Función: Dirige a los equipos de apoyo interno. Supervisa que los procedimientos del plan se ejecuten correctamente.'),
    emptyLine(),
    para('Apoyo Interno:'),
    bullet('Líderes de Evacuación (Líderes de Piso): Son residentes voluntarios y capacitados, idealmente uno por cada piso o sector. Su misión es guiar la evacuación ordenada de su zona.'),
    bullet('Personal del Condominio (Conserjes): Son el principal apoyo operativo. Sus tareas incluyen: dar la alarma, llamar a los servicios de emergencia, controlar accesos y apoyar la evacuación.'),
    emptyLine(),
    para('Apoyo Externo:'),
    para('Son las instituciones y servicios profesionales que se harán cargo de controlar la emergencia: Bomberos, Carabineros, SAMU, y otros organismos especializados.'),
    pageBreak(),
  );

  // --- CAPÍTULO 3: RECURSOS TÉCNICOS ---
  sections.push(
    heading('CAPÍTULO N°3: RECURSOS TÉCNICOS'),
  );
  if (d.lucesEmergencia) {
    sections.push(
      heading2('Luces de Emergencia'),
      para('Para garantizar una evacuación segura, el edificio está equipado con un sistema de alumbrado de emergencia autónomo en pasillos, escaleras y vías de evacuación. Estas luces se activan automáticamente ante un corte del suministro eléctrico principal.'),
    );
  }
  sections.push(
    heading2('Sistema de Combate de Incendios'),
    para('El sistema de combate de incendios del edificio se compone de los siguientes elementos:'),
  );
  if (d.redHumeda) {
    sections.push(
      emptyLine(),
      para('Red Húmeda:'),
      bullet('Propósito y Uso: La Red Húmeda es el sistema de primera intervención para el control de fuegos incipientes (amagos). Está diseñada para ser utilizada por cualquier persona capacitada.'),
      bullet('Ubicación y Componentes: Los gabinetes de la Red Húmeda se encuentran en los pasillos de cada piso. Cada uno está equipado con una manguera semirrígida y un pitón.'),
      bullet('Funcionamiento: El sistema se mantiene siempre presurizado y es abastecido por la bomba de incendios y los estanques de reserva de agua del edificio.'),
      para('Instrucciones de Uso Básico:'),
      bullet('Abra el gabinete.'),
      bullet('Extienda completamente la manguera hacia el lugar del amago.'),
      bullet('Una vez extendida, abra la llave de paso para permitir el flujo de agua.'),
      bullet('Sujete firmemente el pitón y dirija el chorro a la base del fuego.'),
    );
  }
  if (d.redSeca) {
    sections.push(
      emptyLine(),
      para('Red Seca:'),
      bullet('La Red Seca es un sistema de uso exclusivo de Bomberos, compuesto por una red de tuberías vacías que recorren verticalmente el edificio.'),
      bullet('Su conexión se encuentra en la fachada exterior del edificio, debidamente señalizada para que el Cuerpo de Bomberos la identifique y conecte su carro bomba.'),
    );
  }
  if (d.extintores) {
    sections.push(
      emptyLine(),
      heading2('Extintores Portátiles'),
      para('El edificio está equipado con extintores portátiles para una primera respuesta ante un amago de incendio, ubicados en cada piso y áreas comunes.'),
      para('Tipos disponibles:'),
      bullet('Polvo Químico Seco (PQS): Para fuegos de Clase A, B y C (materiales comunes, líquidos inflamables y equipos eléctricos).'),
      bullet('Dióxido de Carbono (CO2): Ubicados cerca de salas eléctricas y tableros, para uso especializado en fuegos de origen eléctrico.'),
      para('Instrucciones de Uso Básico:'),
      bullet('Retire el extintor de su soporte y quite el pasador de seguridad.'),
      bullet('Ubíquese a una distancia segura y apunte la boquilla hacia la base del fuego.'),
      bullet('Apriete la manilla superior para descargar el agente extintor.'),
      bullet('Mueva la boquilla de lado a lado (en forma de abanico) hasta apagar las llamas.'),
    );
  }
  sections.push(pageBreak());

  // --- CAPÍTULO 4: SISTEMA DEL EDIFICIO ---
  sections.push(
    heading('CAPÍTULO N°4: SISTEMA DEL EDIFICIO'),
  );
  if (d.citofonia) {
    sections.push(
      heading2('Citofonía'),
      para('El sistema de citofonía del edificio proporciona una comunicación directa y punto a punto entre cada departamento y la conserjería. Es una herramienta clave durante emergencias para transmitir instrucciones.'),
    );
  }
  if (parseInt(d.ascensores) > 0) {
    sections.push(
      heading2('Ascensores'),
      para(`El edificio cuenta con ${d.ascensores} ascensor(es). IMPORTANTE: Durante una emergencia, los ascensores NO deben ser utilizados por los residentes. Quedarán bloqueados para uso exclusivo de Bomberos.`),
    );
  }
  sections.push(pageBreak());

  // --- CAPÍTULO 5: TIPOS DE EVACUACIÓN ---
  sections.push(
    heading('CAPÍTULO N°5: TIPOS DE EVACUACIÓN'),
    heading2('Evacuación Parcial'),
    para('Se ordena cuando la emergencia es detectada a tiempo, está contenida y no representa un riesgo generalizado para todo el edificio. Por ejemplo:'),
    bullet('Focos de incendio menores y controlados que solo afectan un área específica.'),
    bullet('Fugas de agua o inundaciones localizadas en un piso o sector.'),
    bullet('Conflictos o asaltos que ocurren en un área común determinada.'),
    emptyLine(),
    heading2('Evacuación Total'),
    para('Implica la desocupación completa y ordenada de todo el edificio. Se ordena cuando la emergencia es de gran envergadura:'),
    bullet('Incendios declarados, con llamas violentas o gran cantidad de humo.'),
    bullet('Amenaza de bomba o presencia de un artefacto explosivo confirmado.'),
    bullet('Fugas de gas generalizadas o no controladas.'),
    bullet('Daños estructurales visibles o riesgo de colapso después de un terremoto.'),
    bullet('Orden explícita de Bomberos o de la autoridad a cargo.'),
    pageBreak(),
  );

  // --- VÍAS Y ZONAS ---
  sections.push(
    heading('VÍAS PRINCIPALES DE EVACUACIÓN'),
    para('Esta es la ruta de evacuación estándar que deben seguir todos los residentes:'),
    bullet('Salga de su departamento y diríjase a la puerta de acceso a la escalera señalizada como "SALIDA DE EMERGENCIA".'),
    bullet('Ingrese a la caja de escaleras (Zona Vertical de Seguridad).'),
    bullet('Descienda en calma y en orden, utilizando siempre el pasamanos.'),
    bullet('Continúe bajando hasta llegar al primer piso, saliendo del edificio a través del hall principal.'),
    bullet('Una vez fuera, diríjase de inmediato a la Zona de Seguridad exterior designada.'),
    emptyLine(),
    para('⚠ Consideración Especial para Sismos de Gran Magnitud:'),
    bullet('El vestíbulo principal NO debe ser utilizado como punto de reunión temporal.'),
    bullet('Si la salida por el vestíbulo no es segura, se indicará el uso de una ruta alternativa.'),
    emptyLine(),
    heading2('Zona de Seguridad'),
    para(d.zonaSeguridad || 'Se definirá como Zona de Seguridad Principal el área exterior del edificio, en un espacio abierto a distancia prudente de la fachada.'),
    pageBreak(),
  );

  // --- CAPÍTULO 6: PROTOCOLOS ---
  sections.push(
    heading('CAPÍTULO N°6: PROTOCOLOS DE EVACUACIÓN'),
    heading2('El Proceso de Evacuación'),
    bullet('Liderazgo de la Emergencia: El Administrador o el Jefe de Emergencia designado dirigirá las operaciones desde un puesto de mando.'),
    bullet('Evacuación Escalonada: Para evitar la saturación de las escaleras, la evacuación se realizará de forma ordenada y por etapas.'),
    emptyLine(),
    heading2('Instrucciones para Todos los Residentes'),
    bullet('Mantenga la Calma y Siga las Instrucciones del Líder de Evacuación de su piso.'),
    bullet('NO UTILICE LOS ASCENSORES: Use siempre las escaleras.'),
    bullet('Diríjase a la Vía de Evacuación Señalizada.'),
    bullet('Descienda en Orden: Baje en fila utilizando el pasamanos. Camine rápido pero no corra.'),
    bullet('Ayude a Quienes lo Necesiten: niños, adultos mayores o personas con movilidad reducida.'),
    bullet('No se Devuelva: Por ningún motivo regrese a buscar objetos personales.'),
    bullet('Vaya a la Zona de Seguridad y permanezca allí.'),
    emptyLine(),
    heading2('Responsabilidades de los Líderes de Evacuación'),
    para('Antes de Evacuar el Piso:'),
    bullet('Verificar que no quede nadie: revisión completa del piso, incluyendo baños y bodegas.'),
    bullet('Gestionar a las visitas: asegurarse de que evacúen junto a sus anfitriones.'),
    bullet('Revisar la ruta: comprobar que las salidas estén despejadas.'),
    para('Durante el Desplazamiento:'),
    bullet('Guiar al grupo manteniéndolo unido y compacto hasta la Zona de Seguridad.'),
    bullet('Comunicar anomalías al Jefe de Emergencia.'),
    para('En la Zona de Seguridad:'),
    bullet('Realizar un conteo de las personas de su piso.'),
    bullet('Reportar de inmediato si falta alguna persona.'),
    pageBreak(),
  );

  // --- RECOMENDACIONES ---
  sections.push(
    heading('RECOMENDACIONES GENERALES'),
    bullet('Mantenga la Calma: El pánico es el mayor riesgo. Confíe en el plan y en los líderes de piso.'),
    bullet('No Corra, Camine Rápido: Desplácese de forma ágil pero segura.'),
    bullet('¡No Regrese por Ningún Motivo! No vuelva a buscar objetos personales.'),
    bullet('Si Hay Humo, Agáchese: El aire más limpio se encuentra cerca del suelo.'),
    bullet('Siga Siempre las Instrucciones de los líderes de evacuación.'),
    bullet('Circule por su Derecha en las Escaleras y deje el lado izquierdo libre para emergencias.'),
    bullet('Facilite su Desplazamiento: Si usa zapatos con taco alto, quíteselos.'),
    bullet('Diríjase a la Zona de Seguridad y permanezca allí hasta recibir nuevas instrucciones.'),
    pageBreak(),
  );

  // --- CAPÍTULO 7: RECUPERACIÓN ---
  sections.push(
    heading('CAPÍTULO N°7: RECUPERACIÓN'),
    para('Una vez que la emergencia ha sido controlada, comienza la fase de recuperación:'),
    emptyLine(),
    heading2('Paso 1: Control y Aseguramiento del Edificio'),
    para('Asegurar que no existen peligros residuales. El personal de emergencia o el Jefe de Emergencia verificará que el edificio es seguro.'),
    emptyLine(),
    heading2('Paso 2: Inspección Técnica de Seguridad'),
    para('Antes de autorizar el reingreso, se revisará:'),
    bullet('Sistemas eléctricos, de agua potable y de gas.'),
    bullet('Estructura general del edificio (especialmente después de un sismo).'),
    bullet('Sistemas de ascensores y bombas de agua.'),
    bullet('Operatividad de los sistemas de seguridad y comunicaciones.'),
    emptyLine(),
    heading2('Paso 3: Autorización y Retorno Seguro'),
    bullet('El reingreso solo se permitirá cuando las autoridades certifiquen que es seguro.'),
    bullet('El retorno se realizará de forma ordenada con apoyo de los Líderes de Evacuación.'),
    emptyLine(),
    heading2('Paso 4: Evaluación y Mejora del Plan'),
    para('Después de cada emergencia o simulacro, se reunirá el equipo para analizar el manejo de la situación e identificar mejoras.'),
    emptyLine(),
    heading2('Paso 5: Activación de Seguros y Reparaciones'),
    para('La Administración se encargará de la evaluación de daños materiales y la activación de los seguros correspondientes.'),
    pageBreak(),
  );

  // --- CONCLUSIONES ---
  sections.push(
    heading('CONCLUSIONES'),
    bullet('El Conocimiento Individual es la Base de la Prevención: Cada ocupante del edificio tiene la responsabilidad de conocer los equipos de seguridad, vías de evacuación y zonas de seguridad.'),
    bullet('La Cooperación Colectiva es la Clave del Éxito: El resultado de una evacuación depende de la capacidad de todos para seguir las instrucciones de manera calmada y ordenada.'),
    bullet('El Liderazgo Efectivo Salva Vidas: Los Líderes de Evacuación son el pilar de la operación en terreno.'),
    bullet('La Mejora Continua Fortalece Nuestra Seguridad: Este plan es un documento vivo que debe ser repasado y practicado constantemente.'),
    pageBreak(),
  );

  // --- ANEXOS ---
  sections.push(
    heading('ANEXO N°1: NÚMEROS TELEFÓNICOS DE EMERGENCIA'),
    emptyLine(),
    boldPara('Bomberos', '132'),
    boldPara('Carabineros', '133'),
    boldPara('Ambulancia / SAMU', '131'),
    boldPara('PDI', '134'),
    boldPara('Emergencias General', '113'),
    boldPara('Administración del Edificio', d.telefonoAdmin || 'Por definir'),
    emptyLine(),
    heading('ANEXO N°2: REGISTRO DE DIFUSIÓN DEL PLAN'),
    para('Se debe mantener un registro firmado de la difusión de este plan a todos los residentes y personal del condominio.'),
    emptyLine(),
    heading('ANEXO N°3: PLANOS DE EVACUACIÓN'),
    para('Se adjuntarán los planos de evacuación de cada piso del edificio, indicando: vías de evacuación, ubicación de extintores, red húmeda, alarmas y zonas de seguridad.'),
  );

  if (d.observaciones) {
    sections.push(
      emptyLine(),
      heading('OBSERVACIONES ADICIONALES'),
      para(d.observaciones),
    );
  }

  const doc = new Document({
    sections: [{
      properties: {},
      children: sections,
    }],
  });

  return await Packer.toBuffer(doc);
}

module.exports = { generatePEE };
