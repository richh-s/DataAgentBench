code = """import json, re
import pandas as pd

# Load mongo docs (possibly large) from file path
mongo_res = var_call_XGZPtEzqZQuC7x9sOwNsaJzI
if isinstance(mongo_res, str) and mongo_res.endswith('.json'):
    with open(mongo_res, 'r', encoding='utf-8') as f:
        mongo_docs = json.load(f)
else:
    mongo_docs = mongo_res

funding = var_call_oDEiecqq34jcgWlszexqyt8U
fund_df = pd.DataFrame(funding)
if not fund_df.empty:
    fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce')

proj_names = sorted(set(fund_df['Project_Name'].dropna().tolist()))

# Extract status from documents by locating project name and nearby status section
status_keywords = {
    'design': [r'\bdesign\b', r'\bfinal design\b', r'\bcomplete design\b', r'\bpreliminary design\b'],
    'completed': [r'\bcompleted\b', r'\bconstruction was completed\b', r'\bnotice of completion\b', r'\bcomplete construction\b'],
    'not started': [r'\bnot started\b', r'\bidentified\b', r'\bproject description\b']
}

def infer_status(context: str):
    ctx = context.lower()
    scores = {k:0 for k in status_keywords}
    for k, pats in status_keywords.items():
        for p in pats:
            if re.search(p, ctx):
                scores[k] += 1
    # heuristic priorities
    if scores['completed']>0 and scores['completed']>=scores['design']:
        return 'completed'
    if scores['design']>0:
        return 'design'
    if scores['not started']>0:
        return 'not started'
    return None

status_map = {}
for pn in proj_names:
    pn_low = pn.lower()
    best = None
    for d in mongo_docs:
        text = d.get('text','')
        t_low = text.lower()
        idx = t_low.find(pn_low)
        if idx != -1:
            start = max(0, idx-400)
            end = min(len(text), idx+800)
            ctx = text[start:end]
            st = infer_status(ctx)
            if st:
                best = st
                # break on strong signals
                if st in ('completed','design','not started'):
                    break
    status_map[pn] = best

fund_df['Status'] = fund_df['Project_Name'].map(status_map)
# Also include emergency-related if any in funding table; already filtered. ensure rows
out_df = fund_df[['Project_Name','Funding_Source','Amount','Status']].sort_values(['Project_Name','Funding_Source'])

result = out_df.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_XGZPtEzqZQuC7x9sOwNsaJzI': 'file_storage/call_XGZPtEzqZQuC7x9sOwNsaJzI.json', 'var_call_oDEiecqq34jcgWlszexqyt8U': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
