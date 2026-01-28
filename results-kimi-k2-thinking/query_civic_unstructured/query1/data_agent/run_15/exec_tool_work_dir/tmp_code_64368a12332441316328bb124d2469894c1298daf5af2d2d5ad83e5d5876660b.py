code = """import json

# Load funding data
funding_file = locals()['var_functions.query_db:64']
with open(funding_file) as f:
    funding_records = json.load(f)

# Load civic documents
civic_file = locals()['var_functions.query_db:40']
with open(civic_file) as f:
    civic_docs = json.load(f)

# Create sets for project names
high_funding = {}
for record in funding_records:
    name = record['Project_Name']
    high_funding[name] = name.lower().strip()

design_projects = []

# Extract design projects from each document
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design projects section (between headers)
    if 'Capital Improvement Projects (Design)' in text:
        # Get the section between Design and Construction
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            section = parts[1].split('Capital Improvement Projects (Construction)')[0]
            
            # Process each line
            for line in section.split('\n'):
                line = line.strip()
                
                # Filter for actual project names (not empty, not markers, etc)
                if len(line) > 15 and not line.startswith('('):
                    if 'Updates:' not in line and 'Schedule:' not in line:
                        # Clean up common markers
                        clean_line = line.replace('(cid:190)', '').replace('(cid:131)', '').strip()
                        
                        # Only add reasonable length project names
                        if len(clean_line) > 15:
                            design_projects.append(clean_line)

# Normalize for comparison
design_normalized = [p.lower().strip() for p in design_projects]
funding_normalized = {k: v for k, v in high_funding.items()}

# Count exact matches
exact_matches = []
for i, design_norm in enumerate(design_normalized):
    if design_projects[i] in high_funding:
        exact_matches.append(design_projects[i])

# Try normalized matching if needed
all_matches = exact_matches

# Get unique count
unique_matches = list(set(all_matches))

# Create final result
result = {
    'high_funding_projects': len(funding_normalized),
    'design_projects_extracted': len(design_projects),
    'matching_projects_count': len(unique_matches),
    'sample_matches': unique_matches[:5]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:32': [{'count': '276'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
