code = """import json, re, pandas as pd

# Load civic docs result (may be file path)
docs = var_call_S9eGRvgPwItXH0e9Rr8NvrK1
if isinstance(docs, str) and docs.endswith('.json'):
    with open(docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)

fund = var_call_zAXHutBjmTRzKfnibDeak42P
fund_df = pd.DataFrame(fund)
if not fund_df.empty:
    fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce')

text_all = "\n".join(d.get('text','') for d in docs)

# Extract project sections and infer statuses from headings
statuses = {}
current_status = None
for line in text_all.splitlines():
    l = line.strip()
    if not l:
        continue
    low = l.lower()
    if 'capital improvement projects' in low and '(design' in low:
        current_status = 'design'
        continue
    if 'capital improvement projects' in low and '(construction' in low:
        current_status = 'construction'
        continue
    if 'capital improvement projects' in low and '(not started' in low:
        current_status = 'not started'
        continue
    if 'disaster recovery projects' in low:
        current_status = 'disaster recovery'
        continue

    # Candidate project name line
    if current_status and len(l) >= 4 and not re.search(r'^(updates|project schedule|estimated schedule|project description)\b', low):
        if ':' not in l and re.search(r'[A-Za-z]', l) and len(l) <= 120:
            if low in {'recommended action', 'discussion'}:
                continue
            if re.search(r'^page\s+\d+', low):
                continue
            if 'agenda item' in low:
                continue
            statuses.setdefault(l, current_status)

results = []
for _, r in fund_df.iterrows():
    pname = r['Project_Name']
    stat = statuses.get(pname)
    if stat is None:
        base = re.sub(r'\s*\([^)]*\)\s*$', '', str(pname)).strip()
        for k, v in statuses.items():
            kbase = re.sub(r'\s*\([^)]*\)\s*$', '', k).strip()
            if kbase.lower() == base.lower():
                stat = v
                break
    if stat is None:
        if re.search(r'fema|caloes|caljpia', str(pname), re.I):
            stat = 'disaster recovery'
        elif re.search(r'emergency', str(pname), re.I):
            stat = 'unknown'
    results.append({
        'Project_Name': pname,
        'Funding_Source': r['Funding_Source'],
        'Amount': None if pd.isna(r['Amount']) else int(r['Amount']),
        'Status': stat or 'unknown'
    })

res_df = pd.DataFrame(results).sort_values(['Project_Name', 'Funding_Source'])
print('__RESULT__:')
print(json.dumps(res_df.to_dict(orient='records')))"""

env_args = {'var_call_S9eGRvgPwItXH0e9Rr8NvrK1': 'file_storage/call_S9eGRvgPwItXH0e9Rr8NvrK1.json', 'var_call_zAXHutBjmTRzKfnibDeak42P': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
