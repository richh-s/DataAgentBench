code = """import json

# Load funding data from file
with open('var_functions.query_db:6', 'r') as f:
    funding_data = json.load(f)

# Load civic documents from file  
with open('var_functions.query_db:64', 'r') as f:
    civic_data = json.load(f)

# Step 1: Filter funding for amounts > $50,000
high_funding_recs = []
for record in funding_data:
    if int(record['Amount']) > 50000:
        high_funding_recs.append(record)

# Step 2: Extract capital projects in design phase from civic docs
design_project_list = []

for doc in civic_data:
    txt = doc.get('text', '')
    
    if 'Capital Improvement Projects (Design)' not in txt:
        continue
    
    # Split to get design section
    parts = txt.split('Capital Improvement Projects (Design)')
    if len(parts) > 1:
        design_section = parts[1]
        # Extract lines with project names
        for line in design_section.split('\n'):
            clean_line = line.strip()
            if clean_line and not clean_line.startswith('(') and not clean_line.startswith('Capital'):
                if 'To:' not in clean_line and 'From:' not in clean_line:
                    if 'Date:' not in clean_line and 'Subject:' not in clean_line:
                        if len(clean_line) > 5 and clean_line[0].isupper():
                            design_project_list.append(clean_line)

# Remove duplicates
unique_design = list(set(design_project_list))

# Step 3: Count matches with funding data
funding_names = set(r['Project_Name'] for r in high_funding_recs)
match_count = 0

for design_name in unique_design:
    for fund_name in funding_names:
        # Check for exact match or with suffix like (FEMA Project)
        if design_name == fund_name or fund_name.startswith(design_name + ' '):
            match_count += 1
            break

# Print result in required format
print('__RESULT__:')
result_str = json.dumps(match_count)
print(result_str)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json'}

exec(code, env_args)
