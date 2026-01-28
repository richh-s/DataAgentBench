code = """import json

# Load FEMA project funding data
with open('var_functions.query_db:46', 'r') as f:
    fema_funding = json.load(f)

# Load civic documents  
with open('var_functions.query_db:42', 'r') as f:
    civic_docs = json.load(f)

# Build results list
results = []

# Process each FEMA-funded project
for item in fema_funding:
    proj_name = item['Project_Name']
    status = 'not started'  # default
    
    # Try to find status in documents
    for doc in civic_docs:
        text = doc.get('text', '')
        if proj_name in text or proj_name.split('(')[0].strip() in text:
            txt = text.lower()
            if 'under construction' in txt:
                status = 'construction'
            elif 'design' in txt:
                status = 'design'
            elif 'completed' in txt or 'complete' in txt:
                status = 'completed'
            break
    
    results.append({
        'project': proj_name,
        'funding': item['Funding_Source'],
        'amount': int(item['Amount']),
        'status': status,
        'topics': 'FEMA',
        'type': 'disaster'
    })

# Find additional emergency projects in documents
emergency_names = set()
for doc in civic_docs:
    txt = doc.get('text', '').lower()
    if 'emergency' in txt:
        # Extract project names from this document
        lines = doc.get('text', '').split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            if len(line) > 10 and not any(h in line for h in ['Capital Improvement', 'Disaster Recovery']):
                if i+1 < len(lines) and '(cid:190)' in lines[i+1]:
                    # Check if not already in results
                    found = False
                    for r in results:
                        if line in r['project'] or r['project'] in line:
                            found = True
                            break
                    if not found:
                        emergency_names.add(line)

# Add emergency projects (status will be basic since no direct funding match)
for name in emergency_names:
    results.append({
        'project': name,
        'funding': 'No funding record',
        'amount': 0,
        'status': 'not started',
        'topics': 'emergency',
        'type': 'capital'
    })

# Format output
out_lines = []
for r in results:
    out_lines.append('Project: ' + r['project'])
    out_lines.append('  Funding Source: ' + r['funding'])
    out_lines.append('  Amount: $' + str(r['amount']))
    out_lines.append('  Status: ' + r['status'])
    out_lines.append('  Topics: ' + r['topics'])
    out_lines.append('  Type: ' + r['type'])
    out_lines.append('')

answer = '\n'.join(out_lines)
print('__RESULT__:')
print(answer)"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': [{'name': 'Funding'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.query_db:38': 'file_storage/functions.query_db:38.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.list_db:44': ['civic_docs'], 'var_functions.query_db:46': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}], 'var_functions.query_db:48': []}

exec(code, env_args)
