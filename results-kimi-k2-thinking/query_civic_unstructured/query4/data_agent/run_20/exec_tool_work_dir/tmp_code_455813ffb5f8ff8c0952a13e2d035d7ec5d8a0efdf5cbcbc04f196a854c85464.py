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

# More targeted approach - look for actual project names and their schedules
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for lines that might be project names (often title case, without colons early on)
    lines = text.split('\n')
    for i, line in enumerate(lines):
        line = line.strip()
        # Skip empty lines and obvious non-project lines
        if not line or len(line) < 10:
            continue
            
        # Common patterns that indicate project names
        if (line.startswith(('•', '·', 'o', '□', '■', '-')) or 
            (line[0].isupper() and ':' not in line[:40] and 
             not line.startswith('Page') and 
             not line.startswith('To:') and
             not line.startswith('From:') and
             not line.startswith('Subject:') and
             not line.startswith('Date:') and
             not line.startswith('RECOMMENDED') and
             not line.startswith('DISCUSSION:'))):
            
            # Clean the project name
            project_name = line.strip('•·o□■-').strip()
            
            # Look for date patterns in the surrounding text (next 5 lines typically)
            context = '\n'.join(lines[i:min(i+8, len(lines))])
            
            for pattern in spring_patterns:
                if re.search(pattern, context, re.IGNORECASE):
                    # This project starts in Spring 2022
                    if project_name and project_name not in [p['name'] for p in spring_2022_projects]:
                        spring_2022_projects.append({'name': project_name, 'start_date': 'Spring 2022'})

# Look for more explicit project descriptions  
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Pattern: "Project Description:" followed by project name/details
    desc_matches = re.finditer(r'Project Description: ?\n?([^\n]+(?:\n[^\n]+){0,2})', text, re.IGNORECASE)
    for match in desc_matches:
        project_desc = match.group(1).strip()
        # Look for schedule info after this description
        desc_pos = match.end()
        after_desc = text[desc_pos:desc_pos+500]
        
        for pattern in spring_patterns:
            if re.search(pattern, after_desc, re.IGNORECASE):
                # Extract project name (first line of description)
                project_name = project_desc.split('\n')[0].strip()
                if project_name and project_name not in [p['name'] for p in spring_2022_projects]:
                    spring_2022_projects.append({'name': project_name, 'start_date': 'Spring 2022'})

import pandas as pd

# Get all funding records
funding_df = pd.DataFrame(funding_data)

# Match projects with funding - clean up the matching logic
matched_projects = []
total_funding = 0
project_names_seen = set()

for project in spring_2022_projects:
    proj_name = project['name']
    
    # Skip common non-project headings
    skip_patterns = ['Capital Improvement', 'Disaster Recovery', 'Project Schedule', 
                    'Updates:', 'Project Description', 'RECOMMENDED ACTION', 'DISCUSSION:']
    if any(skip in proj_name for skip in skip_patterns):
        continue
    
    # Try direct match first
    funding_match = funding_df[funding_df['Project_Name'] == proj_name]
    
    if funding_match.empty:
        # Try if project name contains funding project name or vice versa
        for _, fund_row in funding_df.iterrows():
            fund_name = fund_row['Project_Name'].lower()
            proj_lower = proj_name.lower()
            
            # Check for partial matches
            if (fund_name in proj_lower or proj_lower in fund_name or
                any(word in fund_name for word in proj_lower.split() if len(word) > 4)):
                
                funding_match = funding_df[funding_df['Project_Name'] == fund_row['Project_Name']]
                break
    
    if not funding_match.empty and proj_name not in project_names_seen:
        for _, match in funding_match.iterrows():
            matched_projects.append({
                'project_name': proj_name,
                'funding_id': match['Funding_ID'],
                'amount': int(match['Amount']),
                'source': match['Funding_Source']
            })
            total_funding += int(match['Amount'])
            project_names_seen.add(proj_name)

# Prepare results
result = {
    'project_count': len(project_names_seen),
    'total_funding': total_funding,
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '14', 'Project_Name': 'City Hall Solar Project', 'Funding_Source': 'Research Institution Funding', 'Amount': '38000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '16', 'Project_Name': 'Citywide Asphalt Concrete Berms Repairs', 'Funding_Source': 'Environmental Grant', 'Amount': '10000'}, {'Funding_ID': '17', 'Project_Name': 'Citywide Guardrail Replacement', 'Funding_Source': 'Infrastructure Bond', 'Amount': '30000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '19', 'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'Funding_Source': 'Crowdfunding', 'Amount': '45000'}, {'Funding_ID': '20', 'Project_Name': 'Civic Center Way Improvements', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '37000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
