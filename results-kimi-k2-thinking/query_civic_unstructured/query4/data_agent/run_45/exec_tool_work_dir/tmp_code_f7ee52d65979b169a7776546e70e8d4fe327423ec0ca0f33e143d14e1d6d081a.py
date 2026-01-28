code = """import json

# Load the civic documents
file_path = locals()['var_functions.query_db:2']
with open(file_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

print('Examining document structure...')
print('Total documents:', len(civic_docs))

# Look at the first document in detail
first_doc = civic_docs[0]
print('\nFirst document filename:', first_doc['filename'])
print('\nSample text showing date patterns:')

# Show sections containing date patterns
sample_text = first_doc['text']
patterns = ['2022', 'Spring', 'Fall', 'Summer', 'Winter', '2021', '2023']

lines = sample_text.split('\n')
for i, line in enumerate(lines[:50]):  # First 50 lines
    if any(p in line for p in patterns):
        print(f'Line {i}: {line[:120]}')

# Try to find sections that might contain project information
print('\n=== Searching for start dates ===')
start_date_patterns = ['Complete Design', 'Estimated Schedule', 'Project Schedule']

projects_with_dates = []
for doc in civic_docs:
    text = doc.get('text', '')
    if '2022' in text:  # Focus on documents mentioning 2022
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            # Look for lines that might indicate a project with a date
            for pattern in start_date_patterns:
                if pattern in line:
                    # Look for project name in nearby lines (usually before)
                    project_name = None
                    for j in range(max(0, i-10), i):
                        prev_line = lines[j].strip()
                        if prev_line and any(kw in prev_line for kw in ['Project', 'Improvements', 'Repairs']):
                            # Check if it looks like a project name
                            upper_count = sum(1 for c in prev_line if c.isupper())
                            total_alpha = len([c for c in prev_line if c.isalpha()])
                            if total_alpha > 0 and upper_count / total_alpha > 0.2:
                                project_name = prev_line
                                break
                    
                    # Check if there's a Spring 2022 date near this
                    context_start = max(0, i-5)
                    context_end = min(len(lines), i+5)
                    context_text = ' '.join(lines[context_start:context_end])
                    
                    if project_name and ('2022-Spring' in context_text or 'Spring 2023' in context_text or '2022-03' in context_text or '2022-04' in context_text or '2022-05' in context_text):
                        projects_with_dates.append({
                            'project': project_name,
                            'date_context': context_text
                        })

print('Projects with Spring 2022 dates found:', len(projects_with_dates))
for proj in projects_with_dates[:10]:
    print('\nProject:', proj['project'])
    print('Context:', proj['date_context'][:200])

result = {'project_count': len(projects_with_dates), 'projects': projects_with_dates[:20]}
print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:46': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json', 'var_functions.execute_python:53': {'count': 0, 'projects': []}}

exec(code, env_args)
