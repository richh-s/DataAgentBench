code = """import json

# Access the data directly from the variables
civic_docs_data = json.loads(json.dumps(var_functions.query_db_10))
funding_data = json.loads(json.dumps(var_functions.query_db_11))

# Create funding map
funding_map = {}
for record in funding_data:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    funding_map[project_name] = amount

# Extract projects with Spring 2022 start dates
spring_2022_projects = []

for doc in civic_docs_data:
    text = doc.get('text', '')
    
    # Look for Spring 2022 in text
    if '2022' in text and ('Spring' in text or 'March' in text or 'April' in text or 'May' in text):
        # This document contains Spring 2022 references
        # Try to extract project names (look for lines that start with capital letters and are reasonable length)
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            if (len(line) > 5 and 
                line[0].isalpha() and 
                line[0].isupper() and 
                ':' not in line and 
                not line.startswith('(') and
                len(line.split()) <= 15):
                
                # Check if this project line or nearby text mentions Spring 2022
                line_pos = text.find(line)
                nearby_text = text[line_pos:line_pos+500]
                
                lower_text = nearby_text.lower()
                if '2022' in nearby_text and any(m in lower_text for m in ['spring', 'march', 'april', 'may']):
                    if line not in spring_2022_projects:
                        spring_2022_projects.append(line)

# Remove duplicates and limit to reasonable projects
spring_2022_projects = [p for p in spring_2022_projects if len(p) > 10]

# Match with funding data
total_funding = 0
matched_projects = []

for proj_name in spring_2022_projects:
    # Direct match
    if proj_name in funding_map:
        total_funding += funding_map[proj_name]
        matched_projects.append({'name': proj_name, 'funding': funding_map[proj_name]})
    else:
        # Try fuzzy match by checking if base names match (remove suffixes)
        base_name = proj_name.split('(')[0].strip().lower()
        
        for fund_name, amount in funding_map.items():
            fund_base = fund_name.split('(')[0].strip().lower()
            if base_name in fund_base or fund_base in base_name:
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
