code = """import json, re

# Load data
funding_file = locals()['var_functions.query_db:0']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

civic_file = locals()['var_functions.query_db:2']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create funding map for projects > $50,000
funding_map = {}
for r in funding_data:
    amt = int(r['Amount'])
    if amt > 50000:
        funding_map[r['Project_Name']] = amt

# Find capital projects with design status
design_projects = set()

for doc in civic_docs:
    text = doc['text']
    
    # Look for "Capital Improvement Projects (Design)" section
    if 'Capital Improvement Projects (Design)' in text:
        # Get the section after this header
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            design_section = parts[1].split('Capital Improvement Projects')[0]
            
            # Extract project names (look for title case lines)
            for line in design_section.split('\n'):
                line = line.strip()
                if len(line) > 10 and line[0].isupper() and not line.startswith('('):
                    # Check if it contains project keywords
                    if any(kw in line for kw in ['Project', 'Improvements', 'Repair', 'Replacement', 'Road', 'Park', 'Drainage', 'Bridge', 'Culvert', 'Wall', 'Signs']):
                        # Check if funded
                        if line in funding_map:
                            design_projects.add(line)
                        else:
                            # Check for name variations
                            for funded in funding_map:
                                if line in funded or funded.startswith(line.split(' (')[0]):
                                    design_projects.add(funded)
                                    break

print('__RESULT__:')
print(json.dumps({'count': len(design_projects)}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'funding_records': 276, 'civic_documents': 5}}

exec(code, env_args)
