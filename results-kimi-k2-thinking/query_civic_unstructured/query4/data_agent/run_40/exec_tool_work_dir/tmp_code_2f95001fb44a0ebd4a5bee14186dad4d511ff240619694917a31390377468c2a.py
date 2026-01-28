code = """import json, re, os

# Load data
with open('/root/shared_data/var_functions.query_db:5.json', 'r') as f:
    funding = json.load(f)
with open('/root/shared_data/var_functions.query_db:2.json', 'r') as f:
    civic = json.load(f)

print('Loaded', len(funding), 'funding records and', len(civic), 'civic documents')

# Step 1: Extract Spring 2022 projects from civic documents
spring_2022_projects = []

for doc in civic:
    text = doc.get('text', '')
    # Check if document contains Spring 2022 indicators
    if 'Spring 2022' in text or '2022-Spring' in text or '2022-March' in text or '2022-April' in text or '2022-May' in text:
        lines = text.split('\n')
        for i in range(len(lines)):
            line = lines[i].strip()
            # Look for schedule lines
            if 'Spring 2022' in line or '2022-Spring' in line:
                # Look backwards for project name (usually a previous header/line)
                for j in range(i-1, max(0, i-6), -1):
                    prev_line = lines[j].strip()
                    # Heuristic for project name:
                    if (prev_line and len(prev_line) > 15 and 
                        not prev_line.startswith('(') and 
                        'Page' not in prev_line and
                        'Item' not in prev_line):
                        spring_2022_projects.append(prev_line)
                        break

print('Found', len(spring_2022_projects), 'Spring 2022 project candidates')

# Step 2: Match with funding records
total_funding = 0
matched_project_names = set()

for fund_record in funding:
    fund_name = fund_record['Project_Name']
    fund_amount = int(fund_record['Amount'])
    
    for project_candidate in spring_2022_projects:
        # Check for matching
        project_candidate_lower = project_candidate.lower()
        fund_name_lower = fund_name.lower()
        
        # Match if:
        # 1. Fund name is exact match or contains the project name
        # 2. Project name contains fund name
        if (fund_name_lower in project_candidate_lower or 
            project_candidate_lower in fund_name_lower):
            if fund_name not in matched_project_names:
                matched_project_names.add(fund_name)
                total_funding += fund_amount
                break

project_count = len(matched_project_names)
print('Matched', project_count, 'projects with total funding', total_funding)

# Format result in required JSON format
result = {'project_count': project_count, 'total_funding': total_funding}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
