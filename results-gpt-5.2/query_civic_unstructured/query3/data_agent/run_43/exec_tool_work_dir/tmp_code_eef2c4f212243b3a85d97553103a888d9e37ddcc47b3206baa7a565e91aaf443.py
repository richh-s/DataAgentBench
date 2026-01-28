code = """import json, re
import pandas as pd

funding = pd.DataFrame(var_call_fyLs3qjXV7BV87Fevpq7dIuY)
funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce')

# Load mongo results (may be file path)
mongo_res = var_call_skPCPR1rSEFwLv0O1Oncyo5G
if isinstance(mongo_res, str):
    with open(mongo_res, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = mongo_res

projects = set(funding['Project_Name'].dropna().unique().tolist())

# Build regex to locate project blocks and infer status from section headers
# We'll parse each doc by lines and track current status based on headings.
status_map = {
    'Design': 'design',
    'Construction': 'design',  # keep only three statuses; treat construction as design/in progress
    'Not Started': 'not started',
    'Completed': 'completed'
}

def infer_status_from_line(line):
    l=line.lower()
    if 'capital improvement projects (design)' in l or 'disaster recovery projects (design)' in l:
        return 'design'
    if 'capital improvement projects (construction)' in l or 'disaster recovery projects (construction)' in l:
        return 'design'
    if 'capital improvement projects (not started)' in l or 'disaster recovery projects (not started)' in l:
        return 'not started'
    if 'capital improvement projects (completed)' in l or 'disaster recovery projects (completed)' in l:
        return 'completed'
    return None

found = {}
for d in docs:
    text = d.get('text','')
    lines = text.splitlines()
    cur_status = None
    for i, line in enumerate(lines):
        s = infer_status_from_line(line)
        if s:
            cur_status = s
            continue
        # check exact project name match in line
        for pn in list(projects):
            if pn in line:
                found[pn] = cur_status or found.get(pn)

# default unknown statuses to 'unknown'
status_df = pd.DataFrame([{'Project_Name':k,'Status':(v if v else 'unknown')} for k,v in found.items()])

# join; keep all funding projects even if status not found
out = funding.merge(status_df, on='Project_Name', how='left')
out['Status'] = out['Status'].fillna('unknown')

# filter for emergency or FEMA related based on project name
mask = out['Project_Name'].str.contains('FEMA', case=False, na=False) | out['Project_Name'].str.contains('emergency', case=False, na=False)
out = out[mask].copy()

# order
out = out.sort_values(['Project_Name','Funding_Source'], kind='stable')

records = out.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(records))"""

env_args = {'var_call_fyLs3qjXV7BV87Fevpq7dIuY': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_skPCPR1rSEFwLv0O1Oncyo5G': 'file_storage/call_skPCPR1rSEFwLv0O1Oncyo5G.json'}

exec(code, env_args)
