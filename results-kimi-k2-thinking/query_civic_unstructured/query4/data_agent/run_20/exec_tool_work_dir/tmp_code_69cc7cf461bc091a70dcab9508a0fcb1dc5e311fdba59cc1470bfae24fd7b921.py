code = """import json
import re
import pandas as pd

# Access the civic documents data
# The data is stored in a file whose path is in the variable
civic_docs_path = var_functions.query_db_18
with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

# Access the funding data directly
funding_data = var_functions.query_db_9

# Look for Spring 2022 start dates
spring_patterns = [
    r'Begin Construction: Spring 2022',
    r'Start: Spring 2022', 
    r'2022[-\s]?Spring',
    r'2022[-\s]?March',
    r'2022[-\s]?April',
    r'2022[-\s]?May'
]

spring_2022_projects = set()

# Extract project names that have Spring 2022 start dates
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find all potential project sections
    # Look for patterns that indicate project info
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 8:
            continue
            
        # Identify likely project names
        if line[0].isupper() and not any(x in line for x in ['Page', 'To:', 'From:', 'Subject:', 'Date:', 'RECOMMENDED', 'DISCUSSION']) and not line.startswith('('):
            # Check if next few lines contain Spring 2022
            next_lines = '\n'.join(lines[i:i+10])
            for pattern in spring_patterns:
                if re.search(pattern, next_lines, re.IGNORECASE):
                    clean_name = re.sub(r'^[•·o□■-]+\s*', '', line).strip()
                    if clean_name:
                        spring_2022_projects.add(clean_name)

# Create funding dataframe
funding_df = pd.DataFrame(funding_data)

# Match projects with funding
matched = []
total = 0

for proj_name in spring_2022_projects:
    # Direct match
    matches = funding_df[funding_df['Project_Name'] == proj_name]
    
    if matches.empty:
        # Try partial match
        for _, row in funding_df.iterrows():
            fund_name = row['Project_Name']
            if (proj_name.lower() in fund_name.lower() or 
                fund_name.lower() in proj_name.lower()):
                matches = funding_df[funding_df['Project_Name'] == fund_name]
                break
    
    if not matches.empty:
        for _, row in matches.iterrows():
            matched.append({
                'project_name': proj_name,
                'amount': int(row['Amount']),
                'source': row['Funding_Source']
            })
            total += int(row['Amount'])

result = {
    'project_count': len(set(m['project_name'] for m in matched)),
    'total_funding': total,
    'projects': matched
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '14', 'Project_Name': 'City Hall Solar Project', 'Funding_Source': 'Research Institution Funding', 'Amount': '38000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '16', 'Project_Name': 'Citywide Asphalt Concrete Berms Repairs', 'Funding_Source': 'Environmental Grant', 'Amount': '10000'}, {'Funding_ID': '17', 'Project_Name': 'Citywide Guardrail Replacement', 'Funding_Source': 'Infrastructure Bond', 'Amount': '30000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '19', 'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'Funding_Source': 'Crowdfunding', 'Amount': '45000'}, {'Funding_ID': '20', 'Project_Name': 'Civic Center Way Improvements', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '37000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
