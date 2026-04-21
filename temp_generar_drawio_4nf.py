import math
import re
from pathlib import Path
import xml.etree.ElementTree as ET

base = Path(r"base de datos")
md_path = base / "17_diccionario_normalizado_4NF.md"
mmd_path = base / "ER-SGSPCSI-legible-por-modulos.mmd"
out_path = base / "10_diagrama_tablas_contenedor_lista_completo_4NF.drawio"

md_text = md_path.read_text(encoding="utf-8")
mmd_text = mmd_path.read_text(encoding="utf-8")

section_pattern = re.compile(r"^##\s+Tabla:\s*(.+?)\s*$", re.MULTILINE)
sections = list(section_pattern.finditer(md_text))

tables = []
for i, m in enumerate(sections):
    table_name = m.group(1).strip()
    start = m.end()
    end = sections[i + 1].start() if i + 1 < len(sections) else len(md_text)
    block = md_text[start:end]

    lines = block.splitlines()
    header_idx = None
    for idx, line in enumerate(lines):
        if line.strip().startswith("| Columna"):
            header_idx = idx
            break
    if header_idx is None:
        continue

    attrs = []
    for line in lines[header_idx + 2:]:
        s = line.strip()
        if not s.startswith("|"):
            if attrs:
                break
            continue
        parts = [p.strip() for p in s.strip("|").split("|")]
        if len(parts) < 7:
            continue
        col, typ, nul, default, key = parts[0], parts[1], parts[2], parts[3], parts[4]
        key_null = (f"{key} {nul}").strip() if key != "-" else nul
        attrs.append({
            "col": col,
            "typ": typ,
            "nul": nul,
            "default": default,
            "key": key,
            "key_null": key_null.strip(),
        })
    tables.append({"name": table_name, "attrs": attrs})

name_to_table = {t["name"].lower(): t for t in tables}

def norm_table_name(token: str) -> str:
    return token.strip().lower()

rel_pattern = re.compile(r"^\s*([A-Z0-9_]+)\s+([|o}{\-]+)\s+([A-Z0-9_]+)\s*:\s*([^\n]+?)\s*$")
relations = []
seen = set()
for line in mmd_text.splitlines():
    m = rel_pattern.match(line)
    if not m:
        continue
    left, card, right, label = m.group(1), m.group(2), m.group(3), m.group(4).strip()
    l = norm_table_name(left)
    r = norm_table_name(right)
    if l in name_to_table and r in name_to_table:
        key = (l, r, card, label)
        if key not in seen:
            seen.add(key)
            relations.append({"left": l, "right": r, "card": card, "label": label})

mxfile = ET.Element("mxfile", {"host": "app.diagrams.net"})
diagram = ET.SubElement(mxfile, "diagram", {"id": "ER-4NF-LISTA-COMPLETO", "name": "ER 4NF Lista Completo"})
model = ET.SubElement(diagram, "mxGraphModel", {
    "dx": "3600", "dy": "2400", "grid": "1", "gridSize": "10", "guides": "1", "tooltips": "1",
    "connect": "1", "arrows": "1", "fold": "1", "page": "1", "pageScale": "1",
    "pageWidth": "5200", "pageHeight": "3600", "math": "0", "shadow": "0"
})
root = ET.SubElement(model, "root")
ET.SubElement(root, "mxCell", {"id": "0"})
ET.SubElement(root, "mxCell", {"id": "1", "parent": "0"})

id_counter = 10

def next_id():
    global id_counter
    id_counter += 1
    return str(id_counter)

title_id = next_id()
title = ET.SubElement(root, "mxCell", {
    "id": title_id,
    "value": "Diagrama ER SGSPCSI 4NF - Contenedor Lista por Tabla",
    "style": "text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;fontSize=24;fontStyle=1;fontColor=#111827;",
    "parent": "1",
    "vertex": "1"
})
ET.SubElement(title, "mxGeometry", {"x": "1200", "y": "20", "width": "2200", "height": "40", "as": "geometry"})

sub_id = next_id()
sub = ET.SubElement(root, "mxCell", {
    "id": sub_id,
    "value": "Formato lista: columna | tipo | llave+null | default",
    "style": "text;html=1;strokeColor=none;fillColor=none;align=center;verticalAlign=middle;fontSize=12;fontColor=#4B5563;",
    "parent": "1",
    "vertex": "1"
})
ET.SubElement(sub, "mxGeometry", {"x": "1200", "y": "58", "width": "2200", "height": "24", "as": "geometry"})

n_tables = len(tables)
cols = max(4, min(7, math.ceil(math.sqrt(max(n_tables, 1)))))
row_gap = 90
col_gap = 70
base_x = 80
base_y = 120
cell_min_w = 420
cell_max_w = 560
row_h = 26
header_h = 30

widths = []
heights = []
for t in tables:
    max_len = max((len(f"{a['col']} | {a['typ']} | {a['key_null']} | {a['default']}") for a in t["attrs"]), default=30)
    w = max(cell_min_w, min(cell_max_w, 220 + max_len * 4))
    h = header_h + max(1, len(t["attrs"])) * row_h
    widths.append(w)
    heights.append(h)

positions = []
for idx, t in enumerate(tables):
    r = idx // cols
    c = idx % cols
    y = base_y
    for rr in range(r):
        row_start = rr * cols
        row_end = min(row_start + cols, n_tables)
        y += max(heights[row_start:row_end]) + row_gap
    x = base_x
    for cc in range(c):
        prev_idx = r * cols + cc
        if prev_idx < n_tables:
            x += widths[prev_idx] + col_gap
    positions.append((x, y))

table_cell_ids = {}
attribute_rows = 0

for i, t in enumerate(tables):
    tid = next_id()
    table_cell_ids[t["name"].lower()] = tid
    x, y = positions[i]
    w = widths[i]
    h = heights[i]
    swim = ET.SubElement(root, "mxCell", {
        "id": tid,
        "value": t["name"].upper(),
        "style": "swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize=30;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;fillColor=#dae8fc;strokeColor=#6c8ebf;",
        "parent": "1",
        "vertex": "1"
    })
    ET.SubElement(swim, "mxGeometry", {"x": str(x), "y": str(y), "width": str(w), "height": str(h), "as": "geometry"})

    for r_idx, a in enumerate(t["attrs"], start=1):
        rid = next_id()
        value = f"{a['col']} | {a['typ']} | {a['key_null']} | {a['default']}"
        row = ET.SubElement(root, "mxCell", {
            "id": rid,
            "value": value,
            "style": "text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=4;spacingRight=4;overflow=hidden;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;rotatable=0;whiteSpace=wrap;html=1;",
            "parent": tid,
            "vertex": "1"
        })
        ET.SubElement(row, "mxGeometry", {"y": str(header_h + (r_idx - 1) * row_h), "width": str(w), "height": str(row_h), "as": "geometry"})
        attribute_rows += 1

edge_style = "edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;endArrow=block;endFill=1;strokeColor=#2563eb;fontSize=10;"
rel_count = 0
for rel in relations:
    s = table_cell_ids.get(rel["left"])
    t = table_cell_ids.get(rel["right"])
    if not s or not t:
        continue
    eid = next_id()
    edge = ET.SubElement(root, "mxCell", {
        "id": eid,
        "value": f"{rel['card']} | {rel['label']}",
        "style": edge_style,
        "parent": "1",
        "source": s,
        "target": t,
        "edge": "1"
    })
    ET.SubElement(edge, "mxGeometry", {"relative": "1", "as": "geometry"})
    rel_count += 1

xml_str = ET.tostring(mxfile, encoding="utf-8", xml_declaration=False)
out_path.write_bytes(xml_str)

print(f"TABLAS={n_tables}")
print(f"ATRIBUTOS={attribute_rows}")
print(f"RELACIONES={rel_count}")
print(f"ARCHIVO={out_path}")
print(f"EXISTE={out_path.exists()}")
