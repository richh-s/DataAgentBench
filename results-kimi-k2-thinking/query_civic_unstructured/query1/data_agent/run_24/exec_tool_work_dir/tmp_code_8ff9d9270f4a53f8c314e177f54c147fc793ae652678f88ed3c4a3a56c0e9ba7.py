code = """import json

# Load the funding data 
funding_file = open('/tmp/tmp8o8_0d3p/query_db_result.json')
funding_data = json.load(funding_file)
funding_file.close()

# Load the civic documents
civic_file = open('/tmp/tmpu9h1_67a/query_db_result.json')
civic_data = json.load(civic_file)
civic_file.close()

# Step 1: Filter funding for amounts > $50,000
high_funding = []
for record in funding_data:
    if int(record['Amount']) > 50000:
        high_funding.append(record)

# Step 2: Extract design capital projects from civic documents
design_projects = []

for doc in civic_data:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    # Find design section
    parts = text.split('Capital Improvement Projects (Design)')
    if len(parts) > 1:
        design_section = parts[1]
        for line in design_section.split('\n'):
            line = line.strip()
            if line and not line.startswith('(') and not line.startswith('Capital'):
                if 'To:' not in line and 'From:' not in line and 'Date' not in line:
                    if 'Subject:' not in line and 'RECOMMENDED' not in line:
                        if len(line) > 5:
                            design_projects.append(line)

# Remove duplicates
unique_design = list(set(design_projects))

# Step 3: Count matches
matched = 0
funding_names = [r['Project_Name'] for r in high_funding]

for proj in unique_design:
    for fund_name in funding_names:
        # Check if project name matches funding name
        if proj == fund_name or fund_name.startswith(proj + ' '):
            matched += 1
            break

print('__RESULT__:')
print(json.dumps(matched))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.list_db:80': ['civic_docs']}

exec(code, env_args)
