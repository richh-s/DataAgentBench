code = """import json, re, pandas as pd

funding = pd.DataFrame(var_call_NnWBks8Y6mmsD3WqUYoVt8aZ)
# normalize types
funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

# load civic docs results (may be filepath)
docs_src = var_call_cAw0sAyDs5xaOdmq3DVXQB08
if isinstance(docs_src, str) and docs_src.endswith('.json'):
    with open(docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

# Extract project names and statuses from text blocks.
# Heuristic: find occurrences of each funded project name in docs; infer status by whether it appears under headings.
status_keywords = {
    'design': [r'\(Design\)', r'Under Design', r'Final Design', r'Complete Design', r'preliminary design', r'finalize the design'],
    'completed': [r'\bcompleted\b', r'Notice of completion', r'Construction was completed', r'Complete Construction:'],
    'not started': [r'\(Not Started\)', r'not started']
}

# Determine section-based status from doc text by scanning around match

def infer_status(text, proj):
    tlow = text.lower()
    # section cues
    idx = tlow.find(proj.lower())
    if idx == -1:
        return None
    window = text[max(0, idx-600): idx+600]
    for st, pats in status_keywords.items():
        for pat in pats:
            if re.search(pat, window, flags=re.I):
                return st
    # if appears under 'Capital Improvement Projects (Design)' etc
    pre = text[max(0, idx-1500):idx]
    # find nearest heading before idx
    headings = [
        ('design', r'Capital Improvement Projects \(Design\)'),
        ('completed', r'Capital Improvement Projects \(Construction\)'),
        ('not started', r'Capital Improvement Projects \(Not Started\)'),
        ('design', r'Disaster Recovery Projects \(Design\)'),
        ('completed', r'Disaster Recovery Projects \(Construction\)'),
        ('not started', r'Disaster Recovery Projects \(Not Started\)')
    ]
    last_pos = -1
    last_status = None
    for st, pat in headings:
        for m in re.finditer(pat, pre, flags=re.I):
            if m.start() > last_pos:
                last_pos = m.start()
                last_status = st
    return last_status

# Create mapping: Project_Name -> status (first non-null found)
proj_status = {}
for d in docs:
    text = d.get('text','')
    for proj in funding['Project_Name'].unique():
        if proj in proj_status and proj_status[proj] is not None:
            continue
        if proj.lower() in text.lower():
            proj_status[proj] = infer_status(text, proj)

funding['Status'] = funding['Project_Name'].map(proj_status)

# If still null, infer based on name contains 'Design'
funding.loc[funding['Status'].isna() & funding['Project_Name'].str.contains('design', case=False, na=False), 'Status'] = 'design'

# Aggregate by Project_Name and Funding_Source (keep separate) and format amounts
out = funding.sort_values(['Project_Name','Funding_Source']).copy()
# Convert Amount to int where possible
out['Amount'] = out['Amount'].fillna(0).astype(int)

records = out[['Project_Name','Funding_Source','Amount','Status']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(records))"""

env_args = {'var_call_NnWBks8Y6mmsD3WqUYoVt8aZ': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_cAw0sAyDs5xaOdmq3DVXQB08': 'file_storage/call_cAw0sAyDs5xaOdmq3DVXQB08.json', 'var_call_wzoSAIX4N0rZmpRpWxXIM4gL': ['Funding']}

exec(code, env_args)
