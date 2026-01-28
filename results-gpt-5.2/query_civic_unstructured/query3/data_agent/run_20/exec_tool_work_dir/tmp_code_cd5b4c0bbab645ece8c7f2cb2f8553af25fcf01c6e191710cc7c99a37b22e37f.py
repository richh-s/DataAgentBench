code = """import json, re, pandas as pd

funding = var_call_lOAdHXcLpnX75TLkZ7KTBA06

# Load mongo docs (may be file path)
raw = var_call_hPPurtu5M8Q6CE1SFBSalqKe
if isinstance(raw, str):
    with open(raw, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = raw

project_names = sorted({r['Project_Name'] for r in funding if r.get('Project_Name')})

# Build regex to find project blocks; allow minor spacing differences
escaped = sorted([re.escape(p) for p in project_names], key=len, reverse=True)
name_re = re.compile(r'(?im)^(%s)\s*$' % ('|'.join(escaped))) if escaped else None

status_map = {
    'design': re.compile(r'(?im)^\s*(Capital Improvement Projects|Disaster Recovery Projects)\s*\(\s*Design\s*\)\s*$'),
    'construction': re.compile(r'(?im)^\s*(Capital Improvement Projects|Disaster Recovery Projects)\s*\(\s*Construction\s*\)\s*$'),
    'not started': re.compile(r'(?im)^\s*(Capital Improvement Projects|Disaster Recovery Projects)\s*\(\s*Not Started\s*\)\s*$'),
}

# For each doc, find sections and parse project names within section
statuses = {p: set() for p in project_names}

for d in docs:
    text = d.get('text','')
    if not text or not name_re:
        continue
    lines = text.splitlines()
    current_status = None
    for line in lines:
        # update section
        for st, rgx in status_map.items():
            if rgx.search(line):
                current_status = st
                break
        m = name_re.match(line.strip())
        if m:
            pname = m.group(1)
            if current_status:
                statuses[pname].add(current_status)

# Produce final table joining funding rows + status (prefer single status if exists)
rows=[]
for r in funding:
    pname=r['Project_Name']
    st = statuses.get(pname, set())
    if not st:
        status='(status not found in agendas)'
    elif len(st)==1:
        status=next(iter(st))
    else:
        status='; '.join(sorted(st))
    rows.append({
        'Project_Name': pname,
        'Funding_Source': r.get('Funding_Source'),
        'Amount': int(r['Amount']) if str(r.get('Amount','')).isdigit() else r.get('Amount'),
        'Status': status
    })

df=pd.DataFrame(rows)
# sort by project then source
if not df.empty:
    df=df.sort_values(['Project_Name','Funding_Source'], kind='stable')

result = df.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_lOAdHXcLpnX75TLkZ7KTBA06': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_hPPurtu5M8Q6CE1SFBSalqKe': 'file_storage/call_hPPurtu5M8Q6CE1SFBSalqKe.json'}

exec(code, env_args)
