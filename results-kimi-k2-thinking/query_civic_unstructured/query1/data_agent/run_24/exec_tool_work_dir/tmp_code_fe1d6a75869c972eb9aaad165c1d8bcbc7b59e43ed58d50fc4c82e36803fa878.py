code = """import json

# Read funding data from the stored file path
funding_file = "/tmp/tmp8o8_0d3p/query_db_result.json"
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

# Read civic documents from the stored file path
civic_file = "/tmp/tmpu9h1_67a/query_db_result.json"
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Step 1: Filter for funding > $50,000
high_funding = [r for r in funding_records if int(r['Amount']) > 50000]

# Step 2: Extract design capital projects from civic documents
design_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    # Extract design section
    parts = text.split('Capital Improvement Projects (Design)')
    if len(parts) > 1:
        design_section = parts[1]
        
        # Get lines and extract project names
        lines = design_section.split('\n')
        for line in lines:
            line = line.strip()
            if line and not line.startswith('(') and not line.startswith('Capital'):
                if 'To:' not in line and 'From:' not in line and 'Date' not in line:
                    if 'Subject:' not in line and 'RECOMMENDED' not in line:
                        if len(line) > 5 and line[0].isalpha():
                            design_projects.append(line)

# Remove duplicates
unique_design = list(set(design_projects))

# Step 3: Match with funding
matched = 0
funding_names = [r['Project_Name'] for r in high_funding]

for proj in unique_design:
    for fund_name in funding_names:
        if proj == fund_name or fund_name.startswith(proj + ' '):
            matched += 1
            break

print('__RESULT__:')
print(json.dumps(matched))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
