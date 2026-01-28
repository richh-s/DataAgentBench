code = """import json

# Load funding data - get file path as string
funding_data = None
civic_docs = None

funding_path = var_functions.query_db:0
with open(funding_path) as f:
    funding_data = json.load(f)

civic_path = var_functions.query_db:2
with open(civic_path) as f:
    civic_docs = json.load(f)

# Get projects with funding > $50,000
high_funding_names = []
for record in funding_data:
    amount = int(record['Amount'])
    if amount > 50000:
        high_funding_names.append(record['Project_Name'])

# Extract capital design project names from civic documents
design_project_names = []

# Simple extraction - look for lines that seem like project names
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start == -1:
        continue
    
    # Get content after this header
    content_after_header = text[design_start:]
    
    # Roughly cut at next major section
    design_content = content_after_header
    for marker in ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Disaster Recovery Projects']:
        marker_pos = design_content.find(marker)
        if marker_pos > 0:
            design_content = design_content[:marker_pos]
            break
    
    # Extract potential project names from paragraphs
    blocks = design_content.split('\n\n')
    for block in blocks:
        block = block.strip()
        if len(block) > 10:
            lines = block.split('\n')
            if lines:
                first_line = lines[0].strip()
                # Filter for likely project names
                if len(first_line) > 10 and not first_line.isupper():
                    design_project_names.append(first_line)

# Count matches using simple string comparison
matched_count = 0

for proj_name in design_project_names:
    proj_lower = proj_name.lower()
    
    for fund_name in high_funding_names:
        fund_lower = fund_name.lower()
        
        # Check for exact match
        if proj_lower == fund_lower:
            matched_count += 1
            break
        
        # Check if one name contains the other
        if proj_name in fund_name or fund_name in proj_name:
            matched_count += 1
            break

# Output result
result = matched_count
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'count': '276'}], 'var_functions.query_db:56': [{'count': '276'}]}

exec(code, env_args)
