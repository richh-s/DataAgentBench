code = """import json, re
import pandas as pd
from pathlib import Path

mongo_path = var_call_ajQkmkioQe4FJsSq6FRdKUl4
if isinstance(mongo_path, str) and mongo_path.endswith('.json'):
    records = json.loads(Path(mongo_path).read_text())
else:
    records = mongo_path

fund = pd.DataFrame(var_call_B1ysM46pTiq3zfO0FUEXNup4)
if not fund.empty:
    fund['Amount'] = pd.to_numeric(fund['Amount'], errors='coerce')

statuses = {}
status_patterns = [
    ('design', re.compile(r'Capital Improvement Projects \(Design\)|\(Design\)', re.I)),
    ('construction', re.compile(r'Capital Improvement Projects \(Construction\)|\(Construction\)', re.I)),
    ('not started', re.compile(r'Capital Improvement Projects \(Not Started\)|\(Not Started\)', re.I)),
]

proj_line = re.compile(r"^[A-Z0-9][A-Za-z0-9\-\&\,\'\(\)\s\/\u2019]+$")

for doc in records:
    text = doc.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    current = None
    for ln in lines:
        if not ln:
            continue
        switched = False
        for st, pat in status_patterns:
            if pat.search(ln):
                current = st
                switched = True
                break
        if switched:
            continue
        if current and len(ln) <= 140 and proj_line.match(ln):
            low = ln.lower()
            if ('updates' in low) or ('project schedule' in low) or ('project description' in low) or ('agenda item' in low) or low.startswith('page '):
                continue
            if re.search(r'\b(fema|emergency)\b', ln, re.I):
                statuses.setdefault(ln, current)

out = fund.copy()
out['Status'] = out['Project_Name'].map(statuses)

if out['Status'].isna().any() and statuses:
    s_items = list(statuses.items())
    def find_status(pn):
        if pn in statuses:
            return statuses[pn]
        pn_l = str(pn).lower()
        for name, st in s_items:
            nl = name.lower()
            if nl in pn_l or pn_l in nl:
                return st
        return None
    mask = out['Status'].isna()
    out.loc[mask, 'Status'] = out.loc[mask, 'Project_Name'].apply(find_status)

out = out[['Project_Name','Funding_Source','Amount','Status']].sort_values(['Project_Name','Funding_Source'], kind='stable')
result = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ajQkmkioQe4FJsSq6FRdKUl4': 'file_storage/call_ajQkmkioQe4FJsSq6FRdKUl4.json', 'var_call_B1ysM46pTiq3zfO0FUEXNup4': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
