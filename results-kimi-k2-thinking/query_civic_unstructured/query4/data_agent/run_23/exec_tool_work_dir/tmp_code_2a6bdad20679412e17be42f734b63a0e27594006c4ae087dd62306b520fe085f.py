code = """import json
import re

# Access the files
civic_docs_file = locals()['var_functions.query_db:16']
funding_file = locals()['var_functions.query_db:17']

# Load data
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding = json.load(f)

# Compile regex for Spring 2022 dates
spring_2022_patterns = [
    r'2022[-\s]spring',
    r'spring[-\s]2022',
    r'2022[-\s]march',
    r'2022[-\s]april', 
    r'2022[-\s]may',
    r'2022[-\s]03',
    r'2022[-\s]04',
    r'2022[-\s]05'
]

# Extract projects with potential Spring 2022 dates
potential_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if not text:
        continue
        
    # split into lines and process
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 10:
            continue
            
        # Check if this line might be a project name
        # Look for common project name patterns
        project_indicators = [
            'project',
            'improvement',
            'repair',
            'replacement',
            'construction',
            'drainage',
            'road',
            'bridge',
            'park',
            'facility'
        ]
        
        line_lower = line.lower()
        if any(indicator in line_lower for indicator in project_indicators):
            
            # Check surrounding context for date info
            context_start = max(0, i-2)
            context_end = min(len(lines), i+5)
            context = ' '.join(lines[context_start:context_end]).lower()
            
            # Check if Spring 2022 date appears in context
            has_spring_2022 = any(re.search(pattern, context) for pattern in spring_2022_patterns)
            
            if has_spring_2022:
                potential_projects.append({
                    'Project_Name': line.strip(),
                    'Source': doc.get('filename', 'unknown')
                })

# Deduplicate projects by name
deduplicated = []
seen_names = set()
for proj in potential_projects:
    if proj['Project_Name'] not in seen_names:
        deduplicated.append(proj)
        seen_names.add(proj['Project_Name'])

print('__RESULT__:')
print(json.dumps({
    'total_potential_projects': len(deduplicated),
    'sample_projects': deduplicated[:10]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:17': 'file_storage/functions.query_db:17.json', 'var_functions.execute_python:22': {'civic_docs_count': 5, 'funding_count': 500, 'sample_civic_doc_filename': 'malibucity_agenda_03222023-2060.txt', 'total_funding_available': 28094000}}

exec(code, env_args)
