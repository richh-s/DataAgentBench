code = """import json
docs_file = locals()['var_functions.query_db:2']
with open(docs_file) as f:
    civic_docs = json.load(f)

print('Loaded', len(civic_docs), 'documents')

spring_projects = []
spring_patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May', '2022-03', '2022-04', '2022-05']

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        # Check if this line or nearby lines mention Spring 2022
        context_start = max(0, i-3)
        context_end = min(len(lines), i+4)
        context = ' '.join(lines[context_start:context_end])
        
        has_spring = any(pattern in context for pattern in spring_patterns)
        
        # Look for project name patterns (lines that end with Project/Improvements/etc and have uppercase)
        if has_spring and ('Project' in line or 'Improvements' in line or 'Repair' in line):
            upper_count = sum(1 for c in line if c.isupper())
            total_chars = len([c for c in line if c.isalpha()])
            if total_chars > 0 and upper_count / total_chars > 0.3:  # More than 30% uppercase
                spring_projects.append(line.strip())

unique_projects = list(set(spring_projects))
print('Spring 2022 projects found:', len(unique_projects))

# Show first few
for proj in unique_projects[:10]:
    print(' -', proj[:100])

result = {'count': len(unique_projects), 'projects': unique_projects}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:46': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:48': 'file_storage/functions.query_db:48.json'}

exec(code, env_args)
