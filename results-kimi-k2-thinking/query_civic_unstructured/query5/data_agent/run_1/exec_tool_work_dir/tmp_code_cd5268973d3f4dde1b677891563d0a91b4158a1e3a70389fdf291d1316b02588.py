code = """import json

# Load data from query results
civic_docs_raw = locals()['var_functions.query_db:54']
funding_raw = locals()['var_functions.query_db:55']

# Load civic documents
if isinstance(civic_docs_raw, str):
    with open(civic_docs_raw, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = list(civic_docs_raw)

# Load funding data
if isinstance(funding_raw, str):
    with open(funding_raw, 'r') as f:
        funding = json.load(f)
else:
    funding = list(funding_raw)

# Build funding lookup dictionary
funding_lookup = {}
for rec in funding:
    name = rec.get('Project_Name', '').strip()
    amount = int(rec.get('Amount', '0'))
    funding_lookup[name] = amount

# Track total funding and identify projects
TOTAL_FUNDING = 0
PROJECTS = []

# Find disaster projects with 2022 in the name from funding data
for project_name, amount in funding_lookup.items():
    if '2022' in project_name and any(marker in project_name for marker in ['(FEMA', '(CalOES', '(CalJPIA']):
        TOTAL_FUNDING += amount
        PROJECTS.append({'name': project_name, 'amount': amount})

# Check civic documents for 2022 disaster projects not in funding data
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            # Skip short or obviously non-project lines
            if len(line) < 10:
                continue
            # Skip headers
            if any(skip in line for skip in ['Capital Improvement', 'Disaster Recovery', 'AGENDA', 'Page']):
                continue
            # Check for disaster projects
            if any(marker in line for marker in ['(FEMA', '(CalOES', '(CalJPIA']):
                # Check if 2022 is in context
                has_2022 = False
                for j in range(max(0, i-3), min(len(lines), i+4)):
                    if '2022' in lines[j]:
                        has_2022 = True
                        break
                if has_2022:
                    # Find funding if not already counted
                    if line not in [p['name'] for p in PROJECTS]:
                        if line in funding_lookup:
                            TOTAL_FUNDING += funding_lookup[line]
                            PROJECTS.append({'name': line, 'amount': funding_lookup[line]})
                        else:
                            # Try partial match
                            for fund_name in funding_lookup:
                                if line in fund_name or fund_name in line:
                                    if fund_name not in [p['name'] for p in PROJECTS]:
                                        TOTAL_FUNDING += funding_lookup[fund_name]
                                        PROJECTS.append({'name': fund_name, 'amount': funding_lookup[fund_name]})
                                    break

# Create output
result = {}
result['total_funding'] = TOTAL_FUNDING
result['project_count'] = len(PROJECTS)
result['projects'] = PROJECTS

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.list_db:3': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:22': {'civic_docs_count': 3, 'funding_records_count': 500, 'first_civic_doc_sample': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E', 'first_funding_sample': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, 'disaster_funding_count': 27, 'sample_disaster_names': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:25': 'file_storage/functions.query_db:25.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:47': 'file_storage/functions.query_db:47.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:55': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}]}

exec(code, env_args)
