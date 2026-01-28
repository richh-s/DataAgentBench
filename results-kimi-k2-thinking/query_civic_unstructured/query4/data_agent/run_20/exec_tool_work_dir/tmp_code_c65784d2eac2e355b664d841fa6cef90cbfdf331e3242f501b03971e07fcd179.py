code = """import json
import re

# Get civic documents data
civic_docs_file = var_functions.query_db:5
civic_docs = json.load(open(civic_docs_file))

# Get funding data
funding_data = var_functions.query_db:9

# Extract projects with Spring 2022 start dates from civic documents
spring_2022_projects = []
spring_patterns = [
    r'2022[-\s]?Spring',
    r'2022[-\s]?March',
    r'2022[-\s]?April', 
    r'2022[-\s]?May'
]

for doc in civic_docs:
    text = doc.get('text', '')
    # Look for project names and their start dates
    # Common patterns in the documents
    lines = text.split('\n')
    for line in lines:
        line = line.strip()
        # Look for project names (often start with bullet points or are title-like)
        if line and (line.startswith('•') or line.startswith('·') or line.startswith('o') or 
                     line.startswith('□') or line.startswith('■') or 
                     (len(line) > 5 and line[0].isupper() and ':' not in line[:30])):
            # Clean up the line
            project_name = line.replace('•', '').replace('·', '').replace('o', '').replace('□', '').replace('■', '').strip()
            
            # Check if this project has a Spring 2022 start date mentioned anywhere in the document
            for pattern in spring_patterns:
                if re.search(pattern, text, re.IGNORECASE):
                    # Also check if this specific project name appears near a date pattern
                    project_context = text[text.find(project_name)-200:text.find(project_name)+200] if project_name in text else ''
                    if re.search(pattern, project_context, re.IGNORECASE) or re.search(pattern, text, re.IGNORECASE):
                        if project_name and project_name not in [p['name'] for p in spring_2022_projects]:
                            spring_2022_projects.append({'name': project_name, 'start_date': 'Spring 2022'})

# Also look for more structured project information
# Look for patterns like "Project Name\nProject Schedule:\nBegin: Spring 2022"
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Pattern 1: Project name followed by schedule
    schedule_matches = re.finditer(r'(?:Project\s+Name|Project\s+Description|:)\s*[:\n]\s*([^\n]+(?:\n[^\n]+){0,3})\s*(?:Project\s+Schedule|Estimated\s+Schedule|Updates:)?\s*[:\n]\s*([^\n]+(?:\n[^\n]+){0,5})', text, re.IGNORECASE)
    
    for match in schedule_matches:
        project_name = match.group(1).strip()
        schedule_section = match.group(2).strip()
        
        # Check if schedule mentions Spring 2022
        for pattern in spring_patterns:
            if re.search(pattern, schedule_section, re.IGNORECASE):
                if project_name and project_name not in [p['name'] for p in spring_2022_projects]:
                    spring_2022_projects.append({'name': project_name, 'start_date': 'Spring 2022'})

# Get all funding records
funding_df = pd.DataFrame(funding_data)

# Match projects with funding
matched_projects = []
total_funding = 0

for project in spring_2022_projects:
    proj_name = project['name']
    
    # Exact match
    funding_match = funding_df[funding_df['Project_Name'] == proj_name]
    
    if funding_match.empty:
        # Try fuzzy matching - check if project name contains a key part
        key_parts = proj_name.split()
        if len(key_parts) >= 2:
            # Try matching on first few words
            partial_name = ' '.join(key_parts[:3])
            funding_match = funding_df[funding_df['Project_Name'].str.contains(partial_name, case=False, na=False)]
    
    if not funding_match.empty:
        for _, match in funding_match.iterrows():
            matched_projects.append({
                'project_name': proj_name,
                'funding_id': match['Funding_ID'],
                'amount': int(match['Amount']),
                'source': match['Funding_Source']
            })
            total_funding += int(match['Amount'])

# Prepare results
result = {
    'project_count': len(set(p['project_name'] for p in matched_projects)),
    'total_funding': total_funding,
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '14', 'Project_Name': 'City Hall Solar Project', 'Funding_Source': 'Research Institution Funding', 'Amount': '38000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '16', 'Project_Name': 'Citywide Asphalt Concrete Berms Repairs', 'Funding_Source': 'Environmental Grant', 'Amount': '10000'}, {'Funding_ID': '17', 'Project_Name': 'Citywide Guardrail Replacement', 'Funding_Source': 'Infrastructure Bond', 'Amount': '30000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '19', 'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'Funding_Source': 'Crowdfunding', 'Amount': '45000'}, {'Funding_ID': '20', 'Project_Name': 'Civic Center Way Improvements', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '37000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
