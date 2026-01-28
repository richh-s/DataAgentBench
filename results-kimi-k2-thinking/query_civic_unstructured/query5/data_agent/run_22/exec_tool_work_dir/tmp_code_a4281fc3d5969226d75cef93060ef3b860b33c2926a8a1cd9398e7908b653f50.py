code = """import json, re

# Load funding data
with open(locals()['var_functions.query_db:6']) as f:
    funding = json.load(f)

# Load civic documents  
with open(locals()['var_functions.query_db:7']) as f:
    civic_docs = json.load(f)

# Build funding map
fund_map = {}
for r in funding:
    proj_name = r.get('Project_Name', '')
    amount = int(r.get('Amount', 0))
    fund_map[proj_name] = amount

# Find disaster projects with 2022 start dates from civic documents
disaster_projects_2022 = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines) - 1):
        line = lines[i].strip()
        if not line:
            continue
            
        # Check if next line indicates project info
        next_line = lines[i+1].strip() if i+1 < len(lines) else ''
        if 'Updates:' in next_line or 'Project Schedule:' in next_line:
            proj_name = line
            
            # Look for disaster and 2022 indicators in following lines
            is_disaster = False
            has_2022 = False
            
            for j in range(i+1, min(i+10, len(lines))):
                check_line = lines[j].upper()
                
                # Disaster indicators
                disaster_indicators = ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER']
                for indicator in disaster_indicators:
                    if indicator in check_line:
                        is_disaster = True
                        break
                
                # 2022 date indicators
                if '2022' in check_line and ('DESIGN' in check_line or 'CONSTRUCTION' in check_line or 'BEGIN' in check_line):
                    has_2022 = True
            
            if is_disaster and has_2022:
                disaster_projects_2022.append(proj_name)

# Calculate total funding for disaster projects started in 2022
total_funding = 0

for disaster_proj in disaster_projects_2022:
    for fund_proj, amount in fund_map.items():
        # Match project names
        if disaster_proj == fund_proj or disaster_proj in fund_proj or fund_proj in disaster_proj:
            total_funding += amount
            break

result = {
    'total_funding': total_funding,
    'disaster_projects_count': len(disaster_projects_2022),
    'sample_projects': disaster_projects_2022[:3]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
