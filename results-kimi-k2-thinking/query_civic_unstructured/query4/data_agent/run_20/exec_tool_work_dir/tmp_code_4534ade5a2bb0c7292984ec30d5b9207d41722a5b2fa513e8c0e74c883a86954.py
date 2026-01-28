code = """import json
import re

# Load civic documents
civic_docs_file = var_functions.query_db_5
civic_docs = json.load(open(civic_docs_file))

# Load funding data  
funding_data = var_functions.query_db_9

# Find projects with Spring 2022 start dates
spring_2022_projects = []

# Spring 2022 patterns (March, April, May 2022)
spring_patterns = [
    r'2022[-\s]?Spring',
    r'2022[-\s]?March', 
    r'2022[-\s]?April',
    r'2022[-\s]?May'
]

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line or len(line) < 8:
            continue
            
        # Look for project names (title case lines, not metadata)
        is_potential_project = (
            line[0].isupper() and 
            not line.startswith(('Page', 'To:', 'From:', 'Subject:', 'Date:', 'RECOMMENDED', 'DISCUSSION', 'Agenda', 'Public Works', 'Chair', 'Prepared', 'Approved', 'Meeting')) and
            not line.startswith('(') and
            len(line.split()) >= 2 and
            len(line) < 100
        )
        
        if is_potential_project:
            # Check surrounding context for Spring 2022 dates
            context_lines = lines[max(0, i-2):min(len(lines), i+8)]
            context = '\n'.join(context_lines)
            
            # Check if this project has Spring 2022 in its context
            for pattern in spring_patterns:
                if re.search(pattern, context, re.IGNORECASE):
                    # Clean the project name
                    clean_name = re.sub(r'^[•·o□■-]+\s*', '', line)
                    clean_name = clean_name.strip()
                    
                    if clean_name and not any(p['name'] == clean_name for p in spring_2022_projects):
                        spring_2022_projects.append({'name': clean_name, 'start_date': 'Spring 2022'})
                        break

# Match with funding data
import pandas as pd
funding_df = pd.DataFrame(funding_data)

matched_projects = []
total_funding = 0
seen_projects = set()

for project in spring_2022_projects:
    proj_name = project['name']
    
    # Skip non-project headers
    if any(skip in proj_name for skip in ['Capital Improvement', 'Disaster Recovery', 'Project Schedule']):
        continue
    
    # Direct match
    match = funding_df[funding_df['Project_Name'] == proj_name]
    
    # Try partial match if no exact match
    if match.empty:
        for _, row in funding_df.iterrows():
            fund_name = row['Project_Name'].lower()
            proj_lower = proj_name.lower()
            if (fund_name in proj_lower or proj_lower in fund_name) and len(proj_lower) > 10:
                match = funding_df[funding_df['Project_Name'] == row['Project_Name']]
                break
    
    if not match.empty and proj_name not in seen_projects:
        for _, row in match.iterrows():
            matched_projects.append({
                'project_name': proj_name,
                'funding_id': int(row['Funding_ID']),
                'amount': int(row['Amount']),
                'source': row['Funding_Source']
            })
            total_funding += int(row['Amount'])
            seen_projects.add(proj_name)

# Results
result = {
    'project_count': len(seen_projects),
    'total_funding': total_funding,
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '14', 'Project_Name': 'City Hall Solar Project', 'Funding_Source': 'Research Institution Funding', 'Amount': '38000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '16', 'Project_Name': 'Citywide Asphalt Concrete Berms Repairs', 'Funding_Source': 'Environmental Grant', 'Amount': '10000'}, {'Funding_ID': '17', 'Project_Name': 'Citywide Guardrail Replacement', 'Funding_Source': 'Infrastructure Bond', 'Amount': '30000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '19', 'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'Funding_Source': 'Crowdfunding', 'Amount': '45000'}, {'Funding_ID': '20', 'Project_Name': 'Civic Center Way Improvements', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '37000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
