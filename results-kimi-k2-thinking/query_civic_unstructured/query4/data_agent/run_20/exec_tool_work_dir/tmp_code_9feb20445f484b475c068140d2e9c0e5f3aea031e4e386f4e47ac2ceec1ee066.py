code = """import json
import pandas as pd

# Load the data
civic_docs_file = var_functions.query_db_24
with open(civic_docs_file, 'r') as f:
    civic_docs = json.load(f)

# Load all funding data
funding_file = var_functions.query_db_26
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Look for projects with Spring 2022 start dates
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Look for lines that might be project names and have spring 2022 references
        if ('2022' in line and 
            len(line) > 10 and 
            not line.startswith('Page') and 
            not any(x in line for x in ['To:', 'From:', 'Subject:', 'Date:'])):
            
            # Check if this looks like a project name
            if line[0].isupper() and line.count(' ') >= 2:
                # Look at context for spring/summer timing
                context = ' '.join(lines[max(0,i-3):min(len(lines),i+5)])
                if any(season in context.lower() for season in ['spring', 'summer', 'fall', 'winter', 'begin construction', 'advertise']):
                    spring_2022_projects.append(line.strip())

# Also search for explicit spring 2022 mentions
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Spring 2022' in text or 'spring 2022' in text:
        # Get project names near this mention
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if '2022' in line and 'Morning View' in line:
                if line.strip() not in spring_2022_projects:
                    spring_2022_projects.append(line.strip())

# Create funding dataframe
funding_df = pd.DataFrame(funding_data)

# Match projects
matched_projects = []
total_funding = 0
seen = set()

for proj_name in spring_2022_projects:
    # Direct match
    matches = funding_df[funding_df['Project_Name'] == proj_name]
    
    if matches.empty:
        # Try partial match for longer names
        for _, row in funding_df.iterrows():
            fund_name = row['Project_Name']
            # Check if funding project name is contained in doc project name
            if fund_name in proj_name and len(fund_name) > 15:
                matches = funding_df[funding_df['Project_Name'] == fund_name]
                break
    
    if not matches.empty and proj_name not in seen:
        for _, row in matches.iterrows():
            matched_projects.append({
                'project_name': proj_name,
                'amount': int(row['Amount']),
                'source': row['Funding_Source']
            })
            total_funding += int(row['Amount'])
            seen.add(proj_name)

# Calculate final results
project_count = len(seen)

result = {
    'project_count': project_count,
    'total_funding': total_funding,
    'projects': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '14', 'Project_Name': 'City Hall Solar Project', 'Funding_Source': 'Research Institution Funding', 'Amount': '38000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '16', 'Project_Name': 'Citywide Asphalt Concrete Berms Repairs', 'Funding_Source': 'Environmental Grant', 'Amount': '10000'}, {'Funding_ID': '17', 'Project_Name': 'Citywide Guardrail Replacement', 'Funding_Source': 'Infrastructure Bond', 'Amount': '30000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '19', 'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'Funding_Source': 'Crowdfunding', 'Amount': '45000'}, {'Funding_ID': '20', 'Project_Name': 'Civic Center Way Improvements', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '37000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
