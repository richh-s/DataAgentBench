code = """import json

# Load funding data - filter Amount > 50000
funding_path = var_functions.query_db:6
with open(funding_path) as f:
    funding = json.load(f)

funding_over_50k = [r for r in funding if int(r['Amount']) > 50000]
funding_names = set(r['Project_Name'] for r in funding_over_50k)

# Load civic documents and extract design capital projects
civic_path = var_functions.query_db:5
with open(civic_path) as f:
    civic_docs = json.load(f)

design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    # Find design section
    start = text.find('Capital Improvement Projects (Design)')
    section = text[start:]
    
    # Split into lines and extract projects
    lines = section.split('\n')[2:]  # Skip header line and blank line
    for line in lines:
        line = line.strip()
        # Stop at next major section
        if 'Capital Improvement Projects (' in line and 'Design' not in line:
            break
        # Skip empty or marker lines
        if line and not line.startswith('(') and not line.startswith('Capital Improvement Projects'):
            # Filter out metadata lines
            if not any(kw in line for kw in ['To:', 'From:', 'Date:', 'Subject:', 'RECOMMENDED', 'DISCUSSION:']):
                design_projects.append(line)

# Count matches with funding data
matched_count = sum(1 for proj in design_projects if proj in funding_names or any(fn.startswith(proj + ' ') for fn in funding_names))

print('__RESULT__:')
print(json.dumps(matched_count))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
