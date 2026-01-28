code = """import json, re
import pandas as pd

funding = pd.DataFrame(var_call_aihEUhXh4vTRIOaVBqlycOK4)
funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

# Load civic docs (may be path)
docs_obj = var_call_VeGWnfLSDtVAtGjYRztSsGY4
if isinstance(docs_obj, str):
    with open(docs_obj, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_obj

text = "\n".join(d.get('text','') for d in docs)

# Extract status blocks for FEMA/emergency-related projects
# Pattern: Project Name then 'Updates:' line(s) then maybe schedule; we infer status by keywords.
name_pat = re.compile(r"\n([A-Z][A-Za-z0-9\-\&\(\)\/'\., ]{3,}?(?:FEMA|Emergency)[^\n]{0,120})\n", re.I)
# Also include specific known project names without FEMA word in title but emergency topic (e.g., Outdoor Warning Sirens/Signs)
known_extra = [
    'Outdoor Warning Sirens', 'Outdoor Warning Signs', 'Outdoor Warning Sirens - Design',
    'Storm Drain Master Plan', 'Clover Heights Storm Drainage Improvements',
    'Latigo Canyon Road Retaining Wall Repair Project'
]

# Find candidate names from funding table as authoritative
candidates = sorted(set(funding['Project_Name'].dropna().tolist()))

# Build status map by searching each candidate name in text and grabbing nearby context
status_map = {}
for pname in candidates:
    idx = text.lower().find(pname.lower().split(' (')[0].lower())
    if idx == -1:
        continue
    window = text[max(0, idx-200): idx+800]
    wlow = window.lower()
    status = None
    if 'currently under construction' in wlow or 'begin construction' in wlow or 'construction:' in wlow:
        status = 'construction'
    if 'construction was completed' in wlow or 'notice of completion' in wlow or 'completed' in wlow:
        status = 'completed'
    if 'finalize the design' in wlow or 'design plans' in wlow or 'final design' in wlow or 'preliminary design' in wlow:
        # if not already completed/construction
        if status not in ['completed','construction']:
            status = 'design'
    if 'out to bid' in wlow or 'advertise' in wlow:
        if status not in ['completed','construction']:
            status = 'design'
    if 'not started' in wlow or 'identified' in wlow:
        status = 'not started'
    status_map[pname] = status

# Join funding with status
out = funding.copy()
out['Status'] = out['Project_Name'].map(status_map)

# Aggregate by project name (keep multiple funding sources)
out = out.sort_values(['Project_Name','Funding_Source'])
records = out.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(records))"""

env_args = {'var_call_aihEUhXh4vTRIOaVBqlycOK4': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_VeGWnfLSDtVAtGjYRztSsGY4': 'file_storage/call_VeGWnfLSDtVAtGjYRztSsGY4.json'}

exec(code, env_args)
