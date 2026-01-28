code = """import json
import re

# Load data
civic_docs_file = locals()['var_functions.query_db:4']
funding_file = locals()['var_functions.query_db:5']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding = json.load(f)

# Function to extract Spring 2022 projects
spring_2022_projects = set()

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines and headers
        if not line or line.startswith('Page') or line.startswith('Item'):
            continue
        
        # Look for potential project name (usually uppercase or title case)
        # and check if next lines contain project indicators
        if (len(line) > 10 and 
            (line.isupper() or (line[0].isupper() and any(c.isupper() for c in line[1:])))):
            
            # Check if following lines contain project schedule/updates
            following_text = ' '.join(lines[i+1:min(i+8, len(lines))])
            if 'Updates:' in following_text or 'Schedule:' in following_text or 'Project Schedule:' in following_text:
                current_project = line
        
        # Look for Spring 2022 dates in schedule lines
        if current_project:
            # Check various patterns for Spring 2022
            lower_line = line.lower()
            
            # Patterns: "Spring 2022", "2022-Spring", "2022 - Spring", "Mar/Apr/May 2022", "2022-03/04/05"
            spring_patterns = [
                r'spring\s+2022',
                r'2022\s*-\s*spring',
                r'2022\s+-\s+spring',
                r'mar(?:ch)?\s+2022',
                r'apr(?:il)?\s+2022',
                r'may\s+2022',
                r'2022\s*[-/]\s*0[3-5]',
            ]
            
            # Check if this line mentions Spring 2022 with begin/start/advertise/complete
            if ('begin' in lower_line or 'advertise' in lower_line or 'start' in lower_line or 'complete' in lower_line or 
                'design' in lower_line or 'construction' in lower_line):
                
                for pattern in spring_patterns:
                    if re.search(pattern, lower_line):
                        spring_2022_projects.add(current_project)
                        break

# Convert set to sorted list
project_list = sorted(list(spring_2022_projects))

# Match with funding data
total_funding = 0
matched_records = []

for fund in funding:
    fund_name = fund['Project_Name']
    fund_name_lower = fund_name.lower()
    amount = int(fund['Amount'])
    
    matched = False
    for project in spring_2022_projects:
        proj_lower = project.lower()
        # Match if one string is contained in the other
        if proj_lower in fund_name_lower or fund_name_lower in proj_lower:
            total_funding += amount
            matched_records.append({'project': project, 'funding': fund_name, 'amount': amount})
            matched = True
            break
        # Also check partial word matches
        elif any(word in fund_name_lower for word in proj_lower.split() if len(word) > 6):
            total_funding += amount
            matched_records.append({'project': project, 'funding': fund_name, 'amount': amount})
            matched = True
            break

result = {
    'number_of_spring_2022_projects': len(project_list),
    'total_funding_amount': total_funding,
    'project_names': project_list,
    'funding_match_count': len(matched_records)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:28': {'spring_2022_docs': 4}, 'var_functions.execute_python:34': {'spring_2022_projects': 4, 'funding_matches': 31, 'total_funding': 1614000}, 'var_functions.execute_python:44': {'spring_2022_projects': 4, 'total_funding': 0}, 'var_functions.execute_python:50': {'spring_2022_projects': 4, 'total_funding': 83000}, 'var_functions.execute_python:54': {'spring_2022_projects': 4, 'total_funding': 0}}

exec(code, env_args)
