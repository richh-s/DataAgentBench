code = """import json
import os

# Get data paths
civic_docs_file = str(var_functions.query_db_10)
funding_file = str(var_functions.query_db_11)

# Read files
civic_docs_data = []
funding_data = []

if os.path.exists(civic_docs_file):
    with open(civic_docs_file, 'r') as f:
        civic_docs_data = json.load(f)
if os.path.exists(funding_file):
    with open(funding_file, 'r') as f:
        funding_data = json.load(f)

print(f"Loaded {len(civic_docs_data)} documents and {len(funding_data)} funding records")

# Create funding map
funding_map = {}
for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_map[project_name] = amount

# Extract Spring 2022 projects
spring_projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    
    # Check if document mentions 2022 Spring months
    lower_text = text.lower()
    mentions_2022 = '2022' in lower_text
    mentions_spring = 'spring' in lower_text or 'march' in lower_text or 'april' in lower_text or 'may' in lower_text
    
    if mentions_2022 and mentions_spring:
        lines = text.split('\n')
        for i, line in enumerate(lines):
            line = line.strip()
            
            # Skip short lines and bullets
            if len(line) < 5:
                continue
            if line[0] in ['(', '•', '-', '□', '■']:
                continue
            
            # Look for project names (capitalized, reasonable length, not metadata)
            if line[0].isalpha() and line[0].isupper() and ':' not in line and len(line.split()) <= 20:
                if 'capital improvement' in line.lower() or 'project' in line.lower():
                    continue
                
                # Check nearby lines for 2022 Spring reference
                nearby = ' '.join(lines[i:min(i+5, len(lines))])
                nearby_lower = nearby.lower()
                
                if '2022' in nearby and any(m in nearby_lower for m in ['spring', 'march', 'april', 'may']):
                    spring_projects.append(line)

# Remove duplicates
spring_projects = list(dict.fromkeys(spring_projects))

print(f"Found {len(spring_projects)} Spring 2022 projects")

# Match with funding
total_funding = 0
matched_projects = []

for proj in spring_projects:
    # Direct match
    if proj in funding_map:
        total_funding += funding_map[proj]
        matched_projects.append({'name': proj, 'funding': funding_map[proj]})
    else:
        # Try base name match
        proj_base = proj.split('(')[0].strip().lower()
        for fund_name, amount in funding_map.items():
            if any(m['name'] == fund_name for m in matched_projects):
                continue
            fund_base = fund_name.split('(')[0].strip().lower()
            if proj_base in fund_base or fund_base in proj_base:
                total_funding += amount
                matched_projects.append({'name': fund_name, 'funding': amount})
                break

result = {'project_count': len(matched_projects), 'total_funding': total_funding, 'projects': matched_projects}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
