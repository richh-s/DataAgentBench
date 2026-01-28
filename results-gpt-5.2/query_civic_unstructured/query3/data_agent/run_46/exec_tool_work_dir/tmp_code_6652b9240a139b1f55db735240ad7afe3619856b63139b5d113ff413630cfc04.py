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

full_text = "\n".join(d.get('text','') for d in docs)

candidates = sorted(set(funding['Project_Name'].dropna().tolist()))

status_map = {}
for pname in candidates:
    key = pname.split(' (')[0].strip()
    idx = full_text.lower().find(key.lower())
    if idx == -1:
        continue
    window = full_text[max(0, idx-200): idx+800]
    wlow = window.lower()
    status = None
    if 'construction was completed' in wlow or 'notice of completion' in wlow:
        status = 'completed'
    elif 'currently under construction' in wlow:
        status = 'construction'
    elif 'design plans' in wlow or 'final design' in wlow or 'preliminary design' in wlow or 'finalize plans' in wlow or 'plans and specifications' in wlow:
        status = 'design'
    elif 'not started' in wlow or 'identified' in wlow:
        status = 'not started'
    status_map[pname] = status

out = funding.copy()
out['Status'] = out['Project_Name'].map(status_map)
out = out.sort_values(['Project_Name','Funding_Source'])
records = out.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(records))"""

env_args = {'var_call_aihEUhXh4vTRIOaVBqlycOK4': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_VeGWnfLSDtVAtGjYRztSsGY4': 'file_storage/call_VeGWnfLSDtVAtGjYRztSsGY4.json'}

exec(code, env_args)
