code = """import json, re, os

# Load civic documents from previous query
civic_path = locals().get('var_functions.query_db:26')
print('Civic documents path:', civic_path)

if isinstance(civic_path, str) and civic_path.endswith('.json'):
    with open(civic_path, 'r') as f:
        civic_docs = json.load(f)
else:
    civic_docs = []

print('Total civic documents loaded:', len(civic_docs))

# Extract project information from documents
disaster_projects_2022 = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project sections in the text
    # Projects often appear with names and schedules
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        # Skip empty lines
        if not line:
            continue
            
        # Check if line looks like a project name (often title case, not bullet points)
        if (len(line) > 10 and 
            not line.startswith('(') and 
            not line.startswith('•') and 
            not line.startswith('-') and
            not line.startswith('□') and
            not line.startswith('\n') and
            (line[0].isupper() or line[0].isdigit())):
            
            # Check if it's disaster-related
            is_disaster = any(indicator in line for indicator in [
                '(FEMA', '(CalJPIA', '(CalOES', 'FEMA/CalOES', 
                'Disaster', 'Fire', 'Emergency', 'Woolsey'
            ])
            
            if is_disaster:
                # Look for date information in subsequent lines
                date_context = '\n'.join(lines[i:i+5])  # Check next few lines
                
                # Look for 2022 dates
                if '2022' in date_context:
                    # Extract potential start date mentions
                    date_patterns = [
                        r'\d{4}[-\s]*(Spring|Summer|Fall|Winter)',
                        r'\d{4}[-\s]*(January|February|March|April|May|June|July|August|September|October|November|December)',
                        r'(Spring|Summer|Fall|Winter)[-\s]*\d{4}',
                        r'(January|February|March|April|May|June|July|August|September|October|November|December)[-\s]*\d{4}'
                    ]
                    
                    found_date = False
                    for pattern in date_patterns:
                        if re.search(pattern, date_context):
                            found_date = True
                            break
                    
                    if found_date or '2022' in line:
                        disaster_projects_2022.append({
                            'name': line,
                            'source_filename': filename,
                            'context': date_context[:200]  # First 200 chars for context
                        })

print('Found', len(disaster_projects_2022), 'disaster projects with 2022 mentions')

# Show some examples
for proj in disaster_projects_2022[:10]:
    print('Project:', proj['name'])
    print('Context:', proj['context'][:100])
    print('---')

# Get unique project names
project_names = list(set([p['name'] for p in disaster_projects_2022]))
print('\nUnique disaster project names with 2022 dates:', len(project_names))

# Save results
result = {
    'total_found': len(disaster_projects_2022),
    'unique_projects': project_names,
    'all_projects': disaster_projects_2022
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:6': ['civic_docs'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:22': [{'total_disaster_funding': '1410000'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
