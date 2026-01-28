code = """import json

# Load data from files
funding_file = locals()['var_functions.query_db:40']
civic_file = locals()['var_functions.query_db:5']

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

with open(civic_file, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Find capital design projects from civic documents
design_projects = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Simple approach: find lines in design section
    if 'Capital Improvement Projects (Design)' in text:
        start = text.find('Capital Improvement Projects (Design)')
        # Get a chunk of text
        chunk = text[start:start + 2500]
        
        # Split by lines and look for project names
        for line in chunk.split('\n'):
            clean = line.strip()
            # Look for lines that contain Project and are reasonable length
            if clean and len(clean) > 10 and 'Project' in clean:
                # Skip FEMA/disaster projects
                low = clean.lower()
                if 'fema' not in low and 'disaster' not in low:
                    design_projects.add(clean)

# Match with funding > $50,000
matched_count = 0
matched_names = set()

for funding in funding_data:
    amount = int(funding['Amount'])
    if amount > 50000:
        project_name = funding['Project_Name']
        # Remove suffix if exists
        if '(' in project_name:
            base = project_name.split('(')[0].strip()
        else:
            base = project_name
        
        if base in design_projects:
            matched_names.add(base)

result = {'count': len(matched_names)}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json'}

exec(code, env_args)
