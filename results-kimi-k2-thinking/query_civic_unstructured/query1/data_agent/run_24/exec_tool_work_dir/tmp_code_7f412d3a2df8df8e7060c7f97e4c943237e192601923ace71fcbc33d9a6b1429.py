code = """import json

# Get file paths
funding_path = var_functions.query_db:6
civic_path = var_functions.query_db:5

# Read funding data
with open(funding_path, 'r') as f:
    funding_data = json.load(f)

# Read civic documents
with open(civic_path, 'r') as f:
    civic_data = json.load(f)

# Filter funding > 50k
high_funding = [r for r in funding_data if int(r['Amount']) > 50000]

# Extract project names from design section
design_section_projects = []
for doc in civic_data:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        # Find the design section and extract lines
        start = text.index('Capital Improvement Projects (Design)')
        section = text[start:start+2000]  # Take first 2000 chars of section
        lines = section.split('\n')
        # Look for lines that look like project names
        for line in lines[2:15]:  # Skip header lines
            line = line.strip()
            if line and not line.startswith('(') and ':' not in line:
                if 'To:' not in line and 'From:' not in line and 'Date' not in line:
                    design_section_projects.append(line)

# Remove duplicates
design_section_projects = list(set(design_section_projects))

# Count matches with funding
funding_names = set(r['Project_Name'] for r in high_funding)
matches = sum(1 for proj in design_section_projects if proj in funding_names)

print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
