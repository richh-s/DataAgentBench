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

# Define helper to check if project started in 2022
def started_in_2022(st_value):
    if not st_value:
        return False
    return '2022' in str(st_value)

# Initialize list for disaster projects starting in 2022
disaster_2022_projects = []

# Process each document
for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for disaster-related projects
    if 'FEMA' in text or 'CalOES' in text or 'CalJPIA' in text or 'disaster' in text.lower() or 'fire' in text.lower():
        lines = text.split('\n')
        
        for idx, line in enumerate(lines):
            line = line.strip()
            
            # Check if this line indicates a disaster project
            if any(keyword in line for keyword in ['FEMA', 'CalOES', 'CalJPIA']) or 'disaster' in line.lower():
                project_name = None
                
                # Look backwards for project name (typically previous few lines)
                for i in range(max(0, idx-10), idx):
                    prev_line = lines[i].strip()
                    if len(prev_line) > 5 and not prev_line.startswith('('):
                        # Heuristic: capitalized with enough length
                        if sum(1 for c in prev_line if c.isupper()) > len(prev_line) * 0.3:
                            project_name = prev_line
                            break
                
                if not project_name and idx > 0:
                    project_name = lines[idx-1].strip()
                
                if project_name and len(project_name) > 3:
                    # Look for dates in nearby lines
                    start_date = ''
                    end_date = ''
                    
                    for near_idx in range(max(0, idx-5), min(len(lines), idx+10)):
                        near_line = lines[near_idx]
                        
                        if '2022' in near_line:
                            near_lower = near_line.lower()
                            if any(word in near_lower for word in ['begin', 'start', 'advertise', 'design', 'construction']):
                                start_date = '2022'
                            elif any(word in near_lower for word in ['complete', 'end', 'finish']):
                                end_date = '2022'
                    
                    if started_in_2022(start_date):
                        disaster_2022_projects.append({
                            'Project_Name': project_name,
                            'type': 'disaster',
                            'start_date': start_date,
                            'end_date': end_date,
                            'source_file': filename
                        })

# Create DataFrame and deduplicate
disaster_df = pd.DataFrame(disaster_2022_projects)
if not disaster_df.empty:
    disaster_df = disaster_df.drop_duplicates(subset=['Project_Name'], keep='first')
    print('Unique disaster projects starting in 2022:', len(disaster_df))
    print('Sample projects:', disaster_df.head())

# Match with funding data
total_funding = 0.0
funding_matches = []

if not disaster_df.empty and not funding_df.empty:
    for _, disaster_proj in disaster_df.iterrows():
        disaster_name = disaster_proj['Project_Name'].strip()
        
        # Look for matching funding record
        for _, funding_record in funding_df.iterrows():
            funding_name = funding_record['Project_Name'].strip()
            
            # Various matching strategies
            if disaster_name == funding_name:
                total_funding += funding_record['Amount']
                funding_matches.append((disaster_name, funding_name, funding_record['Amount']))
                break
            elif disaster_name in funding_name or funding_name in disaster_name:
                total_funding += funding_record['Amount']
                funding_matches.append((disaster_name, funding_name, funding_record['Amount']))
                break
            elif any(part in funding_name.lower() for part in disaster_name.lower().split()[:3]):
                if len(disaster_name) > 15:
                    total_funding += funding_record['Amount']
                    funding_matches.append((disaster_name, funding_name, funding_record['Amount']))
                    break

print('Total matched funding:', total_funding)

result = {
    'total_funding': float(total_funding),
    'project_count': len(disaster_df) if not disaster_df.empty else 0,
    'matches': len(funding_matches)
}

__RESULT__: json.dumps(result)"""

env_args = {'var_functions.query_db:0': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
