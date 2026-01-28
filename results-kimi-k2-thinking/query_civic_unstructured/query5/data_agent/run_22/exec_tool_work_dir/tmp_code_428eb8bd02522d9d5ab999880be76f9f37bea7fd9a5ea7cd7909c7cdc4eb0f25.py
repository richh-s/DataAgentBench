code = """import json
import re
import os

# Load data from stored file paths
with open(locals()['var_functions.query_db:6']) as f:
    funding_data = json.load(f)
with open(locals()['var_functions.query_db:7']) as f:
    civic_docs_data = json.load(f)

# Build a map of project names to funding amounts
fund_map = {}
for record in funding_data:
    proj_name = record.get('Project_Name', '')
    amount = int(record.get('Amount', 0))
    if proj_name:
        fund_map[proj_name] = fund_map.get(proj_name, 0) + amount

# Extract disaster projects with 2022 start dates from civic documents
disaster_projects_2022 = []
for doc in civic_docs_data:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line or line.startswith('(') or 'page' in line.lower() or 'agenda item' in line.lower():
            continue
        
        # Check if this looks like a project title (next line has project info)
        if i < len(lines) - 1 and ('Updates:' in lines[i+1] or 'Project Schedule:' in lines[i+1]):
            project_name = line
            is_disaster = False
            has_2022 = False
            
            # Check next few lines for indicators
            for j in range(i+1, min(i+15, len(lines))):
                check_line = lines[j]
                
                # Look for disaster indicators
                if any(indicator in check_line.upper() for indicator in ['FEMA', 'CALOES', 'CALJPIA', 'DISASTER', 'RECOVERY', 'WOOLSEY']):
                    is_disaster = True
                
                # Look for 2022 dates in schedule context
                if '2022' in check_line:
                    if any(word in check_line.upper() for word in ['DESIGN', 'CONSTRUCTION', 'BEGIN', 'COMPLETE', 'SCHEDULE']):
                        has_2022 = True
            
            if is_disaster and has_2022 and project_name:
                disaster_projects_2022.append(project_name)

# Calculate total funding for disaster projects started in 2022
total_funding = 0
matched_projects = 0

for proj_name in disaster_projects_2022:
    for fund_proj_name, amount in fund_map.items():
        # Exact match or substring match
        if proj_name == fund_proj_name or proj_name in fund_proj_name or fund_proj_name in proj_name:
            total_funding += amount
            matched_projects += 1
            break
        
        # Word-based matching for similar names
        proj_words = set([w.lower() for w in re.findall(r'\w+', proj_name) if len(w) > 6])
        fund_words = set([w.lower() for w in re.findall(r'\w+', fund_proj_name) if len(w) > 6])
        
        if proj_words and fund_words and len(proj_words.intersection(fund_words)) > 1:
            total_funding += amount
            matched_projects += 1
            break

# Prepare result
result = {
    'total_funding': total_funding,
    'disaster_projects_found': len(disaster_projects_2022),
    'projects_with_funding_data': matched_projects,
    'sample_projects': disaster_projects_2022[:3]
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:2': ['Funding'], 'var_functions.list_db:3': ['civic_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.execute_python:12': {'funding_count': 500, 'civic_docs_count': 5}, 'var_functions.execute_python:18': {'funding_type': "<class 'str'>", 'civic_type': "<class 'str'>"}}

exec(code, env_args)
