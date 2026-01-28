code = """import json
import re

# Load the data
with open('var_functions.query_db_18', 'r') as f:
    civic_docs = json.load(f)

funding_data = var_functions.query_db_9

# Look for specific spring 2022 start date patterns
spring_2022_patterns = [
    r'Begin Construction: Spring 2022',
    r'Start: Spring 2022', 
    r'2022[-\s]?Spring',
    r'2022[-\s]?March',
    r'2022[-\s]?April', 
    r'2022[-\s]?May'
]

# Extract projects that mention Spring 2022
spring_2022_projects = []
project_names = set()

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for project information blocks
    # Pattern: Project name line, then project details including schedule
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
            
        # Detect project names (typically standalone title case lines)
        if (len(line) > 10 and 
            line[0].isupper() and 
            not any(skip in line for skip in ['Page', 'To:', 'From:', 'Subject:', 'Date:', 'RECOMMENDED', 'DISCUSSION', 'Agenda', 'Public Works', 'Chair', 'Prepared by', 'Approved by', 'Staff', 'City Council']) and
            not line.startswith('(') and
            line.count(' ') >= 2):
            
            current_project = line.strip('•·o□■-')
            
        # If we have a current project, look for spring 2022 dates in following lines
        if current_project:
            # Look ahead up to 10 lines
            lookahead = lines[i:min(i+12, len(lines))]
            context = '\n'.join(lookahead)
            
            # Check for spring 2022 patterns
            for pattern in spring_2022_patterns:
                if 'Begin' in context and re.search(pattern, context, re.IGNORE_CASE):
                    if current_project not in project_names:
                        spring_2022_projects.append({
                            'name': current_project,
                            'context': context
                        })
                        project_names.add(current_project)
                        current_project = None
                        break
            
            # Reset current project if we've gone too far
            if i > 0 and lines[i-1].strip() and not lines[i-1].strip()[0].isupper():
                current_project = None

# Match with funding data
import pandas as pd
funding_df = pd.DataFrame(funding_data)

# Find exact matches for projects that started in Spring 2022
matched_projects = []
total_funding = 0

for project in spring_2022_projects:
    proj_name = project['name']
    
    # Skip obvious non-projects
    if any(skip in proj_name for skip in ['Capital Improvement', 'Disaster Recovery', 'Project Schedule', 'Updates:']):
        continue
    
    # Try to match with funding table
    match = funding_df[funding_df['Project_Name'] == proj_name]
    
    if not match.empty:
        for _, row in match.iterrows():
            matched_projects.append({
                'project_name': proj_name,
                'funding_id': int(row['Funding_ID']),
                'amount': int(row['Amount']),
                'source': row['Funding_Source']
            })
            total_funding += int(row['Amount'])

# Also check for projects starting with "2022" in their name (often indicate start year)
for doc in civic_docs:
    text = doc.get('text', '')
    # Find lines starting with 2022
    matches = re.finditer(r'^\s*(2022[^\n]{5,80})$', text, re.MULTILINE)
    for match in matches:
        line = match.group(1).strip()
        if line and not any(skip in line for skip in ['Page', 'To:', 'From:']):
            proj_name = line
            if proj_name not in [p['project_name'] for p in matched_projects]:
                match = funding_df[funding_df['Project_Name'] == proj_name]
                if not match.empty:
                    for _, row in match.iterrows():
                        matched_projects.append({
                            'project_name': proj_name,
                            'funding_id': int(row['Funding_ID']),
                            'amount': int(row['Amount']),
                            'source': row['Funding_Source']
                        })
                        total_funding += int(row['Amount'])

result = {
    'project_count': len(set(p['project_name'] for p in matched_projects)),
    'total_funding': total_funding,
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result, indent=2))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '14', 'Project_Name': 'City Hall Solar Project', 'Funding_Source': 'Research Institution Funding', 'Amount': '38000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '16', 'Project_Name': 'Citywide Asphalt Concrete Berms Repairs', 'Funding_Source': 'Environmental Grant', 'Amount': '10000'}, {'Funding_ID': '17', 'Project_Name': 'Citywide Guardrail Replacement', 'Funding_Source': 'Infrastructure Bond', 'Amount': '30000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '19', 'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'Funding_Source': 'Crowdfunding', 'Amount': '45000'}, {'Funding_ID': '20', 'Project_Name': 'Civic Center Way Improvements', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '37000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
