code = """import json
import re

# Load funding data (Amount > 50000)
with open('/tmp/tmp4q6n_5e0.json', 'r') as f:
    funding_data = json.load(f)

# Load civic docs data
with open('/tmp/tmp3d0s1x5g.json', 'r') as f:
    civic_docs = json.load(f)

# Extract project information from civic docs
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for Capital Improvement Projects (Design) section
    # Split by sections to find projects with design status
    if 'Capital Improvement Projects (Design)' in text:
        # Find the section
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
            # Skip empty lines, markup, and known non-project lines
            skip_patterns = ['(', 'cid:', 'Updates:', 'Project Schedule:', 
                           'Complete Design:', 'Advertise:', 'Begin Construction:',
                           'Spring', 'Summer', 'Fall', 'Winter', '2023', '2024']
            
            should_skip = any(pattern in line for pattern in skip_patterns) or \
                         not line or line.isupper() or len(line) < 10
            
            if not should_skip:
                # Clean up the line - remove any trailing colons or special characters
                clean_line = line.strip(':-•')
                if clean_line:
                    projects.append({
                        'Project_Name': clean_line,
                        'type': 'capital',
                        'status': 'design'
                    })

# Match with funding data
matches = []
matched_funding_ids = set()

for proj in projects:
    proj_name = proj['Project_Name'].lower()
    
    for fund in funding_data:
        fund_id = fund['Funding_ID']
        fund_name = fund['Project_Name']
        fund_name_lower = fund_name.lower()
        amount = int(fund['Amount'])
        
        # Check if already matched
        if fund_id in matched_funding_ids:
            continue
            
        # Check for match
        if (proj_name in fund_name_lower or 
            fund_name_lower in proj_name or
            proj_name.replace('project', '').strip() in fund_name_lower):
            matches.append({
                'Project_Name': fund_name,
                'type': proj['type'],
                'status': proj['status'],
                'Amount': amount
            })
            matched_funding_ids.add(fund_id)
            break

print('__RESULT__:')
print(json.dumps({
    'count': len(matches),
    'projects': matches
}))"""

env_args = {'var_functions.list_db:0': ['Funding'], 'var_functions.list_db:1': ['civic_docs'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
