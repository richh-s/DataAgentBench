code = """import json

# Read funding data file path
funding_path = var_functions.query_db:6
with open(funding_path) as f:
    funding = json.load(f)

# Read civic documents file path
civic_path = var_functions.query_db:5
with open(civic_path) as f:
    civic_docs = json.load(f)

# Step 1: Get funding records with amount > 50,000
high_amount_recs = [r for r in funding if int(r['Amount']) > 50000]

# Step 2: Extract capital projects in design phase from civic documents
design_capital_list = []

for doc in civic_docs:
    content = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' not in content:
        continue
    
    # Get section after design header
    parts = content.split('Capital Improvement Projects (Design)')
    if len(parts) > 1:
        section = parts[1]
        # Get lines and check for project names
        lines = section.split('\n')
        for line in lines:
            line_stripped = line.strip()
            if line_stripped and not line_stripped.startswith('(') and not line_stripped.startswith('Capital'):
                if 'To:' not in line_stripped and 'From:' not in line_stripped and 'Date' not in line_stripped:
                    if len(line_stripped) > 5:
                        design_capital_list.append(line_stripped)

# Remove duplicates
design_capital_list = list(set(design_capital_list))

# Step 3: Count projects that match funding records
matched_num = 0

for proj_name in design_capital_list:
    for fund_rec in high_amount_recs:
        fund_project_name = fund_rec['Project_Name']
        # Check exact match or with suffix
        if proj_name == fund_project_name or fund_project_name.startswith(proj_name + ' '):
            matched_num += 1
            break

# Output result as JSON
print('__RESULT__:')
print(json.dumps(matched_num))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
