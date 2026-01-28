code = """import json

# Load data
civic_docs = json.load(open(locals()['var_functions.query_db:46'], 'r')) if isinstance(locals()['var_functions.query_db:46'], str) else list(locals()['var_functions.query_db:46'])
funding = json.load(open(locals()['var_functions.query_db:47'], 'r')) if isinstance(locals()['var_functions.query_db:47'], str) else list(locals()['var_functions.query_db:47'])

# Build funding lookup
funding_lookup = {rec['Project_Name']: int(rec['Amount']) for rec in funding}

# Find eligible projects
total = 0
projects = []

# First, get all disaster-related funding with 2022 in name
for name, amount in funding_lookup.items():
    if '2022' in name and any(x in name for x in ['(FEMA', '(CalOES', '(CalJPIA']):
        total += amount
        projects.append({'name': name, 'amount': amount})

# Then check civic docs
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' not in text:
        continue
    
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Skip headers
        if any(x in line for x in ['Capital Improvement', 'AGENDA', 'Page']):
            continue
        
        # Check for disaster markers
        if any(x in line for x in ['(FEMA', '(CalOES', '(CalJPIA']):
            # Check context for 2022
            start = max(0, i-3)
            end = min(len(lines), i+4)
            context_has_2022 = any('2022' in lines[j] for j in range(start, end))
            
            if context_has_2022 and line not in [p['name'] for p in projects]:
                # Find funding
                if line in funding_lookup:
                    total += funding_lookup[line]
                    projects.append({'name': line, 'amount': funding_lookup[line]})
                else:
                    # Try partial match
                    for fund_name in funding_lookup:
                        if line in fund_name or fund_name in line:
                            if fund_name not in [p['name'] for p in projects]:
                                total += funding_lookup[fund_name]
                                projects.append({'name': fund_name, 'amount': funding_lookup[fund_name]})
                            break

# Create simple output dictionary
result = {}
result['total_funding'] = total
result['project_count'] = len(projects)
result['projects'] = projects

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.list_db:3': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:22': {'civic_docs_count': 3, 'funding_records_count': 500, 'first_civic_doc_sample': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E', 'first_funding_sample': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, 'disaster_funding_count': 27, 'sample_disaster_names': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:25': 'file_storage/functions.query_db:25.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:47': 'file_storage/functions.query_db:47.json'}

exec(code, env_args)
