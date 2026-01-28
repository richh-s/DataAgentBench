code = """import json
import re

civic_docs_file = locals()['var_functions.query_db:4']
funding_file = locals()['var_functions.query_db:5']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding = json.load(f)

# Step 1: Extract projects with Spring 2022 dates
spring_projects = []

for doc in civic_docs:
    text = doc['text']
    # Look for Spring 2022 patterns anywhere in the document
    spring_2022_mentions = []
    
    # Find all lines that mention Spring 2022 or related patterns
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line_lower = line.lower()
        if ('spring' in line_lower and '2022' in line_lower) or \
           ('2022-spring' in line_lower) or \
           ('2022' in line_lower and any(m in line_lower for m in ['mar', 'apr', 'may', '03/', '04/', '05/'])):
            # Look backwards for project name (usually a few lines before)
            project_name = None
            for j in range(max(0, i-5), i):
                prev_line = lines[j].strip()
                if (len(prev_line) > 10 and prev_line[0].isupper() and 
                    not prev_line.startswith('Page') and not prev_line.startswith('Item') and
                    not any(x in prev_line for x in ['PUBLIC WORKS', 'COMMISSION', 'AGENDA'])):
                    project_name = prev_line
                    break
            
            if project_name:
                spring_projects.append({
                    'name': project_name,
                    'context': line.strip()
                })

# Deduplicate projects
unique_projects = []
seen_names = set()
for p in spring_projects:
    if p['name'] not in seen_names:
        unique_projects.append(p)
        seen_names.add(p['name'])

# Step 2: Match with funding data
funding_matches = []
total_funding = 0

for fund in funding:
    fund_name = fund['Project_Name']
    fund_name_lower = fund_name.lower()
    
    for project in unique_projects:
        proj_name = project['name']
        proj_lower = proj_name.lower()
        
        # More sophisticated matching
        # 1. Exact match
        # 2. One contains the other
        # 3. Keyword overlap
        if proj_lower == fund_name_lower or \
           proj_lower in fund_name_lower or \
           fund_name_lower in proj_lower:
            funding_matches.append({
                'project': proj_name,
                'funding': fund_name,
                'amount': int(fund['Amount'])
            })
            total_funding += int(fund['Amount'])
            break

# If no matches with strict method, try a broader approach
if len(funding_matches) == 0:
    # Create a set of all project keywords
    project_keywords = set()
    for p in unique_projects:
        # Extract key terms from project name
        words = re.findall(r'\b[A-Za-z]+\b', p['name'])
        # Filter out common words
        common = {'project', 'improvements', 'repairs', 'and', 'the', 'phase', 'canyon', 'road'}
        keywords = [w.lower() for w in words if w.lower() not in common and len(w) > 3]
        project_keywords.update(keywords)
    
    for fund in funding:
        fund_name_lower = fund['Project_Name'].lower()
        # Check if any project keyword appears in funding name
        for keyword in project_keywords:
            if keyword in fund_name_lower:
                funding_matches.append({
                    'project': 'Multiple matches',
                    'funding': fund['Project_Name'],
                    'amount': int(fund['Amount'])
                })
                total_funding += int(fund['Amount'])
                break

result = {
    'spring_2022_projects_count': len(unique_projects),
    'total_funding': total_funding,
    'project_names': [p['name'] for p in unique_projects],
    'funding_records_count': len(funding_matches)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:28': {'spring_2022_docs': 4}, 'var_functions.execute_python:34': {'spring_2022_projects': 4, 'funding_matches': 31, 'total_funding': 1614000}}

exec(code, env_args)
