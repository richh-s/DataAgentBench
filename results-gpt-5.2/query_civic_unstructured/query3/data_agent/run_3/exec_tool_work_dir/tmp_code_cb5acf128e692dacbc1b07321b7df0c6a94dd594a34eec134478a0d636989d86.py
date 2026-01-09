code = """import json, re, pandas as pd

# Load civic docs results (may be file path)
docs = var_call_bIW9Om38i6pcCZVlbclH5TYB
if isinstance(docs, str):
    with open(docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)

funding = var_call_yTLv7lM8RRF1uol2mu15Nrd4

df_fund = pd.DataFrame(funding)
if not df_fund.empty:
    df_fund['Amount'] = pd.to_numeric(df_fund['Amount'], errors='coerce')

# Extract project statuses from docs
status_map = {}
projects_of_interest = set(df_fund['Project_Name'].tolist()) if not df_fund.empty else set()

status_patterns = [
    (re.compile(r'Capital Improvement Projects \(Design\)', re.I), 'design'),
    (re.compile(r'Capital Improvement Projects \(Construction\)', re.I), 'construction'),
    (re.compile(r'Capital Improvement Projects \(Not Started\)', re.I), 'not started'),
    (re.compile(r'Disaster Recovery Projects \(Design\)', re.I), 'design'),
    (re.compile(r'Disaster Recovery Projects \(Construction\)', re.I), 'construction'),
    (re.compile(r'Disaster Recovery Projects \(Not Started\)', re.I), 'not started'),
]

# helper to normalize
norm = lambda s: re.sub(r'\s+', ' ', s.strip())

for d in docs:
    text = d.get('text','')
    lines = [norm(x) for x in text.splitlines()]
    current_status = None
    for line in lines:
        if not line:
            continue
        for pat, st in status_patterns:
            if pat.search(line):
                current_status = st
                break
        # attempt match on exact project name lines
        if current_status:
            if line in projects_of_interest and line not in status_map:
                status_map[line] = current_status
            else:
                # some docs may have project names with minor punctuation differences; try fuzzy simple contains for FEMA/emergency projects
                if ('fema' in line.lower() or 'emergency' in line.lower()):
                    for p in list(projects_of_interest):
                        if p not in status_map and line.lower() == p.lower():
                            status_map[p] = current_status

# Build answer rows
rows = []
for _, r in df_fund.iterrows():
    pname = r['Project_Name']
    rows.append({
        'Project_Name': pname,
        'Funding_Source': r['Funding_Source'],
        'Amount': None if pd.isna(r['Amount']) else int(r['Amount']),
        'Status': status_map.get(pname)
    })

# If status missing, try infer from name: FEMA projects likely disaster; but status unknown -> 'unknown'
for row in rows:
    if not row['Status']:
        row['Status'] = 'unknown'

# Sort
rows = sorted(rows, key=lambda x: (x['Project_Name'], x['Funding_Source']))

print('__RESULT__:')
print(json.dumps(rows))"""

env_args = {'var_call_bIW9Om38i6pcCZVlbclH5TYB': 'file_storage/call_bIW9Om38i6pcCZVlbclH5TYB.json', 'var_call_yTLv7lM8RRF1uol2mu15Nrd4': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}]}

exec(code, env_args)
