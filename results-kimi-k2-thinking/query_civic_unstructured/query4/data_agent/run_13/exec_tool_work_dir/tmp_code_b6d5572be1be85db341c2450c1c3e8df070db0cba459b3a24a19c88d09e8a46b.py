code = """import json
import re

# Load the civic documents data
civic_docs_file = locals()['var_functions.query_db:4']
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Load the funding data
funding_file = locals()['var_functions.query_db:5']
with open(funding_file, 'r') as f:
    funding = json.load(f)

# Find all projects that started in Spring 2022
spring_2022_projects = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    for i in range(len(lines)):
        line = lines[i].strip()
        if not line:
            continue
        
        # Look for Spring 2022 patterns
        lower_line = line.lower()
        if ('spring' in lower_line and '2022' in lower_line) or \
           ('2022-spring' in lower_line) or \
           ('2022' in lower_line and any(m in lower_line for m in ['mar', 'apr', 'may'])):
            
            # Look backwards for project name (up to 5 lines)
            for j in range(max(0, i-5), i):
                prev_line = lines[j].strip()
                # Heuristic: project names are uppercase/title case, not headers
                if len(prev_line) > 10 and prev_line[0].isupper():
                    if not prev_line.startswith('Page') and not prev_line.startswith('Item'):
                        if 'PUBLIC WORKS' not in prev_line and 'COMMISSION' not in prev_line:
                            spring_2022_projects.add(prev_line)
                            break

# Extract funding for these projects
total_funding = 0
for fund in funding:
    fund_name = fund['Project_Name']
    # Check if this is a 2022 project
    if '2022' in fund_name and ('Spring' in fund_name or 'Morning View' in fund_name):
        total_funding += int(fund['Amount'])

result = {
    'spring_2022_projects': len(spring_2022_projects),
    'total_funding': total_funding,
    'project_names': sorted(list(spring_2022_projects))
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:28': {'spring_2022_docs': 4}, 'var_functions.execute_python:34': {'spring_2022_projects': 4, 'funding_matches': 31, 'total_funding': 1614000}, 'var_functions.execute_python:44': {'spring_2022_projects': 4, 'total_funding': 0}, 'var_functions.execute_python:50': {'spring_2022_projects': 4, 'total_funding': 83000}, 'var_functions.execute_python:54': {'spring_2022_projects': 4, 'total_funding': 0}, 'var_functions.query_db:58': [{'total_funding': 'None', 'project_count': '0'}], 'var_functions.execute_python:64': {'spring_2022_projects': 4, 'total_funding': 83000}, 'var_functions.query_db:70': [{'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}

exec(code, env_args)
