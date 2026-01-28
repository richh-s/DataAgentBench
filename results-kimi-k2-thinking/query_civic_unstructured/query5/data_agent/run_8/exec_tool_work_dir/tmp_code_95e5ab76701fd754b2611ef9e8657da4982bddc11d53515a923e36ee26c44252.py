code = """import json
import pandas as pd
import re

# Load data from storage
civic_docs_file = locals()['var_functions.query_db:2']
with open(civic_docs_file) as f:
    civic_docs = json.load(f)

funding_data = locals()['var_functions.query_db:0']
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce')

# Extract project information from civic documents
projects = []

def is_likely_project_name(line):
    line = line.strip()
    if len(line) < 10:
        return False
    if line.startswith('-'):
        return False
    uppercase_ratio = sum(1 for c in line if c.isupper()) / len(line)
    if uppercase_ratio > 0.5:
        return True
    return False

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    lines = text.split('\n')
    
    for line in lines:
        line = line.strip()
        if 'FEMA' in line or 'CalOES' in line or 'CalJPIA' in line or ('disaster' in line.upper()):
            project_info = {
                'Project_Name': '',
                'type': 'disaster',
                'status': '',
                'st': '',
                'et': '',
                'source_file': filename
            }
            
            if is_likely_project_name(line):
                project_info['Project_Name'] = line
            else:
                project_info['Project_Name'] = filename
            
            # Look for 2022 dates in the next few lines
            line_idx = lines.index(line)
            for nearby_line in lines[line_idx:line_idx+5]:
                if '2022' in nearby_line:
                    nearby_lower = nearby_line.lower()
                    if any(word in nearby_lower for word in ['begin', 'start', 'advertise', 'design']):
                        project_info['st'] = '2022'
                    elif any(word in nearby_lower for word in ['complete', 'end', 'finish']):
                        project_info['et'] = '2022'
            
            projects.append(project_info)

projects_df = pd.DataFrame(projects)
print('Total disaster projects found:', len(projects_df))
print('Projects with 2022 start date:', len(projects_df[projects_df['st'] == '2022']))

# Match with funding data
total_funding = 0
matched_projects = []

if not projects_df.empty:
    disaster_2022 = projects_df[projects_df['st'] == '2022']
    print('\nDisaster projects starting in 2022:', len(disaster_2022))
    
    for _, proj in disaster_2022.iterrows():
        proj_name = proj['Project_Name']
        
        for _, fund in funding_df.iterrows():
            fund_name = fund['Project_Name']
            
            # Exact match or partial match
            if proj_name.lower() == fund_name.lower():
                total_funding += fund['Amount']
                matched_projects.append({
                    'project': proj_name,
                    'funding_project': fund_name,
                    'amount': fund['Amount']
                })
                break
            elif (proj_name.lower() in fund_name.lower() or 
                  fund_name.lower() in proj_name.lower()):
                total_funding += fund['Amount']
                matched_projects.append({
                    'project': proj_name,
                    'funding_project': fund_name,
                    'amount': fund['Amount']
                })

result = {
    'total_funding': float(total_funding),
    'matched_projects': matched_projects
}

print('Final result:', result)
__RESULT__: json.dumps(result)"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
