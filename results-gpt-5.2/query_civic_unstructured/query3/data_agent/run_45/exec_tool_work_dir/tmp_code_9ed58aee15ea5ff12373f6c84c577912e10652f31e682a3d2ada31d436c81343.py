code = """import json, re, pandas as pd

# Load mongo docs (may be a file path)
raw = var_call_uML9cp3dJYjcNUiQ2RCbPVty
if isinstance(raw, str) and raw.endswith('.json'):
    with open(raw, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = raw

fund = pd.DataFrame(var_call_IYL2MnzkJ10EAsXSRVPjsXya)
if not fund.empty:
    fund['Amount'] = pd.to_numeric(fund['Amount'], errors='coerce')

# Heuristic: get project name candidates by matching funding Project_Name in doc text
project_names = fund['Project_Name'].dropna().unique().tolist() if not fund.empty else []

status_map = {}
# Determine status from lines near project mention
status_patterns = [
    (re.compile(r'Construction was completed|Notice of completion filed|Completed', re.I), 'completed'),
    (re.compile(r'currently under construction|Begin construction|out to bid|Bids are due|Advertise', re.I), 'design'),
    (re.compile(r'Not Started', re.I), 'not started'),
    (re.compile(r'working with.*design|finalize the design|under review|submitted plans', re.I), 'design'),
]

for pn in project_names:
    found_status = None
    for d in docs:
        text = d.get('text','')
        idx = text.lower().find(pn.lower())
        if idx != -1:
            window = text[max(0, idx-400): idx+800]
            # Prefer explicit section headers in window
            for pat, st in status_patterns:
                if pat.search(window):
                    found_status = st
                    break
            if found_status:
                break
    status_map[pn] = found_status

fund['Status'] = fund['Project_Name'].map(status_map)

# Also include emergency projects found in docs but possibly not in funding table: "Outdoor Warning Signs" etc.
# We'll extract a small set of known emergency-related projects from doc text and then look up funding by name substring.
emergency_candidates = set()
for d in docs:
    t = d.get('text','')
    for m in re.finditer(r'\n([A-Z][A-Za-z0-9&/\-\s\(\)]+?)\n\n\(cid:190\)|\n([A-Z][A-Za-z0-9&/\-\s\(\)]+?)\n\n\(cid:131\)', t):
        name = (m.group(1) or m.group(2) or '').strip()
        if not name:
            continue
        if re.search(r'emergency|warning|FEMA|sirens', name, re.I):
            emergency_candidates.add(name)

# Create combined answer rows based primarily on funding table, filtered to emergency/FEMA
rows = fund.copy()
rows = rows[rows['Project_Name'].str.contains('fema|emergency', case=False, na=False) | rows['Funding_Source'].str.contains('fema|emergency', case=False, na=False)].copy()
rows = rows.sort_values(['Project_Name','Funding_Source']).reset_index(drop=True)

# Format for output
out = rows[['Project_Name','Funding_Source','Amount','Status']].to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_uML9cp3dJYjcNUiQ2RCbPVty': 'file_storage/call_uML9cp3dJYjcNUiQ2RCbPVty.json', 'var_call_IYL2MnzkJ10EAsXSRVPjsXya': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
