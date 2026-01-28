code = """import json

# Read funding data from file
funding_path = var_functions.query_db:6
f = open(funding_path, 'r')
funding_data = json.load(f)
f.close()

# Read civic documents from file
civic_path = var_functions.query_db:5
c = open(civic_path, 'r')
civic_data = json.load(c)
c.close()

# Filter for funding > 50000
high_funding = []
for record in funding_data:
    if int(record['Amount']) > 50000:
        high_funding.append(record)

# Extract design capital projects
design_projects = []
for doc in civic_data:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            design_section = parts[1]
            lines = design_section.split('\n')
            for line in lines:
                line = line.strip()
                if line and not line.startswith('(') and not line.startswith('Capital'):
                    if 'To:' not in line and 'From:' not in line:
                        if len(line) > 5:
                            design_projects.append(line)

# Remove duplicates
unique_design = list(set(design_projects))

# Count matches
funding_names = set(r['Project_Name'] for r in high_funding)
match_count = 0
for project in unique_design:
    for funding_name in funding_names:
        if project == funding_name or funding_name.startswith(project + ' '):
            match_count += 1
            break

print('__RESULT__:')
print(json.dumps(match_count))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
