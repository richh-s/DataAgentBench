code = """import json, re, pandas as pd

funding = pd.DataFrame(var_call_TTRz13Rmh4qh0LiTwZbQ4qrj)
funding['Amount'] = pd.to_numeric(funding['Amount'], errors='coerce').fillna(0).astype(int)

text_recs = var_call_NUsVwLESouXKKYBN5GZqZUD8
if isinstance(text_recs, str):
    with open(text_recs, 'r', encoding='utf-8') as f:
        text_recs = json.load(f)

status_map = {}

def infer_status(t):
    t = (t or '').lower()
    if any(k in t for k in ['construction was completed','notice of completion','was completed','completed,','completed']):
        return 'completed'
    if any(k in t for k in ['not started','identified in','waiting for the agreement']):
        return 'not started'
    if any(k in t for k in ['working with the consultant','finalize the design','plans are under review','preliminary design','final design','awaiting']):
        return 'design'
    if any(k in t for k in ['under construction','currently under construction']):
        return 'construction'
    return None

for rec in text_recs:
    lines = (rec.get('text') or '').splitlines()
    for pname in funding['Project_Name'].unique():
        key = re.sub(r"\s*\([^)]*\)\s*$", "", pname).strip()
        if not key:
            continue
        key_l = key.lower()
        for i, line in enumerate(lines):
            if key_l in line.lower():
                window = "\n".join(lines[i:i+25])
                st = infer_status(window)
                if st and pname not in status_map:
                    status_map[pname] = st
                break

funding['Status'] = funding['Project_Name'].map(status_map)

projects = []
for pname, g in funding.groupby('Project_Name'):
    status = g['Status'].dropna().iloc[0] if g['Status'].notna().any() else None
    funding_list = [{'Funding_Source': fs, 'Amount': int(am)} for fs, am in zip(g['Funding_Source'], g['Amount'])]
    projects.append({
        'Project_Name': pname,
        'Status': status,
        'Funding': funding_list,
        'Total_Amount': int(g['Amount'].sum())
    })

print('__RESULT__:')
print(json.dumps(projects))"""

env_args = {'var_call_TTRz13Rmh4qh0LiTwZbQ4qrj': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_call_NUsVwLESouXKKYBN5GZqZUD8': 'file_storage/call_NUsVwLESouXKKYBN5GZqZUD8.json', 'var_call_OkYJzOFekPgiCrTCBoNMXFUJ': ['Funding']}

exec(code, env_args)
