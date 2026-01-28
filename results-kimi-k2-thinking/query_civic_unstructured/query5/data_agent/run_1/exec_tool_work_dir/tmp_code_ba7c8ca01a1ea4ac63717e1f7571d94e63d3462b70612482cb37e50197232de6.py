code = """import json

# Load the data
civic_docs_data = locals()['var_functions.query_db:54']
funding_data = locals()['var_functions.query_db:55']

# Convert to usable format
civic_docs_list = list(civic_docs_data) if not isinstance(civic_docs_data, str) else json.load(open(civic_docs_data))
funding_list = list(funding_data) if not isinstance(funding_data, str) else json.load(open(funding_data))

# Initialize tracking variables
total_funding = 0
projects_with_funding = []

# Step 1: Find disaster projects in funding data that have 2022 in the name
for funding_record in funding_list:
    project_name = funding_record.get('Project_Name', '')
    # Check if it's a disaster project (has FEMA/CalOES/CalJPIA marker) and has 2022
    if '2022' in project_name and any(marker in project_name for marker in ['(FEMA', '(CalOES', '(CalJPIA')]:
        amount = int(funding_record.get('Amount', 0))
        total_funding += amount
        projects_with_funding.append({'name': project_name, 'amount': amount})

# Step 2: Look through civic documents for disaster projects with 2022 references
for doc in civic_docs_list:
    doc_text = doc.get('text', '')
    if '2022' not in doc_text:
        continue
    
    # Split by lines and look for project names
    lines = doc_text.split('\n')
    for i, line in enumerate(lines):
        # Clean up the line
        clean_line = line.strip()
        
        # Skip garbage lines
        if len(clean_line) < 10 or len(clean_line) > 200:
            continue
            
        # Skip header lines
        skip_words = ['Capital Improvement', 'Disaster Recovery', 'AGENDA', 'Page', 'Prepared by:', 'Approved by:', 'Item']
        if any(word in clean_line for word in skip_words):
            continue
        
        # Check if this is a disaster project
        if any(marker in clean_line for marker in ['(FEMA', '(CalOES', '(CalJPIA']):
            # Check context for 2022 (3 lines before and after)
            has_2022_nearby = False
            for lookback in range(max(0, i-3), min(len(lines), i+4)):
                if '2022' in lines[lookback]:
                    has_2022_nearby = True
                    break
            
            if has_2022_nearby:
                # Find funding for this project
                project_name = clean_line
                if project_name in funding_lookup:
                    # Check if already counted
                    if project_name not in [p['name'] for p in projects_with_funding]:
                        amount = funding_lookup[project_name]
                        total_funding += amount
                        projects_with_funding.append({'name': project_name, 'amount': amount})
                else:
                    # Try to find a matching funding record
                    for funding_name in funding_lookup.keys():
                        if project_name in funding_name or funding_name in project_name:
                            if funding_name not in [p['name'] for p in projects_with_funding]:
                                amount = funding_lookup[funding_name]
                                total_funding += amount
                                projects_with_funding.append({'name': funding_name, 'amount': amount})
                            break

# Prepare final result
result = {
    'total_funding': total_funding,
    'project_count': len(projects_with_funding),
    'projects': projects_with_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['civic_docs'], 'var_functions.list_db:3': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:22': {'civic_docs_count': 3, 'funding_records_count': 500, 'first_civic_doc_sample': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil E', 'first_funding_sample': {'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, 'disaster_funding_count': 27, 'sample_disaster_names': ['Birdview Avenue Improvements (CalOES Project)', 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Clover Heights Storm Drain (FEMA Project)', 'Corral Canyon Culvert Repairs (FEMA Project)']}, 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:25': 'file_storage/functions.query_db:25.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:33': 'file_storage/functions.query_db:33.json', 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.query_db:47': 'file_storage/functions.query_db:47.json', 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json', 'var_functions.query_db:55': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}]}

exec(code, env_args)
