code = """import json

# Load civic documents
x1 = locals()['var_functions.query_db:32']
if isinstance(x1, str) and x1.endswith('.json'):
    with open(x1, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = list(x1) if x1 else []

# Load funding data
x2 = locals()['var_functions.query_db:33']
if isinstance(x2, str) and x2.endswith('.json'):
    with open(x2, 'r') as f:
        funding = json.load(f)
else:
    funding = list(x2) if x2 else []

# Build funding lookup
funding_lookup = {}
for rec in funding:
    name = rec.get('Project_Name', '').strip()
    amount = int(rec.get('Amount', '0'))
    funding_lookup[name] = amount

# Find disaster projects with 2022
eligible = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    
    lines = text.split('\n')
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10:
            continue
        
        # Skip headers
        if 'Capital Improvement' in line or 'AGENDA' in line or 'Page ' in line:
            continue
        
        # Check context for 2022
        start = max(0, i-6)
        end = min(len(lines), i+8)
        context = '\n'.join(lines[start:end])
        
        if '2022' in context:
            # Check if disaster-related
            if '(FEMA' in line or '(CalOES' in line or '(CalJPIA' in line:
                eligible.add(line)
            else:
                # Check against disaster funding names
                for fund_name in funding_lookup.keys():
                    if '(FEMA' in fund_name or '(CalOES' in fund_name or '(CalJPIA' in fund_name:
                        if line in fund_name or fund_name in line:
                            eligible.add(fund_name)
                            break

# Calculate funding totals
total = 0
project_list = []

for proj_name in eligible:
    if proj_name in funding_lookup:
        amount = funding_lookup[proj_name]
        total += amount
        project_list.append({'name': proj_name, 'amount': amount})
    else:
        # Try partial match
        for fund_name in funding_lookup.keys():
            if proj_name in fund_name or fund_name in proj_name:
                amount = funding_lookup[fund_name]
                total += amount
                project_list.append({'name': fund_name, 'amount': amount})
                break

# Add disaster funding records with 2022 in name
for fund_name in funding_lookup.keys():
    if '2022' in fund_name:
        if '(FEMA' in fund_name or '(CalOES' in fund_name or '(CalJPIA' in fund_name:
            already_included = any(p['name'] == fund_name for p in project_list)
            if not already_included:
                amount = funding_lookup[fund_name]
                total += amount
                project_list.append({'name': fund_name, 'amount': amount})

result = json.dumps({'total_funding': total, 'project_count': len(project_list), 'projects': project_list})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.list_db:3': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:22': {'civic_docs_count': 3, 'funding_records_count': 500, 'first_civic_doc_sample': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E', 'first_funding_sample': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, 'disaster_funding_count': 27, 'sample_disaster_names': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:25': 'file_storage/functions.query_db:25.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json'}

exec(code, env_args)
