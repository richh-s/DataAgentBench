code = """import json

# Load data from the variables
civic_docs = json.loads(json.dumps(globals().get('var_functions.query_db_10')))
funding = json.loads(json.dumps(globals().get('var_functions.query_db_11')))

# Create funding map
funding_map = {}
for record in funding:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_map[project_name] = amount

# Simple extraction: look for projects mentioned with 2022 Spring dates
spring_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Check if document mentions Spring 2022
    has_2022 = '2022' in text
    has_spring = any(x in text.lower() for x in ['spring', 'march', 'april', 'may'])
    
    if has_2022 and has_spring:
        # Extract potential project names (lines with title case, reasonable length)
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if (len(line) > 5 and 
                line[0].isalpha() and 
                line[0].isupper() and 
                ':' not in line and 
                line[0] not in ['(', '•', '-'] and
                len(line.split()) <= 20):
                
                spring_projects.append(line)

# Remove duplicates
spring_projects = list(dict.fromkeys(spring_projects))

# Match with funding
matched_projects = []
total_funding = 0

for proj in spring_projects:
    if proj in funding_map:
        total_funding += funding_map[proj]
        matched_projects.append({'name': proj, 'funding': funding_map[proj]})
    else:
        # Try base name match
        base = proj.split('(')[0].strip().lower()
        for fund_name, amount in funding_map.items():
            fund_base = fund_name.split('(')[0].strip().lower()
            if base in fund_base or fund_base in base:
                total_funding += amount
                matched_projects.append({'name': fund_name, 'funding': amount})
                break

result = {
    'project_count': len(matched_projects),
    'total_funding': total_funding,
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json'}

exec(code, env_args)
