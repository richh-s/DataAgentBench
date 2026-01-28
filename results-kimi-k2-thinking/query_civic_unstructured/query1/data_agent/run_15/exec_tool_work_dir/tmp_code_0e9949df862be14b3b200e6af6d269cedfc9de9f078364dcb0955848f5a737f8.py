code = """import json

# Load funding data file path
funding_file = '/tmp/tmp_query_result_46b1b2a4.json'
with open(funding_file) as f:
    funding = json.load(f)

# Load civic docs file path  
civic_file = '/tmp/tmp_query_result_e3c5f8a1.json'
with open(civic_file) as f:
    docs = json.load(f)

# Get projects with funding > 50000
high_funding = set()
for record in funding:
    amount = int(record['Amount'])
    if amount > 50000:
        high_funding.add(record['Project_Name'])

# Extract capital projects with design status from civic documents
design_projects = set()

for doc in docs:
    text = doc.get('text', '')
    
    # Find the Capital Improvement Projects (Design) section
    if 'Capital Improvement Projects (Design)' in text:
        # Split at the design header
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            design_section = parts[1]
            
            # Split at the construction header to get only design projects
            if 'Capital Improvement Projects (Construction)' in design_section:
                design_section = design_section.split('Capital Improvement Projects (Construction)')[0]
            
            # Extract project names from lines
            lines = design_section.split('\n')
            for line in lines:
                line = line.strip()
                # Skip empty lines and common markers
                if not line or len(line) < 10:
                    continue
                if line.startswith('(') or line.startswith('•') or line.startswith('-'):
                    continue
                if 'Updates:' in line or 'Schedule:' in line or 'Page' in line:
                    continue
                
                # Clean the line
                clean_line = line
                if clean_line and len(clean_line) > 15:
                    design_projects.add(clean_line)

# Find matching projects (exact matches)
matching_projects = high_funding.intersection(design_projects)
match_count = len(matching_projects)

# If no exact matches found, try normalized matching
if match_count == 0 and design_projects:
    norm_funding = {name.lower().strip() for name in high_funding}
    for project in design_projects:
        if project.lower().strip() in norm_funding:
            match_count += 1

result = {
    'total_high_funding': len(high_funding),
    'total_design_projects': len(design_projects),
    'matching_projects': match_count
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:32': [{'count': '276'}], 'var_functions.query_db:36': [], 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
