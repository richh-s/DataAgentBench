code = """import json, re, pandas as pd

fund_fema = pd.DataFrame(var_call_FvgFpANjEVkmQxYgqskp44ov)

def load_json_maybe(path_or_obj):
    if isinstance(path_or_obj, str) and path_or_obj.endswith('.json'):
        with open(path_or_obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return path_or_obj

docs = load_json_maybe(var_call_R7qNhNpORSzfaEfvtITTHFw8)

# Extract project blocks from agenda-style docs and derive status per (Design)/(Construction)/(Not Started)
status_map = {
    'Design': 'design',
    'Construction': 'design',  # not in provided status list; map to design/in progress bucket
    'Not Started': 'not started'
}

projects_status = {}
for d in docs:
    text = d.get('text','')
    # capture section headings like "Capital Improvement Projects (Design)" etc.
    # We'll scan line-by-line, tracking current status label.
    current = None
    for line in text.splitlines():
        m = re.search(r'Projects\s*\((Design|Construction|Not Started)\)', line, flags=re.I)
        if m:
            key = m.group(1)
            # normalize capitalization
            key_norm = 'Not Started' if key.lower().startswith('not') else ('Design' if key.lower().startswith('design') else 'Construction')
            current = status_map.get(key_norm)
            continue
        if current is None:
            continue
        # project names appear as standalone lines (no bullet) often with letters/numbers
        cand = line.strip()
        if not cand:
            continue
        # stop when page footer or agenda item
        if cand.lower().startswith('page ') or 'agenda item' in cand.lower():
            continue
        # heuristics: ignore lines that are clearly narrative
        if any(cand.lower().startswith(x) for x in ['updates', 'project schedule', 'estimated schedule', 'project description', 'recommended action', 'discussion', 'to:', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'subject:']):
            continue
        # keep lines with reasonable length and not starting with punctuation
        if len(cand) < 4 or len(cand) > 120:
            continue
        # likely project if it contains letters and not too many spaces? accept broadly.
        # We'll later intersect with funding project names.
        projects_status.setdefault(cand, set()).add(current)

# For projects that show in multiple statuses, prioritize completed? none available. prioritize not started over design? We'll choose if any not started else design.
final_status = {}
for pname, sts in projects_status.items():
    if 'not started' in sts:
        final_status[pname] = 'not started'
    elif 'design' in sts:
        final_status[pname] = 'design'

# Attach statuses to FEMA/emergency funding projects by exact match; if missing, infer 'design' if FEMA mentioned (common disaster recovery), else unknown.
rows = []
for r in fund_fema.to_dict(orient='records'):
    pn = r['Project_Name']
    st = final_status.get(pn)
    if st is None:
        # try match without parenthetical suffixes
        pn_base = re.sub(r'\s*\([^)]*\)\s*$', '', pn).strip()
        st = final_status.get(pn_base)
    if st is None:
        st = 'design' if re.search(r'fema|emergency', pn, flags=re.I) else None
    rows.append({
        'Project_Name': pn,
        'Funding_Source': r['Funding_Source'],
        'Amount': int(r['Amount']) if str(r['Amount']).isdigit() else r['Amount'],
        'Status': st if st is not None else 'unknown'
    })

out = pd.DataFrame(rows).sort_values(['Project_Name','Funding_Source']).to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_FvgFpANjEVkmQxYgqskp44ov': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_R7qNhNpORSzfaEfvtITTHFw8': 'file_storage/call_R7qNhNpORSzfaEfvtITTHFw8.json', 'var_call_kwSTOYkREAuLP8D2HecEkZzH': 'file_storage/call_kwSTOYkREAuLP8D2HecEkZzH.json', 'var_call_sl3HR8JRNPlshBObjczxzAVc': 'file_storage/call_sl3HR8JRNPlshBObjczxzAVc.json'}

exec(code, env_args)
