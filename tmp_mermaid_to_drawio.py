import re
import os
import uuid
import xml.etree.ElementTree as ET

input_path = r"base de datos/ER-SGSPCSI-legible-por-modulos.mmd"
output_path = r"base de datos/ER-SGSPCSI-legible-por-modulos.drawio"

with open(input_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

entity_re = re.compile(r"^\s*([A-Z0-9_]+)\s*\{\s*$")
relation_re = re.compile(r"^\s*([A-Z0-9_]+)\s+([|o{}\-]+)\s+([A-Z0-9_]+)\s*:\s*(.+?)\s*$")

entities = []
seen_entities = set()
relations = []

for line in lines:
    em = entity_re.match(line)
    if em:
        name = em.group(1)
        if name not in seen_entities:
            seen_entities.add(name)
            entities.append(name)
        continue

    rm = relation_re.match(line)
    if rm and "--" in rm.group(2):
        src = rm.group(1)
        dst = rm.group(3)
        label = rm.group(4).strip()
        relations.append((src, dst, label))

security_structure = {
    "ROL", "USUARIO", "USUARIO_ROL", "USUARIO_CREDENCIAL", "MENU_OPCION", "ROL_MENU_OPCION",
    "AREA", "USUARIO_AREA", "SISTEMA", "AREA_SISTEMA", "SISTEMA_DESARROLLADOR"
}
solicitudes = {
    "TIPO_SOLICITUD", "PRIORIDAD_SOLICITUD", "ESTADO_SOLICITUD", "SOLICITUD", "SOLICITUD_DESARROLLADOR",
    "SOLICITUD_HISTORIAL_ESTADO", "SOLICITUD_APROBACION", "SOLICITUD_COMENTARIO", "SOLICITUD_ADJUNTO",
    "NOTIFICACION", "TIPO_MODIFICACION", "SOLICITUD_MODIFICACION", "SOLICITUD_REQUERIMIENTO_TECNICO"
}
desarrollo_proyectos = {
    "TAREA_DESARROLLO", "TAREA_DESARROLLO_ASIGNACION", "ACTIVIDAD_RECIENTE", "PROYECTO", "PROYECTO_SOLICITUD",
    "PROYECTO_MIEMBRO", "DOCUMENTO_PROYECTO", "EVENTO_CALENDARIO", "EVENTO_PARTICIPANTE"
}

x_by_col = {0: 60, 1: 430, 2: 800}
y_counters = {0: 40, 1: 40, 2: 40}
node_w = 280
node_h = 56
v_gap = 26

positions = {}
for name in entities:
    if name in security_structure:
        col = 0
    elif name in solicitudes:
        col = 1
    else:
        col = 2 if name in desarrollo_proyectos else 1
    x = x_by_col[col]
    y = y_counters[col]
    y_counters[col] += node_h + v_gap
    positions[name] = (x, y)

mxfile = ET.Element("mxfile", {
    "host": "app.diagrams.net",
    "modified": "2026-01-01T00:00:00.000Z",
    "agent": "python-script",
    "version": "24.7.17",
    "type": "device"
})

diagram = ET.SubElement(mxfile, "diagram", {
    "id": str(uuid.uuid4())[:12],
    "name": "ER-SGSPCSI"
})

model = ET.SubElement(diagram, "mxGraphModel", {
    "dx": "1600", "dy": "1200", "grid": "1", "gridSize": "10", "guides": "1", "tooltips": "1",
    "connect": "1", "arrows": "1", "fold": "1", "page": "1", "pageScale": "1", "pageWidth": "2200",
    "pageHeight": "1600", "math": "0", "shadow": "0"
})
root = ET.SubElement(model, "root")
ET.SubElement(root, "mxCell", {"id": "0"})
ET.SubElement(root, "mxCell", {"id": "1", "parent": "0"})

node_style = (
    "rounded=0;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=#1f2937;"
    "fontColor=#111827;fontStyle=1;align=center;verticalAlign=middle;"
)
edge_style = (
    "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;"
    "strokeColor=#1f2937;fontColor=#111827;endArrow=block;endFill=1;"
)

id_map = {}
next_id = 2
for name in entities:
    cid = str(next_id)
    next_id += 1
    id_map[name] = cid
    cell = ET.SubElement(root, "mxCell", {
        "id": cid,
        "value": name,
        "style": node_style,
        "vertex": "1",
        "parent": "1"
    })
    x, y = positions[name]
    ET.SubElement(cell, "mxGeometry", {
        "x": str(x), "y": str(y), "width": str(node_w), "height": str(node_h), "as": "geometry"
    })

created_rel = 0
for src, dst, label in relations:
    if src not in id_map or dst not in id_map:
        continue
    eid = str(next_id)
    next_id += 1
    edge = ET.SubElement(root, "mxCell", {
        "id": eid,
        "value": label,
        "style": edge_style,
        "edge": "1",
        "parent": "1",
        "source": id_map[src],
        "target": id_map[dst]
    })
    ET.SubElement(edge, "mxGeometry", {"relative": "1", "as": "geometry"})
    created_rel += 1

ET.indent(mxfile, space="  ")
xml_text = ET.tostring(mxfile, encoding="utf-8", xml_declaration=True)
with open(output_path, "wb") as f:
    f.write(xml_text)

exists = os.path.exists(output_path)
print(f"Nodos creados: {len(entities)}")
print(f"Relaciones creadas: {created_rel}")
print(f"Archivo generado: {output_path}")
print(f"Existe archivo: {exists}")
