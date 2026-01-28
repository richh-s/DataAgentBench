code = """import json
import pandas as pd
import re

funding = pd.DataFrame(var_call_v7D3LXcCANVs1qA8PwKliMXc)
if not funding.empty:
    funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

docs_obj = var_call_gI23tXyWMsQLx1PXccJ0IS8e
if isinstance(docs_obj, str):
    with open(docs_obj, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_obj

all_text = "\n".join([d.get('text','') for d in docs])

status_map = {}

def norm_spaces_regex(s):
    return re.escape(s).replace('\\ ', r'\\s+')

if not funding.empty and all_text:
    for pn in funding['Project_Name'].dropna().unique():
        def snippet_for(name):
            pat = norm_spaces_regex(name)
            rgx = re.compile(pat + r"[\s\S]{0,400}?\b(Updates|Update)\b[\s\S]{0,200}", re.IGNORECASE)
            m = rgx.search(all_text)
            return None if not m else all_text[m.start():m.start()+600]

        snip = snippet_for(pn)
        if snip is None:
            pn_base = re.sub(r"\s*\([^\)]*\)\s*$", "", pn).strip()
            if pn_base and pn_base != pn:
                snip = snippet_for(pn_base)

        status = None
        if snip:
            t = snip.lower()
            if ('construction was completed' in t) or ('notice of completion' in t) or re.search(r"\bcompleted\b", t):
                status = 'completed'
            elif 'not started' in t:
                status = 'not started'
            elif ('currently under construction' in t) or ('begin construction' in t) or ('final design' in t) or ('finalize' in t) or ('awaiting' in t) or ('under review' in t) or ('plans' in t) or ('design' in t):
                status = 'design'

        if status:
            status_map[pn] = status

out = []
if not funding.empty:
    funding['Status'] = funding['Project_Name'].map(status_map)
    out = funding.sort_values(['Project_Name','Funding_Source']).to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_v7D3LXcCANVs1qA8PwKliMXc': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_gI23tXyWMsQLx1PXccJ0IS8e': 'file_storage/call_gI23tXyWMsQLx1PXccJ0IS8e.json'}

exec(code, env_args)
