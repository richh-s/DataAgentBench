code = """import json

# Load funding data (Amount > 50000)
funding_file = '/tmp/tmp4q6n_5e0.json'
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic docs data
civic_file = '/tmp/tmp3d0s1x5g.json'
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Extract project information from civic docs
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find Capital Improvement Projects (Design) section
    if 'Capital Improvement Projects (Design)' in text:
        start = text.find('Capital Improvement Projects (Design)')
        end = text.find('Capital Improvement Projects (Construction)', start)
        if end == -1:
            end = text.find('Capital Improvement Projects (Not Started)', start)
        if end == -1:
            end = text.find('Disaster Recovery Projects', start)
        if end == -1:
            end = len(text)
        
        section_text = text[start:end]
        lines = section_text.split('\n')
        
        for line in lines:
            line = line.strip()
            # Skip empty lines, headers, metadata, and schedule lines
            if not line or line.isupper() or len(line) < 10:
                continue
            if '(' in line or 'cid:' in line or 'Updates:' in line or 'Schedule:' in line:
                continue
            if 'Complete Design:' in line or 'Advertise:' in line or 'Begin Construction:' in line:
                continue
            if line.startswith('Spring') or line.startswith('Summer') or line.startswith('Fall') or line.startswith('Winter'):
                continue
            if '2023' in line or '2024' in line:
                continue
                
            # Clean line and add to projects
            clean_line = line.strip(':-•')
            if clean_line and len(clean_line) > 10:
                projects.append({'Project_Name': clean_line, 'type': 'capital', 'status': 'design'})

# Match projects with funding data
matches = []
matched_funding_ids = set()

for proj in projects:
    proj_name_lower = proj['Project_Name'].lower()
    for fund in funding_data:
        fund_id = fund['Funding_ID']
        if fund_id in matched_funding_ids:
            continue
        fund_name = fund['Project_Name']
        fund_name_lower = fund_name.lower()
        amount = int(fund['Amount'])
        
        # Check for match between project name and funding name
        if proj_name_lower in fund_name_lower or fund_name_lower in proj_name_lower:
            matches.append({
                'Project_Name': fund_name,
                'type': proj['type'],
                'status': proj['status'],
                'Amount': amount
            })
            matched_funding_ids.add(fund_id)
            break

# Create result
result = {
    'count': len(matches),
    'projects': matches
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.list_db:1': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
