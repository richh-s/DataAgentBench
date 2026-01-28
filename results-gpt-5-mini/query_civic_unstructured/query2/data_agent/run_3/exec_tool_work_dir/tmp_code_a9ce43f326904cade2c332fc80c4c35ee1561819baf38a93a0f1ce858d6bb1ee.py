code = """import json
p = var_call_lGT6WoCuyWvDkZO6yDO1wveb
with open(p, 'r', encoding='utf-8') as f:
    docs = json.load(f)
funding = var_call_tBrGfdRy0x9zearyqJkym5P9

keywords = ['park','playground','walkway','shade','bluffs','point dume','trancas']
completed_projects = set()
for doc in docs:
    text = doc.get('text','')
    paragraphs = text.split('\n\n')
    for para in paragraphs:
        low = para.lower()
        if 'completed' in low and '2022' in low:
            for k in keywords:
                if k in low:
                    first_line = para.strip().split('\n')[0].strip()
                    if first_line.lower().endswith('project'):
                        first_line = first_line[: -len('project')].strip()
                    completed_projects.add(first_line)

# match funding records to completed projects using case-insensitive containment
matched_records = []
for rec in funding:
    pname = rec.get('Project_Name','')
    plow = pname.lower()
    for cp in completed_projects:
        if cp and (cp.lower() in plow or plow in cp.lower()):
            matched_records.append({'Project_Name': pname, 'Amount': int(rec.get('Amount',0))})
            break

# compute total
total = sum(r['Amount'] for r in matched_records)

output = {'completed_projects_found': sorted(list(completed_projects)), 'matched_funding_records': matched_records, 'total_funding': total}
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_lGT6WoCuyWvDkZO6yDO1wveb': 'file_storage/call_lGT6WoCuyWvDkZO6yDO1wveb.json', 'var_call_tBrGfdRy0x9zearyqJkym5P9': [{'Project_Name': 'Bluffs Park Shade Structure', 'Amount': '21000'}, {'Project_Name': 'Bluffs Park Workout Station', 'Amount': '39000'}, {'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Amount': '41000'}, {'Project_Name': 'Legacy Park Paver Repair Project', 'Amount': '69000'}, {'Project_Name': 'Malibu Bluffs Park Roof Replacement Project', 'Amount': '44000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway', 'Amount': '91000'}, {'Project_Name': 'Malibu Bluffs Park South Walkway Repairs', 'Amount': '81000'}, {'Project_Name': 'Malibu Park Drainage Improvements', 'Amount': '17000'}, {'Project_Name': 'Malibu Park Resurfacing Project', 'Amount': '14000'}, {'Project_Name': 'Malibu Park Storm Drain Repairs', 'Amount': '50000'}, {'Project_Name': 'PCH at Trancas Canyon Road Right Turn Lane', 'Amount': '90000'}, {'Project_Name': 'Permanent Skate Park', 'Amount': '97000'}, {'Project_Name': 'Point Dume Decomposed Granite Walkway Repair Project', 'Amount': '86000'}, {'Project_Name': 'Point Dume Walkway Repairs', 'Amount': '59000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs', 'Amount': '78000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Amount': '92000'}, {'Project_Name': 'Trancas Canyon Park Playground', 'Amount': '24000'}, {'Project_Name': 'Trancas Canyon Park Playground Resurfacing', 'Amount': '65000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project', 'Amount': '68000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Amount': '43000'}, {'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Amount': '32000'}, {'Project_Name': 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Amount': '23000'}, {'Project_Name': 'Trancas Playground Resurfacing', 'Amount': '90000'}]}

exec(code, env_args)
