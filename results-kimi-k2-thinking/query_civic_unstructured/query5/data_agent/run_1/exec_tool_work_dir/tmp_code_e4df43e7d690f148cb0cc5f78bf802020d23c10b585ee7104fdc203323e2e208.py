code = """import json

# Access the query results
x1 = locals()['var_functions.query_db:32']
x2 = locals()['var_functions.query_db:33']

# Load data
if isinstance(x1, str) and x1.endswith('.json'):
    with open(x1, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = list(x1) if x1 else []

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

# Find disaster projects with 2022 in civic documents
disaster_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or len(line) < 10 or len(line) > 300:
            continue
        
        # Skip headers
        skip = False
        header_terms = ['Capital Improvement', 'Disaster Recovery', 'AGENDA', 'Page ', 'RECOMMENDED ACTION', 'Prepared by:', 'Approved by:']
        for term in header_terms:
            if term in line:
                skip = True
                break
        if skip:
            continue
        
        # Check context
        start = max(0, i-6)
        end = min(len(lines), i+8)
        context = '\n'.join(lines[start:end])
        
        if '2022' in context:
            # Check if disaster
            is_disaster = False
            if any(m in line for m in ['(FEMA', '(CalOES', '(CalJPIA']):
                is_disaster = True
            
            # Or matches disaster funding
            if not is_disaster:
                for disaster_name in funding_lookup.keys():
                    if '(FEMA' in disaster_name or '(CalOES' in disaster_name or '(CalJPIA' in disaster_name:
                        if line in disaster_name or disaster_name in line:
                            is_disaster = True
                            line = disaster_name
                            break
            
            if is_disaster:
                disaster_projects.add(line)

# Match with funding
total = 0
matches = []

for proj in disaster_projects:
    if proj in funding_lookup:
        amount = funding_lookup[proj]
        total += amount
        matches.append({'name': proj, 'amount': amount})
    else:
        for fund_name in funding_lookup.keys():
            if proj in fund_name or fund_name in proj:
                amount = funding_lookup[fund_name]
                total += amount
                matches.append({'name': fund_name, 'amount': amount})
                break

# Add 2022 disaster funding records
for fund_name in funding_lookup.keys():
    if '2022' in fund_name:
        if any(m in fund_name for m in ['(FEMA', '(CalOES', '(CalJPIA']):
            already_included = any(p['name'] == fund_name for p in matches)
            if not already_included:
                amount = funding_lookup[fund_name]
                total += amount
                matches.append({'name': fund_name, 'amount': amount})

result = {
    'total_funding': total,
    'project_count': len(matches),
    'projects': matches
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.list_db:3': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:22': {'civic_docs_count': 3, 'funding_records_count': 500, 'first_civic_doc_sample': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E', 'first_funding_sample': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, 'disaster_funding_count': 27, 'sample_disaster_names': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:25': 'file_storage/functions.query_db:25.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json'}

exec(code, env_args)
