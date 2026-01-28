code = """import json
import re

funding_key = 'var_functions.query_db:6'
funding_data = locals()[funding_key]
if isinstance(funding_data, str) and funding_data.endswith('.json'):
    with open(funding_data) as f:
        funding_data = json.load(f)

civic_key = 'var_functions.query_db:8'
civic_docs = locals()[civic_key]
if isinstance(civic_docs, str) and civic_docs.endswith('.json'):
    with open(civic_docs) as f:
        civic_docs = json.load(f)

funding_map = {}
for r in funding_data:
    funding_map[r['Project_Name']] = int(r['Amount'])

disaster_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        if '(FEMA' in line or '(CalOES' in line or '(CalJPIA' in line:
            proj_name = line
            has_2022 = False
            for j in range(i, min(i+15, len(lines))):
                if '2022' in lines[j]:
                    has_2022 = True
                    break
            if has_2022:
                disaster_projects.append(proj_name)

total_funding = 0
matched = []
for name in disaster_projects:
    if name in funding_map:
        amt = funding_map[name]
        total_funding += amt
        matched.append([name, amt])
    else:
        m = re.search(r'^(.+?)\s*\([^)]*\)$', name)
        if m:
            base = m.group(1)
            for fund_name in funding_map:
                if fund_name.startswith(base) or base.startswith(fund_name):
                    amt = funding_map[fund_name]
                    total_funding += amt
                    matched.append([name, amt, fund_name])
                    break

result = {"total_funding": total_funding, "matched_count": len(matched)}
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
