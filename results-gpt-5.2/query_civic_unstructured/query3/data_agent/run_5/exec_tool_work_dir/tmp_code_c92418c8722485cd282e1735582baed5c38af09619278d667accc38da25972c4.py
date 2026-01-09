code = """import json, re, pandas as pd

funding = pd.DataFrame(var_call_k3bHCb6ODDlzrF95q32iKAIs)
if not funding.empty:
    funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

docs_var = var_call_mXfD90V7fTedjST6l9Ob5Vdj
if isinstance(docs_var, str) and docs_var.endswith('.json'):
    with open(docs_var, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_var

projects_interest = set(funding['Project_Name'].tolist())
status_map = {}

def infer_status(snippet: str):
    s = snippet.lower()
    if 'currently under construction' in s or 'construction was completed' in s or 'notice of completion' in s or re.search(r'\bcomplete(?:d)?\b', s):
        return 'completed'
    if any(k in s for k in ['working with','finalize','plans','design','under review','preliminary design','awaiting']):
        return 'design'
    if any(k in s for k in ['not started','identified','waiting for the agreement']):
        return 'not started'
    return None

for d in docs:
    text = d.get('text','')
    text_low = text.lower()
    for pname in projects_interest:
        if pname in status_map:
            continue
        idx = text_low.find(pname.lower())
        if idx == -1:
            continue
        window = text[idx: idx+800]
        pre = text[max(0, idx-500):idx]
        pre_low = pre.lower()
        cat = None
        if 'capital improvement projects (design)' in pre_low or 'disaster recovery projects (design)' in pre_low:
            cat = 'design'
        elif 'capital improvement projects (construction)' in pre_low or 'disaster recovery projects (construction)' in pre_low:
            cat = 'construction'
        elif 'capital improvement projects (not started)' in pre_low or 'disaster recovery projects (not started)' in pre_low:
            cat = 'not started'
        inf = infer_status(window)
        status = inf or (cat if cat in ['design','not started'] else None)
        if status is None and cat == 'construction':
            status = 'design'
        if status:
            status_map[pname] = status

funding['Status'] = funding['Project_Name'].map(status_map).fillna('unknown')
funding = funding.sort_values(['Project_Name','Funding_Source']).reset_index(drop=True)

out = funding[['Project_Name','Funding_Source','Amount','Status']].to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_k3bHCb6ODDlzrF95q32iKAIs': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_mXfD90V7fTedjST6l9Ob5Vdj': 'file_storage/call_mXfD90V7fTedjST6l9Ob5Vdj.json', 'var_call_VcuhlnjlDQuJd1UBrGD4nkBl': ['Funding']}

exec(code, env_args)
