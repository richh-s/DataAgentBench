code = """import json
import re

# The variables should be available directly
civic_docs = json.load(open(var_functions.query_db_10))
funding = json.load(open(var_functions.query_db_11))

# Create funding map
funding_map = {r['Project_Name']: int(r['Amount']) for r in funding}

spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    current = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if len(line) < 5 or line[0] in ['(', '•', '-']: continue
        
        if line[0].isalpha() and line[0].isupper() and ':' not in line and len(line.split()) <= 20:
            current = line
            continue
        
        if current:
            combined = line + ' ' + ' '.join(lines[i+1:min(i+3, len(lines))])
            combined_lower = combined.lower()
            
            if '2022' in combined_lower and any(m in combined_lower for m in ['spring', 'march', 'april', 'may']):
                if current not in spring_projects:
                    spring_projects.append(current)
                current = None

# Remove duplicates
spring_projects = list(dict.fromkeys(spring_projects))

# Match with funding
total_funding = 0
matched = []

for proj in spring_projects:
    if proj in funding_map:
        total_funding += funding_map[proj]
        matched.append({'name': proj, 'funding': funding_map[proj]})
    else:
        base = proj.split('(')[0].strip().lower()
        for fund_name, amount in funding_map.items():
            fund_base = fund_name.split('(')[0].strip().lower()
            if base in fund_base or fund_base in base:
                total_funding += amount
                matched.append({'name': fund_name, 'funding': amount})
                break

result = {'project_count': len(matched), 'total_funding': total_funding, 'projects': matched}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
