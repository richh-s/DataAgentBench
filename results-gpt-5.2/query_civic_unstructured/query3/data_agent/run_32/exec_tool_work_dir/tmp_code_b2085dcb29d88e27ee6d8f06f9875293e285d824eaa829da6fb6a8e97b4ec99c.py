code = """import json, re, pandas as pd

funding = pd.DataFrame(var_call_LRT25hxdhYoi1YJNN7nnnsHs)
funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

path = var_call_m4I7uOQzrx1GGpNk6fV53Cdx
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

projects = {}
status_map = [
    (re.compile(r'\bcompleted\b', re.I), 'completed'),
    (re.compile(r'\bunder construction\b|\bcurrently under construction\b|construction was completed', re.I), 'completed'),
    (re.compile(r'\bnot started\b', re.I), 'not started'),
    (re.compile(r'\bpreliminary design\b|\bfinal design\b|\bcomplete design\b|\bdesign\b', re.I), 'design'),
    (re.compile(r'\bawaiting\b|\bsubmitted\b|\bunder review\b|\bworking with\b', re.I), 'design'),
]

for d in docs:
    text = d.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if not ln:
            continue
        if re.search(r'\b(FEMA|emergency)\b', ln, re.I):
            name = re.sub(r'^[-•\u2022\*]+\s*', '', ln)
            if len(name) > 150:
                continue
            window = "\\n".join(lines[i:i+20])
            st = None
            for pat, lab in status_map:
                if pat.search(window):
                    st = lab
                    break
            if name not in projects:
                projects[name] = {'Project_Name': name, 'Status': st}
            else:
                if projects[name].get('Status') is None and st is not None:
                    projects[name]['Status'] = st

statuses = pd.DataFrame(list(projects.values())) if projects else pd.DataFrame(columns=['Project_Name','Status'])
res = funding.merge(statuses, on='Project_Name', how='left')
res['Status'] = res['Status'].fillna('unknown')
res = res[res['Project_Name'].str.contains('fema|emergency', case=False, na=False) | res['Funding_Source'].str.contains('fema|emergency', case=False, na=False)]
res = res.sort_values(['Project_Name','Funding_Source']).reset_index(drop=True)

out = res.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_LRT25hxdhYoi1YJNN7nnnsHs': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_m4I7uOQzrx1GGpNk6fV53Cdx': 'file_storage/call_m4I7uOQzrx1GGpNk6fV53Cdx.json'}

exec(code, env_args)
