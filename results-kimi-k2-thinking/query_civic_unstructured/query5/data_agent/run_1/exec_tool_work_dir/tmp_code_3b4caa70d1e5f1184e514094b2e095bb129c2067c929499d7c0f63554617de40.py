code = """import json

# Load query results
civic_data = locals()['var_functions.query_db:54']
fund_data = locals()['var_functions.query_db:55']

# Parse documents
if isinstance(civic_data, str):
    civic_docs = json.load(open(civic_data))
else:
    civic_docs = list(civic_data)

if isinstance(fund_data, str):
    funding = json.load(open(fund_data))
else:
    funding = list(fund_data)

# Build funding lookup
funding_lookup = {rec['Project_Name']: int(rec['Amount']) for rec in funding}

# Collect disaster projects with 2022
total = 0
found_projects = []

# From funding data - disaster projects with 2022 in name
for name, amount in funding_lookup.items():
    if '2022' in name and any(x in name for x in ['(FEMA', '(CalOES', '(CalJPIA']):
        if name not in [p['name'] for p in found_projects]:
            total += amount
            found_projects.append({'name': name, 'amount': amount})

# From civic documents
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text and any(x in text for x in ['(FEMA', '(CalOES', '(CalJPIA']):
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if len(line) < 10:
                continue
            if any(x in line for x in ['(FEMA', '(CalOES', '(CalJPIA']):
                # Check context for 2022
                has_2022 = False
                for j in range(max(0, i-3), min(len(lines), i+4)):
                    if '2022' in lines[j]:
                        has_2022 = True
                        break
                if has_2022:
                    project_name = line
                    if project_name not in [p['name'] for p in found_projects]:
                        if project_name in funding_lookup:
                            amount = funding_lookup[project_name]
                            total += amount
                            found_projects.append({'name': project_name, 'amount': amount})
                        else:
                            for fund_name in funding_lookup:
                                if project_name in fund_name or fund_name in project_name:
                                    if fund_name not in [p['name'] for p in found_projects]:
                                        amount = funding_lookup[fund_name]
                                        total += amount
                                        found_projects.append({'name': fund_name, 'amount': amount})
                                    break

# Output result
result = {'total_funding': total, 'project_count': len(found_projects), 'projects': found_projects}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.list_db:3': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:22': {'civic_docs_count': 3, 'funding_records_count': 500, 'first_civic_doc_sample': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E', 'first_funding_sample': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, 'disaster_funding_count': 27, 'sample_disaster_names': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:25': 'file_storage/functions.query_db:25.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:47': 'file_storage/functions.query_db:47.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:55': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}]}

exec(code, env_args)
