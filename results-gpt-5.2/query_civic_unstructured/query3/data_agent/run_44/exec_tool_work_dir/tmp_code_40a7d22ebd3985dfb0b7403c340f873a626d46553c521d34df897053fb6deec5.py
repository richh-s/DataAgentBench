code = """import json, re, pandas as pd

# Load civic docs (may be file path)
docs = var_call_l3n0v9YCZIyBiNtG7XVbaXSp
if isinstance(docs, str):
    with open(docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)

funding = pd.DataFrame(var_call_Ngl4yP7vcjlROy9ONaXq7jKN)
# normalize Amount
funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

# Extract project statuses from docs: look for known status section headers and capture following project lines
status_headers = {
    'design': re.compile(r'^(?:Capital Improvement Projects \(Design\)|Disaster Recovery Projects \(Design\)|Disaster Recovery Projects\s*\(Design\)|Disaster Recovery Projects \(Design\)|Disaster Recovery Projects \(Design\))\s*$', re.I),
    'construction': re.compile(r'^(?:Capital Improvement Projects \(Construction\)|Disaster Recovery Projects \(Construction\))\s*$', re.I),
    'not started': re.compile(r'^(?:Capital Improvement Projects \(Not Started\)|Disaster Recovery Projects \(Not Started\))\s*$', re.I),
    'completed': re.compile(r'^(?:Capital Improvement Projects \(Completed\)|Disaster Recovery Projects \(Completed\))\s*$', re.I),
}

known_projects = set(funding['Project_Name'].dropna().unique().tolist())

proj_status = {}

for d in docs:
    text = d.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    current_status = None
    for ln in lines:
        if not ln:
            continue
        # update current status
        for st, pat in status_headers.items():
            if pat.match(ln):
                current_status = st
                break
        else:
            # within a status section, detect project lines by exact match to known project names or close variants
            if current_status:
                # Some lines have bullets or weird characters; clean leading bullets
                clean = re.sub(r'^[•\(cid:[0-9]+\)\-\*]+\s*', '', ln).strip()
                # Direct match
                if clean in known_projects:
                    proj_status.setdefault(clean, set()).add(current_status)
                else:
                    # try match if line starts with a known project name (common)
                    for pn in known_projects:
                        if clean.startswith(pn):
                            proj_status.setdefault(pn, set()).add(current_status)
                            break

# If multiple statuses found, prefer completed > construction > design > not started
pref = {'completed':0,'construction':1,'design':2,'not started':3}
final_status = {}
for pn, sts in proj_status.items():
    final_status[pn] = sorted(list(sts), key=lambda x: pref.get(x, 99))[0]

funding['Status'] = funding['Project_Name'].map(final_status).fillna('unknown')

# Filter to emergency/FEMA related based on project name or funding source
mask = funding['Project_Name'].str.contains('fema|emergency', case=False, na=False) | funding['Funding_Source'].str.contains('fema|emergency', case=False, na=False)
res = funding.loc[mask, ['Project_Name','Funding_Source','Amount','Status']].copy()

# Order for readability
res = res.sort_values(['Project_Name','Funding_Source']).reset_index(drop=True)

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_Ngl4yP7vcjlROy9ONaXq7jKN': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_l3n0v9YCZIyBiNtG7XVbaXSp': 'file_storage/call_l3n0v9YCZIyBiNtG7XVbaXSp.json'}

exec(code, env_args)
