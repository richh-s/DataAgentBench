code = """import json, re
import pandas as pd

# funding FEMA/emergency by project name
fund_name = pd.DataFrame(var_call_dvFSDtayQNqg2nvSfFTHDjT1)

# load civic docs result file
path = var_call_aiSOvTsHK53taJtsJFKAr8nY
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Build a set of candidate project names from funding results
proj_names = sorted(set(fund_name['Project_Name'].dropna().astype(str)))

# status inference from headings in doc: Design / Construction / Not Started / Completed
status_map = {
    'design':'design',
    'construction':'construction',
    'not started':'not started',
    'completed':'completed'
}

def infer_status(text, project):
    # find first occurrence
    idx = text.lower().find(project.lower())
    if idx == -1:
        return None
    # look back 1500 chars for latest heading keyword
    window = text[max(0, idx-2000):idx].lower()
    # find last occurrence of known headings
    last = (-1, None)
    for k,v in status_map.items():
        p = window.rfind(k)
        if p > last[0]:
            last = (p, v)
    return last[1]

# Search across docs for each project, infer status
status_by_project = {}
for p in proj_names:
    for d in docs:
        txt = d.get('text','')
        if re.search(re.escape(p), txt, flags=re.I):
            st = infer_status(txt, p)
            if st:
                status_by_project[p] = st
                break
    if p not in status_by_project:
        status_by_project[p] = None

fund_name['Amount'] = pd.to_numeric(fund_name['Amount'], errors='coerce')
fund_name['Status'] = fund_name['Project_Name'].map(status_by_project)

# keep only projects related to emergency/FEMA (all are FEMA in name here)
out = fund_name.sort_values(['Project_Name','Funding_Source']).reset_index(drop=True)

# format for answer table-like text
out['Amount'] = out['Amount'].fillna(0).astype(int)

records = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(records))"""

env_args = {'var_call_dvFSDtayQNqg2nvSfFTHDjT1': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_aiSOvTsHK53taJtsJFKAr8nY': 'file_storage/call_aiSOvTsHK53taJtsJFKAr8nY.json', 'var_call_Pzx3Y4yAJkYOqnVTbibGlKg4': 'file_storage/call_Pzx3Y4yAJkYOqnVTbibGlKg4.json', 'var_call_ouPZGYnGjZhWaW6SmV5UzAXN': [], 'var_call_5eBoROu3emEBniwG5rHfjIqw': 'file_storage/call_5eBoROu3emEBniwG5rHfjIqw.json'}

exec(code, env_args)
