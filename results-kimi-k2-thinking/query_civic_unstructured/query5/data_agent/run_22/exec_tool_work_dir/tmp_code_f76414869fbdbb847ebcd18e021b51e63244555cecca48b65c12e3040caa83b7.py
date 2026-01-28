code = """import json, re

# Load data files
with open(locals()['var_functions.query_db:66']) as f:
    funding_data = json.load(f)
with open(locals()['var_functions.query_db:67']) as f:
    civic_docs_data = json.load(f)

# Build funding map
fund_map = {}
for record in funding_data:
    proj_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    fund_map[proj_name] = fund_map.get(proj_name, 0) + amount

# Find disaster projects with 2022 start dates
disaster_projects = []
for doc in civic_docs_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines) - 1):
        curr = lines[i].strip()
        nxt = lines[i+1].strip() if i+1 < len(lines) else ''
        
        if not curr or curr.startswith('(') or 'page' in curr.lower():
            continue
            
        if 'Updates:' in nxt or 'Project Schedule:' in nxt:
            proj_name = curr
            is_disaster = False
            has_2022 = False
            
            for j in range(i+1, min(i+15, len(lines))):
                cline = lines[j].upper()
                
                # Disaster indicators
                for ind in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'WOOLSEY']:
                    if ind in cline:
                        is_disaster = True
                        break
                
                # 2022 dates with schedule context
                if '2022' in cline:
                    for sw in ['DESIGN', 'CONSTRUCTION', 'BEGIN', 'COMPLETE', 'ADVERTISE']:
                        if sw in cline:
                            has_2022 = True
                            break
            
            if is_disaster and has_2022 and proj_name:
                disaster_projects.append(proj_name)

# Remove duplicates
disaster_projects = list(set(disaster_projects))

# Calculate funding total
total_funding = 0
for proj in disaster_projects:
    for fund_proj, amount in fund_map.items():
        if proj in fund_proj or fund_proj in proj:
            total_funding += amount
            break

result = {
    'total_funding': total_funding,
    'disaster_projects': len(disaster_projects),
    'sample_projects': disaster_projects[:3]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}, 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json', 'var_functions.query_db:67': 'file_storage/functions.query_db:67.json'}

exec(code, env_args)
