code = """import json
import re

# Load funding data
funding_path = locals()['var_functions.query_db:6']
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_path = locals()['var_functions.query_db:5']
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

# Process funding data - get projects with > $50,000
high_funding = []
for record in funding_data:
    if int(record['Amount']) > 50000:
        high_funding.append(record)

# Create set of project names for matching
funding_project_names = set()
for record in high_funding:
    funding_project_names.add(record['Project_Name'])

# Extract capital projects with design status from civic documents
design_capital_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find the design section
    design_match = re.search(r'Capital Improvement Projects \(Design\)(.*?)(?=\n\nCapital Improvement Projects|DISCUSSION:|$)', text, re.DOTALL)
    if design_match:
        design_section = design_match.group(1)
        # Extract project names from this section
        lines = design_section.split('\n')
        for line in lines:
            line = line.strip()
            # Skip empty lines and lines that are just markers
            if line and not line.startswith('(') and not line.startswith('Capital Improvement Projects'):
                # Heuristic: likely a project name if it's not a header/metadata
                if len(line) > 5 and not any(kw in line for kw in ['To:', 'From:', 'Date:', 'Subject:', 'RECOMMENDED']):
                    design_capital_projects.append(line)

# Remove duplicates
unique_design_projects = list(set(design_capital_projects))

# Count matches with funding data
match_count = 0
matched_projects = []

for design_project in unique_design_projects:
    # Check if this design project has funding > $50,000
    for funding_record in high_funding:
        funding_name = funding_record['Project_Name']
        # Match exact name or with suffix (e.g., "Project (FEMA Project)")
        if design_project == funding_name or funding_name.startswith(design_project + ' '):
            match_count += 1
            matched_projects.append(design_project)
            break

print('__RESULT__:')
print(json.dumps(match_count))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
