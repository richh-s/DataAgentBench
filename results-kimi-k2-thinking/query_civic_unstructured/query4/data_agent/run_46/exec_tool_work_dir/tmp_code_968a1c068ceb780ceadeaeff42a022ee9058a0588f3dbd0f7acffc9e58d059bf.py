code = """import json
import re

civic_docs_file = locals()['var_functions.query_db:2']
funding_file = locals()['var_functions.query_db:5']

with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Build funding lookup map
funding_map = {}
for record in funding_data:
    name = record['Project_Name']
    amount = int(record['Amount'])
    funding_map[name] = funding_map.get(name, 0) + amount

# Search for Spring 2022 projects with more flexible matching
spring_project_names = []

for doc in civic_docs:
    text = doc.get('text', '')
    lower_text = text.lower()
    
    # Check if document mentions spring 2022
    has_spring_2022 = False
    spring_indicators = ['2022-spring', 'spring 2022', '2022-mar', '2022-apr', '2022-may']
    for indicator in spring_indicators:
        if indicator in lower_text:
            has_spring_2022 = True
            break
    
    if has_spring_2022:
        # Extract project names
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            # Skip metadata and bullet points
            if not line or line.startswith('cid:') or line.startswith('To:') or line.startswith('Prepared'):
                continue
            
            # Look for project name pattern
            if len(line) > 10 and line[0].isupper() and len(line) < 150:
                # Check if this line is near a spring date
                context = '\n'.join(lines[max(0, i-3):i+3])
                context_lower = context.lower()
                
                has_date_nearby = False
                for indicator in spring_indicators:
                    if indicator in context_lower:
                        has_date_nearby = True
                        break
                
                if has_date_nearby:
                    # Clean name
                    clean_name = re.sub(r'^[\-\*\u2022]+\s*', '', line)
                    clean_name = re.sub(r'^cid:\d+\s*', '', clean_name)
                    clean_name = ' '.join(clean_name.split())
                    
                    if clean_name and 'agenda' not in clean_name.lower() and 'report' not in clean_name.lower():
                        spring_project_names.append(clean_name)

# Remove duplicates
spring_project_names = list(set(spring_project_names))
print('Spring 2022 projects found:', len(spring_project_names))

# Match with funding
matched_projects = []
total_funding_amount = 0

for project in spring_project_names:
    if project in funding_map:
        amount = funding_map[project]
        matched_projects.append([project, amount])
        total_funding_amount += amount
    else:
        # Try fuzzy matching
        project_clean = re.sub(r'[^A-Za-z0-9]', '', project).lower()
        for fund_name, amount in funding_map.items():
            fund_clean = re.sub(r'[^A-Za-z0-9]', '', fund_name).lower()
            if project_clean in fund_clean or fund_clean in project_clean:
                matched_projects.append([project, amount])
                total_funding_amount += amount
                break

print('Matched projects:', len(matched_projects))
print('Total funding:', total_funding_amount)

result = {
    'project_count': len(matched_projects),
    'total_funding': total_funding_amount
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.execute_python:14': {'civic_count': 5, 'funding_count': 500}, 'var_functions.execute_python:20': {'civic_file': 'var_functions.query_db:2', 'funding_file': 'var_functions.query_db:5'}, 'var_functions.execute_python:22': {'civic_path': 'file_storage/functions.query_db:2.json', 'funding_path': 'file_storage/functions.query_db:5.json', 'civic_exists': True, 'funding_exists': True}, 'var_functions.execute_python:36': {'project_count': 0, 'total_funding': 0}}

exec(code, env_args)
