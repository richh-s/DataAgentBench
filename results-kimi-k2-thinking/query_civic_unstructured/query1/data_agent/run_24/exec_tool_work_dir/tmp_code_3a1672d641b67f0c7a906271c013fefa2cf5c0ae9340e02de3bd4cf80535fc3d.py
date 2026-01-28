code = """import json

# Load funding data
with open('/tmp/tmp8o8_0d3p/query_db_result.json', 'r') as f:
    funding_data = json.load(f)

# Load civic documents
with open('/tmp/tmpu9h1_67a/query_db_result.json', 'r') as f:
    civic_docs = json.load(f)

# Get funding records > $50,000
design_funding_names = []
for record in funding_data:
    if int(record['Amount']) > 50000:
        design_funding_names.append(record['Project_Name'])

# Extract design capital project names from civic documents
design_civic_names = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    if 'Capital Improvement Projects (Design)' not in text:
        continue
    
    # Split to get design section
    parts = text.split('Capital Improvement Projects (Design)')
    if len(parts) > 1:
        design_section = parts[1]
        # Find the end of design section
        end_markers = [
            'Capital Improvement Projects (Construction)',
            'Capital Improvement Projects (Not Started)',
            'DISCUSSION:'
        ]
        
        for marker in end_markers:
            marker_pos = design_section.find(marker)
            if marker_pos > 0:
                design_section = design_section[:marker_pos]
                break
        
        # Extract project names from this section
        for line in design_section.split('\n'):
            line = line.strip()
            if line and not line.startswith('(') and not line.startswith('Capital'):
                if 'To:' not in line and 'From:' not in line and 'Date' not in line:
                    if 'Subject:' not in line and 'RECOMMENDED' not in line:
                        if 'Updates:' not in line and 'Project Schedule:' not in line:
                            if len(line) > 5:
                                design_civic_names.append(line)

# Remove duplicates
design_civic_names = list(set(design_civic_names))

# Count matches
matched_count = 0

for civic_name in design_civic_names:
    for fund_name in design_funding_names:
        # Check exact match or with suffix (e.g., '(FEMA Project)')
        if civic_name == fund_name or fund_name.startswith(civic_name + ' '):
            matched_count += 1
            break

print('__RESULT__:')
print(json.dumps(matched_count))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:64': 'file_storage/functions.query_db:64.json', 'var_functions.list_db:80': ['civic_docs'], 'var_functions.query_db:86': 'file_storage/functions.query_db:86.json'}

exec(code, env_args)
